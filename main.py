from Tabla import *
from minimax import *

def faza1_igrac():
    for dugme in tabla.dugmici:
        dugme.config(state="normal")

    #sacekaj da odigra igrac 1
    tabla.wait_variable(tabla.sacekaj)
    #porveri jel mesto slobodno
    mesto = tabla.sacekaj.get()
    while not jel_prazno_skroz(tabla.a, tabla.b, mesto):
        tabla.napisi_poruku("Ovo mesto je već zauzeto\n")
        tabla.wait_variable(tabla.sacekaj)
        mesto = tabla.sacekaj.get()

    #kada odigra nacrtaj na tabli
    tabla.postavi(1, mesto)

    #proveri jel mill
    if jel_mill(tabla.a, mesto)[0]:
        tabla.napisi_poruku("Ukloni figuru drugog igrača\n")
        tabla.wait_variable(tabla.sacekaj)
        mesto = tabla.sacekaj.get()
        while not moze_da_se_ukloni(tabla.b, mesto):
            tabla.napisi_poruku("Nije moguće ukloniti ovu figuru\n")
            tabla.wait_variable(tabla.sacekaj)
            mesto = tabla.sacekaj.get()
        tabla.ukloni(2, mesto)


def faza1_ai(i):
    for dugme in tabla.dugmici:
        dugme.config(state="disabled")

    sledeci = sledeci_potez_faza1(tabla.a, tabla.b, 4, i, True)
    tabla.postavi(2, sledeci)
    #ukloni protivniku figuru ako je mill
    if jel_mill(tabla.b, sledeci)[0]:
        for j in moja_polja(tabla.a):
            if moze_da_se_ukloni(tabla.a, j):
                tabla.ukloni(1, j)
                tabla.napisi_poruku(f"Kompjuter je uklonio vašu figuru\n")
                break
    

def faza1_2(prva, druga, *args):
    druga(*args)
    prva()

def faza1_1(prva, druga, *args):
    prva()
    druga(*args)

def faza2_igrac():
    #korisnik, igrac broj 1
    for dugme in tabla.dugmici:
        dugme.config(state="normal")

    #sacekaj da ukloni igrac 1
    tabla.wait_variable(tabla.sacekaj)
    mesto_ukloni = tabla.sacekaj.get()
    while len(moguc_potez(tabla.a, tabla.b, mesto_ukloni)) == 0:
        tabla.napisi_poruku("Figura ne može da se premesti\n")
        tabla.wait_variable(tabla.sacekaj)
        mesto_ukloni = tabla.sacekaj.get()
    while mesto_ukloni not in moja_polja(tabla.a):
        tabla.napisi_poruku("Figura koju želite da pomerite nije vaša\n")
        tabla.wait_variable(tabla.sacekaj)
        mesto_ukloni = tabla.sacekaj.get()
    tabla.postavi_privremen(mesto_ukloni)

    #sacekaj da ukloni igrac 1
    tabla.wait_variable(tabla.sacekaj)
    mesto_dodaj = tabla.sacekaj.get()
    while not mesto_dodaj in moguc_potez(tabla.a, tabla.b, mesto_ukloni):
        tabla.napisi_poruku("Figuru nije moguće pomeriti na ovo mesto\n")
        tabla.wait_variable(tabla.sacekaj)
        mesto_dodaj = tabla.sacekaj.get()
    tabla.ukloni(1, mesto_ukloni)
    tabla.postavi(1, mesto_dodaj)

    #proveri jel mill
    if jel_mill(tabla.a, mesto_dodaj)[0]:
        tabla.napisi_poruku("Ukloni figuru drugog igrača\n")
        tabla.wait_variable(tabla.sacekaj)
        mesto = tabla.sacekaj.get()
        while not moze_da_se_ukloni(tabla.b, mesto):
            tabla.napisi_poruku("Nije moguće ukloniti ovu figuru\n")
            tabla.wait_variable(tabla.sacekaj)
            mesto = tabla.sacekaj.get()
        tabla.ukloni(2, mesto)

    #porvera jel gotovo
    if jel_gotovo(tabla.a, tabla.b, 1):
        tabla.napisi_poruku("POBEDILI STE")
        return False
    return True

def faza2_ai():
    for dugme in tabla.dugmici:
        dugme.config(state="disabled")
    
    sledeci = sledeci_potez_faza2(tabla.a, tabla.b, 3, True)
    tabla.ukloni(2, sledeci[0])
    tabla.postavi(2, sledeci[1])

    #ukloni protivniku figuru ako je mill
    if jel_mill(tabla.b, sledeci[1])[0]:
        for j in moja_polja(tabla.a):
            if moze_da_se_ukloni(tabla.a, j):
                tabla.ukloni(1, j)
                tabla.napisi_poruku(f"Kompjuter je uklonio vašu figuru\n")
                break

    #provera jel gotovo
    if jel_gotovo(tabla.a, tabla.b, 2):
        tabla.napisi_poruku("IZGUBILI STE")
        return False
    return True


def faza2(prva, druga):
    jos_se_igra = True
    jos_se_igra = prva()
    if not jos_se_igra:
        return False
    jos_se_igra = druga()
    if not jos_se_igra:
        return False
    return True

def gotovo():
    if jel_gotovo(tabla.a, tabla.b, 2):
        tabla.napisi_poruku("IZGUBILI STE")
        return False
    if jel_gotovo(tabla.a, tabla.b, 1):
        tabla.napisi_poruku("POBEDILI STE")
        return False
    return True
    

######IGRA######

nije_kraj = True
tabla = Tabla()

if tabla.pocetak.get() == 1:
    tabla.napisi_poruku("PRVA FAZA\n")
    for i in range(9):
        faza1_1(faza1_igrac, faza1_ai, i)
    tabla.napisi_poruku("DRUGA FAZA\n")
    #jel gotovo
    nije_kraj = gotovo()
    while nije_kraj:
        nije_kraj = faza2(faza2_igrac, faza2_ai)
else:
    tabla.napisi_poruku("PRVA FAZA\n")
    for i in range(9):
        faza1_2(faza1_igrac, faza1_ai, i)
    tabla.napisi_poruku("DRUGA FAZA\n")
    #jel gotovo
    nije_kraj = gotovo()
    while nije_kraj:
        nije_kraj = faza2(faza2_ai, faza2_igrac)

tabla.mainloop()

