'''
356-QSS-声明

指明会作用怎样的样式

语法:
    {
        key: value;
        key: value;
    }

盒子模型:
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |                       MARGIN                      |
            |   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+   |
            |   |                   BORDER                  |   |
            |   |   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+   |   |
            |   |   |              PADDING              |   |   |
            |   |   |   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+   |   |   |
            |   |   |   |                           |   |   |   |
            |   |   |   |          CONTENT          |   |   |   |
            |   |   |   |                           |   |   |   |
            |   |   |   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+   |   |   |
            |   |   |                                   |   |   |
            |   |   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+   |   |
            |   |                                           |   |
            |   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+   |
            |                                                   |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    以边框 border 为基准, margin (外边距), padding (内边距), content (内容矩形)

QSS 控制: margin (外边距), padding (内边距)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('356-QSS-声明')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
