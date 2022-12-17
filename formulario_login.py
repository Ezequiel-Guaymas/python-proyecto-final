import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
from formulario_user import User
from formulario_tableroAdmi import TableroAdmi
import bll.usuarios as user
from formulario_tableroPedidoCliente import Pedido_Usuario



class Login(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Login")
        width=585
        height=186
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLineEdit_575=tk.Entry(self, name="txtUsuario")
        GLineEdit_575["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_575["font"] = ft
        GLineEdit_575["fg"] = "#333333"
        GLineEdit_575["justify"] = "left"
        GLineEdit_575["text"] = ""
        GLineEdit_575.place(x=140,y=30,width=391,height=30)
        
        GLabel_183=tk.Label(self)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_183["font"] = ft
        GLabel_183["fg"] = "#333333"
        GLabel_183["justify"] = "right"
        GLabel_183["text"] = "Usuario"
        GLabel_183.place(x=0,y=30,width=125,height=30)

        GLineEdit_775=tk.Entry(self, name ="txtContrasenia", show="*")
        GLineEdit_775["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_775["font"] = ft
        GLineEdit_775["fg"] = "#333333"
        GLineEdit_775["justify"] = "left"
        GLineEdit_775["text"] = ""
        GLineEdit_775.place(x=140,y=80,width=390,height=30)

        GLabel_570=tk.Label(self)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_570["font"] = ft
        GLabel_570["fg"] = "#333333"
        GLabel_570["justify"] = "right"
        GLabel_570["text"] = "Contraseña"
        GLabel_570.place(x=0,y=80,width=125,height=30)

        GButton_507=tk.Button(self)
        GButton_507["bg"] = "#f0f0f0"
        GButton_507["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=11, underline=True, weight='bold')
        GButton_507["font"] = ft
        GButton_507["fg"] = "#f51616"
        GButton_507["justify"] = "center"
        GButton_507["text"] = "Crear cuenta"
        #GButton_507["relief"] = "groove"
        GButton_507.place(x=10,y=130,width=137,height=30)
        GButton_507["command"] = self.abrir_user

        GButton_516=tk.Button(self)
        GButton_516["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_516["font"] = ft
        GButton_516["fg"] = "#cc0000"
        GButton_516["justify"] = "center"
        GButton_516["text"] = "ACEPTAR"
        GButton_516.place(x=270,y=130,width=120,height=30)
        GButton_516["command"] = self.iniciar_sesion

        GButton_912=tk.Button(self)
        GButton_912["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_912["font"] = ft
        GButton_912["fg"] = "#cc0000"
        GButton_912["justify"] = "center"
        GButton_912["text"] = "CANCELAR"
        GButton_912.place(x=410,y=130,width=120,height=30)
        GButton_912["command"] = self.cancelar

    def iniciar_sesion(self):
        try:
            txtUsuario = self.nametowidget("txtUsuario")
            usuario = txtUsuario.get()
            print(usuario)

            txtContrasenia = self.nametowidget("txtContrasenia")
            contrasenia = txtContrasenia.get()
            print(contrasenia)
            if usuario != "":
                if user.validar(usuario, contrasenia):                    
                    usuario = user.obtener_nombre_usuario(usuario)
                    print(usuario)
                    if usuario is not None:
                        if usuario[10] == "Administrador":
                            print("Mostrar pantalla para usuario con rol de Administrador")
                            TableroAdmi(self.master)
                            self.destroy()
                        elif usuario[10] == "Cliente":
                            Pedido_Usuario(self.master)
                            #Dashboard(self.master)
                            #self.destroy()
                            # TODO chequear el rol del usuario para abrir el menu/ventana correspondiente
                            print("Mostrar pantalla para usuario con rol de Cliente")
                    else:
                        tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, ingrese nuevamente")
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario/Contraseña incorrecta")
            else:
                tkMsgBox.showwarning(self.master.title(), "Ingrese el Usuario para iniciar sesión")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

    def cancelar(self):
        self.destroy()

    def abrir_Pedido_Usuario(self):
        Pedido_Usuario(self.master)    

    def abrir_user(self):
        User(self.master)
