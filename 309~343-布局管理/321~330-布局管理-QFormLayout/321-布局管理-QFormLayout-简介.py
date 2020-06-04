'''
321-布局管理-QFormLayout-简介

表单布局

构造函数:
    QFormLayout(parent: QWidget=None)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFormLayout, QLabel, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('321-布局管理-QFormLayout-简介')
        self.resize(1000, 500)

        fl = QFormLayout()

        label = QLabel('姓名')
        label.setStyleSheel('')
        le = QLineEdit()

        fl.addWidget(label)
        fl.addWidget(le)

        self.setLayout(fl)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
