'''
283-QLabel-文本交互标志和选中

API:
    setTextInteractionFlags(Qt.TextInteractionFlags flags)
    textInteractionFlags() -> Qt.TextInteractionFlags

附:
    Qt.TextInteractionFlag
        Qt.NoTextInteraction -- 不可能与文本进行交互
        Qt.TextSelectableByMouse -- 可以使用鼠标选择文本并使用上下文菜单或标准键盘快捷键将其复制到剪贴板
        Qt.TextSelectableByKeyboard -- 可以使用键盘上的光标键选择文本。显示文本光标
        Qt.LinksAccessibleByMouse -- 可以使用鼠标突出显示和激活链接
        Qt.LinksAccessibleByKeyboard -- 可以使用选项卡聚焦链接并使用enter激活
        Qt.TextEditable -- 该文字完全可编辑
        Qt.TextEditorInteraction -- 文本编辑器的默认值
            等同于设置 TextSelectableByMouse | TextSelectableByKeyboard | TextEditable
        Qt.TextBrowserInteraction -- QTextBrowser的默认值
            等同于设置 TextSelectableByMouse | LinksAccessibleByMouse | LinksAccessibleByKeyboard
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('283-QLabel-文本交互标志和选中')
        self.resize(1000, 500)

        label = QLabel('测试', self)
        label.move(10, 10)
        label.resize(100, 100)

        '''设置鼠标可选中, 键盘可选中, 内容可编辑'''
        label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
