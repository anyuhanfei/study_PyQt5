'''
258-QFileDialog-静态方法-文件夹操作对话框

getExistingDirectory(parent: QWidget = None, caption: str = '', directory: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = QFileDialog.ShowDirsOnly) -> str
getExistingDirectoryUrl(parent: QWidget = None, caption: str = '', directory: QUrl = QUrl(), options: Union[QFileDialog.Options, QFileDialog.Option] = QFileDialog.ShowDirsOnly, supportedSchemes: Iterable[str] = []) -> QUrl
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('258-QFileDialog-静态方法-文件夹操作对话框')
        self.resize(1000, 500)

        res = QFileDialog.getExistingDirectory(self, "选择一个py文件", './')
        print(res)  # 选择目录的绝对路径


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
