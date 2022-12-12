from dal.db2 import Db

def agregar(nombre, apellido, dni, fecha_nac, email, domicilio, telefono, usuario, contrasenia, rol_Id):    
    sql = "INSERT INTO Usuarios(Nombre, Apellido, DNI, Fecha_Nacimiento, Email, Domicilio, Nro.Telefonico, Usuario, Contraseña, Rol_Id) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
    parametros = (nombre, apellido, dni, Db.formato_fecha_db(fecha_nac), email, domicilio, telefono, Db.encriptar_contraseña(contrasenia), rol_Id)
    Db.ejecutar(sql, parametros)

def actualizar(id, nombre, apellido, dni, fecha_nac, email, domicilio, telefono, contrasenia, rol_Id):    
    sql = "UPDATE Usuarios SET Nombre = ?, Apellido = ?, Dni = ?, Fecha_Nacimiento = ?, Email = ?, Domicilio = ?, Nro.Telefonico = ?, Contrasenia = ?, Rol_Id = ? WHERE Id_usuario = ? AND Activo = 1;"
    parametros = (nombre, apellido, dni, Db.formato_fecha_db(fecha_nac), email, domicilio, telefono, Db.encriptar_contraseña(contrasenia), rol_Id, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE Usuarios SET Activo = 0 WHERE Id_usuario = ? AND Activo = 1;"
    else:
        sql = "DELETE FROM Usuarios WHERE Id_usuario = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT u.Id_usuario, u.Nombre, u.Apellido, u.Dni, u.Fecha_Nacimiento, u.Email, u.Domicilio, u.Nro.Telefonico, u.Usuario, u.Rol_Id, r.Nombre Rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.RolId = r.RolId
            WHERE u.Activo = 1;'''
    result = Db.consultar(sql)
    return result

def filtrar(usuario):    
    sql = '''SELECT u.UsuarioId, u.Apellido, u.Nombre, u.FechaNacimiento, u.Dni, u.CorreoElectronico, u.Usuario, u.RolId, r.Nombre Rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.RolId = r.RolId
            WHERE u.Usuario LIKE ? AND u.Activo = 1;'''    
    parametros = ('%{}%'.format(usuario),)    
    result = Db.consultar(sql, parametros)
    return result

def validar(usuario, contrasenia):    
    sql = "SELECT Usuario FROM Usuarios WHERE Usuario = ? AND Contrasenia = ? AND Activo = 1;"
    parametros = (usuario, Db.encriptar_contraseña(contrasenia))
    result = Db.consultar(sql, parametros, False)
    return result != None

def existe(usuario):
    sql = "SELECT COUNT(*) FROM Usuarios WHERE Usuario = ? AND Activo = 1;"
    parametros = (usuario,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def obtener_id(id):
    sql = '''SELECT u.UsuarioId, u.Apellido, u.Nombre, u.FechaNacimiento, u.Dni, u.CorreoElectronico, u.Usuario, u.RolId, r.Nombre Rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.RolId = r.RolId
            WHERE u.UsuarioId = ? AND u.Activo = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result