'''
347-QSS-组成部分

语法:
    选择器[:伪状态] {
        声明
    }

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel

from Tools import Tools


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('347-QSS-组成部分')
        self.resize(1000, 500)

        label = QLabel('标签', self)
        label.setObjectName('py347_l1')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    Tools.set_qss_to_obj('./text.qss', app)

    sys.exit(app.exec_())
