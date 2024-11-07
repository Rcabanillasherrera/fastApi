create database fastapidb;
use fastapidb;

CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    direccion VARCHAR(100),
    telefono VARCHAR(15),
    email VARCHAR(50),
    INDEX(nombre)
);

insert into clientes( nombre, direccion, telefono, email) values('richard', 'jiron las flores', 999999990, 'richard99@hotmail.com');
insert into clientes( nombre, direccion, telefono, email) values('joel', 'urb virgen del rosario', 999999992, 'joel2@hotmail.com');
insert into clientes( nombre, direccion, telefono, email) values('luciana', 'manuel 32', 999999993, 'luci13@hotmail.com');
insert into clientes( nombre, direccion, telefono, email) values('samir', 'ah la pama', 999999994, 's25a@hotmail.com');

