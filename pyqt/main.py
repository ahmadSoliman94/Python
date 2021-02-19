import sys
from qtpy import QtWidgets

# مكان تشغيل كلاس الي يتم عليها تصميم البرنامج 
from ui.mainwindow import Ui_MainWindow 

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Studierendenverwaltung")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.result.hide()
        self.ui.label_3.hide()

        self.ui.claculate.clicked.connect(self.calculate_bmi)

    def calculate_bmi(self):
        heigh = self.ui.heigh.value()
        weight = self.ui.weight.value()

        if heigh != 0:
            self.ui.result.show()
            self.ui.label_3.show()
            bmi = round(weight / (heigh ** 2), 2)
            self.ui.result.setText(str(bmi)) 
        else: 
            self.ui.result.setText("") 


window = MainWindow()
window.show()

sys.exit(app.exec_())
