'''
278-QLabel-简介

提供了文本或图像的显示 (普通文本, 数字, 富文本, QLabel-超链接, 图片, QLabel-动画等)

没有提供用户交互功能

继承自 QFrame

构造函数:
    QLabel(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QLabel(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('278-QLabel-简介')
        self.resize(1000, 500)

        label = QLabel(self)
        label.setText('测试')
        label.move(10, 10)

        label2 = QLabel('测试2', self)
        label2.move(10, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
