'''
327-布局管理-QFormLayout-标签获取

通过右边的控件或布局来获取左边的标签, 这样做的原因是因为在添加时, 左边的标签控件可以通过字符串直接添加, 这样无法获取, 进而无法修改

labelForField(self, QWidget)->QWidget
labelForField(self, QLayout)->QWidget


'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFormLayout, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('327-布局管理-QFormLayout-标签获取')
        self.resize(1000, 500)

        le = QLineEdit()

        fl = QFormLayout()

        fl.addRow('标签', le)

        self.setLayout(fl)

        label = fl.labelForField(le)
        label.setText('xxx')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
