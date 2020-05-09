'''
297-QErrorMessage-简介

错误消息小部件由文本标签和复选框组成

该复选框允许用户控制将来是否再次显示相同的错误消息

继承自 QDialog

构造函数:
    QErrorMessage(parent: QWidget = None)

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QErrorMessage


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('297-QErrorMessage-简介')
        self.resize(1000, 500)

        em = QErrorMessage(self)
        em.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
