'''
193-QAbstractSpinBox-控件内容

API:
    text() -> str -- 获取内容
    lineEdit() -> QLineEdit -- 获取单行文本对象, 然后可以使用 setText() 函数来设置内容
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QAbstractSpinBox


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

        self.setWindowTitle('193-QAbstractSpinBox-控件内容')
        self.resize(1000, 500)

        asb = MyQSpinBox(self)
        asb.resize(100, 30)

        '''设置内容'''
        asb.lineEdit().setText('123456')

        '''获取内容'''
        print('当前内容:', asb.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
