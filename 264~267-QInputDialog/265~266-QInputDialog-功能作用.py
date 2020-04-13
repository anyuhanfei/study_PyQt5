'''
265~266-QInputDialog-功能作用

构造函数:
    QInputDialog(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
选项设置:
    setOption(self, QInputDialog.InputDialogOption, on: bool = True)
    setOptions(self, Union[QInputDialog.InputDialogOptions, QInputDialog.InputDialogOption])
    testOption(self, QInputDialog.InputDialogOption) -> bool
    options(self) -> QInputDialog.InputDialogOptions
输入模式:
    inputMode(self) -> QInputDialog.InputMode
    setInputMode(self, QInputDialog.InputMode)
界面文本设置:
    setLabelText(str)
    labelText(self) -> str
    setOkButtonText(str)
    setCancelButtonText(str)
各个小分类设置:
    整型:
        setIntMaximum(self, int)
        intMaximum(self) -> int
        setIntMinimum(self, int)
        intMinimum(self) -> int
        setIntRange(self, int, int)
        setIntStep(self, int)
        intStep(self) -> int
        setIntValue(self, int)
        intValue(self) -> int
    浮点型:
        setDoubleMaximum(self, float)
        doubleMaximum() -> float
        setDoubleDecimals(self, int)
        doubleDecimals() -> int
        setDoubleMinimum(self, float)
        doubleMinimum(self) -> float
        setDoubleRange(self, float, float)
        setDoubleStep(self, float)
        doubleStep(self) -> float
        setDoubleValue(self, float)
        doubleValue(self) -> float
    字符串:
        setTextEchoMode(self, QLineEdit.EchoMode)
        textEchoMode(self) -> QLineEdit.EchoMode
        setTextValue(self, str)
        textValue(self) -> str
    下拉列表:
        setComboBoxItems(self, Iterable[str])
        comboBoxItems(self) -> List[str]
        setComboBoxEditable(self, bool)
        isComboBoxEditable(self) -> bool
附:
    QInputDialog.InputDialogOption
        QInputDialog.NoButtons -- 不显示"确定"和"取消"按钮（对"实时对话框"有用）。
        QInputDialog.UseListViewForComboBoxItems -- 使用QListView而不是不可编辑的QComboBox来显示使用setComboBoxItems()设置的项目。
        QInputDialog.UsePlainTextEditForTextInput -- 使用QPlainTextEdit进行多行文本输入。该值在5.2中引入。

    QInputDialog.InputMode
        TextInput
        IntInput
        DoubleInput
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('265~266-QInputDialog-功能作用')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
