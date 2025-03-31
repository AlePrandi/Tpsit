from flask import Flask, render_template, redirect, url_for, request, make_response
import sqlite3
import hashlib
from VendingMachine import VendingMachine

vm = VendingMachine()

app = Flask(__name__)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = sqlite3.connect("./distributore.db")
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username =?", (username,))
            userDb = cur.fetchone()
            print(userDb)

        if userDb and userDb[2] == hash_password(password):
            if userDb[3] == "adm":
                resp = make_response(redirect(url_for('admin')))
            else:
                resp = make_response(redirect(url_for('products')))
            resp.set_cookie('username', username, max_age=60)
            return resp

    return render_template('login.html')


@app.route('/registra', methods=['GET', 'POST'])
def registra():
    conn = sqlite3.connect("./distributore.db")
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = request.form.get('user')

        if not username or not password:
            return render_template('registra.html', alert="Inserisci tutti i dati richiesti!")

        password_hash = hash_password(password)

        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, password, user) VALUES (?, ?, ?)",
                        (username, password_hash, user))
            userDb = cur.fetchone()
            print(userDb)
        return render_template('login.html')

    return render_template('registra.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    resp = None
    if request.method == 'POST':
        if request.form.get('action-logout') == "logout":
            resp = make_response(redirect(url_for('login')))
            resp.delete_cookie('username')
            return resp

        if request.form.get('action-aggiungere') == "aggiungi prodotto":
            id = int(request.form['id'])
            nome = request.form['nome']
            prezzo = float(request.form['prezzo'])
            qt = int(request.form['qt'])
            print(id, nome, prezzo, qt)
            vm.add_product(id, nome, prezzo, qt)

        if request.form.get('action-rimuovere') == "rimuovi prodotto":
            id = int(request.form["id_rimosso"])
            print(id)
            vm.remove_product(id)

        if request.form.get('action-modifica') == "modifica quantità":
            id = int(request.form["id_modifica"])
            qt = int(request.form["qt_modifica"])
            print(id, qt)
            vm.restock(id, qt)

    return render_template('admin.html', products=vm.products)


@app.route('/user', methods=['GET', 'POST'])
def user():
    saldo = 0
    resto = 0
    if request.method == 'POST':
        saldo = request.form['quantity']
        for i in range(0, len(vm.products)+1):
            if request.form.get('product_id') == f"{i}":
                print(vm.products[i])
                if float(vm.products[i]["price"]) < float(saldo):
                    resto = vm.vend(i, float(saldo))
                    print(f"Resto: {resto}")
                else:
                    print("saldo insufficente")
                saldo = resto
    return render_template('products.html', products=vm.products, saldo=saldo)


@app.route('/', methods=['GET', 'POST'])
def index():
    username = request.cookies.get('username')
    print(username)
    if username:
        conn = sqlite3.connect("./distributore.db")
        with conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT tipo FROM users WHERE username = ?", (username))
            user_tipo = cur.fetchone()[0]
            print(user_tipo)
            if user_tipo == "adm":
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('user'))
    return redirect(url_for('login'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('username')
    return resp


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
