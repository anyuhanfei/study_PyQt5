'''
020-QObject-对象的继承-Qt内存管理机制

QObject 继承树：
    所有的对象都是直接或间接的继承自 QObject；
    QObjects 在一个对象树中组织他们自己： 当创建一个 QObject 时，如果使用了其他对象作为其父对象，那么，它就会被添加到父对象的 children() 列表中；
    当父对象被销毁时，这个 QObject 也会被销毁；

QWidget:
    扩展了父子关系；
    当一个控件设置了父控件：
        会包含在父控件内部；
        受父控件区域裁剪；
        父控件被删除时，子控件也会被删除；
    场景案例：
        一个对话框，上面有很多对话按钮(确定，取消)，对话框和按钮就是父子控件关系。我们操作的时候，是操作的对话框控件本身，而不是其内部的子控件。当对话框删除时，内部的子控件也会自动删除；
'''
import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QObject


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.Qt内存管理机制_直接释放父对象()
        time.sleep(0.3)
        print()
        self.Qt内存管理机制_手动释放父对象()
        time.sleep(0.3)
        print()
        self.Qt内存管理机制_不释放父对象()

    def Qt内存管理机制_直接释放父对象(self):
        '''代码执行完成后就会释放'''
        obj1 = QObject()
        obj2 = QObject()
        obj2.setParent(obj1)

        obj2.destroyed.connect(lambda: print('直接释放父对象: obj2对象已经被释放'))  # 监听 obj2 对象被释放信号

    def Qt内存管理机制_不释放父对象(self):
        '''将在程序关闭是释放所有对象'''
        self.obj1 = QObject()
        obj2 = QObject()
        obj2.setParent(self.obj1)

        obj2.destroyed.connect(lambda: print('不释放父对象: obj2对象已经被释放'))

    def Qt内存管理机制_手动释放父对象(self):
        '''程序执行到删除时父对象时，子对象将被释放'''
        self.obj1 = QObject()
        obj2 = QObject()
        obj2.setParent(self.obj1)

        obj2.destroyed.connect(lambda: print('手动释放父对象: obj2对象已经被释放'))

        print('释放 obj1')
        del self.obj1


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
