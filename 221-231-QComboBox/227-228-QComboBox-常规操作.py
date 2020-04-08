'''
227~218-QComboBox-常规操作

API:
    可编辑: (内容是否可以被编辑)
        setEditable(bool editable)
        isEditable()
    可重复: (添加的条目内容可以是否可以是重复的)
        setDuplicatesEnabled(bool enable)
        duplicatesEnabled()
    有框架: (控件是否有框架)
        setFrame(bool)
        hasFrame()
    图标尺寸: (条目项的图标的尺寸设置)
        setIconSize(QSize)
        iconSize()
    尺寸调整策略:
        setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy policy)
        sizeAdjustPolicy() -> QComboBox.SizeAdjustPolicy
        setMinimumContentsLength(int characters)
        minimumContentsLength() -> int
    清空:
        clear() -- 移除所有项目
        clearEditText() -- 清除组合框中用于编辑的行编辑内容
    弹出:
        showPopup()
    完成器:
        setCompleter(QCompleter completer)
        completer() -> QCompleter
    验证器:
        setValidator(QValidator validator)
        validator()

附:
    QComboBox.AdjustToContents -- 组合框将始终根据内容进行调整
    QComboBox.AdjustToContentsOnFirstShow -- 组合框将在第一次显示时调整其内容。
    QComboBox.AdjustToMinimumContentsLength -- 请改用AdjustToContents或AdjustToContentsOnFirstShow。
    QComboBox.AdjustToMinimumContentsLengthWithIcon -- 组合框将调整为minimumContentsLength加上图标的空间。出于性能原因，请在大型模型上使用此策略。
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('227~218-QComboBox-常规操作')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
