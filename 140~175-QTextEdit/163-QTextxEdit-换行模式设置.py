'''
163-QTextEdit-换行模式设置

软换行: 当用户输入了一行超级长的文本时, 有多重处理方式, 不处理一直往后追加, 另一种就是达到最大宽度后会自动向下折一行, 这就是软换行.

单词换行: 软换行模式下, 有一个单词正好在最大宽度上, 不换行会超出, 换行会有空缺, 那么也有这两种解决方法.

API:
    setLineWrapMode(QTextEdit.LineWrapMode) -- 设置软换行模式
    lineWrapMode() -> QTextEdit.LineWrapMode -- 获取软换行模式
    setWordWrapMode(self, QTextOption.WrapMode) -- 设置单词换行模式
    wordWrapMode(self) -> QTextOption.WrapMode -- 获取单词换行模式

附:
    QTextEdit.LineWrapMode
        QTextEdit.NoWrap -- 没有软换行, 超过宽度后, 会产生水平滚动条
        QTextEdit.WidgetWidth -- 以控件的宽度为限制, 但会保持单词的完整性
        QTextEdit.FixedPixelWidth -- 填充像素宽度
        QTextEdit.FixedColumnWidth -- 填充列的宽度
    QTextOption.WrapMode
        QTextOption.NoWrap -- 文本根本没有包装。
        QTextOption.WordWrap -- 保持单词完整性
        QTextOption.ManualWrap -- 与QTextOption.NoWrap相同
        QTextOption.WrapAnywhere -- 宽度够了之后, 随意在任何位置换行
        QTextOption.WrapAtWordBoundaryOrAnywhere -- 尽可能赶在单词的边界, 否则就在任意位置换行
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('163-QTextEdit-换行模式设置')
        self.resize(1000, 500)

        te = QTextEdit(self)

        '''设置软换行和保持单词完整性'''
        te.setLineWrapMode(QTextEdit.WidgetWidth)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
