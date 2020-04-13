'''
264-QInputDialog-静态方法

提供了一个简单方便的对话框，获得来自用户的单个值
输入值可以是字符串，数字或列表中的项目
设置标签以告知用户应输入的内容

继承自 QDialog

常用的静态方法:
    # 数字
    getInt(QWidget, str, str, value: int = 0, min: int = -2147483647, max: int = 2147483647, step: int = 1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> Tuple[int, bool]
    # 浮点型
    getDouble(QWidget, str, str, value: float = 0, min: float = -2147483647, max: float = 2147483647, decimals: int = 1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> Tuple[float, bool]
    # 浮点型
    getDouble(QWidget, str, str, float, float, float, int, Union[Qt.WindowFlags, Qt.WindowType], float) -> Tuple[float, bool]
    # 单行文本
    getText(QWidget, str, str, echo: QLineEdit.EchoMode = QLineEdit.Normal, text: str = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool]
    # 多行文本
    getMultiLineText(QWidget, str, str, text: str = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool]
    # 列表中的项目
    getItem(QWidget, str, str, Iterable[str], current: int = 0, editable: bool = True, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool]
        参数:
            QWidget -- 父类
            str -- 标题
            str -- 提示语
            value -- 默认值
            min -- 最小值
            max -- 最大值
            step -- 步长
            decimals -- 小数位数
            echo -- 输入模式
        返回值:
            str -- 输入的内容
            bool -- 点击确认的键
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('264-QInputDialog-静态方法')
        self.resize(1000, 500)

        '''整型'''
        res = QInputDialog.getInt(self, '标题', '提示语')
        print(res)
        '''文本'''
        res = QInputDialog.getText(self, '标题', '提示语', echo=QLineEdit.Password)
        print(res)
        '''可迭代对象'''
        res = QInputDialog.getItem(self, '标题', '提示语', ['1', '2', '3'])
        print(res)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
