import sys
from Ventana import *

class Principal(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.llenarMatriz)
    
    def llenarMatriz(self):
        import numpy as np
        filas=int(self.lineEdit.text())
        columnas=int(self.lineEdit_2.text())
        self.matriz=[[0 for i in range(columnas)] for j in range(filas)]
        self.tableWidget.setRowCount(filas)
        self.tableWidget.setColumnCount(columnas)
        for i in range(filas):
            for j in range(columnas):
                nota,estado=QtWidgets.QInputDialog.getDouble(self,"Ingrese ","Valor: ")
                if estado:
                    self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(nota)))
                    self.matriz[i][j]=nota 
        print(self.matriz)
        suma=0
        for i in range(filas):
            for j in range(columnas):
                if i==j:
                    suma+=self.matriz[i][j]
        print(suma)
        self.label_3.setText("La suma es "+str(suma))



if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    dialogo=Principal()
    dialogo.show()
    sys.exit(app.exec_())