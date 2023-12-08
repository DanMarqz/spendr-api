### Spendr API
_Una API para crear un administrador de gastos_

[![](https://img.shields.io/badge/Live_preview-8A2BE2?color=darkgreen)](https://spendr-api.1.us-1.fl0.io/)

Para ejecutar este proyecto es necesario:

* Crear un archivo .env para agregar la variable de entorno "MONGO_URI" que es el string de conexion para la base de datos de Mongo
```bash
echo "MONGO_URI=mongodb+srv://..." > .env
```

* Crear un entorno virtual de Python:
```bash
python3 -m venv venv
```

* Ingresar al entorno virtual:
```bash
#Linux
source ./venv/bin/activate

#Windows
.\venv\Scripts\activate
```

* Instalar los paquetes:
```bash
pip install -r requirements.txt
```

* Ejecutar el proyecto:
```bash
uvicorn main:app --hsot 0.0.0.0 --port 5000
```

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