import pickle

filename = 'betalinger.pk'
fodboldtur ={}

PRIS = 4500  # Total pris pr. person

# Gemmer alle data i filen
def gem_data():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()

# Registrer betaling fra et medlem
def registrer_betaling():
    navn_input = input("Indtast navn på medlem: ")
    beløb = float(input("Indtast beløb: "))

    # Find eksisterende medlemmer uanset store/små bogstaver
    eksisterende = None
    for medlem in fodboldtur:
        if medlem.lower() == navn_input.lower():
            eksisterende = medlem
            break

    if eksisterende:
        fodboldtur[eksisterende] += beløb
        print(f"{eksisterende} har nu i alt indbetalt {fodboldtur[eksisterende]} kr.\n")

    # Nye medlemmer
    else:
        fodboldtur[navn_input] = beløb
        print(f"{navn_input} er tilføjet med indbetaling på {beløb} kr.\n")

    gem_data()  # Gem data efter ændring
    menu()

# Udskriv oversigt over alle medlemmer
def printliste():
    print("\n--- Betalingsoversigt ---")
    for navn, betalt in fodboldtur.items():
        mangler = PRIS - betalt
        if mangler <= 0:
            print(f"{navn}: {betalt} kr. (FULDT BETALT)")
        else:
            print(f"{navn}: {betalt} kr. (mangler {mangler} kr.)")
    print("-------------------------------------\n")
    menu()

# Vis de tre medlemmer, der mangler mest
def top3_mangler():
    if not fodboldtur:
        print("Ingen betalinger registreret endnu.")
    else:
        # Sortere de top 3 der mangler mest
        sorteret = sorted(fodboldtur.items(), key=lambda x: (PRIS - x[1]), reverse=True)
        print("\n--- Top 3 der mangler mest ---")
        for navn, betalt in sorteret[:3]:
            mangler = PRIS - betalt
            if mangler > 0:
                print(f"{navn}: mangler {mangler} kr.")
        print("------------------------------\n")
    menu()

# Nulstil listen
def nulstil_liste():
    for medlem in fodboldtur:
        fodboldtur[medlem] = 0  # Sæt alle indbetalinger til 0
        gem_data()  # Gem ændringerne
    print("\nAlle indbetalinger er nulstillet!\n")
    menu()

# Afslut programmet
def afslut():
    gem_data()
    print("\nProgrammet er afsluttet!")

# Menu
def menu():
    print("MENU")
    print("1: Registrer betaling")
    print("2: Print liste")
    print("3: Vis top 3 der mangler mest")
    print("4: Nulstil betalinger")
    print("5: Afslut program")
    valg = input("Indtast dit valg: ")
    if valg == '1':
        registrer_betaling()
    elif valg == '2':
        printliste()
    elif valg == '3':
        top3_mangler()
    elif valg == '4':
        nulstil_liste()
    elif valg == '5':
        afslut()

# Start programmet
infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()