'''
184-QPlainTextEdit-信号

API:
    textChanged() -- 文本改变时
    selectionChanged() -- 选中内容改变时
    modificationChanged(bool) -- 编辑状态改变时
    cursorPositionChanged() -- 光标位置改变时
    blockCountChanged(int) -- 块的个数发生改变时
    updateRequest(QRect rect, int dy) -- 内容更新请求时(内容多可滚动时的滚动操作)
    copyAvailable(bool) -- 复制可用时
    redoAvailable(bool) -- 重做可用时
    undoAvailable(bool) -- 撤销可用时
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPlainTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('184-QPlainTextEdit-信号')
        self.resize(1000, 500)

        pte = QPlainTextEdit(self)

        '''信号'''
        pte.textChanged.connect(lambda: print('文本改变了'))
        pte.selectionChanged.connect(lambda: print('选中内容改变了'))
        pte.modificationChanged.connect(lambda res: print('编辑状态改变了', res))
        pte.cursorPositionChanged.connect(lambda: print('光标位置改变了'))
        pte.blockCountChanged.connect(lambda number: print('块的个数发生改变了', number))
        pte.updateRequest.connect(lambda rect, dy: print('内容更新请求了', rect, dy))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
