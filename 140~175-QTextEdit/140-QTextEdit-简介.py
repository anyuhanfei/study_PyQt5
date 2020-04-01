'''
140-QTextEdit-简介

是一个高级的WYSIWYG(What You See Is What You Get 所见即所得)查看器/编辑器，支持使用HTML样式标签的富文本格式。

支持的HTML4标签子集, 在 https://doc.qt.io/qt-5/richtext-html-subset.html 这个网站中可以查看具体内容, 如果不够, 可以考虑使用WebKit

它经过优化，可以处理大型文档并快速响应用户输入。适用于段落和字符, 如果文本太大而无法在文本编辑的视口中查看，则会出现滚动条

文本编辑可以加载纯文本和富文本文件, 以显示图像，列表和表格
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('140-QTextEdit-简介')
        self.resize(1000, 500)

        '''创建一个 QTextEdit 控件'''
        te = QTextEdit(self)
        te.move(10, 10)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
