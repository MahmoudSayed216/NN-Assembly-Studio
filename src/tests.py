from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import sys


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("NN Assembly Studio")
window.setGeometry(100, 100, 500, 500)

label = QLabel('<h1>Hello, pyqt5<\h1>', parent=window)
label.move(60, 15)

window.show()

sys.exit(app.exec_())