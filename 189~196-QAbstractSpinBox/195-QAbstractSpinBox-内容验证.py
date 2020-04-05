'''
195-QAbstractSpinBox-内容验证

重写方法:
    validate(self, p_str, p_int) -- 验证规则
    fixup(self, p_str) -- 修复方法
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QAbstractSpinBox
from PyQt5.QtGui import QValidator


class MyQSpinBox(QAbstractSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def stepEnabled(self):
        return QAbstractSpinBox.StepUpEnabled or QAbstractSpinBox.StepDownEnabled

    def stepBy(self, p_int):
        self.lineEdit().setText(str(int(self.text()) + p_int))

    def validate(self, p_str, p_int):
        '''判定输入函数
        Args:
            p_str: 输入内容
            p_int: 光标
        '''
        # 要判断在 0 - 180 之间
        number = int(p_str)
        if number > 0 and number < 180:
            # 正确
            return (QValidator.Acceptable, p_str, p_int)
        else:
            # 错误
            return (QValidator.Invalid, p_str, p_int)

    def fixup(self, p_str):
        '''修改函数'''
        return "18"


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('195-QAbstractSpinBox-内容验证')
        self.resize(1000, 500)

        asb = MyQSpinBox(self)
        asb.resize(100, 30)
        asb.lineEdit().setText('180')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
