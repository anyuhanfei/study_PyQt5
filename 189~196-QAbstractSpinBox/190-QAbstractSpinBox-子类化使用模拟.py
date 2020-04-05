'''
190-QAbstractSpinBox-子类化使用

使用:
    1. 子类化此类
    2. 实现控制上下能用的方法 -- stepEnabled(self) -> QAbstractSpinBox.StepEnabled
    3. 实现步长调整方法 -- stepBy(self, p_int)

附:
    QAbstractSpinBox.StepEnabled
        QAbstractSpinBox.StepNone -- 都不能用
        QAbstractSpinBox.StepUpEnabled -- 上可用
        QAbstractSpinBox.StepDownEnabled -- 下可用
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QAbstractSpinBox


class MyQSpinBox(QAbstractSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def stepEnabled(self):
        '''控制按钮有效无效
        限定 0-9
        '''
        if int(self.text()) == 0:
            return QAbstractSpinBox.StepUpEnabled
        elif int(self.text()) == 9:
            return QAbstractSpinBox.StepDownEnabled
        elif int(self.text()) < 0 or int(self.text()) > 9:
            return QAbstractSpinBox.StepNone
        else:
            return QAbstractSpinBox.StepUpEnabled or QAbstractSpinBox.StepDownEnabled

    def stepBy(self, p_int):
        self.lineEdit().setText(str(int(self.text()) + p_int))


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('190-QAbstractSpinBox-子类化使用模拟')
        self.resize(1000, 500)

        asb = MyQSpinBox(self)
        asb.lineEdit().setText('8')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
