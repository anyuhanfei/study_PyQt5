'''
148-QTextEdit-文本内容-文本光标-插入列表

API:
    insertList(QTextListFormat) -> QTextList -- 在当前位置插入一个新块，并使其成为具有给定格式的新创建列表的第一个列表项。返回创建的列表
    insertList(QTextListFormat.Style) -> QTextList -- 在当前位置插入一个新块，并使其成为具有给定格式的新创建列表的第一个列表项。返回创建的列表
    createList(QTextListFormat ) -> QTextList  -- 创建并返回具有给定格式的新列表，并使当前段落的光标位于第一个列表项中
    createList(QTextListFormat.style ) -> QTextList  -- 创建并返回具有给定格式的新列表，并使当前段落的光标位于第一个列表项中

附:
    QTextListFormat  (from PyQt5.QtGui import QTextListFormat)

    API:
        setIndent(int)
        setNumberPrefix(str)
        setNumberSuffix(str)
        setStyle(QTextListFormat_Style)

    QTextListFormat.Style

    API:
        QTextListFormat.ListDisc -- 一个圆圈
        QTextListFormat.ListCircle -- 一个空的圆圈
        QTextListFormat.ListSquare -- 一个方块
        QTextListFormat.ListDecimal -- 十进制值按升序排列
        QTextListFormat.ListLowerAlpha -- 小写拉丁字符按字母顺序排列
        QTextListFormat.ListUpperAlpha -- 大写拉丁字符按字母顺序排列
        QTextListFormat.ListLowerRoman -- 小写罗马数字（仅支持最多4999项）
        QTextListFormat.ListUpperRoman -- 大写罗马数字（仅支持最多4999项）

示例, 类似于:

    - 第一条
    - 第二条
    - 第三条
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextListFormat


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('148-QTextEdit-文本内容-文本光标-插入列表')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)
        te.setText('xxx\naaa')

        te_cursor = te.textCursor()

        '''创建一个新块'''
        te_cursor.createList(QTextListFormat.ListDisc)

        '''插入一个新块'''
        tlf = QTextListFormat()
        tlf.setIndent(3)  # 缩进
        tlf.setNumberPrefix('<<')  # 前缀(样式是数字才会展示,下同)
        tlf.setNumberSuffix('>>')  # 后缀
        tlf.setStyle(QTextListFormat.ListDecimal)  # 设置样式
        til = te_cursor.insertList(tlf)
        print(til)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
