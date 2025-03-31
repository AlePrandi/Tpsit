import datetime
from flask import Flask, render_template, redirect, url_for, request, make_response
import sqlite3

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    conn = sqlite3.connect("./database.db")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("login.html", alert="username o password errate")

        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM utenti WHERE user =?", (username,))
            userDb = cur.fetchone()

        if userDb and userDb[2] == password:
            resp = make_response(redirect(url_for('attivita')))
            resp.set_cookie('username', username, max_age=60)
            return resp

    return render_template('login.html')


@app.route("/", methods=["GET", "POST"])
def index():
    username = request.cookies.get('username')
    if username:
        return redirect(url_for("attivita"))
    return redirect(url_for("login"))


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('username')
    return resp


@app.route("/aggiungi", methods=["GET", "POST"])
def attivita():
    conn = sqlite3.connect("./database.db")
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Attivita")
        atti = cur.fetchall()
        print(atti)
    if request.method == "post":
        if request.form.get('aggiungi') == "aggiungi attivita":
            desc = request.form('desc')
            user = request.cookies.get("username")[0]
            data = datetime.datetime.now()
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO Attivita (desc, data, user_Ass) VALUES (?,?,?)",
                            (desc, data, user))
                cur.fetchone()
            return render_template("attivita.html", ListaAttivita=atti)

        if request.form.get('completa') == "completa attivita":
            id = request.form("id-completa")
            with conn:
                cur = conn.cursor()
                cur.execute(
                    "UPDATE Attivita SET stato = 1 WHERE id = ?", (id,))
                cur.fetchone()
            return render_template("attivita.html", ListaAttivita=atti)

        if request.form.get('elimina') == "elimina attivita":
            return render_template("attivita.html", alert="Attività eliminata")

    return render_template("attivita.html", ListaAttivita=atti)


if __name__ == "__main__":
    app.run(debug=True, host="localhost")
