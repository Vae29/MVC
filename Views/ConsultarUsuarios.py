import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from View.CrearUsuario import CrearUsuario
from View.EliminarUsuario import EliminarUsuario
from View.ModificarUsuario import ModificarUsuario

class ConsultarUsuarios():
    def crearUsuario(self, event):
        pass

    def eliminarUsuario(self, event):
        pass

    def modificarUsuario(self, event):
        pass

    def __init__(self, loggin):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.config(width=600)
        self.ventana.title("Tabla de Usuarios")

        self.lblTitulo = tk.Label(self.ventana, text="Listado de Usuarios")
        self.lblTitulo.pack()

        self.botones = tk.Frame(self.ventana)
        self.botones.config(width=600, height=100)
        self.botones.pack(fill="both", expand=True)

        self.iconoCrear = tk.PhotoImage(file=r"src\icons\user_add.png")
        self.btnCrearUsuario = tk.Button(self.botones, image=self.iconoCrear)
        self.btnCrearUsuario.place(relx=0.5, x=-50, y=25, anchor="nw")
        self.btnCrearUsuario.bind("<Button-1>", self.crearUsuario)

        self.iconoEliminar = tk.PhotoImage(file=r"src\icons\user_delete.png")
        self.btnEliminarUsuario = tk.Button(self.botones, image=self.iconoEliminar)
        self.btnEliminarUsuario.place(relx=0.5, y=25, anchor="n")
        self.btnEliminarUsuario.bind("<Button-1>", self.eliminarUsuario)

        self.iconoModificar = tk.PhotoImage(file=r"src\icons\user_edit.png")
        self.btnModificarUsuario = tk.Button(self.botones, image=self.iconoModificar)
        self.btnModificarUsuario.place(relx=0.5, y=25, x=50, anchor="ne")
        self.btnModificarUsuario.bind("<Button-1>", self.modificarUsuario)

        self.ventana.mainloop()