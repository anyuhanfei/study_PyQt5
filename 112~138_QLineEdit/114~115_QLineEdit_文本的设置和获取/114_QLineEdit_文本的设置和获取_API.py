'''
114_QLineEdit_文本的设置和获取_API

API:
    setText(str) -- 设置内容文本
    insert(newText) -- 在光标处插入文本
    text() -- 获取真实内容文本
    displayText() -- 获取用户能看到的内容文本

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('114_QLineEdit_文本的设置和获取_API')
        self.resize(1000, 500)

        le = QLineEdit(self)

        '''设置内容'''
        le.setText('sz')

        '''在光标处添加内容'''
        le.insert('18')

        '''获取内容'''
        # 真实信息
        print(le.text())
        # 用户看到的信息(密码类型的输入框中可以明显看到差异)
        print(le.displayText())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
