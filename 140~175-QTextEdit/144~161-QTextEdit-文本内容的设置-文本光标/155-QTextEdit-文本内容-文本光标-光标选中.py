'''
155-QTextEdit-文本内容-文本光标-光标选中

API:
    setPosition(int pos, QTextCursor.MoveMode=MoveAnchor) -- 设置光标位置
    movePosition(QTextCursor.MoveOperation, QTextCursor.MoveMode=MoveAnchor, int n = 1) -- 移动指定长度后, 参照移动选项和模式确定最终位置以及是否选中文本
    select(QTextCursor.SelectionType) -- 选中指定内容

注:
    设置和移动光标位置后, 需要再将光标对象指定到文本文档对象上 (setTextCursor)
    设置光标位置一直是以首部为原点计算的, 在使用 QTextCursor.MoveMode 的 keepAnchor 时, 锚固定的话设置光标位置会有选中效果

附:
    QTextCursor:
        QTextCursor.MoveMode
            QTextCursor.MoveAnchor -- 将锚点移动到与光标本身相同的位置。
            QTextCursor.KeepAnchor -- 将锚固定在原处。
        QTextCursor.MoveOperation
            QTextCursor.NoMove -- 将光标保持在原位
            QTextCursor.Start -- 移至文档的开头。
            QTextCursor.StartOfLine -- 移动到当前行的开头。
            QTextCursor.StartOfBlock -- 移动到当前块的开头。
            QTextCursor.StartOfWord -- 移动到当前单词的开头。
            QTextCursor.PreviousBlock -- 移动到上一个块的开头。
            QTextCursor.PreviousCharacter -- 移至上一个字符。
            QTextCursor.PreviousWord -- 移到上一个单词的开头。
            QTextCursor.Up -- 向上移动一行。
            QTextCursor.Left -- 向左移动一个字符。
            QTextCursor.WordLeft -- 向左移动一个单词。
            QTextCursor.End -- 移到文档的末尾。
            QTextCursor.EndOfLine -- 移动到当前行的末尾。
            QTextCursor.EndOfWord -- 移到当前单词的末尾。
            QTextCursor.EndOfBlock -- 移动到当前块的末尾。
            QTextCursor.NextBlock -- 移动到下一个块的开头。
            QTextCursor.NextCharacter -- 移动到下一个角色。
            QTextCursor.NextWord -- 转到下一个单词。
            QTextCursor.Down -- 向下移动一行。
            QTextCursor.Right -- 向右移动一个角色。
            QTextCursor.WordRight -- 向右移动一个单词。
            QTextCursor.NextCell -- 移动到当前表中下一个表格单元格的开头。如果当前单元格是行中的最后一个单元格，则光标将移动到下一行中的第一个单元格。
            QTextCursor.PreviousCell -- 移动到当前表内的上一个表格单元格的开头。如果当前单元格是行中的第一个单元格，则光标将移动到上一行中的最后一个单元格。
            QTextCursor.NextRow -- 移动到当前表中下一行的第一个新单元格。
            QTextCursor.PreviousRow -- 移动到当前表中上一行的最后一个单元格。
        QTextCursor.SelectionType
            QTextCursor.Document -- 选择整个文档。
            QTextCursor.BlockUnderCursor -- 选择光标下的文本块。
            QTextCursor.LineUnderCursor -- 选择光标下的文本行。
            QTextCursor.WordUnderCursor -- 选择光标下的单词。如果光标未定位在可选字符串中，则不选择任何文本。
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextCursor


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('155-QTextEdit-文本内容-文本光标-光标选中')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)
        te.setText('123456789')

        te_cursor = te.textCursor()

        '''设置光标位置'''
        te_cursor.setPosition(1)
        te.setTextCursor(te_cursor)

        '''移动光标位置'''
        # 设置为移动到行尾, 锚固定
        te_cursor.movePosition(QTextCursor.EndOfLine, QTextCursor.KeepAnchor, 1)
        te.setTextCursor(te_cursor)

        '''选中指定内容'''
        te_cursor.select(QTextCursor.Document)
        te.setTextCursor(te_cursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
