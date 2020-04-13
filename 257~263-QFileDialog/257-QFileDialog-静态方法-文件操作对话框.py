'''
257-QFileDialog-静态方法-文件操作对话框

提供了一个对话框，允许用户选择文件或目录
允许用户遍历文件系统，以选择一个或多个文件或目录

继承自 QDialog

获取文件:
    getOpenFileName(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[str, str]

    getOpenFileNames(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[List[str], str]

    getOpenFileUrl(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[QUrl, str]

    getOpenFileUrls(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[List[QUrl], str]

    getSaveFileName(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[str, str]

    getSaveFileUrl(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[QUrl, str]
        参数:
            parent: 父类
            caption: 对话框标题
            directory: 目录
            filter: 过滤字符串 (过滤后缀)
            initialFilter: 默认过滤字符串
            options: 一些选项

附:
    过滤字符串格式: 名称1(*.jpg *.png);;名称2(*.py)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('257-QFileDialog-静态方法-文件操作对话框')
        self.resize(1000, 500)

        # 选择一个文件
        res = QFileDialog.getOpenFileName(self, "选择一个py文件", './', "All(*.*);;Images(*.png);;Py(*.py)", "Py(*.py)")
        # 选则多个文件
        # res = QFileDialog.getOpenFileNames(self, "选择一个py文件", './', "All(*.*);;Images(*.png);;Py(*.py)", "Py(*.py)", )
        print(res)  # ('文件绝对路径', 'Py(*.py)')  (['文件1', '文件2', '文件3'], 'Py(*.py)')

        # url 相关的函数, getOpenFileUrl 和 getOpenFileUrls 基本与文件类似, 只是获取的文件不是文件的绝对路径, 而是 file 协议的文件对象

        # save 相关的函数, getSaveFileName 和 getSaveFileUrl 参数和选择文件一致, 功能是指定要保存文件的路径和名称及后缀, 仅仅是指定, 并没有创建文件和内容, 需要自己后续自定义功能


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
