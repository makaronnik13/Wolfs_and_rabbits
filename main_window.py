from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMessageBox
from matplotlib.backends.qt_compat import QtWidgets
import sys
import Graphs_evaluation
__author__ = 'makar'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.a = 1.
        self.b = 0.1
        self.c = 1.5
        self.d = 0.75
        self.x0 = 10
        self.y0 = 2
        self.create_ui()
        self.evaluator = Graphs_evaluation

    def about(self):
        QMessageBox.information(self, 'Information', "Tishkin Nikita\nMIEM HSE\n2015")

    def create_ui(self):
        self.setWindowTitle('Wolfs_and_rabbits')
        about = self.menuBar().addMenu('About')
        info = about.addAction('Info')
        info.triggered.connect(self.about)
        qle = QtGui.QLineEdit(self)
        qle2 = QtGui.QLineEdit(self)
        qle3 = QtGui.QLineEdit(self)
        qle4 = QtGui.QLineEdit(self)
        qle5 = QtGui.QLineEdit(self)
        qle6 = QtGui.QLineEdit(self)
        lbl = QtGui.QLabel(self)
        lb2 = QtGui.QLabel(self)
        lb3 = QtGui.QLabel(self)
        lb4 = QtGui.QLabel(self)
        lb5 = QtGui.QLabel(self)
        lb6 = QtGui.QLabel(self)
        lbl.setText("growth rate of rabbits")
        lb2.setText("impact of predation on x'/x")
        lb3.setText("death rate of wolfs")
        lb4.setText("net rate of growth of the wolfs")
        lb5.setText("rabbits")
        lb6.setText("wolfs")
        lbl.move(lbl.width()/2, self.frameSize().height()/2-qle.height()*2.5)
        lb2.move(lbl.width()/2, self.frameSize().height()/2-qle.height()*1.5)
        lb3.move(lbl.width()/2, self.frameSize().height()/2-qle.height()*0.5)
        lb4.move(lbl.width()/2, self.frameSize().height()/2+qle.height()*0.5)
        lb5.move(lbl.width()/2, self.frameSize().height()/2+qle.height()*1.5)
        lb6.move(lbl.width()/2, self.frameSize().height()/2+qle.height()*2.5)
        lbl.setFixedWidth(150)
        lb2.setFixedWidth(150)
        lb3.setFixedWidth(150)
        lb4.setFixedWidth(150)
        lb5.setFixedWidth(150)
        lb6.setFixedWidth(150)
        qle.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2-qle.height()*2.5)
        qle2.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2-qle.height()*1.5)
        qle3.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2-qle.height()*0.5)
        qle4.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2+qle.height()*0.5)
        qle5.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2+qle.height()*1.5)
        qle6.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2+qle.height()*2.5)
        qle.setText(str(self.a))
        qle2.setText(str(self.b))
        qle3.setText(str(self.c))
        qle4.setText(str(self.d))
        qle5.setText(str(self.x0))
        qle6.setText(str(self.y0))
        qle.textChanged[str].connect(self.onChanged)
        qle2.textChanged[str].connect(self.onChanged2)
        qle3.textChanged[str].connect(self.onChanged3)
        qle4.textChanged[str].connect(self.onChanged4)
        qle5.textChanged[str].connect(self.onChanged5)
        qle6.textChanged[str].connect(self.onChanged6)
        self.invalidate()

    def onChanged(self, text):
        self.a = text
        self.invalidate()

    def onChanged2(self, text):
        self.b = text
        self.invalidate()

    def onChanged3(self, text):
        self.c = text
        self.invalidate()

    def onChanged4(self, text):
        self.d = text
        self.invalidate()

    def onChanged5(self, text):
        self.x0 = text
        self.invalidate()

    def onChanged6(self, text):
        self.y0 = text
        self.invalidate()

    def invalidate(self):
        grapher = Graphs_evaluation.Evaluation(self.a, self.b, self.c, self.d, self.x0, self.y0)
        grapher.create_graphs()
        i_lable1 = QtGui.QLabel(self)
        i_lable2 = QtGui.QLabel(self)
        myPixmap = QtGui.QPixmap('wolfs_and_rabbits_1.png')
        myScaledPixmap = myPixmap.scaled(480, 360, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        i_lable1.setPixmap(myScaledPixmap)
        i_lable1.setGeometry(370, 105, 480, 360)
        myPixmap = QtGui.QPixmap('wolfs_and_rabbits_2.png')
        myScaledPixmap = myPixmap.scaled(480, 480, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        i_lable2.setPixmap(myScaledPixmap)
        i_lable2.setGeometry(370+480, 105, 480, 360)
        i_lable1.show()
        i_lable2.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowIcon(QtGui.QIcon('icon.png'))
    window.setGeometry(0, 200, 1800, 500)
    sys.exit(app.exec_())