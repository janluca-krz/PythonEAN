class Artikel:
    def __init__(self, name, preis, ean):
        self.name = name
        self.preis = preis
        self.ean = ean

class Kasse:
    def __init__(self):
        self.warenkorb = []
        self.artikel = [
            Artikel("Artikel 1", 10.99, "EAN1"),
            Artikel("Artikel 2", 5.99, "EAN2"),
            Artikel("Artikel 3", 7.49, "EAN3"),
            Artikel("Artikel 4", 5.49, "EAN4"),
            Artikel("Artikel 5", 6.49, "EAN5"),
            Artikel("Artikel 6", 77.49, "EAN6"),
            Artikel("Artikel 7", 71.49, "EAN7"),
            Artikel("Artikel 8", 700.49, "EAN8"),
            Artikel("Artikel 9", 701.49, "EAN9"),
            Artikel("Artikel 10", 1037.49, "EAN10"),
        ]

    def artikel_hinzufuegen(self, ean):
        for artikel in self.artikel:
            if artikel.ean == ean:
                self.warenkorb.append(artikel)
                print(f"{artikel.name} wurde dem Warenkorb hinzugefügt.")
                return
        print("Artikel nicht gefunden.")

    def gesamtpreis_anzeigen(self):
        gesamtpreis = sum(artikel.preis for artikel in self.warenkorb)
        print(f"Gesamtpreis: {gesamtpreis} EUR")

kasse = Kasse()

while True:
    print("1 - Artikel scannen")
    print("2 - Gesamtpreis anzeigen")
    print("0 - Beenden")
    auswahl = input("Auswahl: ")

    if auswahl == "1":
        ean = input("EAN scannen: ")
        if(ean == 90448638):
            kasse.artikel_hinzufuegen(ean)
        elif(ean == 8718832002964):
            kasse.artikel_hinzufuegen(ean)
        elif(ean == 4316268668668):
            kasse.artikel_hinzufuegen(ean)
        elif(ean == 42288039):
            kasse.artikel_hinzufuegen(ean)
        elif(ean == 42376101):
            kasse.artikel_hinzufuegen(ean)
        elif(ean == 5060517883607):
            kasse.artikel_hinzufuegen(ean)
        elif(ean == 90446832):
            kasse.artikel_hinzufuegen(ean)
        elif(ean == 5060751212393):
            kasse.artikel_hinzufuegen(ean)
        elif(ean == 42142379):
            kasse.artikel_hinzufuegen(ean)
        elif(ean == 358786084205477):
            kasse.artikel_hinzufuegen(ean)
        
    elif auswahl == "2":
        kasse.gesamtpreis_anzeigen()
    elif auswahl == "0":
        break
    else:
        print("Ungültige Auswahl.")
