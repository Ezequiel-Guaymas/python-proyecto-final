from dal.db2 import Db

def listar():
    sql = "SELECT Id_categoria, Categoria FROM Categorias ORDER BY Id_categoria;"
    result = Db.consultar(sql)
    return result