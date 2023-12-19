def Brötchenverkauf():
    Wieviel = int(input("wieviel brötchen sollen gekauft werden: "))
    if Wieviel <= 5:
        Kosten_nur = Wieviel * 0.6
        print("es kostet ", Kosten_nur, "€")
#prüft ob es mehr oder gleich 6 brötchen sind und weniger oder gleich 15 sind und multipliziert den preis und zieht die anzahl der brötchen von der variable Wieviel ab
    if Wieviel >=6 and Wieviel <= 15:
        Kosten = 5 * 0.6
        Wieviel -= 5
        kosten_zehn = Wieviel * 0.5
        fertig = kosten_zehn + Kosten
        print("es kostet ", fertig, "€")
#prüft ob es mehr oder gleich 16 brötchen sind und multipliziert den preis und zieht die anzahl der brötchen von der variable Wieviel ab
    if Wieviel >= 16:
        Kosten = 5 * 0.6
        Wieviel -= 5
        kosten_zehn = 10 * 0.5
        Wieviel -= 10
        kosten_mehr = Wieviel * 0.3
        fertig = kosten_zehn + Kosten + kosten_mehr
        print("es kostet ", fertig, "€")

    Nochmal = input("Möchtest du nochmal welche kaufen? y/n:")
    if Nochmal == "y":
        Brötchenverkauf() #Wiederholt den vorgang
    else:
        exit()     #Beendet den code "Sauber"
        
        
Brötchenverkauf()
#Brötchenverkauf() ist ein Funktion und es funktioniert genau wie variable. Ohne print kann man abrufen.