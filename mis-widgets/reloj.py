import sys #librería para pasarle argumentos a QApplication y salir de la app
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QSpinBox, QTimeEdit, QRadioButton, QGroupBox, QStackedWidget)
# motor, ventana base, texto, layouts (vertical/horizontal), botón, selector numérico, selector de hora, radio, contenedor, vistas apiladas
from PyQt6.QtCore import QTimer, Qt, QTime # temporizador, constantes/flags (ej. alineación), hora del sistema
from PyQt6.QtGui import QFont #tipografia

class Reloj(QWidget): #& clase heredada de QWidget para que sepa que es una ventana
    def __init__(self): #* constructor
        super().__init__()
        self.setWindowTitle("Reloj") # nombre del widget
        self.setFixedSize(400, 500) # medidas del widget. x,y
        self.layoutPrincipal = QVBoxLayout() # si no ponemos esto las cosas no aparecen

        #* vista de la hora
        self.label = QLabel("00:00:00") # crea el texto
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter) # centra el texto
        self.label.setFont(QFont("Monospace", 40)) # tipografia y tamaño
        self.layoutPrincipal.addWidget(self.label) # agrega el label al layout inicial

        #* --- botones ---
        self.layoutModos = QHBoxLayout() # layout horizontal para los botones
        self.btnPomodoro = QPushButton("Pomodoro") # crea el boton pomodoro
        self.btnAlarma = QPushButton("Alarma") # crea el boton alarma
        self.layoutModos.addWidget(self.btnPomodoro) # agrega el boton al layout
        self.layoutModos.addWidget(self.btnAlarma) # agrega el boton alarma
        self.layoutPrincipal.addLayout(self.layoutModos) # agrega el layout botones al principal
        #* ---

        self.setLayout(self.layoutPrincipal) # le dice a la ventana que use este layout para acomodar sus elementos

        #* logica del reloj
        self.timer = QTimer() # crea el temporizador (como un reloj interno que "suena" cada cierto tiempo)
        self.timer.timeout.connect(self.actualizarHora) # cuando suene, ejecuta actualizarHora
        self.timer.start(1000) # se actualiza cada segundo
        self.actualizarHora() # llama a la función 

    def actualizarHora(self): #* '¿qué hora es?' funcion
        hora = QTime.currentTime() # guarda la hora actual en la variable
        self.label.setText(hora.toString("hh:mm:ss")) # formatea la hora y convierte a string
       

#& main
app = QApplication(sys.argv) # crea la app
ventana = Reloj() # crea la ventana
ventana.show() # muestra la ventana
sys.exit(app.exec()) # activa el event loop