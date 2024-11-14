# Dieses Programm dient der Implementierung der Raumpläne als ics-Datei für die Datenbank.

import requests
from ics import Calendar

raeume = {
    "H103": "https://owa.sonia.de/owa/calendar/71e98497010c4fbea9fc2038d5910491@ostfalia.de/1814cefa83ba4e4196afde33a988e22a2402963679975286934/calendar.ics",
    "H106": "https://owa.sonia.de/owa/calendar/3a6f4d1d19a64f6b86e1d149fe5d14d9@ostfalia.de/4fafa8b120344c77bd9c3e43b8689f9c16121833101153074541/calendar.ics",
    "C101": "https://owa.sonia.de/owa/calendar/3a6f4d1d19a64f6b86e1d149fe5d14d9@ostfalia.de/4fafa8b120344c77bd9c3e43b8689f9c16121833101153074541/calendar.ics",
    "C103": "https://owa.sonia.de/owa/calendar/e8f30f16c1fd48128c6b5ac82b1bea06@ostfalia.de/bdf362e14e354da7b81e2e97f129a0fe1177157438755253548/calendar.ics"
}

def raumplan_einlesen_ics(raum):
    url = raeume[raum]
    try:
        response = requests.get(url)
        response.raise_for_status()
        calendar = Calendar(response.text)
        return calendar
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei: {e}")
        return None


class Raumplaene_ics:
    def __init__(self, raum):
        self.raum = raum
        self.raumplan = raumplan_einlesen_ics(raum)
        self.event_liste = []

        for event in sorted(self.raumplan.events, key=lambda event: event.begin):
            self.event_liste.append({
                'Name': event.name,
                'Start': event.begin,
                'Ende': event.end
            })

    def raumplan_bibliothek(self):
        bibliothek = {}
        for event in self.event_liste:
            datum = event['Start'].date().strftime("%d.%m.%Y")
            startzeit = event['Start'].time().strftime("%H:%M")
            endzeit = event['Ende'].time().strftime("%H:%M")
            name = event['Name']

            if datum not in bibliothek:
                bibliothek[datum] = [[startzeit, endzeit, name]]
            else:
                bibliothek[datum].append([startzeit, endzeit, name])
        print(bibliothek)

Raumplaene_ics("H103").raumplan_bibliothek()
