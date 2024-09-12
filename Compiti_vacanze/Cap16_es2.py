import datetime


def giorno_della_settimana():
    oggi = datetime.date.today()
    giorno_settimana = oggi.strftime("%A")
    print("Oggi è:", giorno_settimana)


def calcola_eta_e_prossimo_compleanno(data_nascita):
    oggi = datetime.date.today()
    eta = oggi.year - data_nascita.year

    prossimo_compleanno = datetime.date(
        oggi.year, data_nascita.month, data_nascita.day)
    if prossimo_compleanno < oggi:
        prossimo_compleanno = datetime.date(
            oggi.year + 1, data_nascita.month, data_nascita.day)

    giorni_rimasti = (prossimo_compleanno - oggi).days
    ore_rimaste = giorni_rimasti * 24
    minuti_rimasti = ore_rimaste * 60
    secondi_rimasti = minuti_rimasti * 60

    print(f"Età: {eta} anni")
    print(f"Giorni rimanenti al prossimo compleanno: {giorni_rimasti} giorni")
    print(f"Ore rimanenti al prossimo compleanno: {ore_rimaste} ore")
    print(f"Minuti rimanenti al prossimo compleanno: {minuti_rimasti} minuti")
    print(f"Secondi rimanenti al prossimo compleanno: {secondi_rimasti} secondi")


def giorno_del_doppio(data1, data2):
    if data1 > data2:
        data1, data2 = data2, data1

    differenza = data2 - data1
    giorno_del_doppio = data2 + differenza
    print("Il Giorno del Doppio è:", giorno_del_doppio)


def giorno_del_n_volte(data1, data2, n):
    if data1 > data2:
        data1, data2 = data2, data1

    differenza = data2 - data1
    giorno_del_n_volte = data2 + (n - 1) * differenza
    print(f"Il giorno in cui una persona ha {n} volte l'età dell'altra è:", giorno_del_n_volte)


def main():

    giorno_della_settimana()

    data_nascita = datetime.date(1990, 8, 13)
    calcola_eta_e_prossimo_compleanno(data_nascita)

    data1 = datetime.date(1990, 1, 1)
    data2 = datetime.date(1995, 1, 1)
    giorno_del_doppio(data1, data2)

    giorno_del_n_volte(data1, data2, 2)  # per il doppio
    giorno_del_n_volte(data1, data2, 3)  # per il triplo


if __name__ == "__main__":
    main()
