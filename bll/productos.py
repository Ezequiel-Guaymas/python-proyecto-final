from dal.db2 import Db

def agregar(nombre, descripcion, marca, precio, cantidad, fecha_elabor, fecha_venc, categoria_Id):    
    sql = "INSERT INTO Productos(Nombre, Descripcion, Marca, Precio, Cantidad, Fecha_Elabor, Fecha_Venc, Categoria_Id) VALUES(?, ?, ?, ?, ?, ?,?, ?);"
    parametros = (nombre, descripcion, marca, precio, cantidad, Db.formato_fecha_db(fecha_elabor), Db.formato_fecha_db(fecha_venc), categoria_Id)
    Db.ejecutar(sql, parametros)

def actualizar(id, precio, cantidad ):    
    sql = "UPDATE Productos SET Precio = ?, Cantidad = ? WHERE Id_producto = ?;"
    parametros = (precio, cantidad, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "DELETE FROM Productos WHERE Id_producto = ?;"
     
    parametros = (id,)
    Db.ejecutar(sql, parametros)

########################################

def listar():
    sql = '''SELECT p.Id_producto, p.Nombre, p.Descripcion, p.Marca, p.Precio, p.Cantidad, p.Fecha_Elabor, p.Fecha_Venc, p.Categoria_Id, c.Categoria
            FROM Productos p
            INNER JOIN Categorias c ON p.Categoria_Id = c.Id_categoria;'''
    result = Db.consultar(sql)
    return result

def filtrar(producto):
    sql = '''SELECT p.Id_producto, p.Nombre, p.Descripcion, p.Marca, p.Precio, p.Cantidad, p.Fecha_Elabor, p.Fecha_Venc, p.Categoria_Id, c.Categoria 
            FROM Productos p
            INNER JOIN Categorias c ON p.Categoria_Id = c.Id_categoria
            WHERE p.Nombre LIKE ?;'''    
    parametros = ('%{}%'.format(producto),)    
    result = Db.consultar(sql, parametros)
    return result

#def validar(usuario, contrasenia):    
 #   sql = "SELECT Usuario FROM Usuarios WHERE Usuario = ? AND Contraseña = ? AND Activo = 1;"
  #  parametros = (usuario, Db.encriptar_contraseña(contrasenia))
   # result = Db.consultar(sql, parametros, False)
    #return result != None

def existe(producto):
    sql = "SELECT COUNT(*) FROM Productos WHERE Nombre = ?;"
    parametros = (producto,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def obtener_id(id):
    sql = '''SELECT p.Id_producto, p.Nombre, p.Descripcion, p.Marca, p.Precio, p.Cantidad, p.Fecha_Elabor, p.Fecha_Venc, p.Categoria_Id, c.Categoria 
            FROM Productos p
            INNER JOIN Categorias c ON p.Categoria_Id = c.Id_categoria
            WHERE p.Id_producto = ?;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result
    
def obtener_nombre_producto(producto):
    sql = '''SELECT p.Id_producto, p.Nombre, p.Descripcion, p.Marca, p.Precio, p.Cantidad, p.Fecha_Elabor, p.Fecha_Venc, p.Categoria_Id, c.Categoria 
            FROM Productos p
            INNER JOIN Categorias c ON p.Categoria_Id = c.Id_categoria
            WHERE Nombre = ?;'''
    parametros = (producto,)
    result = Db.consultar(sql, parametros, False)    
    return result