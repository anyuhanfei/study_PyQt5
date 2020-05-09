'''
295-QProgressBar-文本标签操作和方向和反转功能

API:
    setTextVisible(bool) -- 设置文本是否展示
    text() -- 获取文本
    setTextDirection(QProgressBar.Direction) -- 文本方向, 仅仅对于垂直进度条有效 (但是垂直方向进度条的文本会隐藏)
            BottomToTop = 1
            TopToBottom = 0
    setOrientation(Qt.Orientation) -- 设置方向
        Qt.Horizo​​ntal -- 水平
        Qt.Vertical -- 垂直
    orientation() -> Qt.Orientation -- 获取方向
    setInvertedAppearance(bool) -- 是否反向

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('295-QProgressBar-文本标签操作和方向和反转功能')
        self.resize(1000, 500)

        pb = QProgressBar(self)
        pb.move(10, 10)
        pb.resize(200, 200)
        pb.setValue(50)

        '''设置为垂直'''
        pb.setOrientation(Qt.Vertical)

        '''设置反向'''
        pb.setInvertedAppearance(True)

        '''设置展示文本(垂直了, 不展示文本)'''
        # pb.setTextVisible(True)
        pb.setTextVisible(False)

        '''设置展示文本方式'''
        pb.setTextDirection(QProgressBar.TopToBottom)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
