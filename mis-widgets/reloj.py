import sys #librería para pasarle argumentos a QApplication y salir limpiamente
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout 
# motor, base de la ventana, texto, acomoda los elementos
from PyQt6.QtCore import QTimer, Qt #temporizador, constantes y flags 
from PyQt6.QtGui import QFont #tipografia

class Reloj(QWidget): #& clase heredada de QWidget para que sepa que es una ventana
    def __init__(self): #* constructor
        super().__init__()
        self.setWindowTitle("Reloj") # nombre del widget
        self.setFixedSize(300, 100) # medidas del widget

        self.label = QLabel("00:00:00") # crea el texto
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter) # lo centra
        self.label.setFont(QFont("Monospace", 40)) # tipografia y tamaño

        layout = QVBoxLayout() # si no ponemos esto las cosas no aparecen
        layout.addWidget(self.label) # agrega el label al layout
        self.setLayout(layout) # asigna el layout a la ventana

        self.timer = QTimer() # crea el temporizador
        self.timer.timeout.connect(self.actualizar_hora) # cada vez que el timer "suena", llama a actualizar_hora
        self.timer.start(1000) # arranca el timer, dispara cada segundo

        self.actualizar_hora() # qué hora es?

    def actualizar_hora(self): #* esta función es la que dirá que hora es
        from PyQt6.QtCore import QTime
        hora = QTime.currentTime() # guarda la hora actual en la variable
        self.label.setText(hora.toString("hh:mm:ss")) # se formatea de forma hora: minuto: segundo y lo pasa a string
        # para que aparezca en la ventana

#& main
app = QApplication(sys.argv) # crea la app
ventana = Reloj() # crea la ventana
ventana.show() # muestra la ventana
sys.exit(app.exec()) # activa el event loop