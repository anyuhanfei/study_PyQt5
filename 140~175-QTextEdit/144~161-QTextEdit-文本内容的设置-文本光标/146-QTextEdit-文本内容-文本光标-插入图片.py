'''
146-QTextEdit-文本内容-文本光标-插入图片

API:
    insertImage(QTextImageFormat) -- 插入图片

附:
    QTextImageFormat (from PyQt5.QtGui import QTextImageFormat)

    API:
        setName(str) -- 设置图片文件路径及名称
        setWidth(int) -- 设置宽
        setHeight(int) -- 设置高
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextImageFormat


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('146-QTextEdit-文本内容-文本光标-插入图片')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        te_cursor = te.textCursor()

        '''插入图片'''
        # 设置文本图片
        tif = QTextImageFormat()
        tif.setName('./xxx.png')
        tif.setWidth(100)
        tif.setHeight(100)
        # 将文本图片插入到文本中
        te_cursor.insertImage(tif)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
