'''
299-QProgressDiaLog-简介

提供了一个缓慢的操作进度反馈
进度对话框用于向用户指示操作将花费多长时间, 并演示应用程序尚未冻结
它还可以为用户提供终止操作的机会

会自动弹出.

继承自 QDialog

构造函数:
    QProgressDialog(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QProgressDialog(str, str, int, int, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QProgressDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('299-QProgressDiaLog-简介')
        self.resize(1000, 500)

        QProgressDialog(self)

        QProgressDialog('提示语', '按钮', 0, 10, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
