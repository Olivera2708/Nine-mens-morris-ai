from Tabla import *
from hashmap import LinearHashMap


hash_map_1 = LinearHashMap()
hash_map_1[1] = 26
hash_map_1[2] = 1
hash_map_1[3] = 6
hash_map_1[4] = 12
hash_map_1[5] = 7

hash_map_2 = LinearHashMap()
hash_map_2[1] = 43
hash_map_2[2] = 10
hash_map_2[3] = 8
hash_map_2[4] = 7
hash_map_2[5] = 42
hash_map_2[6] = 1086

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
        if moguc_potez(protivnik, ja, i) == []:
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
    return broj/2

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


def heruistika_faza1(igrac1, igrac2):
    broj1 = hash_map_1[1] * moj_broj_mill(igrac1) + hash_map_1[2] * broj_blokiranih_figura_protivnika(igrac2, igrac1) + hash_map_1[3] * moj_broj_figura(igrac1) + hash_map_1[4] * potencijalni_mill(igrac1, igrac2) + hash_map_1[5] * dupli_potencijalni_mill(igrac2, igrac1)
    broj2 = hash_map_1[1] * moj_broj_mill(igrac2) + hash_map_1[2] * broj_blokiranih_figura_protivnika(igrac1, igrac2) + hash_map_1[3] * moj_broj_figura(igrac2) + hash_map_1[4] * potencijalni_mill(igrac2, igrac1) + hash_map_1[5] * dupli_potencijalni_mill(igrac1, igrac2)
    return broj1- broj2

def heruistika_faza2(igrac1, igrac2):
    broj1 = hash_map_2[1] * moj_broj_mill(igrac1) + hash_map_2[2] * broj_blokiranih_figura_protivnika(igrac2, igrac1) + hash_map_2[3] * moj_broj_figura(igrac1) + hash_map_2[4] * otvoren_mill(igrac1, igrac2) + hash_map_2[5] * dupli_mill(igrac1) + hash_map_2[6] * pobeda(igrac2, igrac1)
    broj2 = hash_map_2[1] * moj_broj_mill(igrac2) + hash_map_2[2] * broj_blokiranih_figura_protivnika(igrac1, igrac2) + hash_map_2[3] * moj_broj_figura(igrac2) + hash_map_2[4] * otvoren_mill(igrac2, igrac1) + hash_map_2[5] * dupli_mill(igrac2) + hash_map_2[6] * pobeda(igrac1, igrac2)
    return broj1-broj2
