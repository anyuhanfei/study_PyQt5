'''
229-QComboBox-信号

API:
    activated(int index) -- 某个条目被选中时 *
    activated(QString text) -- 某个条目被选中时 *
    currentIndexChanged(int index) -- 当前选中的索引发生改变时
    currentIndexChanged(QString text) -- 当前选中的索引发生改变时
    currentTextChanged(QString text) -- 当前的文本内容发生改变时
    editTextChanged(QString text) -- 编辑的文本发生改变时
    highlighted(int index) -- 高亮
    highlighted(QString text) -- 高亮

        * 标表示必须是用户交互, 造成的值改变才会发射这个信号
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QComboBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('229-QComboBox-信号')
        self.resize(1000, 500)

        cb = QComboBox(self)
        cb.move(10, 10)
        cb.addItems(['a', 'b', 'c', 'd', 'e', 'f'])

        '''条目被选中时'''
        cb.activated.connect(lambda val: print('条目被选中了', val))
        cb.activated[str].connect(lambda val: print('条目被选中了', val))

        '''当前选中的索引发生改变时'''
        cb.currentIndexChanged.connect(lambda val: print('选中的索引发生改变了', val))
        cb.currentIndexChanged[str].connect(lambda val: print('选中的索引发生改变了', val))

        cb.setCurrentIndex(2)

        '''当前的文本内容发生改变时'''
        cb.currentTextChanged.connect(lambda val: print('当前的文本内容发生改变了', val))

        '''编辑的文本发生改变时'''
        cb.editTextChanged.connect(lambda val: print('编辑的文本发生改变了', val))

        cb.setEditable(True)
        cb.setCurrentText('修改内容')

        ''''''


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
