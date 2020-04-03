'''
117~118-QLineEdit-文本输出模式-案例

创建一个窗口，添加两个文本框和按钮
    一个文本框用做账号输入框，另一个用做密码输入框
    点击登录获取输入信息，对比帐号密码信息
    如果账号不存在，则清空账号和密码输入框
    如果密码错误，则情况密码输入框

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel


class Window(QWidget):
    account = 'sz'
    password = '123456'
    label = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('117~118_QLineEdit_文本输出模式_案例')
        self.resize(1000, 500)

        '''先创建控件'''
        self.le_account = QLineEdit(self)
        self.le_account.move(10, 10)
        self.le_password = QLineEdit(self)
        self.le_password.setEchoMode(2)
        self.le_password.move(10, 40)
        self.login_btn = QPushButton(self)
        self.login_btn.setText('登录')
        self.login_btn.move(10, 70)

        '''登录按钮信号'''
        self.login_btn.pressed.connect(self._login_verify)

    def _login_verify(self):
        '''登录验证'''
        account = self.le_account.text()
        password = self.le_password.text()
        if account != self.account:
            self.le_account.setText('')
            self.le_password.setText('')
            self._show_return(False)
            return
        if password != self.password:
            self.le_password.setText('')
            self._show_return(False)
            return
        self._show_return(True)
        return

    def _show_return(self, result):
        '''展示结果
        Args:
            result: bool, 登录验证结果
        '''
        if result is True:
            result_text = '登录成功'
        else:
            result_text = '登录失败'
        if self.label is None:
            self.label = QLabel(self)
            self.label.setText(result_text)
            self.label.move(10, 100)
            self.label.show()
        else:
            self.label.setText(result_text)
            self.label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
