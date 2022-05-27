from Tabla import *

#broj tri povezane od igraca
def moj_broj_mill(ja):
    broj = 0
    vec_presli = []
    for i in moja_polja(ja):
        jeste, par = jel_mill(ja, i)
        if jeste and i not in vec_presli:
            broj += 1
            vec_presli.append(par[0])
            vec_presli.append(par[1])
    return broj

#broj blokiranih figura portivnika
def broj_blokiranih_figura_protivnika(protivnik, ja):
    broj = 0
    for i in moja_polja(protivnik):
        if moguc_potez(protivnik, ja, i) == ():
            broj += 1
    return broj

#broj figura na tabli od igraca
def moj_broj_figura(igrac):
    return postavljenih(igrac)

#konfiguracija sa dve figure u liniji sa trecim praznim mestom
def potencijalni_mill(ja, protivnik):
    broj = 0
    for i in moja_polja(slobodne_pozicije(ja, protivnik)):
        if jel_mill(ja, i)[0]:
            broj += 1
    return broj

#konfiguracija sa 3 figure, tako da postoji sigurnost da ce jedna ostati prazna
def dupli_potencijalni_mill(ja, protivnik):
    broj = 0
    slobodne = moja_polja(slobodne_pozicije(ja, protivnik))
    for i in slobodne:
        jeste1, par1 = jel_mill(ja, i)
        if jeste1:
            for j in slobodne:
                jeste2, par2 = jel_mill(ja, j)
                if jeste2 and i != j and (i in par2 or par1[0] in par2 or par1[1] in par2):
                    broj += 1
    return int(broj/2)

#broj duplih 3 povezane od igraca
def dupli_mill(ja):
    broj = 0
    vec_presli = []
    for i in moja_polja(ja):
        jeste, el = jel_dupli_mill(ja, i)
        if jeste and i not in vec_presli:
            vec_presli.append(el[0][0])
            vec_presli.append(el[0][1])
            vec_presli.append(el[1][0])
            vec_presli.append(el[1][1])
            broj += 1
    return broj

#jedan potez da se mill zatvori
def otvoren_mill(protivnik, ja):
    broj = 0
    for i in moja_polja(slobodne_pozicije(ja, protivnik)):
        jeste, par = jel_mill(protivnik, i)
        if jeste:
            for j in susedna_polja(i):
                if j in moja_polja(protivnik) and j not in par:
                    broj += 1
    return broj

#da li je igrac pobedio
def pobeda(ja, protivnik):
    if jel_gotovo(ja, protivnik):
        return 1
    return 0

#broj blokiranih mill
def broj_blokiranih_mill(ja, protivnik):
    broj = 0
    prosli = []
    for i in moja_polja(protivnik):
        jeste, par = jel_mill(protivnik, i)
        if jeste and i not in prosli:
            if moguc_potez(protivnik, ja, i) == () and moguc_potez(protivnik, ja, par[0]) == () and moguc_potez(protivnik, ja, par[1]) == ():
                prosli.extend((i, par[0], par[1]))
                broj += 1
    return broj

#broj mogucih poteza
def broj_mogucih_poteza(ja, protivnik):
    broj = 0
    for i in moja_polja(ja):
        broj += len(moguc_potez(ja, protivnik, i))
    return broj


def heruistika_faza1(igrac1, igrac2):
    broj1 = 26 * moj_broj_mill(igrac1) + 10 * broj_blokiranih_figura_protivnika(igrac2, igrac1) + 6 * moj_broj_figura(igrac1) + 12 * potencijalni_mill(igrac1, igrac2) + 7 * dupli_potencijalni_mill(igrac2, igrac1) + 50 * broj_blokiranih_mill(igrac1, igrac2) + broj_mogucih_poteza(igrac1, igrac2) 
    broj2 = 26 * moj_broj_mill(igrac2) + 10 * broj_blokiranih_figura_protivnika(igrac1, igrac2) + 6 * moj_broj_figura(igrac2) + 12 * potencijalni_mill(igrac2, igrac1) + 7 * dupli_potencijalni_mill(igrac1, igrac2) + 50 * broj_blokiranih_mill(igrac2, igrac1) + broj_mogucih_poteza(igrac2, igrac1)
    return broj1 - broj2

def heruistika_faza2(igrac1, igrac2):
    broj1 = 43 * moj_broj_mill(igrac1) + 15 * broj_blokiranih_figura_protivnika(igrac2, igrac1) + 8 * moj_broj_figura(igrac1) + 70 * otvoren_mill(igrac1, igrac2) + 42 * dupli_mill(igrac1) + 1200 * pobeda(igrac2, igrac1) + 50 * broj_blokiranih_mill(igrac1, igrac2) + broj_mogucih_poteza(igrac1, igrac2)
    broj2 = 43 * moj_broj_mill(igrac2) + 15 * broj_blokiranih_figura_protivnika(igrac1, igrac2) + 8 * moj_broj_figura(igrac2) + 70 * otvoren_mill(igrac2, igrac1) + 42 * dupli_mill(igrac2) + 1200 * pobeda(igrac1, igrac2) + 50 * broj_blokiranih_mill(igrac2, igrac1) + broj_mogucih_poteza(igrac2, igrac1)
    return broj1 - broj2
