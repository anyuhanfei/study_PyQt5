'''
345-QSS-使用方式-局部和全局

局部:
    指定需要设置外观的控件, 调用该控件的 setStyleSheet 方法

    参考作用范围是控件本事和子控件
    最终作用范围是符合筛选的控件(可能通过选择器进行二次筛选)

全局:
    指定全局的 QApplication 对象, 调用对应的 setStyleSheet 方法

    参考作用范围是应用程序所有控件
    最终作用范围是符合筛选的控件(可能通过选择器进行二次筛选)

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('345-QSS-使用方式-局部和全局')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
