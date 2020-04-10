'''
247-QDialog-信号

accepted()
finished(int result)
rejected()
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('247-QDialog-信号')
        self.resize(1000, 500)

        d = QDialog(self)

        btn1 = QPushButton(d)
        btn1.move(10, 10)
        btn1.setText('确认')
        btn1.clicked.connect(lambda: d.accept())

        btn2 = QPushButton(d)
        btn2.move(10, 60)
        btn2.setText('取消')
        btn2.clicked.connect(lambda: d.reject())

        btn3 = QPushButton(d)
        btn3.move(10, 110)
        btn3.setText('其他')
        btn3.clicked.connect(lambda: d.done(3))

        d.accepted.connect(lambda: print('点击了确认按钮'))
        d.rejected.connect(lambda: print('点击了取消按钮'))
        d.finished.connect(lambda val: print('点击了完成按钮', val))

        d.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
