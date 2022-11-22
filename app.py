from SQLModels import Login, Univerzita, Fakulta, Clovek, Pozice, Titul, mariadb
from mongodb_insert import inserter
from flask import Flask, render_template, request, session, flash, redirect
from sqlalchemy import func
from redis import Redis
from pymongo import MongoClient
from bson.code import Code
import time
import pickle
from os import listdir
import json
import sys
path = "soubory/"
endOfFile = "divocak"
separator = ","

db = []


def getLineInFile(path):
    file = open(path, "r")
    line = file.readline()
    file.close()
    return line


def writeLineInFile(path, text):
    file = open(path, "w")
    file.write(text)
    file.close()


def loadDB():
    for localPath in listdir(path):
        splitedPath = localPath.split(".")
        if splitedPath[-1] == endOfFile:
            meziDB = []
            meziDB.append(splitedPath[-2].split("/")[-1])
            for kek in getLineInFile(path + localPath).split(separator):
                meziDB.append(kek)
            db.append(meziDB)


def getLastID():
    listOfFiles = listdir(path)
    higestNumber = int(listOfFiles[0].split(".")[-2])
    for value in listOfFiles:
        fileExtension = value.split(".")[1]
        if fileExtension == endOfFile:
            number = int(value.split(".")[0])
            newNumber = number
            if newNumber > higestNumber:
                higestNumber = newNumber
    return higestNumber


def addToDB(nazev, nadpis, text):
    id = getLastID() + 1
    writeLineInFile(path + str(id) + "." + endOfFile, nazev +
                    separator + nadpis + separator + text)
    db.append([id, nazev, nadpis, text])


def backupDeleter():
    backups = []
    backups = r.keys()
    i = 0
    for backup in backups:
        r.delete(backup)
        i = i + 1
    if i > 0:
        print("Bylo smazáno " + str(i) + " redis backupů!")

try:
    loginJson = open("login.json")
except:
    print("Chybí soubor login.json! :---(")
    sys.exit()
logins = json.load(loginJson)

flaskAPR = Flask(__name__)
flaskAPR.app_context().push()
flaskAPR.secret_key = logins["secretkey"]
flaskAPR.config['SQLALCHEMY_DATABASE_URI'] = logins["sql-login"]
flaskAPR.config['SQLALCHEMY_BINDS'] = {
    'mariadbUjep': logins["sql-ujep"]
}
mariadb.init_app(flaskAPR)
mariadb.create_all()

r = Redis(host="82.142.110.169", port=6379)
redisTimeout = 60
backupDeleter()

clientMongo = MongoClient(logins["mongo"])
mongodb = clientMongo["nsql"]
emailResult = mongodb["emailResult"]
pracoResult = mongodb["pracoResult"]
collection = mongodb["nsql"]
collection.drop()
collection.insert_many(inserter())

@flaskAPR.route('/<path:path>', methods=["POST"])
@flaskAPR.route('/', defaults={'path': ''}, methods=["POST"])
def catchall(path):
    if request.method == "POST":
        if request.form["btn"] == "register":
            username = request.form["username"]
            if username not in mariadb.session.execute(mariadb.select(Login.username)).scalars():
                register = Login(
                    username = request.form["username"],
                    password = request.form["password"]
                )
                mariadb.session.add(register)
                mariadb.session.commit()
                session["username"] = request.form["username"]
                flash("regsucces")
                return redirect(request.referrer)  
            else:
                flash("regerror")
                return redirect(request.referrer)  
        elif request.form["btn"] == "login":
            username = request.form["username"]
            password = request.form["password"]
            if username in mariadb.session.execute(mariadb.select(Login.username)).scalars():
                if password == mariadb.session.execute(mariadb.select(Login.password).where(Login.username == username)).scalar():
                    session["username"] = request.form["username"]
                    flash("loginsucces")
                    return redirect(request.referrer)  
                else:
                    flash("loginerror")
                    return redirect(request.referrer)    
            else:
                flash("loginerror")
                return redirect(request.referrer)    
        elif request.form["btn"] == "logout":
            session.pop("username")
            flash("logout")
            return redirect(request.referrer)

@flaskAPR.route("/localdb", methods=["GET", "POST"])
def localdb():
    if request.method == "GET":
        return render_template("localdb.html", databaze=db, session=session)
    elif request.method == "POST":
        if request.form["btn"] == "send":
            nazev = request.form["nazev"]
            nadpis = request.form["nadpis"]
            text = request.form["text"]
            addToDB(nazev, nadpis, text)
            return render_template("localdb.html", oznameni="Uspesne zaslano", databaze=db, session=session)
    return catchall(path)

@flaskAPR.route("/sql", methods=["GET"])
def sql():
    if request.method == "GET":
        logindb = mariadb.session.query(Login.username, Login.password)
        return render_template("sql.html", logindb=logindb, session=session)

