'''
317-布局管理-基类-QBoxLayout-添加空白

相当于一个空白的控件, 占位置

添加空白:
    addSpacing(self, int)
    insertSpacing(self, int, int)  -- 插入空白

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QBoxLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('317-布局管理-基类-QBoxLayout-添加空白')
        self.resize(1000, 500)

        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color: cyan;')
        label2.setStyleSheet('background-color: red;')
        label3.setStyleSheet('background-color: yellow;')

        self.layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.layout.addWidget(label1)
        self.layout.addSpacing(100)  # 包含内间距
        self.layout.addWidget(label2)
        self.layout.addWidget(label3)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
