'''
174-QTextEdit-打开超链接

API:
    anchorAt(QPoint) -> str -- 获取当前位置的锚点信息
    QDesktopServices.openUrl(QUrl(urlString)) -- 打开指定链接地址
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.Qt import QDesktopServices, QUrl, QPoint


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('174-QTextEdit-打开超链接')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.setHtml('<a href="http://www.baidu.com">百度</a>')  # 只有a标签是打不开的

        '''获取指定位置的锚点信息'''
        url_str = te.anchorAt(QPoint(0, 2))
        print(url_str)

        '''打开指定链接地址'''
        QDesktopServices.openUrl(QUrl('http://www.baidu.com'))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
