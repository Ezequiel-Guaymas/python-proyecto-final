import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Supermarket")
        #setting window size
        width=585
        height=186
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_575=tk.Entry(root)
        GLineEdit_575["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_575["font"] = ft
        GLineEdit_575["fg"] = "#333333"
        GLineEdit_575["justify"] = "center"
        GLineEdit_575["text"] = "Entry"
        GLineEdit_575.place(x=140,y=30,width=391,height=30)

        GLabel_183=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_183["font"] = ft
        GLabel_183["fg"] = "#333333"
        GLabel_183["justify"] = "center"
        GLabel_183["text"] = "Usuario"
        GLabel_183.place(x=0,y=30,width=125,height=30)

        GLineEdit_775=tk.Entry(root)
        GLineEdit_775["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_775["font"] = ft
        GLineEdit_775["fg"] = "#333333"
        GLineEdit_775["justify"] = "center"
        GLineEdit_775["text"] = "Entry"
        GLineEdit_775.place(x=140,y=80,width=390,height=30)

        GLabel_570=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_570["font"] = ft
        GLabel_570["fg"] = "#333333"
        GLabel_570["justify"] = "center"
        GLabel_570["text"] = "Contraseña"
        GLabel_570.place(x=0,y=80,width=145,height=30)

        GButton_507=tk.Button(root)
        GButton_507["bg"] = "#f0f0f0"
        GButton_507["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=11)
        GButton_507["font"] = ft
        GButton_507["fg"] = "#f51616"
        GButton_507["justify"] = "center"
        GButton_507["text"] = "Crear cuenta"
        GButton_507["relief"] = "groove"
        GButton_507.place(x=10,y=130,width=137,height=30)
        GButton_507["command"] = self.GButton_507_command

        GButton_516=tk.Button(root)
        GButton_516["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_516["font"] = ft
        GButton_516["fg"] = "#cc0000"
        GButton_516["justify"] = "center"
        GButton_516["text"] = "ACEPTAR"
        GButton_516.place(x=270,y=130,width=120,height=30)
        GButton_516["command"] = self.GButton_516_command

        GButton_912=tk.Button(root)
        GButton_912["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_912["font"] = ft
        GButton_912["fg"] = "#cc0000"
        GButton_912["justify"] = "center"
        GButton_912["text"] = "CANCELAR"
        GButton_912.place(x=410,y=130,width=120,height=30)
        GButton_912["command"] = self.GButton_912_command

    def GButton_507_command(self):
        print("command")


    def GButton_516_command(self):
        print("command")


    def GButton_912_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
