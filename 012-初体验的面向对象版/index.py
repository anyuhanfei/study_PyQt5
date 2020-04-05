'''
高级玩法，面向对象版的 'hello world'
'''
import sys

from PyQt5.QtWidgets import QApplication

from Window import Window


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec_())
