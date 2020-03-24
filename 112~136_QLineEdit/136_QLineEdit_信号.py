'''
136_QLineEdit_信号

API:
    textEdited(text) -- 文本编辑时发射的信号
    textChanged(text) -- 文本框文本发生改变时发出的信号
    returnPressed() -- 按下回车键时发出的信号
    editingFinished() -- 结束编辑时发出的信号
    cursorPositionChanged(int oldPos，int newPos) -- 光标位置发生改变时发出的信号
    selectionChanged() -- 选中的文本发生改变时发出的信号
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('136_QLineEdit_信号')
        self.resize(1000, 500)

        le = QLineEdit(self)
        le.move(10, 10)

        # 文本编辑时发射的信号
        le.textEdited.connect(lambda val: print('文本编辑时发射的信号', val))

        # 文本框文本发生改变时发出的信号
        le.textChanged.connect(lambda val: print('文本框文本发生改变时发出的信号', val))
        le.setText('xxx')  # 仅 textChanged 触发了信号，textEdited 只有在用户编辑时才会被触发。

        # 按下回车键时发出的信号（可用场景，多个单行输入框，按回车意味着输入完毕要输入下一个，可以通过此信号实现功能）
        le.returnPressed.connect(lambda: print('按下回车键时发出的信号'))

        # 结束编辑时发出的信号（结束编辑就是输入框失去了焦点）
        le.editingFinished.connect(lambda: print('结束编辑时发出的信号'))

        # 光标位置发生改变时发出的信号
        le.cursorPositionChanged.connect(lambda old_pos, new_pos: print('光标位置发生改变时发出的信号', old_pos, new_pos))

        # 选中的文本发生改变时发出的信号
        le.selectionChanged.connect(lambda: print('选中的文本发生改变时发出的信号'))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
