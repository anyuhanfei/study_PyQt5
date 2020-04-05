'''
176-QPlainTextEdit-简介

QPlainText和QTextEdit大致功能实现差不多, 但针对纯文本处理进行了优化

适用于段落和字符
    段落是一个格式化的字符串,为了适应控件的宽度, 会自动换行
    默认情况下，在读取纯文本时，一个换行符表示一个段落。
    文档由零个或多个段落组成。段落由硬线断开分隔。
    段落中的每个字符都有自己的属性，例如字体和颜色。
内容的编辑
    文本的选择由QTextCursor类处理，该类提供创建选择，检索文本内容或删除选择的功能
    QPlainTextEdit包含一个QTextDocument对象，可以使用document（）方法检索该对象

与QTextEdit的差异:
    QPlainTextEdit是一个简略版本的类, 使用QTextEdit和QTextDocument作为背后实现的技术支撑
    它的性能优于QTextEdit, 主要是因为在文本文档中使用QPlainTextDocumentLayout简化文本布局
    纯文本文档布局不支持表格或嵌入框架，并使用逐行逐段滚动方法替换像素精确高度计算。

继承自 QAbstractScrollArea

API:
    QPlainTextEdit(parent: QWidget = None)
    QPlainTextEdit(str, parent: QWidget = None)
'''
import sys

from PyQt5.QtWidgets import QApplication, QPlainTextEdit, QWidget


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('176_QPlainTextEdit-简介')
        self.resize(1000, 500)

        '''创建一个 QPlainTextEdit 控件'''
        QPlainTextEdit(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
