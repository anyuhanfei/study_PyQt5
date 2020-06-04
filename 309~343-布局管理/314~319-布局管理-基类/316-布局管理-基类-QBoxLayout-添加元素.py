'''
316-布局管理-基类-QBoxLayout-添加元素

添加控件:
    addWidget(self, QWidget, stretch:int = 0, alignment: Union[Qt.Alignment, Qt.AlignmentFlag])
    insertWidget(self, int, QWidget, stretch: int = 0, alignment: Union[Qt.Alignment, Qt.AlignmentFlag])
添加子布局:
    addLayout(self, QLayout, stretch: int = 0)
    insertLayout(self, int, QLayout, stretch: int = 0)
替换控件:
    replaceWidget(self, QWidget, QWidget, options: Union[Qt.FindChildOptions, Qt.FindChildOption])
移除控件:
    removeWidget(self, QWidget)
    QWidge.hide()

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QBoxLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('316-布局管理-基类-QBoxLayout-添加元素')
        self.resize(1000, 500)

        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color: cyan;')
        label2.setStyleSheet('background-color: red;')
        label3.setStyleSheet('background-color: yellow;')

        self.layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.layout.addWidget(label1)
        self.layout.addWidget(label2)

        '''插入控件'''
        self.layout.insertWidget(0, label3)

        '''移除控件, 需要手动干掉移除的子控件'''
        self.layout.removeWidget(label2)
        label2.hide()

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
