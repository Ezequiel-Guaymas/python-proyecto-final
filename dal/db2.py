import sqlite3
from datetime import date
import hashlib

database = "Supermarket.db" # todo: por ahora ponemos el nombre de la base aqui, ver mejor opcion

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
        sql_usuarios = '''CREATE TABLE "Usuarios" (
                            "Id_usuario"	INTEGER NOT NULL,
                            "Nombre"	TEXT(40) NOT NULL,
                            "Aapellido"	TEXT(40) NOT NULL,
                            "DNI"	INTEGER(20) NOT NULL,
                            "Fecha_Nacimiento"	TEXT(10) NOT NULL,
                            "Email"	TEXT(30) NOT NULL,
                            "Domicilio"	TEXT(30) NOT NULL,
                            "Nro_Telefonico" INTEGER(20) NOT NULL,
                            "Usuario" TEXT(30) NOT NULL UNIQUE,
                            "Contraseña" TEXT(30) NOT NULL UNIQUE,
                            "Rol_Id" INTEGER,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            "Pedido_id"	INTEGER,
                            PRIMARY KEY("Id_usuario" AUTOINCREMENT),
                            FOREIGN KEY("Rol_Id") REFERENCES "Roles"("Id_rol"),
                            FOREIGN KEY("Pedido_id") REFERENCES "Pedidos"("Id_pedido")
                        );'''
        sql_roles = '''CREATE TABLE "Roles" (
                            "Id_rol"	INTEGER NOT NULL,
                            "Rol"	TEXT(50) NOT NULL UNIQUE,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("Id_rol")
                        );'''

        tablas = {"Usuarios": sql_usuarios, "Roles": sql_roles}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
                #cnn.commit() #
                # TODO agregar commit
            
    @staticmethod
    def poblar_tablas():        
        sql_roles = '''INSERT INTO Roles (RolId, Rol) 
                    VALUES 
                        (1, "Administrador"),
                        (2, "Supervisor"),
                        (3, "Operador"),
                        (4, "Cliente");'''

        tablas = {"Roles": sql_roles}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                #cnn.commit() #
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql)
                    #cnn.commit() #

    @staticmethod
    def formato_fecha_db(fecha):
        return date(int(fecha[6:]), int(fecha[3:5]), int(fecha[0:2]))
    
    @staticmethod
    def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()



'''--tabla Usuarios--
CREATE TABLE "Usuarios" (
	"Id_usuario"	INTEGER NOT NULL,
	"Nombre"	TEXT(40) NOT NULL,
	"Apellido"	TEXT(40) NOT NULL,
	"DNI"	INTEGER(10) NOT NULL,
	"Sexo"	TEXT(10) NOT NULL,
	"Nro.Telefonico"	INTEGER(20) NOT NULL,
	"Email"	TEXT(30) NOT NULL,
	"Direccion"	TEXT(30) NOT NULL,
	"Fecha_Registro"	TEXT(10) NOT NULL,
	"Nombre_Usuario"	TEXT(30) NOT NULL UNIQUE,
	"Contraseña"	TEXT(30) NOT NULL UNIQUE,
	"Rol_Id"	INTEGER,
	"Pedido_id"	INTEGER,
	PRIMARY KEY("Id_usuario" AUTOINCREMENT),
	FOREIGN KEY("Rol_Id") REFERENCES "Roles"("Id_rol"),
	FOREIGN KEY("Pedido_id") REFERENCES "Pedidos"("Id_pedido")
)

--tabla Roles--
CREATE TABLE "Roles" (
	"Id_rol"	INTEGER NOT NULL,
	"Rol"	TEXT(50) NOT NULL DEFAULT 'Cliente',
	PRIMARY KEY("Id_rol" AUTOINCREMENT)
)

--Tabla Productos--
CREATE TABLE "Productos" (
	"Id_producto"	INTEGER NOT NULL,
	"Nombre_producto"	TEXT(30) NOT NULL,
	"Descripcion"	TEXT(50) NOT NULL,
	"Marca_producto"	TEXT(30) NOT NULL,
	"Precio"	REAL(10) NOT NULL,
	"Cantidad"	INTEGER NOT NULL,
	"Fecha_elaboracion"	TEXT(20) NOT NULL,
	"fehca_vencimiento"	TEXT(20) NOT NULL,
	"Categoria_id"	INTEGER,
	PRIMARY KEY("Id_producto" AUTOINCREMENT),
	FOREIGN KEY("Categoria_id") REFERENCES "Categorias de Productos"("Id_categoria")
)

--Categoria de Productos--
CREATE TABLE "Categorias de Productos" (
	"Id_categoria"	INTEGER NOT NULL,
	"Categoria"	TEXT(30) NOT NULL,
	PRIMARY KEY("Id_categoria" AUTOINCREMENT)
)

--Tabla Pedidos--
CREATE TABLE "Pedidos" (
	"Id_pedido"	INTEGER NOT NULL,
	"Fecha_pedido"	TEXT(15) NOT NULL,
	"Producto"	TEXT(30) NOT NULL,
	"Cantidad"	INTEGER NOT NULL,
	"Total_pedido"	REAL(10) NOT NULL,
	PRIMARY KEY("Id_pedido" AUTOINCREMENT)
)

--Tabla Detalle/Factura del pedido--
CREATE TABLE "Facturas de Pedidos" (
	"Id_factura"	INTEGER NOT NULL,
	"fecha"	TEXT,
	"Detalle"	TEXT,
	"Cantidad"	INTEGER,
	"Total"	REAL,
	"Pedido_id"	INTEGER,
	FOREIGN KEY("Total") REFERENCES "Pedidos"("Total_pedido"),
	FOREIGN KEY("Cantidad") REFERENCES "Pedidos"("Cantidad"),
	FOREIGN KEY("fecha") REFERENCES "Pedidos"("Fecha_pedido"),
	FOREIGN KEY("Pedido_id") REFERENCES "Pedidos"("Id_pedido"),
	FOREIGN KEY("Detalle") REFERENCES "Pedidos"("Producto"),
	PRIMARY KEY("Id_factura" AUTOINCREMENT)
)
'''