import string

def laskut(osat: list, kirjaimet: dict):

    if osat[0][:2] == "MO":
        if osat[2] not in string.ascii_uppercase:
            kirjaimet[osat[1]] = int(osat[2])
        else:
            kirjaimet[osat[1]] = kirjaimet[osat[2]]
        
    elif osat[0][:2] == "AD":
        if osat[2] not in string.ascii_uppercase:
            kirjaimet[osat[1]] += int(osat[2])
        else:
            kirjaimet[osat[1]] += kirjaimet[osat[2]]

    elif osat[0][:2] == "SU":           
        if osat[2] not in string.ascii_uppercase:
            kirjaimet[osat[1]] -= int(osat[2])
        else:
            kirjaimet[osat[1]] -= kirjaimet[osat[2]]

    elif osat[0][:2] == "MU":
        if osat[2] not in string.ascii_uppercase:
            kirjaimet[osat[1]] *= int(osat[2])
        else:
            kirjaimet[osat[1]] *= kirjaimet[osat[2]]   

    return(kirjaimet)   

def ehdot(mJono: list, kirjaimet: dict, kohdat: dict):

    global alku
    ehtolause = mJono.split(" ")

    # muuttuja ja muuttuja
    if ehtolause[1] in string.ascii_uppercase and ehtolause[3] in string.ascii_uppercase:
        if ehtolause[2] == "==":
            if kirjaimet[ehtolause[1]] == kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == ">=":
            if kirjaimet[ehtolause[1]] >= kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)            
        elif ehtolause[2] == "<=":
            if kirjaimet[ehtolause[1]] <= kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == ">":
            if kirjaimet[ehtolause[1]] > kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == "<":
            if kirjaimet[ehtolause[1]] < kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == "!=":
            if kirjaimet[ehtolause[1]] != kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)
    # muuttuja ja int
    elif ehtolause[1] in string.ascii_uppercase and ehtolause[3] not in string.ascii_uppercase:
        if ehtolause[2] == "==":
            if kirjaimet[ehtolause[1]] == int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == ">=":
            if kirjaimet[ehtolause[1]] >= int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)            
        elif ehtolause[2] == "<=":
            if kirjaimet[ehtolause[1]] <= int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == ">":
            if kirjaimet[ehtolause[1]] > int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == "<":
            if kirjaimet[ehtolause[1]] < int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == "!=":
            if kirjaimet[ehtolause[1]] != int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)    
    # int ja muuttuja
    elif ehtolause[1] not in string.ascii_uppercase and ehtolause[3] in string.ascii_uppercase:
        if ehtolause[2] == "==":
            if int(ehtolause[1]) == kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == ">=":
            if int(ehtolause[1]) >= kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)            
        elif ehtolause[2] == "<=":
            if int(ehtolause[1]) <= kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == ">":
            if int(ehtolause[1]) > kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == "<":
            if int(ehtolause[1]) < kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == "!=":
            if int(ehtolause[1]) != kirjaimet[ehtolause[3]]:
                alku = kohdat[ehtolause[5]]
                return(1)    
    # int ja int
    elif ehtolause[1] not in string.ascii_uppercase and ehtolause[3] not in string.ascii_uppercase:
        if ehtolause[2] == "==":
            if int(ehtolause[1]) == int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == ">=":
            if int(ehtolause[1]) >= int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)            
        elif ehtolause[2] == "<=":
            if int(ehtolause[1]) <= int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
            return(1)
        elif ehtolause[2] == ">":
            if int(ehtolause[1]) > int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == "<":
            if int(ehtolause[1]) < int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)
        elif ehtolause[2] == "!=":
            if int(ehtolause[1]) != int(ehtolause[3]):
                alku = kohdat[ehtolause[5]]
                return(1)

    return(0)

def aliSuorita(ohjelma: list, tulostus: list, kohdat: dict, kirjaimet: dict):

    global alku
    global hyppy

    for i in range(alku, loppu):

        if ohjelma[i][:2] == "IF":
            hyppy = ehdot(ohjelma[i], kirjaimet, kohdat)
            
            if hyppy == 1: # hypätään jos ehto toteutui, alku-muuttujaksi asetettu hyppykohta
                break

            else:
                continue

        else:
            osat = ohjelma[i].split(" ")

            if osat[0][:2] == "PR": #lisätään PRINT käsky tulostuslistaan
    
                if osat[1] not in string.ascii_uppercase:
                    tulostus.append(int(osat[1]))
                else:
                    tulostus.append(kirjaimet[osat[1]])
        
            elif osat[0][:2] == "MO" or osat[0][:2] == "AD" or osat[0][:2] == "SU" or osat[0][:2] == "MU": # suoritetaan lasku
                kirjaimet = laskut(osat, kirjaimet)
                
            elif osat[0][:2] == "JU": # suoritetaan hyppy
                alku = kohdat[osat[1]]
                hyppy = 1
                break

            else:
                hyppy = 0
                continue
    
    return tulostus

def suorita(ohjelma: list) -> list: #pääohjelma

    global alku
    global loppu

    alku = 0
    loppu = len(ohjelma)
    tulostus = []
    kohdat = {} # hyppykohdat
    kirjaimet = {}

    # luodaan muuttujat ja alustetaan nolliksi
    for ckirjain in string.ascii_uppercase:
        kirjaimet[ckirjain] = 0

    # tallennetaan hyppykohdat sanakirjaan
    for i in range(alku, loppu):

        if ohjelma[i][:1] not in string.ascii_uppercase:
            kohdat[ohjelma[i][:-1]] = i

    # aloitetaan pääsuoritus
    while True:

        tulostus = aliSuorita(ohjelma, tulostus, kohdat, kirjaimet)

        if hyppy == 0: # jos aliSuoritus pääsi 'ohjelma'-listan loppuun eikä hyppyjä suoritettu, ohjelma päättyy
            break

    return tulostus


if __name__ == "__main__":

    ohjelma4 = []
    ohjelma4.append("MOV N 50")
    ohjelma4.append("PRINT 2")
    ohjelma4.append("MOV A 3")
    ohjelma4.append("alku:")
    ohjelma4.append("MOV B 2")
    ohjelma4.append("MOV Z 0")
    ohjelma4.append("testi:")
    ohjelma4.append("MOV C B")
    ohjelma4.append("uusi:")
    ohjelma4.append("IF C == A JUMP virhe")
    ohjelma4.append("IF C > A JUMP ohi")
    ohjelma4.append("ADD C B")
    ohjelma4.append("JUMP uusi")
    ohjelma4.append("virhe:")
    ohjelma4.append("MOV Z 1")
    ohjelma4.append("JUMP ohi2")
    ohjelma4.append("ohi:")
    ohjelma4.append("ADD B 1")
    ohjelma4.append("IF B < A JUMP testi")
    ohjelma4.append("ohi2:")
    ohjelma4.append("IF Z == 1 JUMP ohi3")
    ohjelma4.append("PRINT A")
    ohjelma4.append("ohi3:")
    ohjelma4.append("ADD A 1")
    ohjelma4.append("IF A <= N JUMP alku")
    tulos = suorita(ohjelma4)
    print(tulos)