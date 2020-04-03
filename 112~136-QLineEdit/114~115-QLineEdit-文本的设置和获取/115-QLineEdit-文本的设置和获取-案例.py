'''
115-QLineEdit-文本的设置和获取-案例

创建一个窗口，添加两个文本框和一个按钮
    点击按钮后，将文本框A中的内容复制到文本框B中

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('115_QLineEdit_文本的设置和获取_案例')
        self.resize(1000, 500)

        '''创建文本框和按钮'''
        self.le_one = QLineEdit(self)
        self.le_one.move(10, 10)
        self.le_two = QLineEdit(self)
        self.le_two.move(10, 30)
        self.btn = QPushButton(self)
        self.btn.move(30, 70)
        self.btn.setText('复制')

        '''设置点击信号'''
        self.btn.pressed.connect(lambda: self.le_two.setText(self.le_one.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
