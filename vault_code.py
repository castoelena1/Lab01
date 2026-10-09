import random
from operator import truediv

# Costanti del gioco
CODICE_MIN = 1
CODICE_MAX = 50
TENTATIVI_BASE = 6
TENTATIVI_MIN = 3
MAX_LIVELLO = 3


def dai_indizio(tentativo, codice):
    """Restituisce un indizio confrontando il tentativo con il codice segreto"""
    # TODO

    if tentativo in range(CODICE_MIN, CODICE_MAX):
        if tentativo < codice:
           return "Più alto"
        else:
            return"Più basso"

def stampa_tentativi(n, usati):
    """Stampa la riga dei tentativi: O = disponibile, X = già usato"""
    # TODO

    simboli = ["X"] * usati + ["O"] * (n - usati)
    print(" ".join(simboli))


def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco.
    Ritorna:
    * True se il giocatore indovina il codice
    * False se il giocatore esaurisce i tentativi.

    NB: Le funzioni dai_indizio() e stampa_tentativi() vanno chiamate dentro questa funzione
    """

    # Inizializzazioni
    n = TENTATIVI_BASE - livello
    if n < TENTATIVI_MIN:
        n = TENTATIVI_MIN

    codice = random.randint(CODICE_MIN, CODICE_MAX)
    usati = 0

    print(f"\nLivello {livello}) {n} tentativi")

    while usati < n:
        stampa_tentativi(n, usati)

        try:
            tentativo = int(input("Tentativo: "))
        except ValueError:
            print("Inserire un numero valido")

        if tentativo < CODICE_MIN or tentativo > CODICE_MAX:
            print(f"Il codice è tra {CODICE_MIN} e {CODICE_MAX}")
            usati += 1
        elif tentativo == codice:
            print("Accesso consentito!")
            return True
        else:
            indizio = dai_indizio(tentativo, codice)
            print(indizio)
            usati += 1

    print("GAMEOVER: Tentativi esauriti!")
    stampa_tentativi(n, usati)
    return False

    # TODO

def main():
    print("=== Benvenuto in Vault Code ===")
    livello = 0

    while livello <= MAX_LIVELLO:
        completato = gestisci_livello(livello)
        if completato:
            livello += 1
        else:
            break

    if livello > MAX_LIVELLO:
        print("\nHai superato tutti i livelli!")

if __name__ == "__main__":
    main()
