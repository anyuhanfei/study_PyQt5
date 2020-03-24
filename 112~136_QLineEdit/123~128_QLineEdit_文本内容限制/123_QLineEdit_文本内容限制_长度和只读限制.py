'''
123_QLineEdit_文本内容限制_长度和只读限制

API
    setMaxLength(int) -- 设置最大长度
    maxLength() -- 获取最大长度
    setReadOnly(bool) -- 设置是否只读
    isReadOnly() -- 获取是否是只读
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('123_QLineEdit_文本内容限制_长度和只读限制')
        self.resize(1000, 500)

        le_one = QLineEdit(self)
        le_two = QLineEdit(self)
        le_two.move(0, 30)

        '''最大长度限制'''
        le_one.setMaxLength(10)

        '''只读限制'''
        le_two.setReadOnly(True)
        le_two.setText('只读')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
