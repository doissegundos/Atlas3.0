import matplotlib.pyplot as plt
import math
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d
from PyQt5.uic import loadUiType

#recebendo a janela grafica
Ui_MainWindow, QMainWindow = loadUiType('interface.ui')

#lendo o arquivo
arquivo = open('OBJETO.txt', 'r')
text = arquivo.readlines()

"""
    Essa classe contém as configurações,funções da interface
"""
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self,x,y,z):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Atlas")
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.x = x
        self.y = y
        self.z = z

        self.graphLayout.addWidget(self.toolbar)
        self.graphLayout.addWidget(self.canvas)
        self.plot()

        # ao clicar no botão ele invoca as funções
        self.iniciarButton.clicked.connect(self.iniciarbutton)
        self.pausarButton.clicked.connect(self.pausarbutton)
        self.pararButton.clicked.connect(self.pararbutton)

    # funções que irão definir as ações de quando os botões forem pressionados
    def iniciarbutton(self):
        print("INCIAR")

    def pausarbutton(self):
        print("PAUSAR")

    def pararbutton(self):
        print("PARAR")

    def plot(self):
        ax = self.figure.add_subplot(111, projection = '3d')
        ax.scatter(self.x, self.y, self.z, zdir='z', s=5, c=None, depthshade=True)
        self.canvas.draw()


"""
    As funções lista_coordenada e convertendo são responsaveis por
     converter um arquivo text que possui dados em coordenadas esfericas
    para listas sendo 3 listas cada uma com valores rho,phi,theta
"""
def lista_coordenada(lista):
    convertida = list(map(float,lista.split()))
    return convertida
def convertendo(text):
    tam = len(text)
    i = 0
    rho = [];    theta = [];    phi = [] #declarando x,y,z como listas
    while(i<tam):
        lista = lista_coordenada(text[i])
        rhoTemp, thetaTemp, phiTemp = lista
        rho.append(rhoTemp)
        theta.append(thetaTemp)
        phi.append(phiTemp)
        i += 1
    return rho, theta, phi


"""
    A função radiano converte os dados das listas rho,theta,phi para radianos
"""
def radiano(cord):
    i = 0
    tam = len(cord)
    while(i<tam):
        cord[i] = (cord[i]/57.2958)
        i += 1
    return cord

rho, theta, phi = convertendo(text)
theta = radiano(theta)
phi = radiano(phi)
rho = radiano(rho)

"""
    A função cartesiano converte os pontos em coordenadas esfericas para coordenadas cartesianas
"""
def cartesiano(theta, phi, rho):
    tam = len(theta)
    i = 0
    x = [];    y = [];    z = [] #declarando x,y,z como listas
    while(i<tam):
        x.append(rho[i] * (math.sin(phi[i]) * math.cos(theta[i])))
        y.append(rho[i] * (math.sin(phi[i])*math.sin(theta[i])))
        z.append(rho[i] * (math.cos(phi[i])))
        i+=1
    return x,y,z
x,y,z = cartesiano(theta,phi,rho)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main(x,y,z)
    main.show()
    sys.exit(app.exec_())


arquivo.close()
