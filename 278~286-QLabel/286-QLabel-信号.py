'''
286-QLabel-信号

linkActivated(link_str) -- 超链接被激活时
linkHovered(link_str) -- 鼠标放在超链接上
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('286-QLabel-信号')
        self.resize(1000, 500)

        label = QLabel(self)
        label.move(10, 10)
        label.setText("测试<a href='http://www.baidu.com'>链接</a>")

        label.linkActivated.connect(lambda link_str: print('点击了超链接', link_str))
        label.linkHovered.connect(lambda link_str: print('鼠标放在超链接上', link_str))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
