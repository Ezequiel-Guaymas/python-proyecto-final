import tkinter as tk
import tkinter.font as tkFont
from formulario_login import Login
from dal.db2 import Db

class App:
    def __init__(self, root, title):
        self.root = root
        #setting title
        root.title(title)
        #setting window size
        width=498
        height=220
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_522=tk.Button(root)
        GButton_522["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        GButton_522["font"] = ft
        GButton_522["fg"] = "#e82727"
        GButton_522["justify"] = "center"
        GButton_522["text"] = "ABRIR "+ title.upper()
        GButton_522.place(x=60,y=140,width=362,height=37)
        GButton_522["command"] = self.abrir_login

        GLabel_3=tk.Label(root)
        GLabel_3["bg"] = "#cc0000"
        ft = tkFont.Font(family='Times',size=24)
        GLabel_3["font"] = ft
        GLabel_3["fg"] = "#f6f0f0"
        GLabel_3["justify"] = "center"
        GLabel_3["text"] = "BIENVENIDO"
        GLabel_3.place(x=90,y=60,width=290,height=42)

    def abrir_login(self):
        Login(self.root)

if __name__ == "__main__":
    Db.crear_tablas()
    Db.poblar_tablas()
    proyecto = "Supermarket"
    root = tk.Tk()
    root.iconbitmap(default=f"{proyecto}.ico")
    app = App(root,  proyecto.capitalize())
    root.mainloop()