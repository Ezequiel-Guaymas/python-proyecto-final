import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root, proyecto):
        #setting title
        root.title(proyecto)
        #setting window size
        width=555
        height=224
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_803=tk.Button(root)
        GButton_803["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_803["font"] = ft
        GButton_803["fg"] = "#000000"
        GButton_803["justify"] = "center"
        GButton_803["text"] = "ABRIR SUPERMARKET"
        GButton_803.place(x=40,y=120,width=452,height=42)
        GButton_803["command"] = self.GButton_803_command

        GMessage_458=tk.Message(root)
        ft = tkFont.Font(family='Times',size=16)
        GMessage_458["font"] = ft
        GMessage_458["fg"] = "#333333"
        GMessage_458["justify"] = "center"
        GMessage_458["text"] = "BIENVENIDO"
        GMessage_458.place(x=120,y=100,width=400,height=60)

    def GButton_803_command(self):
        print("command")

if __name__ == "__main__":
    proyecto = "supermarket"
    root = tk.Tk()
    root.iconbitmap(default=f"{proyecto}.ico")
    app = App(root,  proyecto.capitalize())
    root.mainloop()
