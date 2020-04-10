'''
251-QFontDialog-信号

currentFontChanged(QFont) -- 当前字体发生改变时
fontSelected(QFont) -- 最终选择字体时
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFontDialog, QLabel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('251-QFontDialog-信号')
        self.resize(1000, 500)

        self.label = QLabel(self)
        self.label.move(10, 10)
        self.label.setText('测试字体')
        self.label.resize(100, 100)

        fd = QFontDialog(self)

        fd.currentFontChanged.connect(lambda obj: self.label.setFont(obj))
        fd.fontSelected.connect(lambda obj: self.label.setFont(obj))

        fd.open()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
