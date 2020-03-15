'''
096_QToolButton_样式风格

095 时提到设置图标后不显示文字，可以设置风格让二者显示其一或者都显示：

API：
    setToolButtonStyle() -- 设置风格
可使用参数:
    Qt.ToolButtonIconOnly -- 仅显示图标
    Qt.ToolButtonTextOnly -- 仅显示文字
    Qt.ToolButtonTextBesideIcon -- 文本显示在图标旁边
    Qt.ToolButtonTextUnderIcon -- 文本显示在图标下方
    Qt.ToolButtonFollowStyle -- 遵循风格
        注：from PyQt5.Qt import Qt
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.Qt import Qt


class Window(QWidget):
    widget = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('096_QToolButton_样式风格')
        self.resize(1000, 500)

        toolb = QToolButton(self)
        # 设置文本和图标
        toolb.setText('工具')
        icon = QIcon('./xxx.png')
        toolb.setIcon(icon)

        '''各种风格'''
        # toolb.setToolButtonStyle(Qt.ToolButtonIconOnly)
        # toolb.setToolButtonStyle(Qt.ToolButtonTextOnly)
        # toolb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # toolb.setToolButtonStyle(Qt.ToolButtonFollowStyle)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
