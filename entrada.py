from PySide2.QtWidgets import QPushButton, QApplication #referencia del path y la clase QApplication()
from mainwindow import MainWindow #archivos con minusculas y clases con mayusculas
import sys

# Aplicación de Qt
app = QApplication()
# Se crea una ventana
window = MainWindow()
# Se hace visible la ventana
window.show()
# Qt loop ==> finaliza el bucle hasta cerrar la ventana
sys.exit(app.exec_())

#correr programa desde este archivo principal
