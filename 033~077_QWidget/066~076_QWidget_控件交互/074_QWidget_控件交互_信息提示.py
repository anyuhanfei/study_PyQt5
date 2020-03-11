'''
074_QWidget_控件交互_信息提示
'''
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.Qt import Qt


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('074_QWidget_控件交互_信息提示')
        self.move(200, 200)
        self.resize(500, 500)

        # 加载状态栏
        # 由于 QMainWindow 控件是懒加载，只有开发者要使用才能开启，也就是默认是关闭的
        self.statusBar()

        # 鼠标悬停状态提示
        self.setStatusTip('用户区')

        label = QLabel(self)
        label.setText('测试')
        label.move(200, 200)

        # 鼠标悬停鼠标旁提示
        label.setToolTip('这是一个 label 控件')
        # 设置提示出现时长
        label.setToolTipDuration(2000)

        # 修改窗口类型
        self.setWindowFlags(Qt.WindowContextHelpButtonHint)
        # 切换到"查看这是啥"模式, 点击该控件时显示
        label.setWhatsThis('这是一个 label 控件!')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
