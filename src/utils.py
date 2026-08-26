# src/utils.py

def format_message(msg):
    # funzione semplice che dovrebbe restituire una stringa formattata
    return f"[aarp] {msg}"

def compute_sum(values):
    # intenzionalmente un errore di tipo/sintassi: usa '+' su None o ritorna stringa
    total = None
    for v in values:
        total = total + v  # errore: total inizializzato a None -> TypeError
    # ritorna stringa invece di int per simulare comportamento sbagliato
    return str(total)

