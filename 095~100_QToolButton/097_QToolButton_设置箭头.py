'''
097_QToolButton_设置箭头

将按钮变成一个具备特殊箭头图标的按钮

API:
    setArrowType(Qt.ArrowType) -- 设置箭头图标类型
    arrowType() -- 获取箭头图标类型

箭头图标类型：
    Qt.NoArrow -- 无箭头
    Qt.UpArrow -- 向上箭头
    Qt.DownArrow -- 向下箭头
    Qt.LeftArrow -- 向左箭头
    Qt.RightArrow -- 向右箭头

注：
    若有设置箭头图标类型(无箭头类型除外)，自定义的图标将被覆盖
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QToolButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('097_QToolButton_设置箭头')
        self.resize(1000, 500)

        toolb = QToolButton(self)
        # 设置文本和图标
        toolb.setText('工具')
        icon = QIcon('./xxx.png')
        toolb.setIcon(icon)

        '''设置箭头'''
        toolb.setArrowType(Qt.UpArrow)
        # toolb.setArrowType(Qt.NoArrow)

        '''获取箭头类型'''
        toolb_arrow_type = toolb.arrowType()

        label = QLabel('当前工具按钮的箭头类型为: %s' % (toolb_arrow_type), self)
        label.move(10, 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
