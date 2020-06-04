'''
309~310-布局管理-诞生背景

布局就是指按照某种规则将子控件摆放在父控件中

手动布局:
    直接给定具体的坐标信息和尺寸信息, 设置后, 后续如果不重新设置, 则一直不变.
    可以重写 resizeEvent(evt), 在内部, 根据父控件的尺寸大小的调整, 重新计算.

布局管理器:
    包含了一些特定的规则: 横着水平排, 竖着垂直排, 网格排, 表单排
    使用这些布局管理员进行布局, 可以快速的实现指定布局效果, 不需要手动计算位置尺寸
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('309~310-布局管理-诞生背景')
        self.resize(1000, 600)

        '''
        若在窗口中创建三个子控件, 这三个子控件垂直排列并占满窗口.

        一般来说, 为了实现这样的功能, 需要手动去计算每个控件的大小和位置.
        '''
        label1 = QLabel('标签1', self)
        label2 = QLabel('标签2', self)
        label3 = QLabel('标签3', self)
        label1.setStyleSheet('background-color: cyan;')
        label2.setStyleSheet('background-color: red;')
        label3.setStyleSheet('background-color: yellow;')

        # 计算位置和大小
        # label_width = self.width()
        # label_height = self.height() / 3
        # label1.resize(label_width, label_height)
        # label2.resize(label_width, label_height)
        # label3.resize(label_width, label_height)
        # label1.move(0, 0)
        # label2.move(0, label_height)
        # label3.move(0, label_height * 2)

        '''
        以上是通过手动计算子控件的位置和大小来控制子控件, 这就有一个问题, 当窗口动态改变大小时, 这些控件不会改变(当然, 这个问题可以通过窗口改变大小的信号来实现动态计算子控件的大小和位置)

        子控件数量改变, 其位置也要重新计算(这问题也可以解决).

        即使手动计算位置和大小也可以通过其他技术和功能实现动态控制大小和位置等等功能, 但是是不是感觉太过麻烦了.

        布局管理解决了以上手动计算子控件的位置和大小那些已表述的和未表述的问题和复杂实现.
        '''
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
