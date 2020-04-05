'''
202-QSpinBox-进制设置

控制文本框内容的显示基数, 以几进制的形式进行展示

API:
    setDisplayIntegerBase(int) -- 设置进制(默认是10进制)
    displayIntegerBase() -> int -- 获取进制

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('202-QSpinBox-进制设置')
        self.resize(1000, 500)

        sb = QSpinBox(self)

        '''显示基数'''
        # 设置
        sb.setDisplayIntegerBase(2)
        # 获取
        print('当前进制数:', sb.displayIntegerBase())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
