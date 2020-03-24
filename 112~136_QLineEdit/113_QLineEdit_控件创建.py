'''
113_QLineEdit_控件创建

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('113_QLineEdit_控件创建')
        self.resize(1000, 500)

        '''创建QLineEdit控件'''
        # 方法一
        le_one = QLineEdit(self)
        le_one.setText('le')
        le_one.move(10, 10)
        # 方法二
        le_two = QLineEdit('le', self)
        le_two.move(10, 50)

        # 二者效果相同，都是创建了一个单行输入控件并且定义了内容，在应用中，一般有默认值或者是修改功能中才会使用到在单行输入控件中定义内容


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
