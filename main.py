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

    print("{:024b}".format(tabla.a & 0x00ffffff))
    print("{:024b}".format(tabla.b & 0x00ffffff))


def faza2():
    pass
    


tabla = Tabla()

for i in range(9):
    faza1(i)

while not jel_gotovo()[0]:
    pass



tabla.mainloop()

