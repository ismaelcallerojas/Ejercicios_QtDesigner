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
        self.matriz2=[[0 for i in range(columnas)] for j in range(filas)]
        self.tableWidget.setRowCount(filas)
        self.tableWidget.setColumnCount(columnas)
        for i in range(filas):
            for j in range(columnas):
                nota,estado=QtWidgets.QInputDialog.getDouble(self,"Ingrese ","Valor: ")
                if estado:
                    self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(nota)))
                    self.matriz[i][j]=nota 
        print(self.matriz)
        
        
        t=np.transpose(self.matriz)
        print(t)
        self.tableWidget_2.setRowCount(filas)
        self.tableWidget_2.setColumnCount(columnas)
        for i in range(filas):
            for j in range(columnas):
                self.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(t[i][j])))
                self.matriz2[i][j]=t[i][j] 
        print(self.matriz2)
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    dialogo=Principal()
    dialogo.show()
    sys.exit(app.exec_())