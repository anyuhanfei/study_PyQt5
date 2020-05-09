'''
298-QErrorMessage-功能作用

API:
    showMessage(str) -- 添加错误信息并展示, 展示的窗口是非模态窗口
    qtHandler() -- 调用此方法后, 可以使用一些封装好的弹出框, 如 Pyqt5.QtCore.qDebug, Pyqt5.QtCore.qWarning
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QErrorMessage
from PyQt5.QtCore import qDebug, qWarning


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('298-QErrorMessage-功能作用')
        self.resize(1000, 500)

        em = QErrorMessage(self)
        em.setWindowTitle('错误提示')

        em.showMessage('这是错误信息')
        em.showMessage('这是错误信息')
        em.showMessage('这是错误信息')
        em.showMessage('这是错误信息!')

        '''模态窗口式打开'''
        em.open()

        '''封装好的弹框'''
        QErrorMessage.qtHandler()
        qDebug('xxxxxx')
        qWarning('oooooo')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
