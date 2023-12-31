import os
import numpy as np

# Funktion zum Einlesen der Daten aus einer Textdatei in ein NumPy-Strukturiertes Array
def einlesen_und_konvertieren(datei_name):
    daten = []
    with open(datei_name, 'r') as file:
        next(file)  # Überspringe die erste Zeile
        for zeile in file:
            uhrzeit, einkaufswert = zeile.strip().split()
    
    dtype = np.dtype(         )
    return  np.array(daten, dtype=dtype)

# Dictionäre verwenden, um die Strukturierten Arrays basierend auf Filialnamen zu speichern
filialen = {}
verzeichnis = "dateien/kasse"

# Durchsuchen Sie das Verzeichnis nach Dateien
for datei_name in os.listdir(verzeichnis):
    if datei_name.endswith('.txt'):
        dateiname, _ = os.path.splitext(datei_name)
        filialname = dateiname.split('_')[0]
        datei_pfad = os.path.join(verzeichnis, datei_name)
        
        if filialname not in filialen:
            filialen[filialname] = einlesen_und_konvertieren(datei_pfad)
        else:
            # Wenn der Filialname bereits im Dictionary vorhanden ist, fügen Sie die Daten zusammen
            filialen[filialname] = 

# Ausgabe der kombinierten Strukturierten Arrays
for filialname, daten in filialen.items():
    # Maximaler Einkauf
    max_einkauf = 
    
    # Durchschnittseinkauf
    durchschnittseinkauf = 
    
    # Durchschnittseinkauf pro Stunde
    # Annahme: Die Uhrzeit ist im Format "hh:mm"
    uhrzeiten = [uhrzeit.split(':')[0] for uhrzeit in daten['Uhrzeit']] #merken welche Uhrzeiten wir haben
    stunden = list(range(8, 20))  # Öffnungszeiten von 8:00 bis 20:00 Uhr
    durchschnittseinkauf_pro_stunde = []

    for stunde in stunden:
        stunden_einkauf = []
        for i, uhr in enumerate(uhrzeiten): #für jede Uhrzeit in unseren Daten prüfen wir ob ein Einkauf vorhanden ist
            if int(uhr) == stunde:
                #merke dir: daten['Einkaufswert (EUR)'][i]

        print(stunden_einkauf)
        if stunden_einkauf: #wenn in der Stunde etwas gekauft wurde
            durchschnitt = 
        else:
            durchschnitt = 0
    	# Erzeugen einer Tupel für stunde, durchschitt und diese in den durchschnittseinkauf_pro_stunde liste setzten
        durchschnittseinkauf_pro_stunde.append((stunde, durchschnitt))

    #Ausgabe pro Filiale
    print(f'Filiale: {filialname} | Anzahl Sätze: {daten.shape[0]}')
    print(f'Maximaler Einkauf: {max_einkauf}')
    print(f'Minimaler Einkauf: {min_einkauf}')
    print(f'Durchschnittseinkauf: {durchschnittseinkauf}')
    print(f'Durchschnittseinkauf pro Stunde: {durchschnittseinkauf_pro_stunde}')
