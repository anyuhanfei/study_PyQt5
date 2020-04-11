'''
260~261-QFileDialog-功能作用

API:
    接收模式
        acceptMode() -> QFileDialog.AcceptMode
        setAcceptMode(QFileDialog.AcceptMode)
默认后缀:
    setDefaultSuffix(str)
    defaultSuffix() -> str
设置文件模式:
    setFileMode(QFileDialog.FileMode)
    fileMode() -> QFileDialog.FileMode
设置名称过滤器:
    setNameFilter(str)
    setNameFilters(str)
显示信息的详细程度:
    setViewMode(QFileDialog.ViewMode)
    viewMode() -> QFileDialog.ViewMode
设置指定角色的标签名称:
    setLabelText(self, QFileDialog.DialogLabel, str)
打开对话框:
    open(self)
    open(PYQT_SLOT) -- 打开后, 会自动连接 filesSelected 信号与此处指定的槽函数
    exec() -> int

附:
    QFileDialog.AcceptMode
        QFileDialog.AcceptOpen -- 打开
        QFileDialog.AcceptSave -- 保存
    QFileDialog.FileMode
        QFileDialog.AnyFile -- 文件的名称，无论是否存在。
        QFileDialog.ExistingFile -- 单个现有文件的名称。
        QFileDialog.Directory -- 目录的名称。显示文件和目录。但是，本机Windows文件对话框不支持在目录选择器中显示文件。
        QFileDialog.ExistingFiles -- 零个或多个现有文件的名称。
    QFileDialog.ViewMode:
        QFileDialog.Detail
        QFileDialog.List
    QFileDialog.DialogLabel:
        QFileDialog.FileName
        QFileDialog.Accept
        QFileDialog.Reject
        QFileDialog.FileType
        QFileDialog.LookIn
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('260~261-QFileDialog-功能作用')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
