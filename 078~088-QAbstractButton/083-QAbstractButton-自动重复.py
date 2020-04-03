'''
083-QAbstractButton-自动重复

当用户点击按钮后，并且按住不松开，就可以触发自动重复功能

API:
    setAutoRepeat(bool) -- 设置自动重复
    setAutoRepeatInterval(毫秒) -- 设置自动重复检测间隔
    setAutoRepeatDelay(毫秒) -- 设置初次检测延迟
    autoRepeat() -- 获取是否自动重复
    autoRepeatInterval() -- 获取自动重复检测间隔
    autoRepeatDelay() -- 获取初次检测延迟
'''

import sys


from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('083_QAbstractButton_自动重复')
        self.resize(500, 500)

        self.设置自动重复()
        self.读取自动重复信息()

    def 设置自动重复(self):
        # 080 的按钮文本 +1 示例
        self.btn = QPushButton(self)
        self.btn.setText('1')
        self.btn.clicked.connect(lambda: self.btn.setText(str(int(self.btn.text()) + 1)))

        '''设置自动重复'''
        # 默认情况下，自动重复是关闭的
        self.btn.setAutoRepeat(True)  # True 开启  False 关闭

        '''设置自动重复初次检测延迟'''
        self.btn.setAutoRepeatDelay(1000)

        '''设置自动重复检测间隔'''
        self.btn.setAutoRepeatInterval(10)

    def 读取自动重复信息(self):
        '''获取自动重复状态'''
        auto_repeat = self.btn.autoRepeat()

        '''获取自动重复初次检测延迟'''
        auto_repeat_interval = self.btn.autoRepeatDelay()

        '''获取自动重复检测间隔'''
        auto_repeat_delay = self.btn.autoRepeatInterval()

        label = QLabel(self)
        label.move(5, 50)
        label.setText('按钮自动重复状态：%s' % (str(auto_repeat)))

        label = QLabel(self)
        label.move(5, 100)
        label.setText('按钮自动重复初次检测延迟：%s' % (str(auto_repeat_interval)))

        label = QLabel(self)
        label.move(5, 150)
        label.setText('按钮自动重复检测间隔：%s' % (str(auto_repeat_delay)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
