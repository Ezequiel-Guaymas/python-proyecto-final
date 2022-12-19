import sqlite3
from datetime import date
import hashlib

database = "Supermarket.db"

class Db:
    @staticmethod
    def ejecutar(consulta, parametros = ()):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, parametros)
            cnn.commit()            
    
    @staticmethod
    def consultar(consulta, pametros = (), fetchAll = True):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, pametros)
            if fetchAll:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            return result
    
    @staticmethod
    def crear_tablas():
        sql_usuarios = '''CREATE TABLE IF NOT EXISTS "Usuarios" (
                            "Id_usuario"	INTEGER NOT NULL,
                            "Nombre"	TEXT(40) NOT NULL,
                            "Aapellido"	TEXT(40) NOT NULL,
                            "DNI"	INTEGER(20) NOT NULL,
                            "Fecha_Nacimiento"	TEXT(10) NOT NULL,
                            "Email"	TEXT(30) NOT NULL,
                            "Domicilio"	TEXT(30) NOT NULL,
                            "Nro_Telefonico" INTEGER(20) NOT NULL,
                            "Usuario" TEXT(30) NOT NULL UNIQUE,
                            "Contraseña" TEXT(30) NOT NULL,
                            "Rol_Id" INTEGER,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            "Pedido_id"	INTEGER,
                            PRIMARY KEY("Id_usuario" AUTOINCREMENT),
                            FOREIGN KEY("Rol_Id") REFERENCES "Roles"("Id_rol"),
                            FOREIGN KEY("Pedido_id") REFERENCES "Pedidos"("Id_pedido")
                        );'''
        sql_roles = '''CREATE TABLE IF NOT EXISTS "Roles" (
                            "Id_rol"	INTEGER NOT NULL,
                            "Rol"	TEXT(50) NOT NULL ,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("Id_rol")
                        );'''
        sql_productos = '''CREATE TABLE IF NOT EXISTS "Productos" (
                            "Id_producto"	INTEGER NOT NULL,
                            "Nombre"	TEXT(30) NOT NULL,
                            "Descripcion"	TEXT(50) NOT NULL,
                            "Marca"	TEXT(30) NOT NULL,
                            "Precio"	REAL(10) NOT NULL,
                            "Cantidad"	INTEGER NOT NULL,
                            "Fecha_Elabor"	TEXT(20) NOT NULL,
                            "Fecha_Venc"	TEXT(20) NOT NULL,
                            "Categoria_Id"	INTEGER,
                            FOREIGN KEY("Categoria_id") REFERENCES "Categorias de Productos"("Id_categoria"),
                            PRIMARY KEY("Id_producto" AUTOINCREMENT)
                        );'''
        sql_categorias = '''CREATE TABLE IF NOT EXISTS "Categorias" (
                            "Id_categoria"	INTEGER NOT NULL,
                            "Categoria"	TEXT(50) NOT NULL,
                            PRIMARY KEY("Id_categoria")
                        )'''

        tablas = {"Usuarios": sql_usuarios, "Roles": sql_roles, "Productos": sql_productos, "Categorias": sql_categorias}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
                cnn.commit() #
                # TODO agregar commit
            
    @staticmethod
    def poblar_tablas():        
        sql_roles = '''INSERT INTO Roles (Id_rol, Rol) 
                    VALUES 
                        (1, "Administrador"),
                        (2, "Supervisor"),
                        (3, "Operador"),
                        (4, "Cliente");'''

        sql_categorias = '''INSERT INTO Categorias (Id_categoria, Categoria) 
                    VALUES 
                        (1, "Aseo"),
                        (2, "Alimentos Frescos"),
                        (3, "Alimentos Congelados"),
                        (4, "Bebidas"),
                        (5, "Bebidas con Alcohol"),
                        (6, "Cuidado Personal"),
                        (7, "Carnes"),
                        (8, "Despensas"),
                        (9, "Golosinas"),
                        (10, "Lacteos");'''

        tablas = {"Roles": sql_roles, "Categorias": sql_categorias}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                cnn.commit() #
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql)
                    cnn.commit() #

    @staticmethod
    def formato_fecha_db(fecha):
        return date(int(fecha[6:]), int(fecha[3:5]), int(fecha[0:2]))
    
    @staticmethod
    def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()