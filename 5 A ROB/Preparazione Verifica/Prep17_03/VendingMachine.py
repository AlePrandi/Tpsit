"""
Modulo: vending_machine.py
Descrizione: Classe per la simulazione di un distributore automatico.
Questo modulo gestisce l'inventario dei prodotti, esegue transazioni di vendita,
gestisce il rifornimento e tiene traccia delle operazioni effettuate.
"""

import datetime

class VendingMachine:
    def __init__(self):
        """
        Inizializza il distributore con un inventario predefinito.
        L'inventario è un dizionario in cui:
            - La chiave è l'ID del prodotto
            - Il valore è un dizionario contenente nome, prezzo e quantità disponibile
        """
        self.products = {
            1: {"name": "Acqua", "price": 1.00, "stock": 10},
            2: {"name": "Bibita", "price": 1.50, "stock": 10},
            3: {"name": "Snack", "price": 2.00, "stock": 5}
        }
        self.balance = 0.0  # Totale incassato dal distributore

    def display_products(self):
        """
        Visualizza in console l'elenco dei prodotti disponibili con relativi dettagli.
        """
        print("Prodotti disponibili:")
        for pid, details in self.products.items():
            print(f"ID: {pid} - Prodotto: {details['name']}, Prezzo: €{details['price']:.2f}, Disponibilità: {details['stock']} unità")

    def vend(self, product_id, amount):
        """
        Esegue una vendita del prodotto specificato se l'importo inserito è sufficiente.

        Parametri:
            product_id (int): ID del prodotto da acquistare.
            amount (float): Importo in euro inserito dall'utente.

        Ritorna:
            float: Il resto da restituire all'utente, oppure None in caso di errore.
        """
        if product_id not in self.products:
            print("Errore: Prodotto non esistente.")
            return None

        product = self.products[product_id]

        if product['stock'] <= 0:
            print("Errore: Prodotto esaurito.")
            return None

        if amount < product['price']:
            print(f"Importo insufficiente. Prezzo richiesto: €{product['price']:.2f}")
            return None

        # Calcola il resto e aggiorna lo stock e il bilancio
        change = round(amount - product['price'], 2)
        product['stock'] -= 1
        self.balance += product['price']

        # Log della transazione
        self.transaction_log(product_id, amount, change)
        print(f"Vendita effettuata: {product['name']}. Restituito: €{change:.2f}")
        return change

    def restock(self, product_id, quantity):
        """
        Aggiunge una quantità specificata allo stock del prodotto.

        Parametri:
            product_id (int): ID del prodotto da rifornire.
            quantity (int): Quantità da aggiungere allo stock.
        """
        if product_id in self.products:
            self.products[product_id]['stock'] += quantity
            print(f"Rifornimento effettuato: {self.products[product_id]['name']} ora ha {self.products[product_id]['stock']} unità disponibili.")
        else:
            print("Errore: Prodotto non esistente.")

    def add_product(self, product_id, name, price, stock):
        """
        Aggiunge un nuovo prodotto al distributore.

        Parametri:
            product_id (int): ID univoco per il nuovo prodotto.
            name (str): Nome del prodotto.
            price (float): Prezzo di vendita del prodotto.
            stock (int): Quantità iniziale in stock.
        """
        if product_id in self.products:
            print("Errore: Prodotto già esistente con questo ID.")
        else:
            self.products[product_id] = {"name": name, "price": price, "stock": stock}
            print(f"Prodotto aggiunto: {name} (ID: {product_id}).")

    def remove_product(self, product_id):
        """
        Rimuove un prodotto dal distributore.

        Parametri:
            product_id (int): ID del prodotto da rimuovere.
        """
        if product_id in self.products:
            removed = self.products.pop(product_id)
            print(f"Prodotto rimosso: {removed['name']} (ID: {product_id}).")
        else:
            print("Errore: Prodotto non esistente.")

    def transaction_log(self, product_id, amount, change):
        """
        Registra la transazione effettuata, stampando i dettagli in console.

        Parametri:
            product_id (int): ID del prodotto venduto.
            amount (float): Importo inserito dall'utente.
            change (float): Resto restituito all'utente.
        """
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = (f"{now} - Transazione: Prodotto ID {product_id} venduto, "
                       f"importo inserito: €{amount:.2f}, resto: €{change:.2f}")
        print(log_message)

# Se il modulo viene eseguito direttamente, esegue un test di simulazione.
if __name__ == "__main__":
    vm = VendingMachine()
    
    # Visualizza i prodotti disponibili
    vm.display_products()
    
    # Simulazione di una vendita: utente sceglie il prodotto con ID 1 e inserisce €2.00
    print("\nSimulazione vendita:")
    product_to_buy = 1
    inserted_amount = 2.00
    change = vm.vend(product_to_buy, inserted_amount)
    
    # Visualizza nuovamente lo stato dei prodotti dopo la vendita
    print("\nStato aggiornato dell'inventario:")
    vm.display_products()