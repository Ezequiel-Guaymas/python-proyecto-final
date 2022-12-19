from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.productos as produc
from formulario_producto import Producto

class Inventario(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("Listado de Productos")        
        width=920
        height=400
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
        GLabel_464["text"] = "PRODUCTOS:"
        GLabel_464.place(x=10,y=10,width=90,height=25)

        tv = ttk.Treeview(self, columns=("nombre", "descripcion", "marca", "precio", "cantidad", "fecha_elaboracion", "fecha_vencimiento", "categoria"), name="tvProductos")
        tv.column("#0", width=80) #id
        tv.column("nombre", width=80, anchor=CENTER)
        tv.column("descripcion", width=160, anchor=CENTER)
        tv.column("marca", width=100, anchor=CENTER)
        tv.column("precio", width=100, anchor=CENTER)
        tv.column("cantidad", width=90, anchor=CENTER)
        tv.column("fecha_elaboracion", width=90, anchor=CENTER)
        tv.column("fecha_vencimiento", width=90, anchor=CENTER)
        tv.column("categoria", width=100, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("nombre", text="Nombre", anchor=CENTER)
        tv.heading("descripcion", text="Descripcion", anchor=CENTER)
        tv.heading("marca", text="Marca", anchor=CENTER)
        tv.heading("precio", text="Precio", anchor=CENTER)
        tv.heading("cantidad", text="Cantidad", anchor=CENTER)
        tv.heading("fecha_elaboracion", text="Fecha Elabor.", anchor=CENTER)
        tv.heading("fecha_vencimiento", text="Fecha Venc.", anchor=CENTER)
        tv.heading("categoria", text="Categoria", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=40,width=900,height=300)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#cc0000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "Agregar"
        btn_agregar.place(x=670,y=10,width=70,height=25)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#cc0000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Editar"
        btn_editar.place(x=750,y=10,width=70,height=25)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#cc0000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=830,y=10,width=70,height=25)
        btn_eliminar["command"] = self.eliminar

        btn_salir = Button(self)
        btn_salir["bg"] = "#f0f0f0"        
        btn_salir["font"] = ft
        btn_salir["fg"] = "#cc0000"
        btn_salir["justify"] = "center"
        btn_salir["text"] = "Salir"
        btn_salir.place(x=760,y=350,width=140,height=40)
        btn_salir["command"] = self.salir

    def obtener_fila(self, event):
        tvProductos = self.nametowidget("tvProductos")
        current_item = tvProductos.focus()
        if current_item:
            data = tvProductos.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Producto(self, True)

    def editar(self): 
        Producto(self, True, self.select_id)

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar este producto del inventario?")   
        if answer:
            produc.eliminar(self.select_id)
            self.refrescar()

    def refrescar(self):        
        tvProductos = self.nametowidget("tvProductos")
        for record in tvProductos.get_children():
            tvProductos.delete(record)
        productos = produc.listar()
        for producto in productos:
            tvProductos.insert("", END, text=producto[0], values=(producto[1], producto[2], producto[3], producto[4], producto[5], producto[6], producto[7], producto[8])) 

    def salir(self):
        self.destroy()