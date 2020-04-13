'''
262-263-QFileDialog-信号

currentChanged(path_str) -- 当前路径发生改变时
currentUrlChanged(QUrl) -- 当前路径url发生改变时
directoryEntered(directory_str) -- 打开选中文件夹时
directoryUrlEntered(QUrl directory) -- 打开选中文件夹url时
filterSelected(filter_str) -- 选择名称过滤器时
fileSelected(str) -- 最终选择文件时
filesSelected([str]) -- 最终选择多个文件时
urlSelected(QUrl url) -- 最终选择url时
urlsSelected(List[QUrl]) -- 最终选择多个url时

疑问:
    关于 url 的信号不会被触发?
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('262-263-QFileDialog-信号')
        self.resize(1000, 500)

        fd = QFileDialog(self, '选择文件', './', 'All(*.*);;Python(*.py)')

        fd.currentChanged.connect(lambda path: print('当前路径发生改变时:', path))
        fd.currentUrlChanged.connect(lambda url: print('当前路径url发生改变时', url))
        fd.directoryEntered.connect(lambda directory_str: print('打开选中文件夹时', directory_str))
        fd.filterSelected.connect(lambda filter_str: print('选择名称过滤器时', filter_str))

        fd.fileSelected.connect(lambda val: print('最终选择文件时', val))
        fd.filesSelected.connect(lambda val: print('最终选择多个文件时', val))
        fd.urlSelected.connect(lambda val: print('最终选择url时', val))
        fd.urlsSelected.connect(lambda val: print('最终选择多个url时', val))

        fd.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
