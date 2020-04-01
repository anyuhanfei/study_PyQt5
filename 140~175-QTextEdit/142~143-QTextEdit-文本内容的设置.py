'''
142~143-QTextEdit-文本内容的设置

除了用户自己输入内容外, 也可以在代码上手动设置文本内容.

API
    普通文本:
        setPlainText(str) -- 设置普通文本格式的内容
        insertPlainText(str) -- 插入普通文本格式的内容(在光标处插入)
        toPlainText() -> str -- 获取普通文本格式的内容
    HTML:
        setHtml(str) -- 设置 html 格式的内容
        insertHtml(str) -- 插入 html 格式的内容(在光标处插入)
        toHtml() -> str -- 获取 html 格式的内容

    setText(str) -- 设置文本(自动判定)
    append(str) -- 追加文本(自动识别格式)(在文本的末尾追加, 无视光标)
    clear() -- 清空(也可以将内容设置为空, 效果相同)

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('142~143-QTextEdit-文本内容的设置')
        self.resize(1000, 500)

        te_one = QTextEdit(self)
        te_one.move(10, 10)
        te_one.resize(100, 100)
        te_two = QTextEdit(self)
        te_two.move(110, 10)
        te_two.resize(100, 100)
        te_three = QTextEdit(self)
        te_three.move(210, 10)
        te_three.resize(100, 100)

        '''设置普通文本'''
        # 设置文本不会修改光标位置
        te_one.setPlainText('<h1>xxx</h1>')

        '''新增普通文本'''
        # 是从光标处插入
        # 新增文本会修改光标位置
        te_one.insertPlainText('<h1>xxx</h1>')

        '''设置html文本'''
        te_two.setHtml('<h1>xxx</h1>')

        '''插入html文本'''
        te_two.insertHtml('<h1>aaa</h1>')

        '''获取普通文本格式内容'''
        print('获取普通文本格式内容:', te_two.toPlainText())

        '''获取 html 格式内容'''
        print('获取 html 格式内容:', te_two.toHtml())

        '''设置文本(自动识别格式)'''
        te_three.setText('<h1>aaa</h1>')

        '''追加文本(自动识别格式)'''
        te_three.append('<h1>bbb</h1>')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
