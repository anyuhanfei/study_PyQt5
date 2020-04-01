'''
147-QTextEdit-文本内容-文本光标-插入文本片段

API:
    insertFragment(QTextDocumentFragment) -- 插入文本片段

附:
    QTextDocumentFragment
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextDocumentFragment


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('147-QTextEdit-文本内容-文本光标-插入文本片段')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        te_cursor = te.textCursor()

        '''插入文本片段'''
        # html 格式文本
        tdf = QTextDocumentFragment.fromHtml("<h1>ddd</h1>")
        te_cursor.insertFragment(tdf)
        # 普通文本
        tdf = QTextDocumentFragment.fromPlainText('<h1>ddd</h1>')
        te_cursor.insertFragment(tdf)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
