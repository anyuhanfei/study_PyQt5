'''
079_QAbstactButton_子类化抽象类
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QAbstractButton


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('079_QAbstactButton_子类化抽象类')
window.resize(500, 500)

'''无法直接使用 QAbstractButton'''
# btn = QAbstractButton(window)
# TypeError: PyQt5.QtWidgets.QAbstractButton represents a C++ abstract class and cannot be instantiated


'''必须创建一个继承 QAbstractButton 的子类才能使用 QAbstractButton 类'''


class MyButton(QAbstractButton):
    '''继承 QAbstractButton 的按钮子类
    必须重构 paintEvent() 方法，否则会报错：
        NotImplementedError: QAbstractButton.paintEvent() is abstract and must be overridden
    '''
    def paintEvent(self, evt):
        '''绘制方法
        视频中举了一个简单的例子，因为后面课程会系统教学，这里没有去细细学习
        '''
        print('绘制按钮')


btn = MyButton(window)
# 测试按钮是否存在
btn.pressed.connect(lambda: print('点击了按钮'))

window.show()

sys.exit(app.exec_())
