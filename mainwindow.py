# referencia al path y la clase QMainWindow
# QfileDialog ==> conexion con cuadro de dialogo
# QMessageBox ==> mostrar cuadro de texto informativo
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
# importación de Slot
from PySide2.QtCore import Slot
from random import randint
# archivos con minusculas y clases con mayusculas
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor, QTransform
from administrador import Administrador
from particula import Particula
# union de codigo de archivo a programa con >
# ejemplo: pyside2-uic mainwindow.ui > ui_mainwindow.py

# llamado al constructor desde aquí
class MainWindow(QMainWindow):
    # funcion
    def __init__(self):
        # super ==> metodo
        super(MainWindow, self).__init__()
        # self se usa para que nuestro objeto exista globalmente y no solo en el constructor.
        self.administrador = Administrador()
        # Ui_MainWindow() ==> objeto referenciado
        self.ui = Ui_MainWindow()
        # setupUi ==> metodo para enbeber la instruccion
        self.ui.setupUi(self)
        # conectar las instrucciones de "conectar_final",
        # "conectar_inicio" y "mostrar"
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        # conectar las acciones
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        # Botones para mostrar la tabla y buscar
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_identificador)

        # Sección del grafo
        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    # Slot del dibujo
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.administrador:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color = QColor(r, g, b)
            pen.setColor(color)

            origen_x = particula.origenx
            origen_y = particula.origeny
            destino_x = particula.destinox
            destino_y = particula.destinoy

            self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
            self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
            self.scene.addLine(origen_x+3, origen_y+3, destino_x, destino_y, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()

    # buscar libros
    @Slot()
    def buscar_identificador(self):
        identificador = self.ui.buscar_lineEdit.text()
        # bandera
        encontrado = False
        for particula in self.administrador:
            if identificador == particula.identificador:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                # asignar 10 columnas en la tabla
                self.ui.tabla.setColumnCount(10)
                # asigna nombres a las columnas
                headers = ["ID", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
                # presenta la coleccion "headers" en el encabezado de las columnas
                self.ui.tabla.setHorizontalHeaderLabels(headers)

                identificador_widget = QTableWidgetItem(str(particula.identificador))
                origenx_widget = QTableWidgetItem(str(particula.origenx))
                origeny_widget = QTableWidgetItem(str(particula.origeny))
                destinox_widget = QTableWidgetItem(str(particula.destinox))
                destinoy_widget = QTableWidgetItem(str(particula.destinoy))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                
                # imprimir solo una particula en la fila
                self.ui.tabla.setItem(0, 0, identificador_widget)
                self.ui.tabla.setItem(0, 1, origenx_widget)
                self.ui.tabla.setItem(0, 2, origeny_widget)
                self.ui.tabla.setItem(0, 3, destinox_widget)
                self.ui.tabla.setItem(0, 4, destinoy_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                # validador de la bandera
                encontrado = True
                return
        # negacion de bandera        
        if not encontrado:
            QMessageBox.warning(
                self,
                "Aviso",
                f'La partícula con identificador "{identificador}" no fue encontrada'
            )

    # funcionamiento del boton de mostrar_tabla
    @Slot()
    def mostrar_tabla(self):
        # asignar 10 columnas en la tabla
        self.ui.tabla.setColumnCount(10)
        # asigna nombres a las columnas
        headers = ["ID", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        # presenta la coleccion "headers" en el encabezado de las columnas
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        # asignacion de filas
        # len(self.libreria) ==> metodo para obtener la cantidad de elementos en la lista                                                   
        self.ui.tabla.setRowCount(len(self.administrador))

        row = 0
        # sacarparticulas del administrador  
        for particula in self.administrador:
            identificador_widget = QTableWidgetItem(str(particula.identificador))
            origenx_widget = QTableWidgetItem(str(particula.origenx))
            origeny_widget = QTableWidgetItem(str(particula.origeny))
            destinox_widget = QTableWidgetItem(str(particula.destinox))
            destinoy_widget = QTableWidgetItem(str(particula.destinoy))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            # metodo para asignar posicion a los elementos de cada particula
            self.ui.tabla.setItem(row, 0, identificador_widget)
            self.ui.tabla.setItem(row, 1, origenx_widget)
            self.ui.tabla.setItem(row, 2, origeny_widget)
            self.ui.tabla.setItem(row, 3, destinox_widget)
            self.ui.tabla.setItem(row, 4, destinoy_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            #incrementar el contador de filas
            row += 1


    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.administrador.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Abrir",
                "Se abrió el archivo " + '\n' '\n' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Abrir",
                "Error al abrir el archivo " + '\n' '\n' + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        # getSaveFileName ==> metodo para recibir parametros y guardarlos
        # ubicacion: asigna posiciones desde cero
        ubicacion = QFileDialog.getSaveFileName(
            self, # el dialogo se lanza desde aqui
            'Guardar Archivo', # titulo de la ventana de dialogo
            '.', # directorio desde el que se corre el archivo ejecutable, desde la carpeta del proyecto
            'JSON (*.json)' # extencion del archivo a guardar
        )[0]
        print(ubicacion)
        if self.administrador.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Guardar",
                "Archivo guardado en: " + '\n' '\n' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Guardar",
                "Archivo no guardado: " + '\n' '\n' + ubicacion
            )


    @Slot()
    def click_mostrar(self):
        # limpiar pantalla de PlaintText
        self.ui.salida.clear()
        # salida datos introducidos por pantalla
        self.ui.salida.insertPlainText(str(self.administrador))

    # funcion Slot para recibir eventos
    @Slot()
    def click_agregar(self):
        # funcion de botones
        # obtener infornacion para las variables
        # .tex() ==> estrae el texto ingresado
        # self. ==> esta asociado a las variables globales de el programa
        identificador = self.ui.identificador_lineEdit.text()
        origenx = self.ui.origen_x_spinBox.value()
        origeny = self.ui.origen_y_spinBox.value()
        destinox = self.ui.destino_x_spinBox.value()
        destinoy = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        # .value() regresa un valor entero
        # elementos de la particula
        particula = Particula(identificador, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        # asociar el apartado globalmente
        # mostrar los datos en el recuadro PlainText
        self.administrador.agregar_final(particula)
        
    # funcion Slot para recibir eventos    
    @Slot()
    def click_agregar_inicio(self):
        # funcion de botones
        # obtener infornacion para las variables
        # .tex() ==> estrae el texto ingresado
        # self. ==> esta asociado a las variables globales de el programa
        identificador = self.ui.identificador_lineEdit.text()
        origenx = self.ui.origen_x_spinBox.value()
        origeny = self.ui.origen_y_spinBox.value()
        destinox = self.ui.destino_x_spinBox.value()
        destinoy = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        #.value() regresa un valor entero
        # elementos de la particula
        particula = Particula(identificador, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        # asociar el apartado globalmente
        # mostrar los datos en el recuadro PlainText
        self.administrador.agregar_inicio(particula)
