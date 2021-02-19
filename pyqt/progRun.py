import sys
from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow # مكان تشغيل كلاس الي يتم عليها تصميم البرنامج 

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setWindowTitle("Studierendenverwaltung")

ui_window = Ui_MainWindow()
ui_window.setupUi(window)

window.show()

sys.exit(app.exec_())
