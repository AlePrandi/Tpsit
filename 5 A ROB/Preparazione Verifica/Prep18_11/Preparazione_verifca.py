import sqlite3
import socket
import threading

rete = "192.168.0."
start_ip = 0
end_ip = 31  # 192.168.0.0/27 include 32 indirizzi (0-31)
porte_com = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995]
database_name = "ip_list.db"

# Creazione del database
def crea_database():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE hosts (
            ip_host VARCHAR(20),
            nome_host VARCHAR(20),
            port_list VARCHAR(20),
            PRIMARY KEY (ip_host)
        )
    """)
    conn.commit()
    conn.close()

def insert_database(ip_host, nome_host, port_list):
    port_list_str = ', '.join(str(port) for port in port_list)
    
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    query = f"""
        INSERT INTO hosts (ip_host, nome_host, port_list)
        VALUES ('{ip_host}','{nome_host if nome_host else "NULL"}','{port_list_str}')
    """
    cursor.execute(query)
    conn.commit()
    conn.close()


class ScanThread(threading.Thread):
    def __init__(self, ip, ports):
        super().__init__()
        self.ip = ip
        self.ports = ports

    def run(self):
        open_ports = []
        for port in self.ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  # Timeout di 1 secondo
                if sock.connect_ex((self.ip, port)) == 0:  # Porta aperta
                    open_ports.append(port)
        try:
            nome_host = socket.gethostbyaddr(self.ip)[0]
        except socket.herror:
            nome_host = None
        insert_database(self.ip, nome_host, open_ports)
        print(f"Scansione completata per {self.ip}. Porte aperte: {open_ports}")

def scan_network(start_ip, end_ip, rete, ports):
    threads = []
    for i in range(start_ip, end_ip + 1):
        ip = f"{rete}{i}"
        thread = ScanThread(ip, ports)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


def query_database():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ip_host, nome_host, port_list
        FROM hosts
        WHERE nome_host IS NOT NULL AND port_list != ''
    """)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    crea_database()
    scan_network(start_ip, end_ip, rete, porte_com)
    results = query_database()
    print("Risultati:")
    for ip_host, nome_host, port_list in results:
        print(f"IP: {ip_host}, Nome Host: {nome_host}, Porte Aperte: {port_list}")
