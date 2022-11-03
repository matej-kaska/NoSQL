from flask import Flask, render_template, request, session, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from os import listdir
from redis import Redis
from SQLModels import Login, Univerzita, Fakulta, Clovek, Pozice, Titul, mariadb
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



flaskAPR = Flask(__name__)
flaskAPR.app_context().push()
flaskAPR.secret_key = "a0X98Bs5Njv%^aJNO43M8rE!E3yAomIM"
flaskAPR.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://nsql:123456@82.142.110.169:3306/nsql'
flaskAPR.config['SQLALCHEMY_BINDS'] = {
    'mariadbUjep': 'mariadb+mariadbconnector://nsql:123456@82.142.110.169:3306/nsql-ujep'
}
mariadb.init_app(flaskAPR)
mariadb.create_all()

redis = Redis(host="redis", port=6379)

@flaskAPR.route('/', defaults={'path': ''}, methods=["POST"])
@flaskAPR.route('/<path:path>', methods=["POST"])
def catchall(path):
    print(path)
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
        elif request.form["btn"] == "send":
            nazev = request.form["nazev"]
            nadpis = request.form["nadpis"]
            text = request.form["text"]
            addToDB(nazev, nadpis, text)
            return render_template("index.html", oznameni="Uspesne zaslano", databaze=db, session=session)

@flaskAPR.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", databaze=db, session=session)
    elif request.method == "POST":
        if request.form["btn"] == "send":
            nazev = request.form["nazev"]
            nadpis = request.form["nadpis"]
            text = request.form["text"]
            addToDB(nazev, nadpis, text)
            return render_template("index.html", oznameni="Uspesne zaslano", databaze=db, session=session)


@flaskAPR.route("/<id>")
def varName(id):
    localDB = []
    for value in db:
        if value[0] == id:
            localDB.append(value)
    return render_template("soubor.html", databaze=db, newDB=localDB, session=session)

@flaskAPR.route("/univerzita")
def univerzita():
    fakultaID = 0
    fakultyList = []
    uni = mariadb.session.execute(mariadb.select(Univerzita.nazev)).scalar()
    fakultyAll = mariadb.session.execute(mariadb.select(Fakulta.nazev)).scalars()
    for fakulta in fakultyAll:
        fakultaID = fakultaID + 1
        fakultaLink = "/univerzita/" + str(fakultaID)
        fakultyList.append([fakultaLink, fakulta])
    return render_template("univerzita.html", uni=uni, fakultyList=fakultyList)

@flaskAPR.route("/univerzita/<id>")
def fakulta(id):
    return("cus")

if __name__ == "__main__":
    loadDB()
    flaskAPR.run(debug=True, host="0.0.0.0")
