'''
111_QCheckBox_信号

大部分都是父类的信号，自己独有的就一个

API:
    stateChanged(int state) -- 选中或清除选中时, 发射此信号
        多这个信号是因为三态的缘故，toggled 信号发出的布尔值，布尔值无法表示三种状态，所以只能再新加一个信号
        若在应用中没有设置为三态，那么这个信号是完全没必要使用的
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('111_QCheckBox_信号')
        self.resize(1000, 500)

        cb_two = QCheckBox('选项', self)
        cb_two.move(10, 10)
        cb_two.setTristate(True)

        '''信号'''
        cb_two.stateChanged.connect(lambda state: print(state))  # 1 第三态 2 选中 0 未选中


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
