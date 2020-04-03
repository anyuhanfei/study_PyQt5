'''
171-QTextEdit-滚动到锚点

滚动到锚点位置

API:
    scrollToAnchor(p_str) -- 滚动到锚点位置

注:
    <a name="锚点名称" href="#锚点内容"> xxx </a> -- 锚点设置
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('171-QTextEdit-滚动到锚点')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.resize(300, 100)
        te.setHtml('asdads<br/>' * 50 + '<a name="mao" href="#mao">锚点</a><br/>' + '12345<br/>' * 2)

        '''滚动到锚点位置'''
        te.scrollToAnchor('mao')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
