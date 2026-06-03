### APUNTES MIENTRAS APRENDO
---
## PYQt6
Qt es una toolkit para widgets y aplicaciones, está mayormente escrito en C++ y se usa para contruir GUIs. PYQt6 es como el traductor que permite usar esa toolkit desde Phyton.

**QApplication** es el motor de la app, solo existe uno, es como el main() para la interfaz gráfica.
**QWidget** es la unidad básica de todo, cualquier cosa que quiera poner en la app o widget (ventana, botón, label, texto) es un QWidget o lo hereda de él.
**Signals and slots** son los event listeners de Qt. El objeto emite una señal cuando algo pasa y otro objeto lo escucha con un slot.
**Layouts** controlan cómo se acomodan los elementos visualmente:
- QVBoxLayout: los apila verticalmente
- QHBoxLayout: los pone en fila horizontal
- QGridLayout: cuadrícula, como una tabla
**QPainter** se usa para dibujar cosas personalizadas, como un canvas.
---
## Plantilla
```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget

# 1. Crea la aplicación
app = QApplication(sys.argv)

# 2. Crea tu ventana (puede ser una clase propia)
ventana = QWidget()
ventana.setWindowTitle("Mi primer widget")
ventana.resize(300, 200)
ventana.show()

# 3. Arranca el loop de eventos, es el event loop
sys.exit(app.exec())
```
---
## Repos útiles
- https://github.com/pythonguis/pythonguis-examples
- https://github.com/pyqt/examples
- https://github.com/HundredVisionsGuy/Guide-to-PyQt6
## venv y uso
Un entorno virtual es una carpeta que contiene su propia instalación de Python y sus propios paquetes, aisalada del resto del sistema. Se usa para que en lugar de que el PYQt6 se instale en toda la compu, se instala en una cajita exclusiva para ese projecto. Si algo se ropme, puedo tirar la cajita y hacer otra nueva sin tocar mi sistema.
Para hacerlo hacemos una carpeta, hacemos el entorno virual donde viviran todos los paquetes `python3 -m venv venv`, y lo activo con `source venv/bin/activate`.
Cada que quiera modificar el proyecto, tengo que activarlo para que Python encuentre el PYQt6. Igual es importante hacer el requirements.txt, que será un archivo con todas las dependencias y sus versionas, así si alguien más quiere correr el proyecto, solo tiene que usar `pip install -r requirements.txt` (<- buena practica).
