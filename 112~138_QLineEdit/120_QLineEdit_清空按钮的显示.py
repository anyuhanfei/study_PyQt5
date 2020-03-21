'''
120_QLineEdit_清空按钮的显示

用作快速清空文本框内容

API:
    setClearButtonEnabled(bool) -- 设置是否有快速清空文本的按钮
    isClearButtonEnabled() -> bool -- 获取是否有快速清空文本的按钮
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('120_QLineEdit_清空按钮的显示')
        self.resize(1000, 500)

        le = QLineEdit(self)

        '''设置快速清空文本的按钮'''
        le.setClearButtonEnabled(True)

        '''获取快速清空文本的按钮'''
        print(le.isClearButtonEnabled())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
