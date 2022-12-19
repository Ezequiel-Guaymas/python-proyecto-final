from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.productos as produc
import bll.categorias as categ
from datetime import date

class Producto(Toplevel):
    def __init__(self, master=None, isAdmin = False, produc_id = None):        
        super().__init__(master)
        self.master = master
        self.produc_id = produc_id       
        self.title("Registro de producto")        
        width=443
        height=423
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        
        GLabel_243 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_243["font"] = ft
        GLabel_243["fg"] = "#333333"
        GLabel_243["anchor"] = "e"
        GLabel_243["text"] = "Nombre:"
        GLabel_243.place(x=10,y=10,width=124,height=30)

        GLineEdit_871 = Entry(self, name="txtNombre")
        GLineEdit_871["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_871["font"] = ft
        GLineEdit_871["fg"] = "#333333"
        GLineEdit_871["justify"] = "left"
        GLineEdit_871["text"] = ""
        GLineEdit_871.place(x=140,y=10,width=284,height=30)

        GLabel_599 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_599["font"] = ft
        GLabel_599["fg"] = "#333333"
        GLabel_599["anchor"] = "e"
        GLabel_599["text"] = "Descripcion:"
        GLabel_599.place(x=10,y=50,width=122,height=30)

        GLineEdit_911 = Entry(self, name="txtDescripcion")
        GLineEdit_911["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_911["font"] = ft
        GLineEdit_911["fg"] = "#333333"
        GLineEdit_911["justify"] = "left"
        GLineEdit_911["text"] = ""
        GLineEdit_911.place(x=140,y=50,width=285,height=30)        

        GLabel_600 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_600["font"] = ft
        GLabel_600["fg"] = "#333333"
        GLabel_600["anchor"] = "e"
        GLabel_600["text"] = "Marca:"
        GLabel_600.place(x=10,y=90,width=123,height=30)

        GLineEdit_208 = Entry(self, name="txtMarca")
        GLineEdit_208["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_208["font"] = ft
        GLineEdit_208["fg"] = "#333333"
        GLineEdit_208["justify"] = "left"
        GLineEdit_208["text"] = ""
        GLineEdit_208.place(x=140,y=90,width=180,height=30)

        GLabel_737 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_737["font"] = ft
        GLabel_737["fg"] = "#333333"
        GLabel_737["anchor"] = "e"
        GLabel_737["text"] = "Precio:"
        GLabel_737.place(x=10,y=130,width=121,height=30)

        GLineEdit_234 = Entry(self, name="txtPrecio")
        GLineEdit_234["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_234["font"] = ft
        GLineEdit_234["fg"] = "#333333"
        GLineEdit_234["justify"] = "left"
        GLineEdit_234["text"] = ""
        GLineEdit_234.place(x=140,y=130,width=133,height=30)

        GLabel_454 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_454["font"] = ft
        GLabel_454["fg"] = "#333333"
        GLabel_454["anchor"] = "e"
        GLabel_454["text"] = "Cantidad:"
        GLabel_454.place(x=10,y=170,width=124,height=30)

        GLineEdit_384 = Entry(self, name="txtCantidad")
        GLineEdit_384["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_384["font"] = ft
        GLineEdit_384["fg"] = "#333333"
        GLineEdit_384["justify"] = "left"
        GLineEdit_384["text"] = ""
        GLineEdit_384.place(x=140,y=170,width=133,height=30)

        GLabel_616 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_616["font"] = ft
        GLabel_616["fg"] = "#333333"
        GLabel_616["anchor"] = "e"
        GLabel_616["text"] = "Fecha Elabor.:"
        GLabel_616.place(x=10,y=210,width=123,height=30)

        GLineEdit_481 = Entry(self, name="txtElabor")
        GLineEdit_481["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_481["font"] = ft
        GLineEdit_481["fg"] = "#333333"
        GLineEdit_481["justify"] = "left"
        GLineEdit_481["text"] = ""
        GLineEdit_481.place(x=140,y=210,width=133,height=30)

        GLabel_61 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_61["font"] = ft
        GLabel_61["fg"] = "#333333"
        GLabel_61["anchor"] = "e"
        GLabel_61["text"] = "Fecha Venc.:"
        GLabel_61.place(x=10,y=250,width=124,height=30)

        GLineEdit_366 = Entry(self, name="txtVenc")
        GLineEdit_366["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_366["font"] = ft
        GLineEdit_366["fg"] = "#333333"
        GLineEdit_366["justify"] = "left"
        GLineEdit_366["text"] = ""
        GLineEdit_366.place(x=140,y=250,width=133,height=30)                

        GLabel_975 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_975["font"] = ft
        GLabel_975["fg"] = "#333333"
        GLabel_975["anchor"] = "e"
        GLabel_975["text"] = "Categoria:"
        GLabel_975.place(x=10,y=330,width=122,height=30)
        
        categorias = dict(categ.listar())
        if isAdmin:
            cb_categorias = ttk.Combobox(self, state="readonly", values=list(categorias.values()), name="cbCategorias")
        cb_categorias.place(x=140,y=330,width=230,height=30)

        GButton_825 = Button(self)
        GButton_825["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_825["font"] = ft
        GButton_825["fg"] = "#cc0000"
        GButton_825["justify"] = "center"
        GButton_825["text"] = "Aceptar"
        GButton_825.place(x=270,y=370,width=70,height=25)
        GButton_825["command"] = self.aceptar
        
        GButton_341 = Button(self)
        GButton_341["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_341["font"] = ft
        GButton_341["fg"] = "#cc0000"
        GButton_341["justify"] = "center"
        GButton_341["text"] = "Cancelar"
        GButton_341.place(x=350,y=370,width=70,height=25)
        GButton_341["command"] = self.GButton_341_command

        if produc_id is not None:
            producto = produc.obtener_id(produc_id)
            if producto is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del producto, reintente nuevamente")
               self.destroy()
            else:
                GLineEdit_871.insert(0, producto[1])
                #GLineEdit_871["state"] = "disabled" 
                GLineEdit_911.insert(0, producto[2])
                #GLineEdit_911["state"] = "disabled"
                GLineEdit_208.insert(0, producto[3])
                #GLineEdit_208["state"] = "disabled"
                GLineEdit_234.insert(0, producto[4])
                GLineEdit_384.insert(0, producto[5])
                fecha_elabor = date(int(producto[6][:4]), int(producto[6][5:7]), int(producto[6][8:]))
                GLineEdit_481.insert(0, fecha_elabor.strftime(r"%d/%m/%Y"))
                #GLineEdit_481["state"] = "disabled"
                fecha_venc = date(int(producto[7][:4]), int(producto[7][5:7]), int(producto[7][8:]))
                GLineEdit_366.insert(0, fecha_venc.strftime(r"%d/%m/%Y"))
                #GLineEdit_366["state"] = "disabled"           
                cb_categorias.set(producto[8])
                #cb_categorias["state"] = "disabled"


    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def GButton_341_command(self):
        self.destroy()

    def aceptar(self):
        try:            
            nombre = self.get_value("txtNombre")
            descripcion = self.get_value("txtDescripcion")
            marca = self.get_value("txtMarca")
            precio = self.get_value("txtPrecio")
            cantidad = self.get_value("txtCantidad")            
            fecha_elabor = self.get_value("txtElabor")
            fecha_venc = self.get_value("txtVenc")            
            categoria_id = self.get_index("cbCategorias")

            if self.produc_id is None:
                print("Alta del producto")
                if not produc.existe(nombre):
                    produc.agregar(nombre, descripcion, marca, precio, cantidad, fecha_elabor, fecha_venc, categoria_id)
                    tkMsgBox.showinfo(self.master.title(), "Producto agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    tkMsgBox.showwarning(self.master.title(), "Producto existente en nuestros inventario")
            else:
                print("Actualizacion de producto")
                produc.actualizar(self.produc_id, precio, cantidad)  
                tkMsgBox.showinfo(self.master.title(), "Producto modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))