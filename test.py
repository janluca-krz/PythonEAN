registrierte_benutzer = {
    "Lavinc": "Schlagsahne123",
    "Nick": "Huansohn",
    "Luca": "Schlagsahne123"
}

 

produkte = []
warenkorb = []

produkte.append({"ean": "8718832002964", "Produkt-name": "Nutten", "Preis": 40})
produkte.append({"ean": "3987460091367", "Produkt-name": "Koks", "Preis": 80})
produkte.append({"ean": "3098446788125", "Produkt-name": "Pizza", "Preis": 8.99})
produkte.append({"ean": "3298445689125", "Produkt-name": "Bier", "Preis": 17.99})
produkte.append({"ean": "9893278490125", "Produkt-name": "Escorts", "Preis": 2000})
produkte.append({"ean": "8170946783997", "Produkt-name": "Apfle", "Preis": 2.35})
produkte.append({"ean": "1198346789873", "Produkt-name": "Bannane", "Preis": 3.47})
produkte.append({"ean": "2918765408461", "Produkt-name": "Crack", "Preis": 60})
produkte.append({"ean": "8170946783997", "Produkt-name": "Schere", "Preis": 6})
produkte.append({"ean": "8398981877445", "Produkt-name": "pc", "Preis": 10})


 

def anmelden():
    while True:
        benutzername = input("Benutzername: ")
        passwort = input("Passwort: ")

 

        if benutzername in registrierte_benutzer and registrierte_benutzer[benutzername] == passwort:
            print("Anmeldung erfolgreich!")
            main_menu()
            break
        else:
            print("Ungültiger Benutzername oder Passwort. Bitte versuche es erneut.")

 

def main_menu():
    while True:
        print("|---- Wählen Sie eine Option ----|")
        print("|                                |")
        print("|1: EAN checker                  |")
        print("|2: Produkt hinzufügen           |")
        print("|3: Produkt entfernen            |")
        print("|4: Kassenbon                    |")
        print("|5: Artikel suchen               |")
        print("|6: Abmelden                     |")
        print("|--------------HS----------------|")

 

        choice = input(">> ").upper()

 

        if choice == "1":
            barcode = input("Bitte geben Sie den 12-stelligen Barcode ein: ")
            pz = berechne_pz(barcode)
            if pz is not None:
                print("Berechnete Prüfziffer:", pz)
        elif choice == "2":
            artikel_hinzufuegen()
        elif choice == "3":
            artikel_entfernen()
        elif choice == "4":
            kassenbon()
        elif choice == "5":
            artikel_suchen()
        elif choice == "6":
            print("Abmelden...")
            anmelden()
            break
        else:
            print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")

 

def artikel_hinzufuegen():
    produkt = input("Bitte geben Sie das Produkt ein, das Sie zum Warenkorb hinzufügen möchten: ")
    for p in produkte:
        if p["ean"] == produkt:
            warenkorb.append(p)
            print(produkt, "wurde zum Warenkorb hinzugefügt.")
            return
    print("Dieses Produkt ist nicht verfügbar.")

 

def artikel_entfernen():
    produkt = input("Bitte geben Sie das Produkt ein, das Sie aus dem Warenkorb entfernen möchten: ")
    for p in warenkorb:
        if p["Produkt-name"] == produkt:
            warenkorb.remove(p)
            print(produkt, "wurde aus dem Warenkorb entfernt.")
            return
    print("Dieses Produkt befindet sich nicht im Warenkorb.")

 

def kassenbon():
    print("Kassenbon:")
    print("----------------------")
    total = 0
    for p in warenkorb:
        print(p["Produkt-name"], "- Preis:", p["Preis"])
        total += p["Preis"]
    print("----------------------")
    print("Gesamt:", total)

 

def artikel_suchen():
    produkt = input("Bitte geben Sie den Namen des gesuchten Produkts ein: ")
    for p in produkte:
        if p["Produkt-name"] == produkt:
            print("Produkt gefunden:")
            print("Name:", p["Produkt-name"])
            print("Preis:", p["Preis"])
            return
    print("Produkt nicht gefunden.")

 

def berechne_pz(barcode: str) -> int:
    if not barcode.isdigit() or len(barcode) != 12:
        print("Ungültige Eingabe.")

 

    summe = 0
    for i in range(12):
        if i % 2 == 0:
            summe += int(barcode[i])
        else:
            summe += int(barcode[i]) * 3

 

    check_pz = (10 - (summe % 10)) % 10
    return check_pz

 


anmelden()
