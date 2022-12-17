import tkinter as tk
import tkinter.font as tkFont

class Pedido_Usuario(tk.Toplevel):
    def __init__(self, master=None):
        #setting title
        super().__init__(master)
        self.master = master
        self.title("Productos")
        #setting window size
        width=600
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_25=tk.Label(self)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_25["font"] = ft
        GLabel_25["fg"] = "#cc0000"
        GLabel_25["justify"] = "center"
        GLabel_25["text"] = "SUPERMARKET"
        GLabel_25.place(x=180,y=20,width=219,height=30)

        GLabel_929=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_929["font"] = ft
        GLabel_929["fg"] = "#333333"
        GLabel_929["justify"] = "center"
        GLabel_929["text"] = "Buscar Nombre"
        GLabel_929.place(x=40,y=60,width=139,height=42)

        GButton_713=tk.Button(self)
        GButton_713["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_713["font"] = ft
        GButton_713["fg"] = "#cc0000"
        GButton_713["justify"] = "center"
        GButton_713["text"] = "Buscar"
        GButton_713.place(x=490,y=70,width=70,height=25)
        GButton_713["command"] = self.GButton_713_command

        GLabel_768=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_768["font"] = ft
        GLabel_768["fg"] = "#333333"
        GLabel_768["justify"] = "center"
        GLabel_768["text"] = "Id del Producto"
        GLabel_768.place(x=40,y=100,width=138,height=30)

        GLabel_80=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_80["font"] = ft
        GLabel_80["fg"] = "#333333"
        GLabel_80["justify"] = "center"
        GLabel_80["text"] = "Cantidad"
        GLabel_80.place(x=210,y=100,width=185,height=30)

        GLineEdit_96=tk.Entry(self)
        GLineEdit_96["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_96["font"] = ft
        GLineEdit_96["fg"] = "#333333"
        GLineEdit_96["justify"] = "center"
        GLineEdit_96["text"] = ""
        GLineEdit_96.place(x=30,y=130,width=167,height=30)

        GLineEdit_280=tk.Entry(self)
        GLineEdit_280["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_280["font"] = ft
        GLineEdit_280["fg"] = "#333333"
        GLineEdit_280["justify"] = "center"
        GLineEdit_280["text"] = ""
        GLineEdit_280.place(x=240,y=130,width=118,height=30)

        GButton_217=tk.Button(self)
        GButton_217["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_217["font"] = ft
        GButton_217["fg"] = "#cc0000"
        GButton_217["justify"] = "center"
        GButton_217["text"] = "Cargar"
        GButton_217.place(x=430,y=130,width=70,height=25)
        GButton_217["command"] = self.GButton_217_command

        GLabel_88=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_88["font"] = ft
        GLabel_88["fg"] = "#333333"
        GLabel_88["justify"] = "center"
        GLabel_88["text"] = "Id del Producto"
        GLabel_88.place(x=10,y=160,width=206,height=30)

        GLabel_234=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_234["font"] = ft
        GLabel_234["fg"] = "#333333"
        GLabel_234["justify"] = "center"
        GLabel_234["text"] = "Cantidad"
        GLabel_234.place(x=250,y=160,width=108,height=30)

        GLineEdit_553=tk.Entry(self)
        GLineEdit_553["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_553["font"] = ft
        GLineEdit_553["fg"] = "#333333"
        GLineEdit_553["justify"] = "center"
        GLineEdit_553["text"] = ""
        GLineEdit_553.place(x=30,y=190,width=169,height=33)

        GLineEdit_448=tk.Entry(self)
        GLineEdit_448["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_448["font"] = ft
        GLineEdit_448["fg"] = "#333333"
        GLineEdit_448["justify"] = "center"
        GLineEdit_448["text"] = ""
        GLineEdit_448.place(x=240,y=190,width=121,height=30)

        GButton_753=tk.Button(self)
        GButton_753["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_753["font"] = ft
        GButton_753["fg"] = "#cc0000"
        GButton_753["justify"] = "center"
        GButton_753["text"] = "Bajar"
        GButton_753.place(x=430,y=190,width=70,height=25)
        GButton_753["command"] = self.GButton_753_command

        GLabel_33=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_33["font"] = ft
        GLabel_33["fg"] = "#333333"
        GLabel_33["justify"] = "center"
        GLabel_33["text"] = "Id del Producto"
        GLabel_33.place(x=50,y=220,width=125,height=30)

        GLabel_761=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_761["font"] = ft
        GLabel_761["fg"] = "#333333"
        GLabel_761["justify"] = "center"
        GLabel_761["text"] = "Cantidad"
        GLabel_761.place(x=250,y=220,width=114,height=30)

        GLineEdit_160=tk.Entry(self)
        GLineEdit_160["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_160["font"] = ft
        GLineEdit_160["fg"] = "#333333"
        GLineEdit_160["justify"] = "center"
        GLineEdit_160["text"] = ""
        GLineEdit_160.place(x=30,y=250,width=165,height=30)

        GLineEdit_65=tk.Entry(self)
        ft = tkFont.Font(family='Times',size=12)
        GLineEdit_65["font"] = ft
        GLineEdit_65["fg"] = "#333333"
        GLineEdit_65["justify"] = "center"
        GLineEdit_65["text"] = ""
        GLineEdit_65.place(x=0,y=0,width=0,height=0)

        GButton_504=tk.Button(self)
        GButton_504["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_504["font"] = ft
        GButton_504["fg"] = "#cc0000"
        GButton_504["justify"] = "center"
        GButton_504["text"] = "modificar"
        GButton_504.place(x=430,y=250,width=70,height=25)
        GButton_504["command"] = self.GButton_504_command

        GLineEdit_768=tk.Entry(self)
        GLineEdit_768["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_768["font"] = ft
        GLineEdit_768["fg"] = "#333333"
        GLineEdit_768["justify"] = "center"
        GLineEdit_768["text"] = ""
        GLineEdit_768.place(x=170,y=60,width=270,height=30)

        GLabel_713=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_713["font"] = ft
        GLabel_713["fg"] = "#333333"
        GLabel_713["justify"] = "center"
        GLabel_713["text"] = "Descripcion del Producto"
        GLabel_713.place(x=180,y=290,width=206,height=30)

        GLineEdit_466=tk.Entry(self)
        GLineEdit_466["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_466["font"] = ft
        GLineEdit_466["fg"] = "#333333"
        GLineEdit_466["justify"] = "center"
        GLineEdit_466["text"] = "Entry"
        GLineEdit_466.place(x=40,y=360,width=535,height=92)

        GLabel_705=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["justify"] = "center"
        GLabel_705["text"] = "Nombre....Marca.....Precio......Cantidad.....Total"
        GLabel_705.place(x=50,y=320,width=452,height=30)

    def GButton_713_command(self):
        print("command")


    def GButton_217_command(self):
        print("command")


    def GButton_753_command(self):
        print("command")


    def GButton_504_command(self):
        print("command")

              


