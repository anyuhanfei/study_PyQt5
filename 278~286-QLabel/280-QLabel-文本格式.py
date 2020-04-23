'''
280-QLabel-文本格式

API:
    setTextFormat(Qt.TextFormat) -- 设置文本格式
    textFormat() -- 获取当前文本格式

附:
    Qt.TextFormat
        Qt.PlainText -- 文本字符串被解释为纯文本字符串。
        Qt.RichText -- 文本字符串被解释为富文本字符串。有关富文本的定义，请参阅支持的HTML子集。
        Qt.AutoText -- 自动识别是否是富文本
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('280-QLabel-文本格式')
        self.resize(1000, 500)

        label = QLabel(self)
        label.move(10, 10)

        '''设置文本'''
        label.setText('测试')
        # label.setText('<h1>测试</h1>')

        '''设置文本格式'''
        label.setTextFormat(Qt.AutoText)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
