'''
288-QLCDNumber-显示数据和位数限制

设置显示数值:
    display(str)
    display(float)
    display(int)
    intValue() -> int
    value() -> float
位数限制:
    setDigitCount(int)
    digitCount() -> int

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('288-QLCDNumber-显示数据和位数限制')
        self.resize(1000, 500)

        lcdn = QLCDNumber(self)
        lcdn.move(10, 10)
        lcdn.resize(300, 40)

        '''位数限制(与构造函数有 int 参数的那种方法作用相同)'''
        # 展示字符串, 超出位数会将最前面的字符串踢出
        # 展示数字, 超出位数会显示为 0
        # 展示浮点型数字, 整数部分超出位数则显示为 0, 浮点数部分超出位数会四舍五入
        lcdn.setDigitCount(20)

        '''设置数值(英文大小写都一样)'''
        lcdn.display("aBCDEFHhlopruUYgS:'")  # 英文字母展示必须设置位数限制, 而且是在设置数值之前


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
