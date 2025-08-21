# progamacion-software
DOCUMENTACION DE PROGRAMACION DE SOFTWARE

# 📌 Pydantic en Python

## 🔹 ¿Qué es Pydantic?
**Pydantic** es una librería de Python que permite **validar datos y crear modelos** de manera sencilla usando **type hints**.  
Convierte automáticamente los datos al tipo correcto y valida que cumplan con las restricciones que definas.  

Ejemplo rápido:

```python
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    activo: bool = True

u = Usuario(id="1", nombre="Emmanuel")
print(u.id, type(u.id))  # 1 <class 'int'>

🔹 ¿Cómo funciona?

Usa type hints de Python (str, int, float, etc.).

Al crear una clase que hereda de BaseModel, Pydantic:

Valida los datos.

Convierte tipos automáticamente (ejemplo: "1" → 1).

Genera errores claros si los datos no son válidos.

Ejemplo con validación:

from pydantic import BaseModel

class Producto(BaseModel):
    nombre: str
    precio: float

try:
    p = Producto(nombre="Zapatos", precio="abc")
except Exception as e:
    print(e)


Resultado:

1 validation error for Producto
precio
  value is not a valid float (type=type_error.float)

🔹 ¿Para qué se usa?

Pydantic se utiliza principalmente en:

🚀 APIs y frameworks (ejemplo: FastAPI
) → Validación automática de entrada/salida de datos.

⚙️ Configuración de proyectos → Manejo de settings con validación automática.

📊 Procesamiento de datos → Garantizar que los datos cumplan un esquema antes de usarlos.

🔹 Instalación

Instala la última versión con:

pip install pydantic


O una versión específica (por ejemplo, v1):

pip install "pydantic<2.0"