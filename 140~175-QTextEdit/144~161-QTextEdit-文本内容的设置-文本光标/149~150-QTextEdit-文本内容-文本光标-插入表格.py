'''
149~150-QTextEdit-文本内容-文本光标-插入表格

API:
    insertTable(int rows, int columns) -> QTextTable -- 插入表格
    insertTable(int rows, int columns, QTextTableFormat) -> QTextTable -- 插入表格(有样式)

附:
    QTextTableFormat  (from PyQt5.QtGui import QTextTableFormat)

    API:
        setAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None) -- 对齐方式
        setCellPadding(self, p_float) -- 内边距
        setCellSpacing(self, p_float) -- 外边距
        setColumnWidthConstraints(self, Iterable, QTextLength=None) -- 设置列宽
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextTableFormat
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('149~150-QTextEdit-文本内容-文本光标-插入表格')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        te_cursor = te.textCursor()

        '''插入一个表格'''
        # 无样式
        te_cursor.insertTable(5, 3)

        # 有样式
        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)
        ttf.setCellPadding(6)
        ttf.setCellPadding(3)
        ttf.setColumnWidthConstraints()
        res = te_cursor.insertTable(5, 3, ttf)
        print(res)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
