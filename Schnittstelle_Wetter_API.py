import requests


def wetter_api_abruf():
    wetter_api = "https://api.open-meteo.com/v1/forecast?latitude=52.17&longitude=10.54&current=temperature_2m,rain,snowfall&hourly=temperature_2m,rain,snowfall,wind_speed_10m,soil_temperature_0cm&timezone=Europe%2FBerlin"
    antwort_wetter = requests.get(wetter_api)
    if antwort_wetter.status_code == 200:
        daten_wetter = antwort_wetter.json()
    else:
        print("Fehler: Die API konnte nicht richtig eingelesen werden.")
    return daten_wetter

def temperatur_ausgabe(daten_api):
    zeit = daten_api["hourly"]["time"]
    temp = daten_api["hourly"]["temperature_2m"]
    for i in range(0,len(zeit)):
        print(f"Zur Zeit: {zeit[i]} beträgt die Temperatur: {temp[i]} Grad Celsius")

temperatur_ausgabe(wetter_api_abruf())
#print(wetter_api_abruf())