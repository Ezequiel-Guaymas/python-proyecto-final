--tabla Usuarios--
CREATE TABLE "Usuarios" (
	"Id_usuario"	INTEGER NOT NULL,
	"Nombre"	TEXT(40) NOT NULL,
	"Aapellido"	TEXT(40) NOT NULL,
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
