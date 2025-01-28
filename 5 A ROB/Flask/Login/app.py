from flask import Flask, make_response, render_template, request, redirect, url_for, jsonify
import sqlite3
import hashlib

app = Flask(__name__)

# Configurazione della connessione al database
DB_PATH = "./login.db"

key_state = {
    'w': False,
    'a': False,
    's': False,
    'd': False
}


def get_db_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # Abilita accesso tipo dizionario alle righe
        return conn
    except sqlite3.Error as e:
        print(f"Errore durante la connessione al database: {e}")
        return None

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('e-mail')
        password = request.form.get('password')

        if not username or not password:
            return render_template('login.html', alert="Inserisci username e password!")

        password_hash = hash_password(password)

        query_login = """ 
            SELECT * 
            FROM credenziali 
            WHERE username = ? AND password = ?
        """

        with get_db_connection() as conn:
            if conn:
                cur = conn.cursor()
                cur.execute(query_login, (username, password_hash))
                user = cur.fetchone()

        if user:
            response = make_response(redirect(url_for('index')))
            response.set_cookie('username', username, max_age=60 * 60 * 24)  # durata un giorno
            return response
        else:
            return render_template('login.html', alert="Credenziali non valide!")
    return render_template('login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form.get('e-mail')
        password = request.form.get('password')

        if not username or not password:
            return render_template('create_account.html', alert="Inserisci tutti i dati richiesti!")

        password_hash = hash_password(password)

        query_insert = """
            INSERT INTO credenziali (username, password)
            VALUES (?, ?)
        """

        with get_db_connection() as conn:
            if conn:
                cur = conn.cursor()
                try:
                    cur.execute(query_insert, (username, password_hash))
                    conn.commit()
                    return redirect(url_for('login'))
                except sqlite3.IntegrityError:
                    return render_template('create_account.html', alert="Username già esistente!")
    return render_template('create_account.html')

@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(redirect(url_for('login')))
    response.delete_cookie('username')
    return response

@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return render_template('index.html', username=username)
    return redirect(url_for('login'))

@app.route("/key_event", methods=['POST'])
def key_event():
    data = request.json
    key = data.get('key')
    state = data.get('state')  # True = premuto, False = rilasciato

    if key in key_state:
        key_state[key] = state
        if state:
            print(f"Tasto premuto: {key}")
        else:
            print(f"Tasto rilasciato: {key}")
        return jsonify({"success": True}), 200
    return jsonify({"success": False}), 400

if __name__ == "__main__":
    app.run(debug=True, host='localhost')
