from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/ciel")
def page_ciel():
    return render_template("ciel.html")

@app.route("/snir")
def page_snir():
    return render_template("snir.html")

@app.route("/etudes-sup")
def page_etudes_sup():
    return render_template("etudes-sup.html")

if __name__ == "__main__":
    app.run(debug=True)
