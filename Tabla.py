from curses import window
from tkinter import *
from turtle import width
import customtkinter

class Tabla(Tk):
    def __init__(self):
        super().__init__()

        #pocetno stanje na tabli, sve slobodno
        self.a = 0b000000000000000000000000
        self.b = 0b000000000000000000000000

        self.sacekaj = IntVar()
        self.pocetak = IntVar()

        self.title("Mice")
        self.geometry("800x800")
        self.resizable(0, 0)
        self.config(bg="#d9b179")

        canvas = Canvas(self, width=800, height=800, bg="#d9b179")
        canvas.pack()

        canvas.create_rectangle(150, 150, 650, 650, outline="#8f7147", width=8)
        canvas.create_text(400, 80, text="Mice", fill="white", font=('Modern 36 bold'))
        canvas.create_text(400, 300, text="Želim da počnem", fill="white", font=('Modern 24 bold'))
        korisnik_prvi = customtkinter.CTkButton(bg_color="#d9b179", fg_color="#8f7147", hover_color="#785a31", text="Prvi", text_font=('Modern 20 bold'), command=lambda: self.pocetak.set(1))
        korisnik_prvi.place(x=300, y=380, width=200, height=36)
        korisnik_drugi = customtkinter.CTkButton(bg_color="#d9b179", fg_color="#8f7147", hover_color="#785a31", text="Drugi", text_font=('Modern 20 bold'), command=lambda: self.pocetak.set(2))
        korisnik_drugi.place(x=300, y=450, width=200, height=36)

        self.wait_variable(self.pocetak)

        korisnik_prvi.destroy()
        korisnik_drugi.destroy()
        canvas.delete("all")
        canvas.create_rectangle(100, 100, 700, 700, outline="#8f7147", width=8)
        canvas.create_rectangle(200, 200, 600, 600, outline="#8f7147", width=8)
        canvas.create_rectangle(300, 300, 500, 500, outline="#8f7147", width=8)
        canvas.create_line(400, 100, 400, 300, fill="#8f7147", width=8)
        canvas.create_line(100, 400, 300, 400, fill="#8f7147", width=8)
        canvas.create_line(500, 400, 700, 400, fill="#8f7147", width=8)
        canvas.create_line(400, 500, 400, 700, fill="#8f7147", width=8)

        self.koordinate_postavi = ((70, 670), (370, 670), (670, 670), \
                    (170, 570), (370, 570), (570, 570), \
                    (270, 470), (370, 470), (470, 470), \
                    (70, 370), (170, 370), (270, 370), (470, 370), (570, 370), (670, 370), \
                    (270, 270), (370, 270), (470, 270), \
                    (170, 170), (370, 170), (570, 170), \
                    (70, 70), (370, 70), (670, 70))

        self.koordinate_prazno = ((80, 680), (380, 680), (680, 680), \
                    (180, 580), (380, 580), (580, 580), \
                    (280, 480), (380, 480), (480, 480), \
                    (80, 380), (180, 380), (280, 380), (480, 380), (580, 380), (680, 380), \
                    (280, 280), (380, 280), (480, 280), \
                    (180, 180), (380, 180), (580, 180), \
                    (80, 80), (380, 80), (680, 80))

        self.slika_prazno = PhotoImage(file="slike/prazno.png")
        self.slika_igrac1 = PhotoImage(file="slike/igrac1.png")
        self.slika_igrac2 = PhotoImage(file="slike/igrac2.png")

        self.dugmici = []
        i = 0

        for koordinata in self.koordinate_prazno:
            i += 1
            dugme = customtkinter.CTkButton(self, image=self.slika_prazno, text="", fg_color="#d9b179", hover_color="#d9b179", command = lambda i=i: self.sacekaj.set(i))
            dugme.place(x=koordinata[0], y=koordinata[1], width=40, height=40)
            self.dugmici.append(dugme)

    
    def ukloni(self, broj_igraca, mesto):
        self.dugmici[mesto-1].config(image = self.slika_prazno)
        self.dugmici[mesto-1].place(x=self.koordinate_prazno[mesto-1][0], y=self.koordinate_prazno[mesto-1][1], width=40, height=40)
        if broj_igraca == 1:
            self.a = ukloni(self.a, mesto)
        else:
            self.b = ukloni(self.b, mesto)


    def postavi(self, broj_igraca, mesto):
        #postavi figuru na tablu
        if broj_igraca == 1:
            self.a = dodaj(self.a, mesto)
            slika = self.slika_igrac1
        else:
            self.b = dodaj(self.b, mesto)
            slika = self.slika_igrac2 

        self.dugmici[mesto-1].config(image = slika)
        self.dugmici[mesto-1].place(x=self.koordinate_postavi[mesto-1][0], y=self.koordinate_postavi[mesto-1][1], width=60, height=60)


