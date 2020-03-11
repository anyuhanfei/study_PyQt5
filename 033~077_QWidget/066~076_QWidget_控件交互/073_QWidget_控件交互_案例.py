'''
073_QWidget_控件交互_案例

创建一个窗口，窗口包含一个文本框和一个按钮和一个标签
    默认情况下，标签隐藏，文本框和按钮显示，按钮设置为不可用状态
    当文本有内容时，让按钮可用
    当文本内容为 sz 是，点击按钮则显示标签，并展示文本为登录成功，否则展示登录失败
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('073_QWidget_控件交互_案例')
        self.move(200, 200)
        self.resize(500, 500)

        # 控件创建
        # 文本框控件文本改变信号连接槽函数
        self.le = QLineEdit(self)
        self.le.move(10, 10)
        self.le.textChanged.connect(self._text_change)

        # 标签控件默认隐藏
        self.label = QLabel(self)
        self.label.move(130, 45)
        self.label.hide()

        # 按钮控件默认不可用，点击信号连接槽函数
        self.btn = QPushButton(self)
        self.btn.move(10, 40)
        self.btn.setText('登录')
        self.btn.setEnabled(False)
        self.btn.clicked.connect(self._click_btn)

    def _text_change(self, content):
        '''文本输入槽函数
        文件改变时，判断文本是否为空，为空则将按钮控件修改为不可用状态；不为空则隐藏标签控件，同时将按钮控件修改为可用状态
        Agrs:
            content: 文本内容
        '''
        if content == '':  # 内容为空（一般是删除输入内容的情况）
            self.btn.setEnabled(False)
        else:  # 内容不为空，修改标签状态，修改按钮状态
            self.btn.setEnabled(True)
            self.label.hide()

    def _click_btn(self):
        '''按钮点击槽函数
        获取文本内容，判断是否是 sz， 如果是则展示登录成功，否则展示登录失败
        '''
        content = self.le.text()
        print(content)
        if content == 'sz':
            self.label.setText('登录成功')
        else:
            self.label.setText('登录失败')
        self.label.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
