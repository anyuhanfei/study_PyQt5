'''
342~343-布局管理-尺寸策略

QWidget.sizeHint() -- 合适的建议大小

QWidget.minimumSizeHint() -- 最小的建议大小
    在layout中不会把一个控件的尺寸设置到比这个值还小, 除非手动设置了最小尺寸(setMinimumSize())和尺寸策略为lgnore

附:
    控件尺寸策略
        一个控件的大小策略会告诉布局系统应该如何对它进行拉伸或收缩
        Qt为它所有的内置控件都提供了合理的默认大小策略值

        一个QSizePolicy包括:水平方向(策略, 拉伸系数), 垂直方向(策略, 拉伸系数)

        策略取值:
            QSizePolicy.Fixed -- widget 的实际尺寸只参考 sizeHint() 的返回值, 不能伸展 (grow) 和收缩 (shrink)
            QSizePolicy.Minimum -- 可以伸展和收缩, 不过 sizeHint() 的返回值规定了 widget 能缩小到的最小尺寸
            QSizePolicy.Maximum -- 可以伸展和收缩, 不过 sizeHint() 的返回值规定了 widget 能伸展到的最大尺寸
            QSizePolicy.Preferred -- 可以伸展和收缩, 但没有优势去获取更大的额外空间使自己的尺寸比 sizeHint() 的返回值大
            QSizePolicy.Expanding -- 可以伸展和收缩, 它会尽可能多地去获取额外的空间, 也就比 Preferred 更具优势
            QSizePolicy.MinimumExpanding -- 可以伸展和收缩, 不过 sizeHint() 的返回值规定了 widget 能缩小到的最小尺寸, 它比 Preferred 更具优势去获取额外空间
            QSizePolicy.lgnore -- 忽略 sizeHint() 的作用

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('342~343-布局管理-尺寸策略')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
