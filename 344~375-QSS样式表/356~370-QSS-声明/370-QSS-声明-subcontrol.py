'''
370-QSS-声明-subcontrol

控制复合控件中的子控件

subcontrol-position -- 对齐方式, top, left, right, bottom, 使用多个需要空格隔开
subcontrol-origin -- 位置参照, padding (默认)内边距, content 内容, border 边框
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('370-QSS-声明-subcontrol')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
