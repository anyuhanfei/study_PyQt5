'''
116_QLineEdit_文本输出模式_API

API:
    setEchoMode(QLineEdit.EchoMode) -- 设置输出模式
    echoMode() -- 获取输出模式,返回 QLineEdit.EchoMode

QLineEdit.EchoMode： 类似枚举类型
    NoEcho = 1 -- 不显示输出，但有内容
    Normal = 0 -- 正常输出
    Password = 2 -- 密文形式
    PasswordEchoOnEdit = 3 -- 编辑时明文, 结束后密文
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('116_QLineEdit_文本输出模式_API')
        self.resize(1000, 500)

        '''创建一个文本框'''
        le = QLineEdit(self)

        '''设置输出模式'''
        le.setEchoMode(QLineEdit.Password)

        '''获取输出模式'''
        print(le.echoMode())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