@flaskAPR.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html", databaze=db, session=session)

@flaskAPR.route("/localdb/<id>")
def varName(id):
    localDB = []
    for value in db:
        if value[0] == id:
            localDB.append(value)
    return render_template("soubor.html", databaze=db, newDB=localDB, session=session)

def getUniverzita():
    data = {}
    fakultaID = 0
    fakultyList = []
    data["uni"] = mariadb.session.execute(mariadb.select(Univerzita.nazev)).scalar()
    fakultyAll = mariadb.session.execute(mariadb.select(Fakulta.nazev)).scalars()
    for fakulta in fakultyAll:
        fakultaID = fakultaID + 1
        fakultaLink = "/univerzita/" + str(fakultaID)
        fakultyList.append([fakultaLink, fakulta])
    data["fakultyList"] = fakultyList
    return data

def getFakulta(id):
    start = time.time()
    data = {}
    fakult = mariadb.session.query(Fakulta.nazev).filter(Fakulta.id == id).scalar()
    data["fakult"] = fakult
    allTituly = ['prof.','doc.','Dr.','DrSc.','DSc.','PaeDr.','PhDr.','Ing.','RNDr.','MUDr.','Mgr.','MgA.','et Bc.','Bc.','A.','CSc.','Ph.D.','Msc.','MBA']
    lidi = []
    pozice = []
    finalLidi = []
    lidiIDs = mariadb.session.query(Clovek.id).join(Clovek, Fakulta.fakulty).filter(Fakulta.id==id).order_by(Clovek.id).all()
    lidiQuery = mariadb.session.query(Clovek.jmeno, Clovek.prijmeni, Pozice.pozice, func.coalesce(func.concat(Titul.titul), "")).join(Clovek, Fakulta.fakulty).outerjoin(Titul, Clovek.tituly).join(Pozice, Clovek.pozices).filter(Fakulta.id==id).group_by(Clovek.id).order_by(Clovek.id).all()
    for clovek in lidiQuery:
        titulyList = []
        allTitulyIndexes = []
        titulyDone = ""
        pozice.append(clovek[2])
        jmeno = str(clovek[0]) + " " + str(clovek[1])
        tituly = clovek[3].split(',')
        allTitulyIndexes = indexLists(tituly, allTituly, allTitulyIndexes)
        zipTituly = sorted(zip(allTitulyIndexes, tituly))
        titulyList = [titul[1] for titul in zipTituly]
        allTitulyIndexes = indexLists(tituly, allTituly, allTitulyIndexes)
        for titul in titulyList:
            if allTitulyIndexes[titulyList.index(titul)] < 15:
                if len(titulyDone) == 0:
                    titulyDone = titul
                else:
                    titulyDone = titulyDone + " " + titul
            else:
                jmeno = jmeno + ", " + titul
        jmeno = titulyDone + " " + jmeno
        lidi.append(jmeno)
    for i in range(len(lidi)):
        finalLidi.append([lidi[i], pozice[i]])
    data["finalLidi"] = finalLidi
    end = time.time()
    print("Načtení z sql trvalo: " + str(end - start) + "s")
    return data, lidiIDs

def indexLists(tituly, allTituly, allTitulyIndexes):
    for titul in tituly:
            for allTitul in allTituly:
                if allTitul == titul:
                    allTitulyIndexes.append(allTituly.index(titul))
                    break
    return allTitulyIndexes

@flaskAPR.route("/univerzita")
def univerzitaRedis():
    if r.exists("univerzita"):
        start = time.time()
        textData = r.get("univerzita")
        data = pickle.loads(textData)
        print("loaded from redis")
        end = time.time()
        return render_template("univerzita.html", uni=data["uni"], fakultyList=data["fakultyList"], time="redis: " + str(end - start) + "s")
    else:
        start = time.time()
        data = getUniverzita()
        textData = pickle.dumps(data)
        r.set("univerzita", textData)
        r.expire("univerzita", redisTimeout)
        print("been saved to redis")
        end = time.time()
        print("uložení do redisu z sql trvalo: " + str(end - start) + "s")
        return render_template("univerzita.html", uni=data["uni"], fakultyList=data["fakultyList"], time="sql: " + str(end - start) + "s")

