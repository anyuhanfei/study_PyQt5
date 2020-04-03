'''
030-QObject-定时器-API
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QObject


class myObject(QObject):
    '''
    自定义一个继承自 QObject 的类，这样可以自定义 QObject 中的 timerEvent() 方法
    '''
    def timerEvent(self, evt):
        '''
        在这里写定时器执行的业务逻辑，第一个参数代表是定时器事件
        '''
        print(evt)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject_定时器_API')
        self.resize(700, 400)
        self.定时器()
        # self.关闭定时器()

    def 定时器(self):
        '''
        startTimer(self, p_int, timerType=None) -- 定时器，每隔指定时间就会执行对象中的 timerEvent 方法

        参数一：设定的时间，单位毫秒
        参数二：定时器的类型，精确度不同
        返回值：timer_id,定时器的唯一标识
        '''
        self.obj = myObject()  # 若在类中使用，记得绑定成类的对象
        self.timer_id = self.obj.startTimer(1000)

    def 关闭定时器(self):
        '''
        killTimer(self, p_int) -- 关闭定时器

        参数 p_int: timer_id
        '''
        self.obj.killTimer(self.timer_id)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
