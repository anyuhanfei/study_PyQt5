'''
060~065-QWidget-窗口-案例

创建一个窗口
    无边框，无标题栏
    窗口半透明
    自定义最小化，最大化，关闭按钮
    支持拖拽用户区移动 （050~052_QWidget_事件_案例 中已做过）
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt


class Window(QWidget):
    top_btn_y = 0
    top_btn_width = 40
    top_btn_height = 30

    def __init__(self):
        super().__init__()
        self.setWindowTitle('060~065_QWidget_窗口_案例')
        self.resize(500, 500)
        self.move(200, 200)

        # 无边框无标题栏
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 窗口半透明
        self.setWindowOpacity(1.0)

        # 创建最小化，最大化，关闭按钮
        self.close_btn = QPushButton(self)  # 创建一个按钮
        # self.close_btn.move(self.width() - self.top_btn_width, self.top_btn_y)  # 移动到右边
        self.close_btn.resize(self.top_btn_width, self.top_btn_height)  # 设置大小
        self.close_btn.setText('×')  # 设置内容
        self.close_btn.pressed.connect(self._close_window)  # 连接点击信号的槽函数

        self.max_btn = QPushButton(self)
        self.max_btn.resize(self.top_btn_width, self.top_btn_height)
        self.max_btn.setText('□')  # ❐  □
        self.max_btn.pressed.connect(self._max_window)

        self.min_btn = QPushButton(self)
        self.min_btn.resize(self.top_btn_width, self.top_btn_height)
        self.min_btn.setText('-')
        self.min_btn.pressed.connect(self._min_window)

    def _close_window(self):
        '''关闭窗口'''
        self.close()

    def _min_window(self):
        '''最小化窗口'''
        self.showMinimized()

    def _max_window(self):
        '''最大化窗口
        最大化窗口，修改按钮内容，修改点击信号的连接槽函数，修改标签位置
        '''
        self.showMaximized()
        self.max_btn.setText('❐')
        self.max_btn.pressed.connect(self._common_window)

    def _common_window(self):
        '''恢复至普通窗口，用于最大化后的恢复'''
        self.showNormal()
        self.max_btn.setText('□')
        self.max_btn.pressed.connect(self._max_window)

    def resizeEvent(self, evt):
        '''当窗口尺寸改变时，自动调用'''
        self.close_btn.move(self.width() - self.top_btn_width, self.top_btn_y)
        self.max_btn.move(self.width() - self.top_btn_width * 2, self.top_btn_y)
        self.min_btn.move(self.width() - self.top_btn_width * 3, self.top_btn_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
