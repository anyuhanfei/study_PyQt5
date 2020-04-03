'''
027-QObject-对象删除

obj.deleteLater()

删除一个对象时, 也会解除它与父对象之间的关系
deleteLater()并没有将对象立即销毁，而是向主消息循环发送了一个event，下一次主消息循环收到这个event之后才会销毁对象
这样做的好处是可以在这些延迟删除的时间内完成一些操作，坏处就是内存释放会不及时
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QObject


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('027_QObject_对象删除')
        self.resize(500, 500)

        self.index()

    def index(self):
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()

        obj1.setParent(self)
        obj2.setParent(obj1)
        obj3.setParent(obj2)

        obj1.destroyed.connect(lambda: print('obj1被释放'))
        obj2.destroyed.connect(lambda: print('obj2被释放'))
        obj3.destroyed.connect(lambda: print('obj3被释放'))

        # 使用 del 关键字释放对象
        # del obj2  # 因为 del obj2 仅仅是切断了 obj2 这个变量指向值的指针，指针没了，变量还是存在的

        obj2.deleteLater()  # 在释放对象时，会解除与父对象的关联，所以可以被释放
        # obj3 的释放是因为父类 obj2 已经被释放，当程序执行完毕时，临时变量被释放掉

        # 执行到这里，obj2 还未被释放，下面一行代码还是能打印出 obj1 的子对象
        # 并且此代码输出顺序在释放输出之前
        print(obj1.children())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
