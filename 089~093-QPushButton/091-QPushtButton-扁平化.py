'''
091-QPushButton-扁平化

扁平化：去掉了边框，看着就像是 QLabel 控制这样的文本，但是保留了按钮的所有功能，仅仅是样式上的改变

同时不会绘制背景颜色

API:
    isFlat() -- 获取当前按钮边框是否扁平
    setFlat(bool) -- 设置按钮边框扁平化，默认值为False
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel


class Window(QWidget):
    widget = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('091_QPushButton_扁平化')
        self.resize(1000, 500)

        self.btn = QPushButton(self)
        self.btn.setText('xxx')
        self.btn.move(10, 10)

        '''设置为扁平化'''
        self.btn.setFlat(True)

        '''检验是否可以绘制背景颜色'''
        self.btn.setStyleSheet('background-color: red;')

        '''是否是扁平化'''
        btn_is_flat = self.btn.isFlat()

        label = QLabel(self)
        label.setText('按钮是否是扁平化的：%s' % (btn_is_flat))
        label.move(10, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
