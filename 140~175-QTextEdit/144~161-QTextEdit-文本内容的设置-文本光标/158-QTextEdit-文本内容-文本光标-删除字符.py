'''
158-QTextEdit-文本内容-文本光标-删除字符

API:
    deleteChar() -- 删除文本光标后一个字符
    deletePreviousChar() -- 删除文本光标前一个字符

注:
    以上两个 API 若在没有选中文本时, 删除内容就和说明的一样; 若有选中文本, 则删除选中文本.
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)
        te.setText('123456789')

        te_cursor = te.textCursor()

        # 移动光标
        te_cursor.setPosition(4)
        te.setTextCursor(te_cursor)

        '''删除文本'''
        te_cursor.deleteChar()
        te_cursor.deletePreviousChar()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
