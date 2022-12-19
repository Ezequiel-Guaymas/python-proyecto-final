import tkinter as tk
import tkinter.font as tkFont

class Pedido(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.title("Realizar Pedido")
        #setting window size
        width=576
        height=660
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_420=tk.Label(self)
        GLabel_420["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_420["font"] = ft
        GLabel_420["fg"] = "#cc0000"
        GLabel_420["justify"] = "center"
        GLabel_420["text"] = "Supermarket"
        GLabel_420.place(x=200,y=0,width=160,height=31)

        GLabel_573=tk.Label(self)
        GLabel_573["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_573["font"] = ft
        GLabel_573["fg"] = "#333333"
        GLabel_573["justify"] = "left"
        GLabel_573["text"] = "Seleccionar productos para el pedido:"
        GLabel_573.place(x=20,y=30,width=301,height=33)

        GLabel_804=tk.Label(self)
        GLabel_804["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "left"
        GLabel_804["text"] = "Buscar Nombre:"
        GLabel_804.place(x=20,y=70,width=126,height=30)

        GLineEdit_876=tk.Entry(self)
        GLineEdit_876["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_876["font"] = ft
        GLineEdit_876["fg"] = "#333333"
        GLineEdit_876["justify"] = "left"
        GLineEdit_876["text"] = ""
        GLineEdit_876.place(x=150,y=70,width=229,height=30)

        GButton_372=tk.Button(self)
        GButton_372["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_372["font"] = ft
        GButton_372["fg"] = "#cc0000"
        GButton_372["justify"] = "center"
        GButton_372["text"] = "BUSCAR"
        GButton_372.place(x=400,y=70,width=125,height=30)
        GButton_372["command"] = self.buscar_producto

        GLineEdit_819=tk.Entry(self)
        GLineEdit_819["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_819["font"] = ft
        GLineEdit_819["fg"] = "#333333"
        GLineEdit_819["justify"] = "center"
        GLineEdit_819["text"] = "Entry"
        GLineEdit_819.place(x=20,y=110,width=529,height=128)

        GLabel_860=tk.Label(self)
        GLabel_860["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_860["font"] = ft
        GLabel_860["fg"] = "#333333"
        GLabel_860["justify"] = "center"
        GLabel_860["text"] = "Colocar ID:"
        GLabel_860.place(x=60,y=240,width=94,height=30)

        GLineEdit_259=tk.Entry(self)
        GLineEdit_259["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_259["font"] = ft
        GLineEdit_259["fg"] = "#333333"
        GLineEdit_259["justify"] = "center"
        GLineEdit_259["text"] = ""
        GLineEdit_259.place(x=20,y=270,width=173,height=30)

        GLabel_171=tk.Label(self)
        GLabel_171["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_171["font"] = ft
        GLabel_171["fg"] = "#333333"
        GLabel_171["justify"] = "center"
        GLabel_171["text"] = "Cantidad:"
        GLabel_171.place(x=230,y=240,width=132,height=30)

        GLineEdit_947=tk.Entry(self)
        GLineEdit_947["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_947["font"] = ft
        GLineEdit_947["fg"] = "#333333"
        GLineEdit_947["justify"] = "center"
        GLineEdit_947["text"] = ""
        GLineEdit_947.place(x=210,y=270,width=174,height=30)

        GButton_940=tk.Button(self)
        GButton_940["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_940["font"] = ft
        GButton_940["fg"] = "#cc0000"
        GButton_940["justify"] = "center"
        GButton_940["text"] = "CARGAR"
        GButton_940.place(x=400,y=270,width=124,height=30)
        GButton_940["command"] = self.cargar_al_pedido

        GLabel_108=tk.Label(self)
        GLabel_108["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=11)
        GLabel_108["font"] = ft
        GLabel_108["fg"] = "#333333"
        GLabel_108["justify"] = "center"
        GLabel_108["text"] = "Vista previa del pedido:"
        GLabel_108.place(x=130,y=300,width=295,height=31)

        GLabel_37=tk.Label(self)
        GLabel_37["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_37["font"] = ft
        GLabel_37["fg"] = "#333333"
        GLabel_37["justify"] = "left"
        GLabel_37["text"] = " ------ Nombre ------ Marca ------ Precio ------ Cantidad ------ Total ------ "
        GLabel_37.place(x=50,y=330,width=505,height=30)

        GLineEdit_668=tk.Entry(self)
        GLineEdit_668["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=8)
        GLineEdit_668["font"] = ft
        GLineEdit_668["fg"] = "#333333"
        GLineEdit_668["justify"] = "center"
        GLineEdit_668["text"] = "Entry"
        GLineEdit_668.place(x=20,y=360,width=532,height=155)

        GLabel_595=tk.Label(self)
        GLabel_595["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_595["font"] = ft
        GLabel_595["fg"] = "#333333"
        GLabel_595["justify"] = "left"
        GLabel_595["text"] = "Eliminar producto del pedido:"
        GLabel_595.place(x=20,y=520,width=255,height=30)

        GLabel_429=tk.Label(self)
        GLabel_429["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_429["font"] = ft
        GLabel_429["fg"] = "#333333"
        GLabel_429["justify"] = "left"
        GLabel_429["text"] = "Colocar Nombre:"
        GLabel_429.place(x=20,y=560,width=121,height=30)

        GLineEdit_284=tk.Entry(self)
        GLineEdit_284["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_284["font"] = ft
        GLineEdit_284["fg"] = "#333333"
        GLineEdit_284["justify"] = "center"
        GLineEdit_284["text"] = ""
        GLineEdit_284.place(x=140,y=560,width=239,height=30)

        GButton_660=tk.Button(self)
        GButton_660["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_660["font"] = ft
        GButton_660["fg"] = "#cc0000"
        GButton_660["justify"] = "center"
        GButton_660["text"] = "BORRAR"
        GButton_660.place(x=400,y=560,width=124,height=30)
        GButton_660["command"] = self.borrar_del_pedido

        GLabel_500=tk.Label(self)
        GLabel_500["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=11)
        GLabel_500["font"] = ft
        GLabel_500["fg"] = "#333333"
        GLabel_500["justify"] = "center"
        GLabel_500["text"] = "CONFIRMAR COMPRA?"
        GLabel_500.place(x=20,y=600,width=168,height=31)

        GButton_140=tk.Button(self)
        GButton_140["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=12)
        GButton_140["font"] = ft
        GButton_140["fg"] = "#cc0000"
        GButton_140["justify"] = "center"
        GButton_140["text"] = "CONFIRMAR"
        GButton_140.place(x=210,y=600,width=175,height=30)
        GButton_140["command"] = self.confirmar_pedido

        GButton_156=tk.Button(self)
        GButton_156["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=12)
        GButton_156["font"] = ft
        GButton_156["fg"] = "#cc0000"
        GButton_156["justify"] = "center"
        GButton_156["text"] = "SALIR"
        GButton_156.place(x=400,y=600,width=122,height=30)
        GButton_156["command"] = self.salir

    def buscar_producto(self):
        print("buscando producto")


    def cargar_al_pedido(self):
        print("cargando al pedido")


    def borrar_del_pedido(self):
        print("borrando producto")


    def confirmar_pedido(self):
        print("confirmando pedido")


    def salir(self):
        self.destroy()


