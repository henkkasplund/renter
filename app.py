from flask import Flask
from flask import render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    db = sqlite3.connect("database.db")
    db.execute("INSERT INTO visits (visited_at) VALUES (datetime('now'))")
    db.commit()
    result = db.execute("SELECT COUNT(*) FROM visits").fetchone()
    count = result[0]
    db.close()
    return "Sivua on ladattu " + str(count) + " kertaa"

@app.route("/form")
def form():
    return render_template("form.html")

# ...existing code...
@app.route("/viesti", methods=["POST"])
def viesti():
    message = request.form.get("message", "")
    return render_template("viesti.html", message=message)
# ...existing code...

@app.route("/asunto")
def asunto():
    return render_template("asunto.html")

@app.route("/ilmoitus", methods=["POST"])
def ilmoitus():
    huoneita = request.form.get("huoneita", "")
    palvelu = request.form.getlist("palvelu")
    message = request.form.get("message", "")
    # pass 'palvelus' to match ilmoitus.html template
    return render_template("ilmoitus.html", huoneita=huoneita, palvelus=palvelu, message=message)


#<img src="/static/kuva.png" />
