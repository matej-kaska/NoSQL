from flask import Flask, render_template, request

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