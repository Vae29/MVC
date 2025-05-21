from tkinter import messagebox
from models.conexionBD import ConexionDB


class Usuario():
    def __init__(self, nombreUsuario, password):
        self.nombreUsuario = nombreUsuario
        self.password = password
        self.root = ""

    def iniciarSesion(self, nombreUsuario, password):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conn = miConexion.getConnetion()
        cursor = conn.cursor()
        cursor.execute("select * from usuario")
        listaUsuario = cursor.fetchall()
        for usuario in listaUsuario:
            if (usuario[1] == nombreUsuario and usuario[2] == password):
                self.rol = usuario[3]
                if(self.rol == "admin"):
                    messagebox.showinfo("Información", "Acceso correcto Administrador!")
                    #crear objeto administrador y abrir menú Administrador
                else:
                    messagebox.showinfo("Información", "Acceso correcto Digitador!")
                miConexion.cerrarConexion()
                return 
        messagebox.showwarning("Advertencia", "El nombre de usuario y/o contraseña no existe, verifique e intente nuevamente!")

