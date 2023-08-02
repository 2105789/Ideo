import sys
from PyQt5.QtWidgets import QApplication
from ide import IDE

app = QApplication(sys.argv)
app.setStyle('Fusion')
ide = IDE()
sys.exit(app.exec_())
