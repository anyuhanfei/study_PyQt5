'''
262-263-QFileDialog-信号

currentChanged(path_str) -- 当前路径发生改变时
currentUrlChanged(QUrl) -- 当前路径url发生改变时
directoryEntered(directory_str) -- 打开选中文件夹时
directoryUrlEntered(QUrl directory) -- 打开选中文件夹url时
filterSelected(filter_str) -- 选择名称过滤器时
fileSelected(str) -- 最终选择文件时
filesSelected([str]) -- 选择多个文件时
urlSelected(QUrl url) -- 最终选择url时
urlsSelected(List[QUrl]) -- 最终选择多个url时
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('262-263-QFileDialog-信号')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
