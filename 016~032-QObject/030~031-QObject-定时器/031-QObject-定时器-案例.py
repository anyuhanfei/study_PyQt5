'''
031-QObject-定时器-案例

1. 创建一个窗口, 并设置一个子控件QLabel
    展示10s倒计时
    倒计时结束, 就停止计时

2. 创建一个窗口, 通过定时器不断增加该窗口的尺寸大小
    每100ms 宽高均增加1px
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyLabel(QLabel):
    '''
    完全自定义的 label 子控件，好处是在使用时仅仅需要实例化就可以使用了，坏处就是如果需要更改功能或者想要更灵活的使用，比如控制倒计时时间、控制定时器开始的时机。

    一些解决方法：
        将需要控制的功能和属性开放接口
    '''
    def __init__(self, *args, **kwargs):
        '''
        因为在使用控件时，会在实例化时传参(最常见的就是指定父类)，但是自定义不能处理这些内容，那么只能接收这些参数，然后原封不动的传给父类
        '''
        super().__init__(*args, **kwargs)

        # 这里设置控件属性和功能
        self.setText('10')
        self.move(100, 100)
        self.timer_id = self.startTimer(1000)

    def timerEvent(self, *args, **kwargs):
        # 获取当前标签内容
        current_sec = self.text()
        res_sec = str(int(current_sec) - 1)
        # 修改显示内容
        self.setText(res_sec)
        # 到 0 停止
        if int(res_sec) <= 0:
            self.killTimer(self.timer_id)


class Window(QWidget):
    width = 500
    height = 400

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject_定时器_API')
        self.resize(self.width, self.height)
        self.案例一()
        self.案例二()

    def 案例一(self):
        # 创建一个带有定时器的 label 控件，最好的办法是创建一个 label 子类，然后将 label 控件的所有属性和功能完善，使用时仅仅需要实例化(目前来讲最好的方法)
        MyLabel(self)

    def 案例二(self):
        # 设置宽高属性来解决当前宽高的获取问题，在类中重写 timerEvent() 方法来实现窗口增大，设置每 100ms 执行一次的定时器
        self.startTimer(100)

    def timerEvent(self, *args, **kwargs):
        self.width += 1
        self.height += 1
        self.resize(self.width, self.height)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
