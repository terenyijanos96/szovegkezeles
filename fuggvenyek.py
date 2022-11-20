szoveg = ""


def nagybetus():
    global szoveg
    szoveg = input("Kérek egy szöveget és én NAGYBETŰSSÉ alakítom!:\n>>").upper()
    return szoveg


def hosszabb_mint10():
    kimenet = False

    if len(szoveg) > 10:
        kimenet = len(szoveg)

    return kimenet


def betu3():

    szoveg = input("Kérek egy legalább 3-betűs szöveget!:\n>>")
    while len(szoveg) < 3:
        szoveg = input("HIBA! Túl rövid a szöveg! Legalább 3 karakternek kell lennie!:\n>>")


def elso_a():
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
