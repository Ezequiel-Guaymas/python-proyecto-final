from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.usuarios as user
from formulario_user import User

class Users(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("Listado de Usuarios")        
        width=1040
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Usuarios:"
        GLabel_464.place(x=10,y=10,width=70,height=25)

        tv = ttk.Treeview(self, columns=("usuario", "nombre", "apellido", "dni", "fecha_nac", "email", "domicilio", "nro_telefono", "rol"), name="tvUsuarios")
        tv.column("#0", width=60) #id
        tv.column("usuario", width=80, anchor=CENTER)
        tv.column("nombre", width=160, anchor=CENTER)
        tv.column("apellido", width=100, anchor=CENTER)
        tv.column("dni", width=80, anchor=CENTER)
        tv.column("fecha_nac", width=80, anchor=CENTER)
        tv.column("email", width=130, anchor=CENTER)
        tv.column("domicilio", width=130, anchor=CENTER)
        tv.column("nro_telefono", width=90, anchor=CENTER)
        tv.column("rol", width=100, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("usuario", text="Usuario", anchor=CENTER)
        tv.heading("nombre", text="Nombre", anchor=CENTER)
        tv.heading("apellido", text="Apellido", anchor=CENTER)
        tv.heading("dni", text="DNI", anchor=CENTER)
        tv.heading("fecha_nac", text="Fecha Nac.", anchor=CENTER)
        tv.heading("email", text="Email", anchor=CENTER)
        tv.heading("domicilio", text="Domicilio", anchor=CENTER)
        tv.heading("nro_telefono", text="Nro. Telefono", anchor=CENTER)
        tv.heading("rol", text="Rol", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=40,width=1020,height=400)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#cc0000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "Agregar"
        btn_agregar.place(x=800,y=10,width=70,height=25)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#cc0000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Editar"
        btn_editar.place(x=880,y=10,width=70,height=25)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#cc0000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=960,y=10,width=70,height=25)
        btn_eliminar["command"] = self.eliminar

        btn_salir = Button(self)
        btn_salir["bg"] = "#f0f0f0"        
        btn_salir["font"] = ft
        btn_salir["fg"] = "#cc0000"
        btn_salir["justify"] = "center"
        btn_salir["text"] = "Salir"
        btn_salir.place(x=890,y=450,width=140,height=40)
        btn_salir["command"] = self.salir

    def obtener_fila(self, event):
        tvUsuarios = self.nametowidget("tvUsuarios")
        current_item = tvUsuarios.focus()
        if current_item:
            data = tvUsuarios.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        User(self, True)

    def editar(self): 
        User(self, True, self.select_id)

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar este registro?")   
        if answer:
            user.eliminar(self.select_id)
            self.refrescar()

    # https://www.youtube.com/watch?v=n0usdtoU5cE
    def refrescar(self):        
        tvUsuarios = self.nametowidget("tvUsuarios")
        for record in tvUsuarios.get_children():
            tvUsuarios.delete(record)
        usuarios = user.listar()
        for usuario in usuarios:
            tvUsuarios.insert("", END, text=usuario[0], values=(usuario[8], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6], usuario[7], usuario[10])) 

    def salir(self):
        self.destroy()