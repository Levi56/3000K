def _1_elert_helyezes(lista, ország):
    for e in lista:
        if e.ország == ország:
            print(e.vbeve, e.helyszin)
