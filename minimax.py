from Tabla import *
from hashmap import LinearHashMap
from heuristika import *

hashmap_faza1 = LinearHashMap()
hashmap_faza2 = LinearHashMap()

def sledeci_potez_faza1(a, b, dubina, broj_postavljenih, max_igrac):
    if max_igrac:
        maksimum = float('-inf')
        najbolji = None #najbolji potez
        for i in moja_polja(slobodne_pozicije(a, b)):
            bx = b
            ax = a
            bx = dodaj(bx, i)
            #provera jel mil, ako jeste ukloni protivniku jedan
            if jel_mill(bx, i)[0]:
                for j in moja_polja(a):
                    if moze_da_se_ukloni(a, j):
                        ax = ukloni(ax, j)
                        rezultat = minimax_faza1(ax, bx, dubina-1, float('-inf'), float('inf'), False, broj_postavljenih+1) + 18
                        hashmap_faza1[(ax, bx)] = rezultat
                        if rezultat > maksimum:
                            maksimum = rezultat
                            najbolji = (i, j)
            else:
                rezultat = minimax_faza1(a, bx, dubina-1, float('-inf'), float('inf'), False, broj_postavljenih+1)
                hashmap_faza1[(a, bx)] = rezultat
                if rezultat > maksimum:
                    maksimum = rezultat
                    najbolji = (i, 0)
    print(maksimum)
    return najbolji

def minimax_faza1(a, b, dubina, alfa, beta, max_igrac, broj_postavljenih):
    #provera jel vec bio ovaj slucaj
    postoji, broj = hashmap_faza1[(a, b)]
    if postoji:
        return broj
    #provera jel gotovo
    if dubina == 0:
        return heruistika_faza1(b, a)
    if broj_postavljenih == 9:
        minimax_faza2(a, b, dubina, float('-inf'), float('inf'), max_igrac)

    if max_igrac:
        maksimum = float('-inf')
        for i in moja_polja(slobodne_pozicije(a, b)):
            bx = b
            ax = a
            bx = dodaj(bx, i)
            #provera jel mil, ako jeste ukloni protivniku jedan
            if jel_mill(bx, i)[0]:
                for j in moja_polja(a):
                    if moze_da_se_ukloni(a, j):
                        ax = ukloni(ax, j)
                        rezultat = minimax_faza1(ax, bx, dubina-1, alfa, beta, False, broj_postavljenih+1) + 18
                        maksimum = max(rezultat, maksimum)
                        alfa = max(alfa, rezultat)
                        if beta <= alfa:
                            break
            else:
                rezultat = minimax_faza1(a, bx, dubina-1, alfa, beta, False, broj_postavljenih+1)
                maksimum = max(rezultat, maksimum)
                alfa = max(alfa, rezultat)
                if beta <= alfa:
                    break
        return maksimum

    else:
        minimum = float('inf')
        for i in moja_polja(slobodne_pozicije(a, b)):
            ax = a
            bx = b
            ax = dodaj(ax, i)
            #porvera jel mill
            if jel_mill(ax, i)[0]:
                for j in moja_polja(b):
                    if moze_da_se_ukloni(b, j):
                        bx = ukloni(bx, j)
                        rezultat = minimax_faza1(ax, bx, dubina-1, alfa, beta, True, broj_postavljenih+1) + 18
                        minimum = min(rezultat, minimum)
                        beta = min(beta, rezultat)
                        if beta <= alfa:
                            break
            else:
                rezultat = minimax_faza1(ax, b, dubina-1, alfa, beta, True, broj_postavljenih+1)
                minimum = min(rezultat, minimum)
                beta = min(beta, rezultat)
                if beta <= alfa:
                    break
        return minimum


def sledeci_potez_faza2(a, b, dubina, max_igrac):
    if max_igrac:
        maksimum = float('-inf')
        najbolji = None #najbolji potez
        for i in moja_polja(b):
            mogucnosti = moguc_potez(a, b, i)
            if mogucnosti != ():
                ax = a
                bx = b
                bx = ukloni(bx, i)
                for j in mogucnosti:
                    bx = dodaj(bx, j)
                    #proveri jel mill
                    if jel_mill(bx, j)[0]:
                        for k in moja_polja(a):
                            if moze_da_se_ukloni(a, k):
                                ax = ukloni(ax, k)
                                rezultat = minimax_faza2(ax, bx, dubina-1, float('-inf'), float('inf'), False) + 14
                                hashmap_faza2[(ax, bx)] = rezultat
                                if rezultat > maksimum:
                                    maksimum = rezultat
                                    najbolji = (i, j, k)

                    else:
                        rezultat = minimax_faza2(a, bx, dubina-1, float('-inf'), float('inf'), False)
                        print(f"Da postavim {i} na {j} -> {rezultat}")
                        hashmap_faza2[(a, bx)] = rezultat
                        if rezultat > maksimum:
                            maksimum = rezultat
                            najbolji = (i, j, 0)
    return najbolji


def minimax_faza2(a, b, dubina, alfa, beta, max_igrac):
    #provera jel vec bio ovaj slucaj
    postoji, broj = hashmap_faza2[(a, b)]
    if postoji:
        return broj
    #provera jel gotovo
    if dubina == 0:
        return heruistika_faza2(b, a)
    if jel_gotovo(a, b):
        return dubina + 2000
    if jel_gotovo(b, a):
        return  - dubina - 2000

    if max_igrac:
        maksimum = float('-inf')
        for i in moja_polja(b):
            mogucnosti = moguc_potez(a, b, i)
            if mogucnosti != ():
                ax = a
                bx = b
                bx = ukloni(bx, i)
                for j in mogucnosti:
                    bx = dodaj(bx, j)
                    #proveri jel mill
                    if jel_mill(bx, j)[0]:
                        for j in moja_polja(a):
                            if moze_da_se_ukloni(a, j):
                                ax = ukloni(ax, j)
                                rezultat = minimax_faza2(ax, bx, dubina-1, alfa, beta, False) + 14
                                maksimum = max(rezultat, maksimum)
                                alfa = max(alfa, rezultat)
                                if beta <= alfa:
                                    break
                    else:
                        rezultat = minimax_faza2(ax, bx, dubina-1, alfa, beta, False)
                        maksimum = max(rezultat, maksimum)
                        alfa = max(alfa, rezultat)
                        if beta <= alfa:
                            break
        return maksimum
    
    else:
        minimum = float('inf')
        for i in moja_polja(a):
            mogucnosti = moguc_potez(a, b, i)
            if mogucnosti != ():
                ax = a
                bx = b
                ax = ukloni(ax, i)
                for j in mogucnosti:
                    ax = dodaj(ax, j)
                    #proveri jel mill
                    if jel_mill(ax, j)[0]:
                        for j in moja_polja(b):
                            if moze_da_se_ukloni(b, j):
                                bx = ukloni(bx, j)
                                rezultat = minimax_faza2(ax, bx, dubina-1, alfa, beta, True) + 14
                                minimum = min(rezultat, minimum)
                                beta = min(beta, rezultat)
                                if beta <= alfa:
                                    break
                    else:
                        rezultat = minimax_faza2(ax, bx, dubina-1, alfa, beta, True)
                        minimum = min(rezultat, minimum)
                        beta = min(beta, rezultat)
                        if beta <= alfa:
                            break
        return minimum
    