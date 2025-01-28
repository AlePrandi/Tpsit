from flask import Flask, render_template, request
import socket
import threading
import time

# Configurazione del server Alphabot
SERVER_ADDRESS = ("192.168.1.140", 9600)
HEARTBEAT_ADDRESS = ("192.168.1.140", 9601)

# Socket principale per i comandi
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(SERVER_ADDRESS)

# Stato dei tasti
key_state = {
    'w': False,
    'a': False,
    's': False,
    'd': False
}

# Velocità base
BASE_SPEED = 50
CURVE_SPEED = 50
TURN_ADJUST = 30  # Differenza di velocità tra le due ruote per girare gradualmente

lock = threading.Lock()

# Stato precedente dei motori
previous_motor_state = (0, 0)

# Flag per controllo dei thread
threads_running = True

def send_heartbeat():
    """Gestisce l'heartbeat inviando messaggi regolari al server."""
    heart_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        heart_socket.connect(HEARTBEAT_ADDRESS)
        while threads_running:
            try:
                heart_socket.sendall("ciao".encode())
                time.sleep(1)  # Invio heartbeat ogni secondo
            except Exception as e:
                print(f"Errore durante l'invio dell'heartbeat: {e}")
                break
    finally:
        heart_socket.close()

def calculate_motor_values():
    """Calcola i valori dei motori in base allo stato dei tasti."""
    global key_state
    left_speed = 0
    right_speed = 0

    with lock:
        if key_state['w']:
            left_speed += BASE_SPEED
            right_speed += BASE_SPEED
        if key_state['s']:
            left_speed -= BASE_SPEED
            right_speed -= BASE_SPEED

        # Gestione di 'a' e 'd'
        if key_state['a'] and not key_state['w'] and not key_state['s']:
            # Se solo 'a' è premuto, gira a sinistra gradualmente
            left_speed = -CURVE_SPEED // 2
            right_speed = CURVE_SPEED // 2
        elif key_state['d'] and not key_state['w'] and not key_state['s']:
            # Se solo 'd' è premuto, gira a destra gradualmente
            left_speed = CURVE_SPEED // 2
            right_speed = -CURVE_SPEED // 2
        else:
            # Regolazioni per svolte durante avanti o indietro
            if key_state['a']:
                left_speed -= TURN_ADJUST
                right_speed += TURN_ADJUST
            if key_state['d']:
                left_speed += TURN_ADJUST
                right_speed -= TURN_ADJUST

    return left_speed, right_speed

def update_motor_values():
    """Invia i valori dei motori al server solo quando cambiano."""
    global previous_motor_state
    while threads_running:
        left_speed, right_speed = calculate_motor_values()
        motor_state = (left_speed, right_speed)

        # Invia solo se lo stato dei motori è cambiato
        if motor_state != previous_motor_state:
            message = f"{left_speed},{right_speed}"
            try:
                s.sendall(message.encode())
                previous_motor_state = motor_state
            except Exception as e:
                print(f"Errore durante l'invio dei comandi: {e}")
                break

# Creazione dell'app Flask
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    global key_state
    if request.method == 'POST':
        with lock:
            key_state = {
                'w': request.form.get('avanti') == 'value1',
                's': request.form.get('indietro') == 'value2',
                'a': request.form.get('sinistra') == 'value3',
                'd': request.form.get('destra') == 'value4'
            }
    return render_template("index.html")

def main():
    """Funzione principale per gestire client, heartbeat e tasti."""
    global threads_running

    # Thread per heartbeat e aggiornamento motori
    heartbeat_thread = threading.Thread(target=send_heartbeat)
    motor_thread = threading.Thread(target=update_motor_values)

    threads_running = True
    heartbeat_thread.start()
    motor_thread.start()

    try:
        app.run(debug=True, host='localhost')
    except KeyboardInterrupt:
        print("Chiusura del client...")
    finally:
        # Arresto sicuro dei thread
        threads_running = False
        heartbeat_thread.join()
        motor_thread.join()
        s.close()

if __name__ == '__main__':
    main()

