#import tkinter as tk
#import tkinter.font as tkFont
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.usuarios as user
import bll.roles as rol
from datetime import date

class User(Toplevel):
    def __init__(self, master=None, isAdmin = False, user_id = None):        
        super().__init__(master)
        self.master = master
        self.user_id = user_id        
        self.title("Registro de cuenta")
        width=559
        height=600
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_966= Label(self)
        GLabel_966["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=20)
        GLabel_966["font"] = ft
        GLabel_966["fg"] = "#cc0000"
        GLabel_966["justify"] = "center"
        GLabel_966["text"] = "Supermarket"
        GLabel_966.place(x=120,y=0,width=314,height=30)

        GLabel_965= Label(self)
        GLabel_965["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_965["font"] = ft
        GLabel_965["fg"] = "#cc0000"
        GLabel_965["justify"] = "center"
        GLabel_965["text"] = "_______________________________DATOS DE LA PERSONALES: ____________________________________"
        GLabel_965.place(x=0,y=30,width=554,height=30)


        GLabel_702= Label(self)
        GLabel_702["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_702["font"] = ft
        GLabel_702["fg"] = "#333333"
        GLabel_702["justify"] = "right"
        GLabel_702["text"] = "Nombre:"
        GLabel_702.place(x=10,y=70,width=120,height=25)

        GLineEdit_728= Entry(self, name="txtNombre")
        GLineEdit_728["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_728["font"] = ft
        GLineEdit_728["fg"] = "#333333"
        GLineEdit_728["justify"] = "left"
        GLineEdit_728["text"] = ""
        GLineEdit_728.place(x=140,y=70,width=405,height=25)

        GLabel_351= Label(self)
        GLabel_351["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_351["font"] = ft
        GLabel_351["fg"] = "#333333"
        GLabel_351["justify"] = "right"
        GLabel_351["text"] = "Apellido:"
        GLabel_351.place(x=10,y=110,width=120,height=25)

        GLineEdit_893= Entry(self, name="txtApellido")
        GLineEdit_893["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_893["font"] = ft
        GLineEdit_893["fg"] = "#333333"
        GLineEdit_893["justify"] = "left"
        GLineEdit_893["text"] = ""
        GLineEdit_893.place(x=140,y=110,width=406,height=25)

        GLabel_767 = Label(self)
        GLabel_767["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_767["font"] = ft
        GLabel_767["fg"] = "#333333"
        GLabel_767["justify"] = "right"
        GLabel_767["text"] = "DNI:"
        GLabel_767.place(x=10,y=150,width=120,height=25)

        GLineEdit_41= Entry(self, name="txtDni")
        GLineEdit_41["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_41["font"] = ft
        GLineEdit_41["fg"] = "#333333"
        GLineEdit_41["justify"] = "left"
        GLineEdit_41["text"] = ""
        GLineEdit_41.place(x=140,y=150,width=183,height=25)

        GLabel_415= Label(self)
        GLabel_415["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_415["font"] = ft
        GLabel_415["fg"] = "#333333"
        GLabel_415["justify"] = "right"
        GLabel_415["text"] = "Fecha Nac.:"
        GLabel_415.place(x=10,y=190,width=120,height=25)

        GLineEdit_585= Entry(self, name="txtFechaNac")
        GLineEdit_585["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_585["font"] = ft
        GLineEdit_585["fg"] = "#333333"
        GLineEdit_585["justify"] = "left"
        GLineEdit_585["text"] = ""
        GLineEdit_585.place(x=140,y=190,width=243,height=25)

        GLabel_529= Label(self)
        GLabel_529["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_529["font"] = ft
        GLabel_529["fg"] = "#333333"
        GLabel_529["justify"] = "center"
        GLabel_529["text"] = "AAAA-MM-DD"
        GLabel_529.place(x=370,y=190,width=141,height=25)

        GLabel_23= Label(self)
        GLabel_23["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_23["font"] = ft
        GLabel_23["fg"] = "#333333"
        GLabel_23["justify"] = "right"
        GLabel_23["text"] = "Email:"
        GLabel_23.place(x=10,y=230,width=120,height=25)

        GLineEdit_655=Entry(self, name="txtEmail")
        GLineEdit_655["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_655["font"] = ft
        GLineEdit_655["fg"] = "#333333"
        GLineEdit_655["justify"] = "left"
        GLineEdit_655["text"] = ""
        GLineEdit_655.place(x=140,y=230,width=342,height=25)

        GLabel_688= Label(self)
        GLabel_688["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_688["font"] = ft
        GLabel_688["fg"] = "#333333"
        GLabel_688["justify"] = "right"
        GLabel_688["text"] = "Domicilio:"
        GLabel_688.place(x=10,y=270,width=120,height=25)

        GLineEdit_908=Entry(self, name="txtDomicilio")
        GLineEdit_908["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_908["font"] = ft
        GLineEdit_908["fg"] = "#333333"
        GLineEdit_908["justify"] = "left"
        GLineEdit_908["text"] = ""
        GLineEdit_908.place(x=140,y=270,width=407,height=25)

        GLabel_172= Label(self)
        GLabel_172["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_172["font"] = ft
        GLabel_172["fg"] = "#333333"
        GLabel_172["justify"] = "right"
        GLabel_172["text"] = "Nro Telefonico:"
        GLabel_172.place(x=10,y=310,width=120,height=25)

        GLineEdit_534=Entry(self, name="txtNroTelefonico")
        GLineEdit_534["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_534["font"] = ft
        GLineEdit_534["fg"] = "#333333"
        GLineEdit_534["justify"] = "left"
        GLineEdit_534["text"] = ""
        GLineEdit_534.place(x=140,y=310,width=243,height=25)

        GLabel_167= Label(self)
        GLabel_167["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_167["font"] = ft
        GLabel_167["fg"] = "#cc0000"
        GLabel_167["justify"] = "center"
        GLabel_167["text"] = "________________________________DATOS DE LA CUENTA: ___________________________________"
        GLabel_167.place(x=0,y=340,width=564,height=30)

        GLabel_256= Label(self)
        GLabel_256["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_256["font"] = ft
        GLabel_256["fg"] = "#333333"
        GLabel_256["justify"] = "right"
        GLabel_256["text"] = "Usuario:"
        GLabel_256.place(x=0,y=380,width=190,height=25)

        GLineEdit_944=Entry(self, name="txtUsuario")
        GLineEdit_944["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_944["font"] = ft
        GLineEdit_944["fg"] = "#333333"
        GLineEdit_944["justify"] = "left"
        GLineEdit_944["text"] = ""
        GLineEdit_944.place(x=200,y=380,width=320,height=25)

        GLabel_95= Label(self)
        GLabel_95["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_95["font"] = ft
        GLabel_95["fg"] = "#333333"
        GLabel_95["justify"] = "right"
        GLabel_95["text"] = "Contraseña:"
        GLabel_95.place(x=0,y=420,width=190,height=25)

        GLineEdit_920= Entry(self, show="*", name="txtContrasenia")
        GLineEdit_920["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_920["font"] = ft
        GLineEdit_920["fg"] = "#333333"
        GLineEdit_920["justify"] = "left"
        GLineEdit_920["text"] = ""
        GLineEdit_920.place(x=200,y=420,width=320,height=25)

        GLabel_304= Label(self)
        GLabel_304["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_304["font"] = ft
        GLabel_304["fg"] = "#333333"
        GLabel_304["justify"] = "right"
        GLabel_304["text"] = "Confirmar contraseña:"
        GLabel_304.place(x=0,y=460,width=190,height=25)

        GLineEdit_903= Entry(self, show="*", name="txtConfirmacion")
        GLineEdit_903["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_903["font"] = ft
        GLineEdit_903["fg"] = "#333333"
        GLineEdit_903["justify"] = "left"
        GLineEdit_903["text"] = ""
        GLineEdit_903.place(x=200,y=460,width=320,height=25)

        GLabel_184= Label(self)
        GLabel_184["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_184["font"] = ft
        GLabel_184["fg"] = "#333333"
        GLabel_184["justify"] = "right"
        GLabel_184["text"] = "Rol:"
        GLabel_184.place(x=0,y=500,width=190,height=25)

        roles = dict(rol.listar())
        if isAdmin:
            cb_roles = ttk.Combobox(self, state="readonly", values=list(roles.values()), name="cbRoles")
        else:
            cb_roles = ttk.Combobox(self, state="disable", values=list(roles.values()), name="cbRoles")
            cb_roles.set(roles[4])
        cb_roles.place(x=200,y=500,width=149,height=25)

        GButton_882= Button(self)
        GButton_882["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=12)
        GButton_882["font"] = ft
        GButton_882["fg"] = "#cc0000"
        GButton_882["justify"] = "center"
        GButton_882["text"] = "ACEPTAR"
        GButton_882.place(x=260,y=550,width=130,height=32)
        GButton_882["command"] = self.aceptar

        GButton_129= Button(self)
        GButton_129["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=12)
        GButton_129["font"] = ft
        GButton_129["fg"] = "#cc0000"
        GButton_129["justify"] = "center"
        GButton_129["text"] = "CANCELAR"
        GButton_129.place(x=400,y=550,width=130,height=32)
        GButton_129["command"] = self.cancelar
        
        if user_id is not None:
            usuario = user.obtener_id(user_id)
            if usuario is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
               self.destroy()
            else:
                # TODO bloquear el campo usuario
                GLineEdit_728.insert(0, usuario[1])
                GLineEdit_893.insert(0, usuario[2])
                GLineEdit_41.insert(0, usuario[3])
                fecha_nac = date(int(usuario[4][:4]), int(usuario[4][5:7]), int(usuario[4][8:]))
                GLineEdit_585.insert(0, fecha_nac.strftime(r"%d/%m/%Y"))
                GLineEdit_655.insert(0, usuario[5])
                GLineEdit_908.insert(0, usuario[6])
                GLineEdit_534.insert(0, usuario[7])
                GLineEdit_944.insert(0, usuario[8])
                GLineEdit_944["state"] = "disabled"
                GLineEdit_920.insert(0, usuario[9])               
                cb_roles.set(usuario[10])

    

    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def GButton_341_command(self):
        self.destroy()

    def aceptar(self):
        try: 
            nombre = self.get_value("txtNombre")           
            apellido = self.get_value("txtApellido")
            dni = self.get_value("txtDni")            
            fecha_nac = self.get_value("txtFechaNac")            
            email = self.get_value("txtEmail")
            domicilio = self.get_value("txtDomicilio")
            telefono = self.get_value("txtNroTelefonico") 
                    
            usuario = self.get_value("txtUsuario")
            contrasenia = self.get_value("txtContrasenia")            
            confirmacion = self.get_value("txtConfirmacion")
            rol_id = self.get_index("cbRoles")

            # TODO validar los datos antes de ingresar
            if self.user_id is None:
                print("Alta de usuario")
                if not user.existe(usuario):
                    user.agregar(nombre, apellido, dni, fecha_nac, email, domicilio, telefono, usuario, contrasenia, rol_id)
                    tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario existente en nuestros registros")
            else:
                print("Actualizacion de usuario")
                user.actualizar(self.user_id, nombre, apellido, dni, fecha_nac, email, domicilio, telefono, contrasenia, rol_id)  # TODO ver el tema de la contraseña
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

    def cancelar(self):
        self.destroy()

    

