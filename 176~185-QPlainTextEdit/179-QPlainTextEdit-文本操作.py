'''
179-QPlainTextEdit-文本操作

API:
    setPlainText(text_str) -- 设置普通文本内容
    insertPlainText(text_str) -- 插入普通文本
    appendPlainText(text_str) -- 追加普通文本
    appendHtml(html_str) -- 追加HTML字符串
    toPlainText() -- 获取内容(纯文本)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPlainTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('179-QPlainTextEdit-文本操作')
        self.resize(1000, 500)

        pte = QPlainTextEdit(self)

        '''设置普通文本内容'''
        pte.setPlainText('123456789')

        '''插入普通文本'''
        # 插入普通文本
        pte.insertPlainText('aaa')

        '''追加普通文本'''
        pte.appendPlainText('bbb')

        '''追加html'''
        pte.appendHtml('<h1>ccc</h1>')

        '''获取内容'''
        print(pte.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
