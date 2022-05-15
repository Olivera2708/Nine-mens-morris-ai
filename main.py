from Tabla import *
from minimax import *

def faza1_igrac():
    for dugme in tabla.dugmici:
        dugme.config(state="normal")

    #sacekaj da odigra igrac 1
    tabla.wait_variable(tabla.sacekaj)
    #kada odigra nacrtaj na tabli
    tabla.postavi(1, tabla.sacekaj.get())

def faza1_ai():
    for dugme in tabla.dugmici:
        dugme.config(state="disabled")

    #sledeci = sledeci_potez()
    sledeci = i+1
    tabla.postavi(2, sledeci)

def faza1(prva, druga):
    prva()
    druga()

def faza2_igrac():
    #korisnik, igrac broj 1
    for dugme in tabla.dugmici:
        dugme.config(state="normal")

    #sacekaj da ukloni igrac 1
    tabla.wait_variable(tabla.sacekaj)
    tabla.ukloni(1, tabla.sacekaj.get())
    #sacekaj da ukloni igrac 1
    tabla.wait_variable(tabla.sacekaj)
    tabla.postavi(1, tabla.sacekaj.get())

    #porvera jel gotovo
    if jel_gotovo(tabla.a, tabla.b, 1):
        return False

def faza2_ai():
    for dugme in tabla.dugmici:
        dugme.config(state="disabled")
    
    #sledeci = sledeci_potez_faza2()
    sledeci = (2, 5)
    tabla.ukloni(2, sledeci[0])
    tabla.postavi(2, sledeci[1])

    #provera jel gotovo
    if jel_gotovo(tabla.a, tabla.b, 2):
        return False


def faza2(prva, druga):
    prva()
    druga()
    

######IGRA######

nije_kraj = True
tabla = Tabla()

if tabla.pocetak.get() == 1:
    for i in range(9):
        faza1(faza1_igrac, faza1_ai)
    while nije_kraj:
        nije_kraj = faza2(faza2_igrac, faza2_ai)
else:
    for i in range(9):
        faza1(faza1_ai, faza1_igrac)
    while nije_kraj:
        nije_kraj = faza2(faza2_ai, faza2_igrac)

tabla.mainloop()

