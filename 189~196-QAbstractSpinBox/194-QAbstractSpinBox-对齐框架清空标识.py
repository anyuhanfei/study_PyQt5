'''
194-QAbstractSpinBox-对齐框架清空标识

API:
    setAlignment(Qt.Alignment) -- 设置文本框中文本的对齐方式
    alignment() -> Qt.Alignment -- 获取文本框中文本的对齐方式
    setFrame(bool) -- 设置周边框架(默认True)
    hasFrame() -> bool -- 获取周边框架的设置
    clear() -- 清空文本框内容

    setButtonSymbols() -- 设置按钮样式
        QAbstractSpinBox.UpDownArrows = 0
        QAbstractSpinBox.PlusMinus = 1
        QAbstractSpinBox.NoButtons = 2
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QAbstractSpinBox
from PyQt5.Qt import Qt


class MyQSpinBox(QAbstractSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def stepEnabled(self):
        return QAbstractSpinBox.StepUpEnabled or QAbstractSpinBox.StepDownEnabled

    def stepBy(self, p_int):
        self.lineEdit().setText(str(int(self.text()) + p_int))


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('194-QAbstractSpinBox-对齐框架清空标识')
        self.resize(1000, 500)

        asb = MyQSpinBox(self)
        asb.resize(100, 30)
        asb.lineEdit().setText('111')

        '''设置对齐方式'''
        asb.setAlignment(Qt.AlignCenter)

        '''获取对齐方式'''
        print('对齐方式:', asb.alignment())

        '''设置周边框架'''
        asb.setFrame(False)

        '''获取周边框架'''
        print('周边框架:', asb.hasFrame())

        '''清空文本内容'''
        asb.clear()

        '''设置按钮样式'''
        asb.setButtonSymbols(QAbstractSpinBox.UpDownArrows)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
