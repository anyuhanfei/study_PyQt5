'''
285-QLabel-内容操作

API:
    文本字符串:
        text() -> str -- 获取文本
        setText(QString) -- 设置文本
    数值数据:
        setNum(int num) -- 设置整型数值
        setNum(double num) -- 设置浮点型数值
    图形图像:
        setPicture(QPicture) -- 设置绘画
        picture() -> QPicture -- 获取绘画
        setPixmap(QPixmap) -- 设置图片
        pixmap() -> QPixmap -- 获取图片
    动图:
        setMovie(QMovie movie)
        movie() -> QMovie -- 此类用于显示没有声音的简单动画
    清空:
        clear()

附:
    QMovie
        setScaledSize(QSize)
        setPaused(bool) -> void
        setSpeed(int percentSpeed) -- 加速(100正常)
        start() -- 开始
        stop() -- 暂停
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPicture, QPainter, QBrush, QColor, QMovie


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('285-QLabel-内容操作')
        self.resize(1000, 500)

        label = QLabel(self)
        label.move(10, 10)

        '''绘画'''
        pic = QPicture()
        painter = QPainter(pic)
        painter.setBrush(QBrush(QColor(100, 200, 100)))
        painter.drawEllipse(0, 0, 200, 200)

        label.setPicture(pic)

        label2 = QLabel(self)
        label2.move(10, 250)

        '''动图'''
        movie = QMovie('xxx.gif')
        label2.setMovie(movie)

        movie.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
