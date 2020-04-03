'''
054-QWidget-父子关系-案例

创建一个窗口，包含若干个 label 控件
    点击哪个 label 控件，就让哪个 label 控件的背景变红
    要使用父控件处理，不要自定义 QLabel 子类
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('053_QWidget_父子关系_API')
        self.resize(500, 500)
        self.move(200, 200)

        self.create_labels(10)

    def create_labels(self, number):
        for i in range(0, number):
            label = QLabel(self)
            label.move(10, 30 * i + 10)
            label.setText('label %s' % (i))

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()

        child_label = self.childAt(x, y)
        if child_label is not None:
            child_label.setStyleSheet('background-color: red;')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
