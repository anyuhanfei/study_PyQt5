'''
050~052-QWidget-事件-案例

1.创建一个窗口包含一个标签
    鼠标进入时，展示"欢迎光临"
    鼠标离开时，展示"谢谢惠顾"
2.创建一个窗口，监听用户按键
    监听用户输入 tab 键
    监听用户输入 Ctrl+s 组合键
    监听用户输入 Ctrl+Shift+a 组合键
3.完成窗口，用户区支持拖拽
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.Qt import Qt


class Window(QWidget):
    site_x = 200
    site_y = 200

    def __init__(self):
        super().__init__()
        self.setWindowTitle('050~052_QWidget_事件_案例')
        self.resize(500, 500)
        self.move(self.site_x, self.site_y)

        self.in_out_label()

    def in_out_label(self):
        self.label = QLabel(self)
        self.label.resize(200, 30)
        self.label.move(10, 10)

    # 案例1
    def enterEvent(self, QEvent):
        self.label.setText('欢迎光临')

    def leaveEvent(self, QEvent):
        self.label.setText('谢谢惠顾')

    # 案例2
    def keyPressEvent(self, evt):
        if evt.key() == Qt.Key_Tab:
            self.label.setText('按下了 Tab 键')

        if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
            self.label.setText('按下了 Ctrl+S 键')

        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A:
            self.label.setText('按下了 Ctrl+Shift+A 键')

    # 案例3
    def mousePressEvent(self, QMouseEvent):
        # 点击左键，获取当前鼠标再桌面坐标系中的位置
        self.old_x = QMouseEvent.globalX()
        self.old_y = QMouseEvent.globalY()

    def mouseMoveEvent(self, QMouseEvent):
        # 鼠标移动，获取当前鼠标再桌面坐标系中的位置
        new_x = QMouseEvent.globalX()
        new_y = QMouseEvent.globalY()

        # 将当前鼠标位置与旧鼠标位置相减，获得移动前和移动后的差量并与窗口位置相加，得到目标位置坐标
        self.site_x += new_x - self.old_x
        self.site_y += new_y - self.old_y
        # 将窗口移动到目标位置
        self.move(self.site_x, self.site_y)

        # 将已经改变的位置坐标修改为旧坐标
        self.old_x = new_x
        self.old_y = new_y


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
