from asyncio.windows_events import NULL
from queue import Empty
from flask import Flask, render_template, request
import csv

db = []

with open("soubory/kek.csv", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        db.append(row)
    csvfile.close()


flaskAPR = Flask(__name__)

@flaskAPR.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", databaze=db)
    elif request.method == "POST":
        nazev = request.form["nazev"]
        nadpis = request.form["nadpis"]
        text = request.form["text"]
        with open("soubory/kek.csv", mode="r+", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_reader = csv.reader(csvfile)
            id = 1
            for row in csv_reader:
                if row is not "":
                    id = id + 1
            csv_writer.writerow([str(id), nazev, nadpis, text])
            db.append([str(id), nazev, nadpis, text])
        return render_template("index.html", oznameni="Uspesne zaslano", databaze=db)
    return render_template("index.html", databaze=db)

if __name__ == "__main__":
    flaskAPR.run(debug=True)