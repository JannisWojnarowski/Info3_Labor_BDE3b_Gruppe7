import pymysql
from unittest.mock import Mock
#from schnittstelle_raumplaene import Raumplaene

class Raumplaene:
    def __init__(self):
        pass

    def get_Raumplaene(self):
        pass

# Verbindung zur Datenbank herstellen
connection = pymysql.connect(host = '127.0.0.1',
                                user = 'root',
                                password = '',
                                database = 'heizungssystem')
# Cursor erstellen
cursor = connection.cursor()

# Tabelle Raeume erstellen

raeume = {"H103": 1}

# Daten für die Tabelle Raeume definieren
raumh103 = Raumplaene()
raumh103.get_Raumplaene = Mock(return_value = {'28.08.2024': [['16:00', '17:00', 'Meier, Jean-Michel Meeting']],
'29.08.2024': [['10:00', '11:00', 'Poll, Inga Kolloquium Frau Lengert'], ['11:30', '12:30', 'Poll, Inga Kolloquium Frau Meyer']],
'19.09.2024': [['10:30', '11:30', 'Poll, Inga Kolloquium Frau Henke']],
'23.09.2024': [['11:30', '12:00', 'MAP Rechnereinführung Homeister'], ['12:00', '13:30', 'Poll EinfVWL']],
'24.09.2024': [['08:00', '08:30', 'Menzel ProzessAddFert'], ['10:00', '11:30', 'Menzel Statistik'], ['12:00', '13:30', 'NIEL WkMoStähle']],
'25.09.2024': [['08:00', '09:30', 'NIEL VerbundKst'], ['10:00', '11:30', 'Poll ExtReWe'], ['12:00', '13:00', 'Poll, Inga Kolloquium Herr Al-Roussan']],
'26.09.2024': [['10:00', '11:30', 'Borbe/MeyJo SimSpanFertSys'], ['12:00', '13:30', 'Engel MaschLern']],
'28.09.2024': [['09:00', '13:00', 'MAP Mengedoht PA1 (LEGO)']],
'30.09.2024': [['16:00', '17:00', 'Haas, Franz-Gregor Absprache Vorgehen mit AWO']],
'11.10.2024': [['14:15', '15:45', 'Neuhaus-Steinmetz, Maximilian Jour fixe - Batteriesortierung - 4. Semesterprojekt'], ['16:00', '21:30', 'MAP Germer/Peters FMT']],
'12.10.2024': [['08:00', '17:00', 'MAP Germer/Peters FMT']],
'23.10.2024': [['09:00', '10:00', 'Rambke, Martin Seminarvortrag Frau Bergmann']],
'28.10.2024': [['13:00', '14:00', 'Brüggemann, Holger Seminarvortrag Blankenburg']],
'29.10.2024': [['14:30', '16:00', 'Haas, Franz-Gregor Besprechung']],
'30.10.2024': [['10:00', '12:00', 'Neuhaus-Steinmetz, Maximilian Raum blocken 103'], ['13:30', '15:00', 'NIEL Kolloq Henking']],
'06.11.2024': [['10:30', '11:30', 'Triltsch, Udo Kolloquium Hr. Eisenbach']],
'13.11.2024': [['10:00', '12:00', 'Neuhaus-Steinmetz, Maximilian Kraftknoten - Pose Estimation - Developments']],
'14.11.2024': [['13:30', '14:30', 'Info3 VorKolloqs']],
'20.11.2024': [['10:00', '11:30', 'Info3 VorKolloqs']],
'25.11.2024': [['08:00', '17:00', 'NiFaR-Schulung MAN']],
'27.11.2024': [['13:00', '14:00', 'Triltsch, Udo Seminarvortrag Herr Baloh']],
'17.12.2024': [['14:30', '15:30', 'Brüggemann, Holger Kolloq Wotschall']],
'17.01.2025': [['15:00', '18:00', 'MAP Proj.präsentationen I+II']]}
)

raumplanh103 = raumh103.get_Raumplaene()

for raumname in raeume:
    cursor.execute("INSERT IGNORE INTO Raeume (Raumname) VALUES (raumname)")

# Tabelle für jeden Raum erstellen und Daten einfügen
for raumname, raumid in raeume.items():
    # Tabelle für den Raum erstellen
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {raumname} (Datum VARCHAR(12), Beginn VARCHAR(5), Ende VARCHAR(5), Veranstaltung_Dozent VARCHAR(255))")
    raumplanh103 = raumh103.get_Raumplaene()
    for tage in raumplanh103:
        cursor.execute(f"INSERT INTO {raumname} (Datum, Beginn, Ende, Veranstaltung_Dozent) VALUES ('{tage}', '{raumh103.get_Raumplaene[tage][0][0]}', '{raumh103.get_Raumplaene[tage][0][1]}', '{raumh103.get_Raumplaene[tage][0][2]}')")

