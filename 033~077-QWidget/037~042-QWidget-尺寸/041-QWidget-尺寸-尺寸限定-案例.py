'''
041-QWidget-尺寸-尺寸限定-案例

创建一个窗口, 设置最小尺寸和最大尺寸
    最小为200, 200
    最大为400, 400
    测试通过resize是否可以改变
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('041_QWidget_尺寸_尺寸限定_案例')

        # 设置最大尺寸，宽高可单独设置，也可同时设置
        self.setMaximumHeight(400)
        self.setMaximumWidth(400)
        # self.setMaximumSize(400, 400)

        # 设置最小尺寸，宽高可单独设置，也可同时设置
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)
        # self.setMinimumSize(200, 200)

        # 测试
        self.resize(1000, 1000)
        # self.resize(100, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
