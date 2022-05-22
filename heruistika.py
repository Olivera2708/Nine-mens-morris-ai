from Tabla import *
from hashmap import LinearHashMap


koeficijent = LinearHashMap()
koeficijent["millovi1"] = 26
koeficijent["blokirane1"] = 1
koeficijent["figure1"] = 6
koeficijent["potencijalni mill"] = 12
koeficijent["dupli potencijalni mill"] = 7
koeficijent["millovi2"] = 43
koeficijent["blokirane2"] = 10
koeficijent["figure2"] = 8
koeficijent["otvoren"] = 7
koeficijent["dupli mill"] = 42
koeficijent["pobeda"] = 1086

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
    broj1 = koeficijent["millovi1"] * moj_broj_mill(igrac1) + koeficijent["blokirane1"] * broj_blokiranih_figura_protivnika(igrac2, igrac1) + koeficijent["figure1"] * moj_broj_figura(igrac1) + koeficijent["potencijalni mill"] * potencijalni_mill(igrac1, igrac2) + koeficijent["dupli potencijalni mill"] * dupli_potencijalni_mill(igrac2, igrac1)
    broj2 = koeficijent["millovi1"] * moj_broj_mill(igrac2) + koeficijent["blokirane1"] * broj_blokiranih_figura_protivnika(igrac1, igrac2) + koeficijent["figure1"] * moj_broj_figura(igrac2) + koeficijent["potencijalni mill"] * potencijalni_mill(igrac2, igrac1) + koeficijent["dupli potencijalni mill"] * dupli_potencijalni_mill(igrac1, igrac2)
    return broj1 - broj2

def heruistika_faza2(igrac1, igrac2):
    broj1 = koeficijent["millovi2"] * moj_broj_mill(igrac1) + koeficijent["blokirane2"] * broj_blokiranih_figura_protivnika(igrac2, igrac1) + koeficijent["figure2"] * moj_broj_figura(igrac1) + koeficijent["otvoren"] * otvoren_mill(igrac1, igrac2) + koeficijent["dupli mill"] * dupli_mill(igrac1) + koeficijent["pobeda"] * pobeda(igrac2, igrac1)
    broj2 = koeficijent["millovi2"] * moj_broj_mill(igrac2) + koeficijent["blokirane2"] * broj_blokiranih_figura_protivnika(igrac1, igrac2) + koeficijent["figure2"] * moj_broj_figura(igrac2) + koeficijent["otvoren"] * otvoren_mill(igrac2, igrac1) + koeficijent["dupli mill"] * dupli_mill(igrac2) + koeficijent["pobeda"] * pobeda(igrac1, igrac2)
    return broj1 - broj2
