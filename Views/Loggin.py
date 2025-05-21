import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound

from Controllers.usuario import usuario

class Loggin():

    def validarCampos(self, event):
        if(len(self.txtUsuario.get()) >= 5 and len(self.txtPassword.get()) >= 5):
            if(len(self.txtUsuario.get()) <= 25 and len(self.txtPassword.get()) <= 25):
                self.btnIngresar.config(state="normal")
            elif(len(self.txtUsuario.get()) <= 25 and len(self.txtPassword.get()) >= 25):
                self.txtPassword.delete(len(self.txtPassword.get())-1, END)
            elif(len(self.txtUsuario.get()) >= 25 and len(self.txtPassword.get()) <= 25):
                self.txtUsuario.delete(len(self.txtUsuario.get())-1, END)
        else:
            self.btnIngresar.config(state="disabled")

    def validarUsuario(self, event):
        caracter = event.keysym
        print(caracter," fue presionado.")
        if(caracter.isalpha() or caracter == '.' or caracter == "BackSpace"): # isdigit() - isalpha() - isalnum()
            self.txtUsuario.config(bg="#ffffff", fg="#000000")
        else:
            self.txtUsuario.config(bg="#f5b7b1", fg="#e74c3c")
            winsound.Beep(1700, 333)


    def verCaracteres(self, event):
        if(self.bandera == True):
            self.txtPassword.config(show='*')
            self.btnVer.config(text="Ver")
            self.bandera = False
        else:
            self.txtPassword.config(show='')
            self.btnVer.config(text="Ocu")
            self.bandera = True

    def ingresar(self, event):
        miusuario = usuario(self.txtUsuario.get(),self.txtPassword.get())
        miusuario.iniciarSesion(miusuario.nombreUsuario,miusuario.password)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=440, height=350)
        self.ventana.title("Inicio de Sesión")

        self.bandera = False

        self.lblTitulo = tk.Label(self.ventana, text="Inicio Sesión")
        self.lblTitulo.place(relx=0.5, y=50, anchor="center")

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:")
        self.lblUsuario.place(x=100, y=125, width=70, height=25)

        self.lblPassword = tk.Label(self.ventana, text="Password*:")
        self.lblPassword.place(x=100, y=200, width=70, height=25)

        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(x=190, y=125, width=150, height=25)
        self.txtUsuario.bind("<KeyRelease>", self.validarCampos)
        self.txtUsuario.bind("<Key>", self.validarUsuario)

        self.txtPassword = tk.Entry(self.ventana, show="*")
        self.txtPassword.place(x=190, y=200, width=150, height=25)
        self.txtPassword.bind("<KeyRelease>", self.validarCampos)

        self.btnAyuda = tk.Button(self.ventana, text="Ayuda")
        self.btnAyuda.place(x=320, y=50)

        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", state="disabled")
        self.btnIngresar.place(x=140, y=275, width=70, height=25)
        self.btnIngresar.bind("<Button-1>", self.ingresar)

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar")
        self.btnLimpiar.place(x=230, y=275, width=70, height=25)

        self.btnVer = tk.Button(self.ventana, text="Ver")
        self.btnVer.place(x=360, y=200, width=30, height=25)
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)

        self.txtUsuario.insert(END, "Juan Pérez")
        self.txtPassword.insert(END, "1234567890")

        self.ventana.mainloop()