import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow): #nota7: cuando llama a la clase, viene por aca

    def __init__(self): #nota8: el __init__ de initialized, es el codigo que SIEMPRE se ejecuta, el def ventanaNueva no se ejecuta porque esta fuera de aca, aca se conectan botones, los eventos que vayan a pasar, las restricciones, etc...
        super().__init__() #superposiciona el init, siempre va.
        uic.loadUi('gui_1.ui', self) #aca se carga la gui
        self.pushButton.clicked.connect(self.ventanaNueva) #aca conecta el boton de nombre pushButton que nos da el designer y lo  conectamos a la funcion ventanaNueva

    def ventanaNueva(self):
        gui2.show() #y aca muestra la ventana y nada mas
        #gui2.showMaximized() #esto esta para que prueven cambiando y viendo como cambia
        #gui2.showMinimized() #esto esta para que prueven cambiando y viendo como cambia

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui_2.ui', self)

if __name__ == '__main__':  #nota1: esto siempre va, es para que el programa siempre ejecute esta parte
    app = QApplication(sys.argv) #Nota2: aca crea un objeto para hacer las aplicaciones
    gui = MainWindow() #Nota3: todas las ventanas tendran su armado mediante esto, un objeto del tipo variable=Clase_del_objeto()
    gui2= Window2() #Nota4: para la gui2
    gui.show() #Nota5: aca muestra la gui principal la main, como ya la tiene armada(en Nota3) ahora la muestra mediante el metodo .show(), hay varias maneras, showMaximiced() la muestra maximixada por ej
    sys.exit(app.exec_()) #Nota6: esto es para que quede abierto, sino se cierra el programa, queda ejecutandose