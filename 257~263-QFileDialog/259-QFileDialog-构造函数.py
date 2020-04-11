'''
259-QFileDialog-构造函数

QFileDialog(QWidget, Union[Qt.WindowFlags, Qt.WindowType])
QFileDialog(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '')
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('259-QFileDialog-构造函数')
        self.resize(1000, 500)

        fd = QFileDialog(self, '上传文件', './', 'All(*.*);;Python(*.py)')
        fd.open()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
