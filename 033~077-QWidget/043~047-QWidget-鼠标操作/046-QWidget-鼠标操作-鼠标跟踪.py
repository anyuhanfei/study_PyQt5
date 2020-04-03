'''
045-QWidget-鼠标操作-鼠标跟踪
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('045_QWidget_鼠标操作_鼠标跟踪')
        self.resize(700, 700)
        self.move(200, 200)

        # 获取鼠标是否被跟踪
        print(self.hasMouseTracking())

        # 设置鼠标跟踪   True 开启跟踪  False 关闭跟踪
        self.setMouseTracking(True)

    def mouseMoveEvent(self, mme):
        '''鼠标跟踪的执行函数
        当鼠标跟踪被触发时，将执行这个函数；
        默认情况下，鼠标未被跟踪，只有按住鼠标左键并移动时，这个函数会被触发；
        当鼠标设置了鼠标跟踪后，只要鼠标移动这个函数就会被触发；

        参数一(QMouseEvent)：鼠标对象
        '''
        print('鼠标移动了')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