@flaskAPR.route("/univerzita/<id>")
def fakultaRedis(id):
    if r.exists("fakulta"+str(id)):
        start = time.time()
        textData = r.get("fakulta"+str(id))
        data = pickle.loads(textData)
        print("loaded from redis")
        end = time.time()
        print("Načtení z redisu trvalo: " + str(end - start) + "s")
        return render_template("fakulta.html", fakult=data["fakult"], finalLidi=data["finalLidi"], time="redis: " + str(end - start) + "s")
    else:
        start = time.time()
        data, lidiIDs = getFakulta(id)
        i = 0
        for idClovek in lidiIDs:
            ide = str(idClovek)[1:-2]
            i = i + 1
            for item in collection.find({ "_id" : ide}):
                for key, value in item.items():
                    if key != "_id":
                        data["finalLidi"][i-1].append(value)
        for clovek in data["finalLidi"]:
            if len(clovek) <= 2:
                clovek.append("")
                clovek.append("")
                clovek.append("")
        textData = pickle.dumps(data)
        r.set("fakulta"+str(id), textData)
        r.expire("fakulta"+str(id), redisTimeout)
        print("been saved to redis")
        end = time.time()
        print("uložení do redisu z sql+mongo trvalo: " + str(end - start) + "s")
        return render_template("fakulta.html", fakult=data["fakult"], finalLidi=data["finalLidi"], time="sql+mongo: " + str(end - start) + "s")

@flaskAPR.route("/redis")
def redisTable():
    start = time.time()
    data = []
    keys = r.scan_iter()
    for key in keys:
        data.append(pickle.loads(r.get(key)))
    end = time.time()
    return render_template("redis.html", redis=data, time="redis: " + str(end - start) + "s")

@flaskAPR.route("/mongo", methods=["GET", "POST"])
def mongoTable():
    if request.method == "GET":
        return loadMongo()
    elif request.method == "POST":
        if request.form["btn"][0:3] == "rem":
            id = request.form["btn"][3:5]
            collection.delete_one( { "_id": id} )
            return loadMongo()
        elif request.form["btn"][0:3] == "upd":
            id = request.form["btn"][3:5]
            pracoviste = request.form[id + "pracoviste"]
            telefon = request.form[id + "telefon"]
            email = request.form[id + "email"]
            collection.update_one({ "_id": id }, {"$set": {"pracoviste": pracoviste, "telefon": telefon, "email": email}})
            return loadMongo()
        elif request.form["btn"] == "create":
            id = request.form["createid"]
            pracoviste = request.form["createpra"]
            telefon = request.form["createtel"]
            email = request.form["createema"]
            if collection.find_one({"_id": str(id)}) == None:
                collection.insert_one({"_id": id, "pracoviste": pracoviste, "telefon": telefon, "email": email})
                return loadMongo()
            flash("invalidid")
            return loadMongo()
    return catchall(path)
        

def loadMongo():
    start = time.time()
    data = []
    col = collection.find({})
    i = 0
    for item in col:
        data.append(item)
    while True:
        i = i + 1
        if collection.find_one({"_id": str(i)}) == None:
            last = str(i)
            break

    #Email Map-Reduce
    emailMap = Code(open('mongojs/emailMap.js', 'r').read())
    emailReduce = Code(open('mongojs/emailReduce.js', 'r').read())
    emailResult.drop()
    mongodb.command({"mapReduce": "nsql", "map": emailMap, "reduce": emailReduce, "out": "emailResult" })
    emailMapRed = {"ujep": 0, "seznam": 0, "numberOfDups": 0, "emailDups": []}
    dups = 0
    ujep = 0
    seznam = 0
    for value in emailResult.find({}):
        for key, val in value.items():
            if key == "_id":
                id = val
            elif key == "value":
                for k, v in val.items():
                    if k == "emailDups" and int(v) > 1:
                        emailMapRed["emailDups"].append(id)
                        dups = dups + 1
                    elif k == "ujep" and v == True:
                        ujep = ujep + 1
                    elif k == "seznam" and v == True:
                        seznam = seznam + 1

    emailMapRed["numberOfDups"] = str(dups)
    emailMapRed["ujep"] = str(ujep)
    emailMapRed["seznam"] = str(seznam)
    
    #Pracoviste Map-Reduce
    pracoMap = Code(open('mongojs/pracoMap.js', 'r').read())
    pracoReduce = Code(open('mongojs/pracoReduce.js', 'r').read())
    pracoResult.drop()
    mongodb.command({"mapReduce": "nsql", "map": pracoMap, "reduce": pracoReduce, "out": "pracoResult" })
    pracoMapRedUnsorted = {}
    pracoMapRed = {}
    for item in pracoResult.find({}):
        for key, val in item.items():
            if key == "_id":
                k = val
            elif key == "value":
                pracoMapRedUnsorted[k] = val
    pracoMapRedAll = dict(sorted(pracoMapRedUnsorted.items(), key=lambda x:x[1], reverse=True))
    pracoMapRedAll.pop('')
    i = 0
    for key, val in pracoMapRedAll.items():
        if i < 3:
            pracoMapRed[key] = val
            i = i + 1

    end = time.time()
    return render_template("mongo.html", mongo=data, emailMapRed=emailMapRed, pracoMapRed=pracoMapRed,time="mongo: " + str(end - start) + "s", last=last)

if __name__ == "__main__":
    loadDB()
    flaskAPR.run(debug=True, host="0.0.0.0")
