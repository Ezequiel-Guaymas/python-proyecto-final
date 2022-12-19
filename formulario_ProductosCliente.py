import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Supermarket")
        #setting window size
        width=481
        height=439
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_136=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_136["font"] = ft
        GLabel_136["fg"] = "#cc0000"
        GLabel_136["justify"] = "center"
        GLabel_136["text"] = "Supermarket"
        GLabel_136.place(x=200,y=10,width=120,height=25)

        GLabel_745=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        GLabel_745["font"] = ft
        GLabel_745["fg"] = "#333333"
        GLabel_745["justify"] = "center"
        GLabel_745["text"] = "Buscar Producto"
        GLabel_745.place(x=0,y=50,width=117,height=30)

        GLineEdit_936=tk.Entry(root)
        GLineEdit_936["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_936["font"] = ft
        GLineEdit_936["fg"] = "#333333"
        GLineEdit_936["justify"] = "center"
        GLineEdit_936["text"] = "Entry"
        GLineEdit_936.place(x=120,y=50,width=258,height=30)

        GButton_168=tk.Button(root)
        GButton_168["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_168["font"] = ft
        GButton_168["fg"] = "#cc0000"
        GButton_168["justify"] = "center"
        GButton_168["text"] = "Buscar"
        GButton_168.place(x=390,y=50,width=70,height=25)
        GButton_168["command"] = self.GButton_168_command

        GLabel_182=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        GLabel_182["font"] = ft
        GLabel_182["fg"] = "#333333"
        GLabel_182["justify"] = "center"
        GLabel_182["text"] = "Id Producto"
        GLabel_182.place(x=20,y=160,width=77,height=30)

        GLineEdit_471=tk.Entry(root)
        GLineEdit_471["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_471["font"] = ft
        GLineEdit_471["fg"] = "#333333"
        GLineEdit_471["justify"] = "center"
        GLineEdit_471["text"] = "Entry"
        GLineEdit_471.place(x=120,y=90,width=344,height=57)

        GLineEdit_920=tk.Entry(root)
        GLineEdit_920["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_920["font"] = ft
        GLineEdit_920["fg"] = "#333333"
        GLineEdit_920["justify"] = "center"
        GLineEdit_920["text"] = "Entry"
        GLineEdit_920.place(x=120,y=160,width=130,height=30)

        GLabel_782=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        GLabel_782["font"] = ft
        GLabel_782["fg"] = "#333333"
        GLabel_782["justify"] = "center"
        GLabel_782["text"] = "Cantidad"
        GLabel_782.place(x=260,y=160,width=70,height=25)

        GLineEdit_439=tk.Entry(root)
        GLineEdit_439["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_439["font"] = ft
        GLineEdit_439["fg"] = "#333333"
        GLineEdit_439["justify"] = "center"
        GLineEdit_439["text"] = "Entry"
        GLineEdit_439.place(x=340,y=160,width=122,height=30)

        GLabel_149=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_149["font"] = ft
        GLabel_149["fg"] = "#333333"
        GLabel_149["justify"] = "center"
        GLabel_149["text"] = "Descripcion"
        GLabel_149.place(x=20,y=210,width=70,height=25)

        GLineEdit_693=tk.Entry(root)
        GLineEdit_693["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_693["font"] = ft
        GLineEdit_693["fg"] = "#333333"
        GLineEdit_693["justify"] = "center"
        GLineEdit_693["text"] = "Entry"
        GLineEdit_693.place(x=20,y=250,width=360,height=64)

        GButton_757=tk.Button(root)
        GButton_757["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_757["font"] = ft
        GButton_757["fg"] = "#cc0000"
        GButton_757["justify"] = "center"
        GButton_757["text"] = "Cargar"
        GButton_757.place(x=390,y=250,width=70,height=25)
        GButton_757["command"] = self.GButton_757_command

        GLabel_948=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_948["font"] = ft
        GLabel_948["fg"] = "#333333"
        GLabel_948["justify"] = "center"
        GLabel_948["text"] = "Borrar Producto"
        GLabel_948.place(x=20,y=330,width=96,height=30)

        GLabel_283=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_283["font"] = ft
        GLabel_283["fg"] = "#333333"
        GLabel_283["justify"] = "center"
        GLabel_283["text"] = "Id Producto"
        GLabel_283.place(x=140,y=330,width=72,height=30)

        GLineEdit_827=tk.Entry(root)
        GLineEdit_827["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_827["font"] = ft
        GLineEdit_827["fg"] = "#333333"
        GLineEdit_827["justify"] = "center"
        GLineEdit_827["text"] = "Entry"
        GLineEdit_827.place(x=220,y=330,width=163,height=31)

        GButton_339=tk.Button(root)
        GButton_339["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_339["font"] = ft
        GButton_339["fg"] = "#cc0000"
        GButton_339["justify"] = "center"
        GButton_339["text"] = "Borrar"
        GButton_339.place(x=390,y=330,width=70,height=25)
        GButton_339["command"] = self.GButton_339_command

        GButton_963=tk.Button(root)
        GButton_963["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=11)
        GButton_963["font"] = ft
        GButton_963["fg"] = "#cc0000"
        GButton_963["justify"] = "center"
        GButton_963["text"] = "Confirmar"
        GButton_963.place(x=290,y=380,width=174,height=36)
        GButton_963["command"] = self.GButton_963_command

        GLabel_434=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_434["font"] = ft
        GLabel_434["fg"] = "#333333"
        GLabel_434["justify"] = "center"
        GLabel_434["text"] = "Confirmar Compra"
        GLabel_434.place(x=150,y=380,width=126,height=33)

    def GButton_168_command(self):
        print("command")


    def GButton_757_command(self):
        print("command")


    def GButton_339_command(self):
        print("command")


    def GButton_963_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
