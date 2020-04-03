'''
133~135-QLineEdit-常用编辑功能

编辑用户输入的文本

API:
    backspace() -- 退格
    del_() -- 删除
    clear() -- 清空
    copy() -- 复制
    cut() -- 剪切
    paste() -- 粘贴
    isUndoAvailable() -- 判断是否可以撤销(有操作后可撤销)
    undo() -- 撤消
    isRedoAvailable() -- 判断是否可以重做(撤销操作后可重做)
    redo() -- 重做
    setDragEnabled(bool) -- 拖放

文本选中API
    setSelection(start_pos, length) -- 选中指定区间的文本
    selectAll() -- 选中所有文本
    deselect() -- 取消选中已选择文本
    hasSelectedText() -- 是否有选中文本
    selectedText() -> str -- 获取选中的文本
    selectionStart() -> int -- 选中的开始位置
    selectionEnd() -> int -- 选中的结束位置
    selectionLength() -> int -- 选中的长度

注：
    对于退格、删除、复制操作，只有使用代码选中的子字符串可以成功被操作，使用鼠标手动操作的无法成功操作。
    使用文本选中API后，不要再使用焦点修改操作了。
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('133~135_QLineEdit_常用编辑功能')
        self.resize(1000, 500)

        self.le = QLineEdit(self)
        self.le.move(10, 10)
        self.btn = QPushButton('按钮', self)
        self.btn.move(10, 40)
        self.btn.clicked.connect(self._cursor)

    def _cursor(self):
        '''编辑功能'''

        # 若在代码中选中一些字符，则可以对选中的字符进行操作
        # self.le.cursorBackward(True, 2)

        # 退格
        # self.le.backspace()

        # 复制
        self.le.cursorBackward(True, 2)
        self.le.copy()

        # 粘贴
        self.le.paste()

        self.le.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
