'''
173-QTextEdit-tab键位控制

在控件中, tab键是用于多个输入控件和按钮控件的焦点切换. 在输入框中, tab键也可以用作制表符输入到文本中, 这就造成了混乱.

API:
    setTabChangesFocus(bool) -- 控制Tab键位的功能, 是否是改变焦点, 默认是False
    setTabStopDistance(p_float) -- 制表位的距离, 默认80(像素)
    setTabStopWidth(p_int) -- 制表位的宽度, 默认80(像素)
    tabStopDistance(self) -> float -- 获取距离
    tabStopWidth() -> int -- 获取宽度
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('173-QTextEdit-tab键位控制')
        self.resize(1000, 500)

        te = QTextEdit(self)

        '''制表位的距离'''
        te.setTabStopDistance(180)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
