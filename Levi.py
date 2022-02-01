def _3_elert_helyezes(lista, orszag):
    print("3)	Írja ki Chile által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
    for e in lista:
        if e.ország==orszag:
            print(e.vbeve, e.helyszin)


def _6_elert_helyezes(lista):
    print("6)	A program olvasson be egy csapat nevet és írja ki a csapat álta elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
    orszag=input("Ajon meg egy országot")
    for e in lista:
        if e.ország==orszag:
            print(e.vbeve, e.helyszin, e.helyezés)

def _9_vilagbajnokok(lista, ev):  
    print("9)	A program írja ki, hogy az '50-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.")  
    for e in lista:
        if str(e.vbeve)[-2:]==ev and e.helyezés==1:
            print(e.orszag, e.vbeve)

def _12_vilagbajnokok(lista, ev):  
    print("12)	A program írja ki, hogy az '80-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.")  
    for e in lista:
        if str(e.vbeve)[-2:]==ev and e.helyezés==1:
            print(e.orszag, e.vbeve)