#Funkcije za cuvanje trenutnog stanja

def slobodne_pozicije(igrac1, igrac2):
    return ~ (igrac1 | igrac2)

def jel_prazno(igrac, mesto):
    res = igrac & 1 << mesto-1
    if res == 0:
        return True
    return False

def moja_polja(igrac):
    polja = []
    for i in range(1, 25):
        if not jel_prazno(igrac, i):
            polja.append(i)
    return tuple(polja)

def jel_prazno_skroz(igrac1, igrac2, mesto):
    return jel_prazno(igrac1, mesto) & jel_prazno(igrac2, mesto)

def ukloni(igrac, mesto):
    return igrac ^ 1 << mesto-1

def dodaj(igrac, mesto):
    return igrac | 1 << mesto-1

def postavljenih(igrac):
    return igrac.bit_count()

def susedna_polja(mesto):
    lista_susednih = ((2,10), (1,3,5), (2,15), (5,11), (2,4,6,8), (5,14), (8, 12), (5,7,9), (8,13), \
                     (1,11,22), (4,10,12,19), (7,11,16), (9,14,18), (6,13,15,21), (3,14,24), \
                     (12,17), (16,18,20), (13,17), (11,20), (17,19,21,23), (14,20), (10,23), (20,22,24), (15,23))
    return lista_susednih[mesto-1]

def moguc_potez(igrac1, igrac2, mesto):
    lista_mogucih = []
    for mogucnost in susedna_polja(mesto):
        if jel_prazno_skroz(igrac1, igrac2, mogucnost):
            lista_mogucih.append(mogucnost)
    return lista_mogucih

def jel_mill(igrac, mesto):
    svi_mill = (((10,22),(2,3)), ((1,3),(5,8)), ((1,2),(15,24)), \
               ((11,19),(5,6)), ((4,6),(2,8)), ((4,5),(14,21)), \
               ((8,9),(12,16)), ((7,9),(2,5)), ((7,8),(13,18)), \
               ((1,22),(11,12)), ((10,12),(4,19)), ((10,11),(7,16)), ((9,18),(14,15)), ((6,21),(13,15)), ((13,14),(3,24)), \
               ((7,12),(17,18)), ((16,18),(20,23)), ((16,17),(9,13)), \
               ((4,11),(20,21)), ((19,21),(17,23)), ((19,20),(6,11)), \
               ((1,10),(23,24)), ((22,24),(17,20)), ((22,23),(3,15)))
    for pokusaj in svi_mill[mesto-1]:
        if not jel_prazno(igrac, pokusaj[0]) and not jel_prazno(igrac, pokusaj[1]):
            return True, pokusaj
    return False, 0

def jel_gotovo(igrac1, igrac2, max_igrac):
    if postavljenih(igrac1) <= 2:
        return (True, 2)
    if postavljenih(igrac2) <= 2:
        return(True, 1)

    if max_igrac:
        igrac_na_potezu = igrac1
        broj = 1
    else:
        igrac_na_potezu = igrac2
        broj = 2

    for i in range(1, 25):
        if not jel_prazno(igrac_na_potezu, i):
            if moguc_potez(igrac1, igrac2, i) != []:
                return (False, broj)
    return (True, broj)


