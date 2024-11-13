# Dieses Programm dient der Implementierung der Raumpläne für die Datenbank.

import pandas as pd

def raumplan_einlesen(raum):
    dateiname = str(raum) + ".csv"
    try:
        raumplan = pd.read_csv(dateiname, sep=';', on_bad_lines='skip')
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei: {e}")
        raumplan = None
    return raumplan

def raumplan_datum(raumplan):
    datum = raumplan["Datum"]
    return datum

def raumplan_beginn(raumplan):
    beginn = raumplan["Beginn"]
    return beginn

def raumplan_ende(raumplan):
    ende = raumplan["Ende"]
    return ende

def raumplan_veranstaltung(raumplan):
    veranstaltung = raumplan["Veranstaltung"]
    return veranstaltung

def raumplan_dozent(raumplan):
    dozent = raumplan["Dozent"]
    return dozent

def raumplan_dozentenplan(raumplan):
    dozentenplan = raumplan["Dozentenplan"]
    return dozentenplan


class Raumplaene:
    def __init__(self, raum):
        self.raum = raum
        self.raumplan = raumplan_einlesen(raum)
        self.datum = raumplan_datum(self.raumplan)
        self.beginn = raumplan_beginn(self.raumplan)
        self.ende = raumplan_ende(self.raumplan)
        self.veranstaltung = raumplan_veranstaltung(self.raumplan)
        self.dozent = raumplan_dozent(self.raumplan)
        self.dozentenplan = raumplan_dozentenplan(self.raumplan)

    def raumplan_bibliothek(self):
        bibliothek = {}
        for i in range(0,len(self.datum)):
            if bibliothek.get(self.datum[i]) == None:
                bibliothek[self.datum[i]] = [[self.beginn[i], self.ende[i], self.veranstaltung[i], self.dozent[i], self.dozentenplan[i]]]
            elif bibliothek.get(self.datum[i]) != None:
                bibliothek[self.datum[i]].append([self.beginn[i], self.ende[i], self.veranstaltung[i], self.dozent[i], self.dozentenplan[i]])
        print(bibliothek)

    def raumplan_ausgabe(self):
        for i in range(0,len(self.datum)):
            print(f"Am {self.datum[i]} von {self.beginn[i]} bis {self.ende[i]} Uhr ist der Raum {self.raum} belegt.")

Raumplaene("A067").raumplan_bibliothek()
