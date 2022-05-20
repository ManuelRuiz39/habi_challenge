# Habi - Technical Challenge

Este microservicio es solo para propósito de prueba.

## Challenge
El problema principal para el primer reto funcional es básicamente el filtrado por lo que por medio de SQL trataria de de cumplir con la mayoría  de las condiciones como lo es solo obtener propiedades con estatus "vendida,en_venta,en_preventa" así como obtener la ultima actualización de la propiedad que se encuentra en la tabla "status_history" y por ultimo remover los campos que estan como vacios en los campos address,year,etc que seran nuestros posteriores filtros. Una vez filtrada la mayoria de informacion se creara una funcion en la cual el usuario pueda realizar multiples filtros ya sea por ciudad(es),año(s) y su estado.

Para la parte de los filtros asumo que el usuario podra hacer multiples filtros en las 3 diferentes categorias, ejemplo el usuario podra filtrar por medio de "medellin" y "bogota".

Por ultimo tome la decision de hacer una funcion suponiendo que esto corriera en lambda function de aws con el cual podriamos sin problema correrlo y pasar los filtros por
api gateway.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies that you need.

```bash
pip install -r requirements.txt
```
## Environments 

Se creo un archivo .env que por motivos de seguridad no fue agregado al repositorio.


## Usage

Dentro de la carpeta source contiene el codigo de la base de datos que se encarga de realizar la conexion y el sql optimizado para realizar todos los filtros requeridos.
Tambien puedes encontrar el codigo principal que solo es una funcion que recibe un diccionario con los posibles filtros.
