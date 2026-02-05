# Sistema de Gestión de Almacén

## Descripción del proyecto

Este proyecto consiste en una aplicación de escritorio desarrollada en
**Python** utilizando la librería **Tkinter**, cuyo objetivo es
gestionar un almacén de productos de forma sencilla e intuitiva.

El sistema permite: - Crear y gestionar productos. - Controlar el stock
disponible. - Registrar ventas y calcular el dinero ganado. - Aplicar y
eliminar descuentos. - Buscar y eliminar productos. - Generar reportes
del estado del almacén. - Guardar automáticamente los datos para su uso
posterior.

Los datos se almacenan de forma persistente en un archivo **JSON**, por
lo que no se pierden al cerrar el programa.

## Requisitos del sistema

-   Python 3.8 o superior
-   Sistema operativo compatible con Tkinter (Windows, Linux o macOS)

No se requieren librerías externas adicionales.

## Estructura del proyecto

/ ├── tareaFinal.py ├── almacen_datos.json └── README.md

El archivo `almacen_datos.json` se genera automáticamente al ejecutar el
programa por primera vez.

## Ejecución del programa

Ejecuta el programa desde la terminal con:

python tareaFinal.py

Al iniciarse, se abrirá la ventana principal del sistema.

## Uso del programa

### Inventario

Muestra el listado de productos con su ID, nombre, precio y stock,
además del valor total del almacén y el dinero ganado.

### Crear producto

Permite añadir un nuevo producto indicando nombre, precio y cantidad
inicial. El ID se asigna automáticamente.

### Vender producto

Registra una venta indicando el ID del producto y la cantidad a vender.
El sistema valida el stock disponible.

### Gestionar stock

Permite aumentar o disminuir la cantidad disponible de un producto
existente.

### Descuentos

Permite aplicar o quitar descuentos porcentuales entre 0 y 100.

### Buscar y eliminar productos

Permite buscar productos por nombre y eliminarlos por ID con
confirmación.

### Reporte

Muestra un informe detallado del estado actual del almacén.

## Persistencia de datos

Todos los cambios se guardan automáticamente en el archivo JSON y se
cargan al reiniciar el programa.

## Posibles mejoras futuras

-   Uso de base de datos SQLite
-   Exportación de reportes
-   Sistema de usuarios
-   Pruebas automáticas
