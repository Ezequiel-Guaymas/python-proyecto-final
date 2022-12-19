import tkinter as tk
import tkinter.font as tkFont
from formulario_usuarios import Users

class TableroAdmi(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.title("Menú Administracion")        
        width=480
        height=400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_996=tk.Label(self)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_996["font"] = ft
        GLabel_996["fg"] = "#cc0000"
        GLabel_996["justify"] = "center"
        GLabel_996["text"] = "Supermarket:"
        GLabel_996.place(x=115,y=10,width=250,height=30)

        GButton_196=tk.Button(self)
        GButton_196["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_196["font"] = ft
        GButton_196["fg"] = "#cc0000"
        GButton_196["justify"] = "center"
        GButton_196["text"] = "USUARIOS"
        GButton_196.place(x=115,y=60,width=250,height=45)
        GButton_196["command"] = self.abrir_usuarios

        GButton_245=tk.Button(self)
        GButton_245["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_245["font"] = ft
        GButton_245["fg"] = "#cc0000"
        GButton_245["justify"] = "center"
        GButton_245["text"] = "PRODUCTOS"
        GButton_245.place(x=115,y=120,width=250,height=45)
        GButton_245["command"] = self.abrir_productos

        GButton_430=tk.Button(self)
        GButton_430["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_430["font"] = ft
        GButton_430["fg"] = "#cc0000"
        GButton_430["justify"] = "center"
        GButton_430["text"] = "PEDIDOS"
        GButton_430.place(x=115,y=180,width=250,height=45)
        GButton_430["command"] = self.abrir_pedidos

        GButton_296=tk.Button(self)
        GButton_296["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_296["font"] = ft
        GButton_296["fg"] = "#cc0000"
        GButton_296["justify"] = "center"
        GButton_296["text"] = "SALIR"
        GButton_296.place(x=115,y=240,width=250,height=45)
        GButton_296["command"] = self.salir

    def abrir_usuarios(self):
        Users(self)

    def abrir_productos(self):
        print("productos")

    def abrir_pedidos(self):
        print("pedidos")
    
    def salir(self):
        self.destroy()