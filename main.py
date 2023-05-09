
produkte = {"Bier": 17.99, "Crack": 50, "Koks": 80}

warenkorb = []

def warenkorb_anzeigen():
    print("Warenkorb:")
    if len(warenkorb) == 0:
        print("Ihr Warenkorb ist leer.")
    else:
        for produkt in warenkorb:
            print("-", produkt)
    gesamtpreis = sum([produkte[produkt] for produkt in warenkorb])
    print("Gesamtpreis:", gesamtpreis)

def produkt_hinzufuegen():
    produkt = input("Bitte geben Sie das Produkt ein, das Sie zum Warenkorb hinzufügen möchten: \n")
    if produkt in produkte:
        warenkorb.append(produkt)
        print(produkt, "wurde zum Warenkorb hinzugefügt.")
    else:
        print("Dieses Produkt ist nicht verfügbar.")

def produkt_entfernen():
    produkt = input("Bitte geben Sie das Produkt ein, das Sie aus dem Warenkorb entfernen möchten: \n")
    if produkt in warenkorb:
        warenkorb.remove(produkt)
        print(produkt, "wurde aus dem Warenkorb entfernt.")
    else:
        print("Dieses Produkt ist nicht im Warenkorb.")

def kassensystem_starten():
    while True:
        print("Was möchten Sie tun?\n")
        print("1. Warenkorb anzeigen\n")
        print("2. Produkt hinzufügen\n")
        print("3. Produkt entfernen\n")
        print("4. Beenden\n")
        auswahl = input("Bitte geben Sie die Nummer der gewünschten Option ein: \n")
        if auswahl == "1":
            warenkorb_anzeigen()
        elif auswahl == "2":
            produkt_hinzufuegen()
        elif auswahl == "3":
            produkt_entfernen()
        elif auswahl == "4":
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine gültige Option aus.")

kassensystem_starten()
