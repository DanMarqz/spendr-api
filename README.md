### Spendr API
_Una API para crear un administrador de gastos_

[![Generic badge](https://img.shields.io/badge/<SUBJECT>-<STATUS>-<COLOR>.svg)](https://shields.io/)

Peticiones que se pueden hacer de acuerdo a las rutas:

* **GET /transactions**: Obtienes todos los registros almacenadas en base de datos.
* **GET /transaction/{id}**: Obtienes un registro definido desde la base de datos.
---
* **POST /transactions**: Para ingresar datos a la base de datos de acuerdo al modelo:

```JSON
// JSON De ejemplo para realizar un POST
  {
    "description": "Camisas",
    "price": 15,
    "date": "04/12/2023",
    "category": "Ropa"
  }
```
* **PUT /transaction/{id}**: Para actualizar un registro en la base de datos
---
* **DELETE /transaction/{id}**: Para eliminar un registro de la base de datos