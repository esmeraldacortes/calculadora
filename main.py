import tkinter
from tkinter import *
from tkinter import messagebox, PhotoImage

calculadora = tkinter.Tk()
calculadora.geometry("500x650+370+370")
calculadora.resizable(False, False)
calculadora.title("Calculadora")

# transparencia
calculadora.attributes('-alpha', 0.9)  # 0-transparente 1-opaco

# icono de ventana
image_icon: PhotoImage = PhotoImage(file="calculadora.png")
calculadora.iconphoto(False, image_icon)


#cursor pirata
calculadora.config(cursor="pirate")


#casilla de resultado
data = StringVar()
lbl = Label(calculadora, text="Label", anchor=SE, font=("courier", 40, "bold"), textvariable=data, fg='white', bg='gray8')
lbl.pack(expand=True, fill="both", )


numero = ""
A = 0
operador = ""

#funciones al clickear
def uno():
    global numero
    numero = numero + "1"
    data.set(numero)


def dos():
    global numero
    numero = numero + "2"
    data.set(numero)


def tres():
    global numero
    numero = numero + "3"
    data.set(numero)


def cuatro():
    global numero
    numero = numero + "4"
    data.set(numero)


def cinco():
    global numero
    numero = numero + "5"
    data.set(numero)


def seis():
    global numero
    numero = numero + "6"
    data.set(numero)


def siete():
    global numero
    numero = numero + "7"
    data.set(numero)


def ocho():
    global numero
    val = numero + "8"
    data.set(numero)


def nueve():
    global numero
    numero = numero + "9"
    data.set(numero)


def cero():
    global numero
    numero = numero + "0"
    data.set(numero)


def suma():
    global A
    global operador
    global numero
    A = int(numero)
    operador = "+"
    numero = numero + "+"
    data.set(numero)


def resta():
    global A
    global operador
    global numero
    A = int(numero)
    operador = "-"
    numero = numero + "-"
    data.set(numero)


def multiplica():
    global A
    global operador
    global numero
    A = int(numero)
    operador = "*"
    numero = numero + "*"
    data.set(numero)


def divide():
    global A
    global operador
    global numero
    A = int(numero)
    operador = "/"
    numero = numero + "/"
    data.set(numero)


def igual():
    global A
    global operador
    global numero
    A = int(numero)
    operador = "="
    numero = numero + "="
    data.set(numero)


def borrar():
    global A
    global operador
    global numero
    numero = ""
    A = 0
    operador = ""
    data.set(numero)


def resultado():
    global A
    global operador
    global numero
    num2 = numero
    if operador == "+":
        x = int((num2.split("+")[1]))
        c = A + x
        data.set(c)
        numero = str(c)
    elif operador == "-":
        x = int((num2.split("-")[1]))
        c = A - x
        data.set(c)
        numero = str(c)
    elif operador == "*":
        x = int((num2.split("*")[1]))
        c = A * x
        data.set(c)
        numero = str(c)
    elif operador == "/":
        x = int((num2.split("/")[1]))
        if x == 0:
            messagebox.show("Error")
            A == ""
            numero = ""
            data.set(numero)
        else:
            c = int(A / x)
            data.set(c)
            numero = str(c)


boton789 = Frame(calculadora)
boton789.pack(expand=True, fill="both", )

boton456 = Frame(calculadora)
boton456.pack(expand=True, fill="both", )

boton123 = Frame(calculadora, bg="#000000")
boton123.pack(expand=True, fill="both", )

boton0igual = Frame(calculadora)
boton0igual.pack(expand=True, fill="both", )

#BOTONES
#  7
siete = Button(boton789,text="7", font=("courier", 40, "bold"), fg='white', bg='black', relief=GROOVE, border=0, command=siete,)
siete.pack(side=LEFT, expand=True, fill="both", )

#  8
ocho = Button(boton789, text="8", font=("courier", 40, "bold"), fg='white', bg='black', relief=GROOVE, border=0, command=ocho,)
ocho.pack(side=LEFT, expand=True, fill="both", )

#  9
nueve = Button(boton789, text="9", font=("courier", 40, "bold"), fg='white', bg='black', relief=GROOVE, border=0, command=nueve,)
nueve.pack(side=LEFT, expand=True, fill="both", )

#  Multiplicar
multiplicar = Button(boton789, text="*", font=("courier", 40, "bold"), fg='white', bg='gray8', relief=GROOVE, border=0, command=multiplica)
multiplicar.pack(side=LEFT, expand=True, fill="both", )


#456-


#  4
cuatro = Button(boton456, text="4", font=("courier", 40, "bold"), fg='white', bg='black', relief=GROOVE, border=0, command=cuatro,)
cuatro.pack(side=LEFT, expand=True, fill="both", )

#  5
cinco = Button(boton456, text="5", font=("courier", 40, "bold"), fg='white', bg='black', relief=GROOVE, border=0, command=cinco,)
cinco.pack(side=LEFT, expand=True, fill="both", )

#  6
seis = Button(boton456, text="6", font=("courier", 40, "bold"), fg='white', bg='black', relief=GROOVE, border=0, command=seis,)
seis.pack(side=LEFT, expand=True, fill="both", )

#  resta
resta = Button(boton456, text="-", font=("courier", 40, "bold"), fg='white', bg='gray8', relief=GROOVE, border=0, command=resta,)
resta.pack(side=LEFT, expand=True, fill="both", )


#123+

#  1
uno = Button(boton123, text="1", font=("courier", 40, "bold"), fg='white', bg='black', relief=GROOVE, border=0, command=uno)
uno.pack(side=LEFT, expand=True, fill="both", )

#  2
dos = Button(boton123, text="2", font=("courier", 40, "bold"), fg='white', bg='black', relief=GROOVE, border=0, command=dos,)
dos.pack(side=LEFT, expand=True, fill="both", )

#  3
tres = Button(boton123, text="3", font=("courier", 40, "bold"), fg='white', bg='black', relief=GROOVE, border=0, command=tres,)
tres.pack(side=LEFT, expand=True, fill="both", )

#  suma
suma = Button(boton123, text="+", font=("courier", 40, "bold"), fg='white', bg='gray8', relief=GROOVE, border=0, command=suma,)
suma.pack(side=LEFT, expand=True, fill="both", )



# botón borrar
borrar = Button(boton0igual, text="B", font=("courier", 40, "bold"), fg='white', bg='gray8', relief=GROOVE, border=0, command=borrar,)
borrar.pack(side=LEFT, expand=True, fill="both", )

# botón 0
cero = Button(boton0igual, text="0", font=("courier", 40, "bold"), fg='white', bg='black', relief=GROOVE, border=0, command=cero,)
cero.pack(side=LEFT, expand=True, fill="both", )

# botón igual
igual = Button(boton0igual, text="=", font=("courier", 40, "bold"), fg='white', bg='gray8', relief=GROOVE, border=0, command=resultado,)
igual.pack(side=LEFT, expand=True, fill="both", )

# botón división
division = Button(boton0igual, text="/", font=("courier", 40, "bold"), fg='white', bg='gray8', relief=GROOVE, border=0, command=divide,)
division.pack(side=LEFT, expand=True, fill="both", )

calculadora.mainloop()
