'''
185-QPlainTextEdit-信号-案例

给文本输入框添加行号
    创建一个与文本输入框同高的控件
    创建标签控件, 并通过 \n 实现竖着书写数字
    当块更新时更新, 更新标签控件内容
    当内容更新时, 更新标签控件展示的内容
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPlainTextEdit, QLabel
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('185-QPlainTextEdit-信号-案例')
        self.resize(1000, 500)

        self._create_label()
        self._create_pte()
        self._pte_signal()

    def _pte_signal(self):
        '''文本框的信号'''
        self.pte.blockCountChanged.connect(self._block_count_changed)
        # 内容改变时, 将行号控件的 y 轴偏移
        self.pte.updateRequest.connect(lambda rect, dy: self.label.move(self.label.x(), self.label.y() + dy))

    def _block_count_changed(self, number):
        '''块数量改变时执行
        更新行预存列表, 并展示
        '''
        self.label.setText('\n'.join(str(i) for i in range(1, number + 1)))
        self.label.adjustSize()

    def _create_pte(self):
        '''创建文本框'''
        self.pte = QPlainTextEdit(self)
        self.pte.move(50, 10)
        self.pte.resize(200, 200)
        self.pte.setFont(QFont('幼圆', 20, 1))

    def _create_label(self):
        '''创建行号'''
        self.widget = QWidget(self)
        self.widget.move(10, 10)
        self.widget.resize(40, 200)
        self.widget.setStyleSheet('background-color: red;')

        self.label = QLabel(self.widget)
        self.label.move(0, 6)
        self.label.resize(40, 200)
        self.label.setText('1\n')
        self.label.setFont(QFont('幼圆', 20, 1))
        self.label.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
