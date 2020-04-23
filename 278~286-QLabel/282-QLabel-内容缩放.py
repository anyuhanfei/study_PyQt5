'''
282-QLabel-内容缩放

缩放内容, 适应控件大小

针对于图片有效

API:
    hasScaledContents() -> bool -- 获取是否内容缩放
    setScaledContents(bool) -- 设置是否内容缩放
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('282-QLabel-内容缩放')
        self.resize(1000, 500)

        label = QLabel(self)
        label.resize(80, 100)

        '''设置图片'''
        label.setPixmap(QPixmap('./xxx.png'))

        '''设置内容缩放'''
        label.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
