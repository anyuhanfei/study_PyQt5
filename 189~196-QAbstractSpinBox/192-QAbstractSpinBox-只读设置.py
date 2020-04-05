'''
192-QAbstractSpinBox-只读设置

只允许用户通过步长调节器调节, 不能使用键盘输入

API:
    setReadOnly(bool r) -- 设置是否是只读
    isReadOnly() -> bool -- 获取是否是只读
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

        self.setWindowTitle('192-QAbstractSpinBox-只读设置')
        self.resize(1000, 500)

        asb = MyQSpinBox(self)
        asb.resize(100, 30)
        asb.lineEdit().setText('0')

        '''设置只读'''
        asb.setReadOnly(True)

        '''获取是否是只读'''
        print('是否是只读:', asb.isReadOnly())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
