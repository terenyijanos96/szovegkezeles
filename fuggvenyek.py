szoveg = ""


def nagybetus():
    global szoveg
    szoveg = input("Kérek egy szöveget és én NAGYBETŰSSÉ alakítom!:\n>>").upper()
    return szoveg


def hosszabb_mint10():
    if len(szoveg) > 10:
        return len(szoveg)

    return False


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
    global szoveg
    betu_ista = []
    betu_szam_lista = []

    i = 0
    while i < len(szoveg):
        if szoveg[i] not in betu_ista:
            betu_ista.append(szoveg[i])
        i += 1

    i = 0

    while i < len(betu_ista):
        j = 0

        while j < len(szoveg):
            if betu_ista[i] == szoveg[i]:
                c+=1
            j+=1
            betu_szam_lista.append(c)
        i += 1

    print(betu_ista)
    print(betu_szam_lista)

