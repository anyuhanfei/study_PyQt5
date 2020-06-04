'''
314-布局管理-基类-QLayout

布局管理器的抽象类

功能作用:
    子控件间的间距:
        setSpacing(int)
        spacing()->int
    外边距:
        setContentsMargins(int left, int top, int right, int bottom)
        contentsMargins() -> obj :
            contentsMargins().top() -- 顶部的外边距(其他方向类似)
    添加子控件:
        addWidget(QWidget w)
    替换子控件:
        replaceWidget(QWidget * from, QWidget * to, Qt.FindChildOption)
        注意: 被替换的子控件不再被布局管理器管理, 需要手动隐藏删除等操作
    添加子控件:
        addLayout(QLayout layout)
    能用性(false失效):
        isEnabled() -> bool
        setEnabled(bool)


QBoxLayout:
    提供水平或垂直方向的布局管理器
    构造函数:
        QBoxLayout(QBoxLayout.Diretion, parent: QWidget = None)
    附:
        QBoxLayout.Diretion:
            QBoxLayout.LeftToRight -- 从左到右水平
            QBoxLayout.RightToLeft -- 从右到左水平
            QBoxLayout.TopToBottom -- 从上到下垂直
            QBoxLayout.BottomToTop -- 从下到上垂直
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QBoxLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('314-布局管理-基类-QLayout')
        self.resize(1000, 500)

        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label4 = QLabel('标签4')
        label1.setStyleSheet('background-color: cyan;')
        label2.setStyleSheet('background-color: red;')
        label3.setStyleSheet('background-color: yellow;')
        label4.setStyleSheet('background-color: blue;')

        '''想在子控件中间添加一个横排的布局管理前'''
        label5 = QLabel('标签5')
        label6 = QLabel('标签6')
        label5.setStyleSheet('background-color: pink;')
        label6.setStyleSheet('background-color: green;')

        layout_s = QBoxLayout(QBoxLayout.LeftToRight)
        layout_s.addWidget(label5)
        layout_s.addWidget(label6)

        layout = QBoxLayout(QBoxLayout.BottomToTop)
        layout.addWidget(label1)
        layout.addLayout(layout_s)
        layout.addWidget(label2)
        layout.addWidget(label3)

        '''替换
        4 替换到 2 上, 2需要被处理, 这里被添加到布局中了
        '''
        layout.replaceWidget(label2, label4)
        layout.addWidget(label2)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
