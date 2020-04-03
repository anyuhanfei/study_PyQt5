'''
056~059-QWidget-窗口-API
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.Qt import Qt


class Window(QWidget):
    height = 10

    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.move(200, 200)

        '''窗口标题'''
        # 设置窗口标题
        self.setWindowTitle('056~059_QWidget_窗口_API')

        # 获取窗口标题
        self._create_label('当前窗口标题为：%s' % (self.windowTitle()))

        '''窗口图标'''
        # 设置窗口图标，使用 QIcon() 类创建一个图标对象
        self.setWindowIcon(QIcon('./xxx.png'))

        # 获取窗口图标对象，获取的就是 QIcon() 类创建出的图标对象
        self._create_label('当前窗口图标对象为：%s' % (self.windowIcon()))

        '''不透明度'''
        # 设置窗口的不透明度, 1.0 为不透明, 0.0 为完全透明
        self.setWindowOpacity(1.0)  # 传入一个不大于 1 的浮点数

        # 获取窗口的不透明度
        self._create_label('当前窗口不透明度为：%s' % (self.windowOpacity()))

        '''窗口状态
        Qt.WindowNoState  无状态
        Qt.WindowMinimized  最小化
        Qt.WindowMaximized  最大化
        Qt.WindowFullScreen  全屏
        Qt.WindowActive  活动窗口
        '''
        # 设置窗口状态
        self.setWindowState(Qt.WindowMaximized)  # 设置为最大化

        # 获取窗口状态，得到的是窗口状态对象
        self._create_label('打开窗口时窗口状态为：%s' % (self.windowState()))

        '''最大化和最小化

        设置:
            showFullScreen()  全屏
            showMaximized()  最大化
            showMinimized()  最小化
            showNormal()  正常

        判断：
            isMinimized()  是否是最小化窗口
            isMaximized()  是否是最大化窗口
            isFullScreen()  是否全屏
        '''
        self.showNormal()  # 设置为正常

        self._create_label('打开窗口时窗口是否是最小化窗口：%s' % (self.isMinimized()))

        '''窗口标志（窗口类型）'''
        # 设置窗口标志 （太多了，只测试一个）
        self.setWindowFlags(Qt.WindowTitleHint)  # 只有标题栏和关闭按钮

        # 获取窗口标志 （窗口标志对象）
        self._create_label('当前窗口标志为：%s' % (self.windowFlags()))

    def _create_label(self, content):
        label = QLabel(self)
        label.setText(content)
        label.move(10, self.height)
        self.height += 30


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
