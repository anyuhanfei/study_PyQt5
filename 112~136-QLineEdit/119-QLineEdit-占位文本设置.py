'''
119-QLineEdit-占位文本设置

在用户输入文本内容之前, 给用户的提示字符串
当文本框为内容为空时显示提示字符串

API
    setPlaceholderText(notice_str) -- 设置提示字符串
    placeholderText() -- 获取提示字符串
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('119_QLineEdit_占位文本设置')
        self.resize(1000, 500)

        le = QLineEdit(self)

        '''设置提示字符串'''
        le.setPlaceholderText('这是一个输入框')

        '''获取提示字符串'''
        print(le.placeholderText())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
