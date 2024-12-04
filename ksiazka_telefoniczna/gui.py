from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QStyleFactory
import sys

app = QApplication([])

window = QWidget()
window.setWindowTitle("Książka Telefoniczna")
#window.setStyle("dark-fusion")
msg = QLabel("Zatwierdź enterem", parent=window)

window.show()

sys.exit(app.exec())