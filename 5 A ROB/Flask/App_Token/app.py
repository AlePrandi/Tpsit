from flask import Flask, make_response, render_template, request, redirect, url_for, jsonify
import sqlite3
import hashlib
import jwt
import datetime

app = Flask(__name__)

# Configurazione della connessione al database
DB_PATH = "./login.db"

# Dizionario per lo stato dei tasti (eventuale uso futuro)
key_state = {
    'w': False,
    'a': False,
    's': False,
    'd': False
}

SECRET_KEY = "secret_key"  # Chiave segreta per firmare i token JWT
ALGORITHM = "HS256"         # Algoritmo di firma per il JWT

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

def generate_token(username):
    """Genera un token JWT valido per 1 giorno."""
    payload = {
        "username": username,
        "exp": datetime.datetime.now() + datetime.timedelta(days=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    # jwt.encode in PyJWT >= 2.0 restituisce una stringa; in versioni precedenti potrebbe restituire un byte string.
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    return token

def verify_token(token):
    """Verifica il token JWT. Restituisce il payload se valido, altrimenti None."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        print("Il token è scaduto.")
    except jwt.InvalidTokenError:
        print("Token non valido.")
    return None

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
            # Genera il token JWT al momento del login
            token = generate_token(username)
            response = make_response(redirect(url_for('index')))
            # Imposta nei cookie sia il nome utente (per la UI) che il token
            response.set_cookie('username', username, max_age=60 * 60 * 24)  # 1 giorno
            response.set_cookie('token', token, max_age=60 * 60 * 24)
            print(f"Token generato: {token}")
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
    response.delete_cookie('token')
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

@app.route("/token_info", methods=['GET'])
def token_info():
    """
    Recupera il token dai cookie, lo verifica e stampa sia il token che il payload.
    Questa route è utile per debug o per mostrare le informazioni del token.
    """
    token = request.cookies.get('token')
    if not token:
        return jsonify({"message": "Token non trovato!"}), 400

    payload = verify_token(token)
    print("Token:", token)
    print("Payload:", payload)
    
    return jsonify({
        "token": token,
        "payload": payload
    }), 200

if __name__ == "__main__":
    app.run(debug=True, host='localhost')
