'''
301-QProgressDialog-信号

信号:
    canceled -- 点击取消按钮
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QProgressDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('301-QProgressDialog-信号')
        self.resize(1000, 500)

        pd = QProgressDialog(self)
        pd.canceled.connect(lambda: print("点击了取消按钮"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
