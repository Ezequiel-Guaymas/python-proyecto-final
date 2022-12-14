from dal.db2 import Db

def listar():
    sql = "SELECT Id_rol, Rol FROM Roles ORDER BY Id_rol;"
    result = Db.consultar(sql)
    return result