'''
294-QProgressBar-文本格式设置

API:
    setFormat(self, str) -- 设置文本,
        其中有一些特殊字符:
            %p -- 百分比
            %v -- 当前值
            %m -- 总值
    format() -> str -- 获取文本
    resetFormat() -- 重置文本
    setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) -- 格式字符对齐方式

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('294-QProgressBar-文本格式设置')
        self.resize(1000, 500)

        pb = QProgressBar(self)
        pb.move(10, 10)
        pb.resize(400, 40)
        pb.setValue(40)

        '''设置文本'''
        pb.setFormat('%v/%m (当前值/总值)')

        '''设置字符对齐方式'''
        pb.setAlignment(Qt.AlignHCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
