from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import time
import datetime
from semaforo import semaforo

app = Flask(__name__)
app.secret_key = "segreto123"

def init_db():
    with sqlite3.connect("semaforo.db") as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS log (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        utente TEXT,
                        azione TEXT,
                        timestamp TEXT)''')
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['utente'] = request.form['user']
        session['password'] = request.form['psw']
        return redirect(url_for('configurazione'))
    return render_template('login.html')

@app.route('/configurazione', methods=['GET', 'POST'])
def configurazione():
    if 'utente' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        verde = int(request.form['verde'])
        giallo = int(request.form['giallo'])
        rosso = int(request.form['rosso'])
        session['durate'] = {'verde': verde, 'giallo': giallo, 'rosso': rosso}
    
    return render_template('configurazione.html')

@app.route('/spegni')
def spegni():
    if 'utente' in session:
        utente = session['utente']
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sqlite3.connect("semaforo.db") as conn:
            c = conn.cursor()
            c.execute("INSERT INTO log (utente, azione, timestamp) VALUES (?, ?, ?)", (utente, 'spento', timestamp))
            conn.commit()
    
    session['stato'] = 'spento'
    return redirect(url_for('configurazione'))

@app.route('/riattiva')
def riattiva():
    if 'utente' in session:
        utente = session['utente']
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sqlite3.connect("semaforo.db") as conn:
            c = conn.cursor()
            c.execute("INSERT INTO log (utente, azione, timestamp) VALUES (?, ?, ?)", (utente, 'riattivato', timestamp))
            conn.commit()
    
    session['stato'] = 'attivo'
    return redirect(url_for('configurazione'))

@app.route('/test')
def test_semaforo():
    sem = semaforo()
    stato = session.get('stato', 'attivo')
    durate = session.get('durate', {'verde': 5, 'giallo': 2, 'rosso': 5})
    
    if stato == 'spento':
        for _ in range(3):
            sem.giallo(1)
            sem.luci_spente(1)
    else:
        sem.verde(durate['verde'])
        sem.giallo(durate['giallo'])
        sem.rosso(durate['rosso'])
    
    return "Test completato. Controlla la console."

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
