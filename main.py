from Tabla import *
from minimax import *

def faza1(i):
    #korisnik ili ai igra prvi

    #ai na redu, igrac broj 2

    #sledeci = sledeci_potez()
    for dugme in tabla.dugmici:
        dugme.config(state="disabled")
    sledeci = i+1
    tabla.postavi(2, sledeci)
    
    #korisnik, igrac broj 1
    for dugme in tabla.dugmici:
        dugme.config(state="normal")

    #sacekaj da odigra igrac 1
    tabla.wait_variable(tabla.sacekaj)
    #kada odigra nacrtaj na tabli
    tabla.postavi(1, tabla.sacekaj.get())


def faza2():
    #igrac2, ai
    for dugme in tabla.dugmici:
        dugme.config(state="disabled")
    #provera jel gotovo
    if jel_gotovo(tabla.a, tabla.b, 2):
        return False
    #sledeci = sledeci_potez_faza2()
    sledeci = (2, 5)
    tabla.ukloni(2, sledeci[0])
    tabla.postavi(2, sledeci[1])

    #korisnik, igrac broj 1
    for dugme in tabla.dugmici:
        dugme.config(state="normal")
    #porvera jel gotovo
    if jel_gotovo(tabla.a, tabla.b, 1):
        return False

    #sacekaj da ukloni igrac 1
    tabla.wait_variable(tabla.sacekaj)
    tabla.ukloni(1, tabla.sacekaj.get())

    #sacekaj da ukloni igrac 1
    tabla.wait_variable(tabla.sacekaj)
    tabla.postavi(1, tabla.sacekaj.get())
    


tabla = Tabla()

for i in range(9):
    faza1(i)

nije_kraj = True
while nije_kraj:
    nije_kraj = faza2()
    



tabla.mainloop()

