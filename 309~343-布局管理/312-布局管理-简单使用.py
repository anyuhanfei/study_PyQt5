'''
312-布局管理-简单使用

1.创建布局对象: 不需要设置父对象

2. 设置布局对象参数:
    setContentsMargins(self, int, int, int, int) -- 设置外边距
    setSpacing(self, int) -- 设置内边距
    setAlignment(self, QWidget, Union[Qt.Alignment, Qt.AlignmentFlag]) -- 对齐方式
    setAlignment(self, QLayout, Union[Qt.Alignment, Qt.AlignmentFlag])
    setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag])

3. 设置给需要布局子控件的父空间或调整方向:
    QWidget.setLayout(QLayout)
    QWidget.setLayoutDirection(Qt.RightToLeft)
        Qt.LeftToRight -- 从左到右
        Qt.RightToLeft -- 从右到左
        Qt.LayoutDirectionAuto -- 自动布局
    QWidget.unsetLayoutDirection()

4. 将布局控件内部的子控件添加到布局管理器中, 自动进行布局. 注意:创建子控件时, 不需要设置父控件
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('312-布局管理-简单使用')
        self.resize(1000, 500)

        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color: cyan;')
        label2.setStyleSheet('background-color: red;')
        label3.setStyleSheet('background-color: yellow;')

        layout = QHBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        '''设置外边距'''
        layout.setContentsMargins(50, 60, 70, 80)
        '''设置内边距'''
        layout.setSpacing(50)
        '''设置排序方式'''
        self.setLayoutDirection(Qt.RightToLeft)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
