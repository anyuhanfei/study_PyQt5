'''
098_QToolButton_自动提升

默认情况下，工具按钮和普通按钮类似，有一个边框和与窗口不同的背景颜色，使它能被明显的认为是一个按钮，但是在一般的应用中，工具按钮应该是类似扁平化(091)的样子，鼠标移动至工具按钮上时才会自动变化。

在自动提升模式下，该按钮仅在鼠标指向时才会绘制3D帧
在工具栏(QToolBar)中, 默认就是自动提升

API:
    setAutoRaise(bool) -- 开关自动提升模式
    autoRaise() -- 获取当前是否是自动提升模式
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QToolButton, QLabel
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('098_QToolButton_自动提升')
        self.resize(1000, 500)

        toolb = QToolButton(self)
        # 设置文本和图标
        toolb.setText('工具')
        icon = QIcon('./xxx.png')
        toolb.setIcon(icon)

        '''设置为自动提升'''
        toolb.setAutoRaise(True)

        '''获取自动提升'''
        toolb_auto_raise = toolb.autoRaise()

        label = QLabel('当前工具按钮是否是自动提升: %s' % (toolb_auto_raise), self)
        label.move(10, 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
