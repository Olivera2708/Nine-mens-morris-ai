from Tabla import *

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

def broj_blokiranih_figura_protivnika(protivnik, ja):
    broj = 0
    for i in moja_polja(protivnik):
        if moguc_potez(protivnik, ja, i) == []:
            broj += 1
    return broj

def moj_broj_figura(igrac):
    return postavljenih(igrac)

def potencijalni_mill(ja, protivnik):
    broj = 0
    for i in moja_polja(slobodne_pozicije(ja, protivnik)):
        if jel_mill(ja, i)[0]:
            broj += 1
    return broj

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
    return broj/2


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

def heruistika_faza1(igrac1, igrac2):
    broj1 = 26 * moj_broj_mill(igrac1) + broj_blokiranih_figura_protivnika(igrac2, igrac1) + 9 * moj_broj_figura(igrac1) + 10 * potencijalni_mill(igrac1, igrac2) + 7 * dupli_potencijalni_mill(igrac2, igrac1)
    broj2 = 26 * moj_broj_mill(igrac2) + broj_blokiranih_figura_protivnika(igrac1, igrac2) + 9 * moj_broj_figura(igrac2) + 10 * potencijalni_mill(igrac2, igrac1) + 7 * dupli_potencijalni_mill(igrac1, igrac2)
    return broj1- broj2

def heruistika_faza2(igrac1, igrac2):
    broj1 = 43 * moj_broj_mill(igrac1) + 10 * broj_blokiranih_figura_protivnika(igrac2, igrac1) + 11 * moj_broj_figura(igrac1) + 8 * dupli_mill(igrac1)
    broj2 = 43 * moj_broj_mill(igrac2) + 10 * broj_blokiranih_figura_protivnika(igrac1, igrac2) + 11 * moj_broj_figura(igrac2) + 8 * dupli_mill(igrac2)
    return broj1-broj2
