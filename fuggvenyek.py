import random

szoveg = ""


def nagybetus():
    global szoveg
    szoveg = input("Kérek egy szöveget és én NAGYBETŰSSÉ alakítom!:\n>>").upper()
    return szoveg


def hosszabb_mint10():
    if len(szoveg) > 10:
        kimenet = f"Hosszabb! (Összesen {len(szoveg)} karakter hosszú)"
    else:
        kimenet = "Nem hosszabb."

    return kimenet


def betu3():
    global szoveg
    szoveg = input("Kérek egy legalább 3-betűs szöveget!:\n>>")
    while len(szoveg) < 3:
        szoveg = input("HIBA! Túl rövid a szöveg! Legalább 3 karakternek kell lennie!:\n>>")


def elso_a():
    global szoveg
    szoveg = input('Kérek egy szöveget és megkeresem az első "a"-betűt!:\n>>')
    i = 0
    elso_index = None
    c = 0
    while i < len(szoveg):
        if szoveg[i] == "a":
            if elso_index is None:
                elso_index = i
            c += 1

        i += 1
    return elso_index, c


def feketeoves():
    i = 0
    betu_lista = []
    while i < len(szoveg):
        if szoveg[i] not in betu_lista:
            betu_lista.append(szoveg[i])
        i += 1

    i = 0
    kimenet = ""

    while i < len(betu_lista):
        j = 0
        szamlalo = 0
        while j < len(szoveg):
            if betu_lista[i] == szoveg[j]:
                szamlalo += 1
            j += 1
        kimenet += f"{betu_lista[i]}: {szamlalo} darab\n"
        i += 1

    return kimenet


nevlista = []


def nev_bekero():
    global nevlista
    fut = True
    print("Kérek adjon meg neveket és azokat nagy kezdőbetűssé alakítom!\n"
          "Kilépéshez adjon meg egy @-jelet (kukac jel)!")

    while fut:
        nev = input(">> ")

        if nev != "@":
            nevlista.append(nev.capitalize())
        else:
            fut = False

    return nevlista


kor = []


def kor_ado():
    global kor

    i = 0

    while i < len(nevlista):
        rand = int(random.random() * 100) + 1
        kor.append(rand)
        i += 1

    return kor


def legidosebb_ember_kereso():
    maximum = kor[0]
    max_index = 0
    i = 1

    while i < len(kor):
        if maximum < kor[i]:
            maximum = kor[i]
            max_index = i
        i += 1

    return nevlista[max_index], maximum
