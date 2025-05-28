from Models.conexionBD import ConexionBD
from tkinter import messagebox


class usuario():
    def __init__(self, nombreUsuario, password):
        self.nombreUsuario = nombreUsuario
        self.password = password
        self.rol = "" #no se sabe que rol tiene el usuario al loggearse se sabe si es admin o no
    
    def iniciarSesion(self,nombreUsuario,password):
        miconexion= ConexionBD()
        miconexion.crearConexion()
        conn = miconexion.getConnection()
        cursor = conn.cursor() #se encarga de ejecutar las consultas
        cursor.execute("select * from usuario ")
        listaUsuarios= cursor.fetchall() #fetchall todos los registros de la consulta
        for  usuario in listaUsuarios:
            if usuario[1] ==nombreUsuario and usuario[2] ==password:
                self.rol = usuario[3]
                if self.rol == "admin":
                    messagebox.showinfo("Informacion","Acceso correcto a administrador")
                    #Crear objeto Administrador y abrir menu administrador y se pone else pq son 2 roles
                else:
                    messagebox.showinfo("Informacion","Acceso correcto Digitador")
                miconexion.cerrarConexion()
                return 
        messagebox.showwarning("ADVERTENCIA","El nombre de usuario y/o contraseña no existen, ¡verifique e intente nuevamente!")


                



    
