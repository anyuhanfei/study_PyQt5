'''
284-QLable-链接和换行

API:
    外部链接
        openExternalLinks() -> bool -- 获取外部链接点击是否有效
        setOpenExternalLinks(bool open) -- 设置外部链接点击是否有效

    单词换行 (单词内容超出一行 是否换行, 保证单词的完整性)
        setWordWrap(bool on) -- 设置单词是否换行
        wordWrap() -> bool -- 获取单词是否换行
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('284-QLable-链接和换行')
        self.resize(1000, 500)

        label = QLabel(self)
        label.move(10, 10)
        label.setText('<a href="http://www.baidu.com">链接</a>')

        '''外部链接'''
        label.setOpenExternalLinks(True)

        label2 = QLabel(self)
        label2.move(10, 50)
        label2.setText('link link link link link link link link')

        '''单词换行'''
        label2.setWordWrap(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
