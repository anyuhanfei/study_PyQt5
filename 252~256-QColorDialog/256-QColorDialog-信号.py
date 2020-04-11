'''
256-QColorDialog-信号

colorSelected(QColor color)
currentColorChanged(QColor color)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QColorDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('256-QColorDialog-信号')
        self.resize(1000, 500)

        cd = QColorDialog(self)

        '''信号'''
        cd.colorSelected.connect(lambda color: print('最终选择的颜色对象为:', color))
        cd.currentColorChanged.connect(lambda color: print('当前选则的颜色对象为:', color))

        cd.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
