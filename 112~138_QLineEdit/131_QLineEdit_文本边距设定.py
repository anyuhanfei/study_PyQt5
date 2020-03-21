'''
131_QLineEdit_文本边距设定

API:
    getTextMargins() -- 获取文本边距
    setTextMargins(int left，int top，int right，int bottom) -- 设置文本边距

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('131_QLineEdit_文本边距设定')
        self.resize(1000, 500)

        le = QLineEdit(self)
        le.resize(100, 100)
        le.move(10, 10)

        '''设置文本边距'''
        le.setTextMargins(20, 20, 20, 20)

        '''获取文本边距'''
        print(le.getTextMargins())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
