'''
328-布局管理-QFormLayout-行包装策略

setRowWrapPolicy(QFormLayout.RowWrapPolicy) -- 设置
rowWrapPolicy()->QFromLayout.RowWrapPolicy -- 获取

附:
    QFormLayout.DontWrapRows -- 字段总是放在标签旁边
    QFormLayout.WrapLongRows -- 标签被赋予足够的水平空间以适合最宽的标签, 其余的空间被赋予字段. 如果字段的最小大小比可用空间宽, 则该字段将换行到下一行
    QFormLayout.WrapAllRows -- 字段总是位于其标签下方

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QFormLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('328-布局管理-QFormLayout-行包装策略')
        self.resize(1000, 500)

        fl = QFormLayout()
        fl.addRow('标签1111111111111111111111111111111', QLineEdit())

        '''修改策略'''
        fl.setRowWrapPolicy(QFormLayout.WrapLongRows)

        self.setLayout(fl)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
