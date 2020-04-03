'''
122-QLineEdit-自动补全联想

根据用户已输入的字符串, 快速联想补全

API
    setCompleter(QCompleter) -- 设置完成器
    completer() -> QCompleter -- 获取完成器
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QCompleter


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('122_QLineEdit_自动补全联想')
        self.resize(1000, 500)

        le = QLineEdit(self)

        '''创建一个完成器'''
        completer = QCompleter(['aaa', 'bbb', 'ccc'], le)

        '''将完成器添加到文本框中'''
        le.setCompleter(completer)

        '''获取文本框中的完成器'''
        print(le.completer())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
