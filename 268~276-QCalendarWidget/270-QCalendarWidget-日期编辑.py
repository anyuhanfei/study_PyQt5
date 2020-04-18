'''
270-QCalendarWidget-日期编辑

当控件获取焦点时, 直接输入数字, 可以快速修改日期

setDateEditEnabled(bool enable) -- 设置是否可编辑, 默认可以被编辑
isDateEditEnabled() -> bool -- 获取是否可编辑
setDateEditAcceptDelay(int delay) -- 设置延时秒数
dateEditAcceptDelay() -> int -- 获取延时秒数

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('270-QCalendarWidget-日期编辑')
        self.resize(1000, 500)

        cw = QCalendarWidget(self)

        '''设置延时秒数'''
        cw.setDateEditAcceptDelay(5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
