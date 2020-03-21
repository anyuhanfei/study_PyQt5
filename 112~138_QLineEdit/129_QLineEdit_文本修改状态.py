'''
129_QLineEdit_文本修改状态

判断文本是否修改过，输入过内容或者手动设置为修改都会被判断为文本已被修改

API:
    isModified() -- 获取文本状态
    setModified(bool) -- 标识文本内容是否被修改

注：
    若文本框中有设置或输入内容时，某个时刻被设置成了未修改状态，当不修改文本内容时，即使文本框中有内容，也是未修改状态
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('129_QLineEdit_文本修改状态')
        self.resize(1000, 500)

        self.le = QLineEdit(self)
        self.le.move(10, 10)
        self.btn = QPushButton('按钮', self)
        self.btn.move(10, 40)

        '''获取文本是否被修改'''
        self.btn.pressed.connect(lambda: print(self.le.isModified()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
