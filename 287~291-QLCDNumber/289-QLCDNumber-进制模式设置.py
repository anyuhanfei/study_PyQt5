'''
289-QLCDNumber-进制模式设置

限制展示的进制, 仅仅是展示, 通过 value() 方法获取时依旧是正常数据

API:
    setMode(self, QLCDNumber.Mode)
    mode(self) -> QLCDNumber.Mode

附:
    QLCDNumber.Mode
        QLCDNumber.Hex -- 十六进制 -- setHexMode()
        QLCDNumber.Dec -- 十进制 -- setDecMode()
        QLCDNumber.Oct -- 八进制 -- setOctMode()
        QLCDNumber.Bin -- 二进制 -- setBinMode()

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('289-QLCDNumber-进制模式设置')
        self.resize(1000, 500)

        lcdn = QLCDNumber(20, self)
        lcdn.move(10, 10)
        lcdn.resize(300, 40)

        lcdn.display(204)

        '''设置进制'''
        lcdn.setMode(QLCDNumber.Bin)  # 二进制


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
