'''
191-QAbstractSpinBox-长按累加加速

API:
    setAccelerated(bool) -- 设置是否是长按累加加速
    isAccelerated() -> bool -- 获取是否是长按累加加速
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

        self.setWindowTitle('191-QAbstractSpinBox-长按累加加速')
        self.resize(1000, 500)

        asb = MyQSpinBox(self)
        asb.resize(100, 30)
        asb.lineEdit().setText('0')

        '''设置长按加速'''
        asb.setAccelerated(True)

        '''获取是否是长按加速'''
        print('是否是长按加速:', asb.isAccelerated())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
