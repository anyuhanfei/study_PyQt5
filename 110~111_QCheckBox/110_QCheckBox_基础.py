'''
110_QCheckBox_基础

一般用于给用户提供若干选项中的多选操作, 左侧会有一个方框图标, 标识用户的选中状态

API:
    setTristate(bool=True) -- 设置是否为三态复选框
    isTristate() -- 获取是否为三态复选框
    setCheckState(Qt.CheckState) -- 设置复选框状态
    checkState() -- 获取复选框当前状态

附：
    Qt.Unchecked -- 不选中
    Qt.PartiallyCheckedv -- 第三态
    Qt.Checked -- 被选中
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('110_QCheckBox_基础')
        self.resize(1000, 500)

        '''创建复选框控件'''
        # 方法一
        cb_one = QCheckBox(self)
        cb_one.setText('选项一')
        cb_one.move(10, 10)

        # 方法二
        cb_two = QCheckBox('选项二', self)
        cb_two.move(90, 10)

        '''其他继承于父类的基本方法，略'''

        '''设置复选框为三态复选框'''
        cb_one.setTristate(True)
        cb_two.setTristate(True)

        '''设置复选框当前的状态'''
        cb_two.setCheckState(Qt.PartiallyChecked)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
