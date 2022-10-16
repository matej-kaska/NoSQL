from flask import Flask, render_template, request
<<<<<<< Updated upstream
=======
import csv
from os import listdir
path = "NoSQL/NoSQL_seminarka/soubory/"
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
    writeLineInFile(path + str(id) + "." + endOfFile, nazev + separator + nadpis + separator + text)
    db.append([id, nazev, nadpis, text])

>>>>>>> Stashed changes

db = {
    1 : "Poseidon Vltavy",
    2 : "Tyler Durden"
}

flaskAPR = Flask(__name__)

@flaskAPR.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", databaze=db)
    elif request.method == "POST":
        text = request.form["text"]
        db[len(db) + 1] = text
        return render_template("index.html", oznameni="Uspesne zaslano", databaze=db)
    return render_template("index.html", databaze=db)

if __name__ == "__main__":
    flaskAPR.run(debug=True)