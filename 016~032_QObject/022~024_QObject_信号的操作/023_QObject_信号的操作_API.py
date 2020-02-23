'''
023-QObject-信号的操作-API
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QObject


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.QObject的信号操作_被释放时的信号()
        self.QObject的信号操作_被修改名称时的信号()
        self.QObject的信号操作_判断信号是否已被阻断()
        self.QObject的信号操作_信号阻断()
        self.QObject的信号操作_信号与槽取消连接()
        self.QObject的信号操作_获取信号连接的槽的数量()

    def QObject的信号操作_被释放时的信号(self):
        # 槽函数，下同
        # 在 destroyed 函数中，会传入一个类对象给槽函数，槽函数可以通过设置第一个参数来获取
        def destroy_slot(obj):
            print("obj被释放了(%s)" % (str(obj)))

        def destroy_self_slot():
            print("self.obj被释放了")

        # 当实例化一个 QObject 对象，并且这个对象是局部变量，那么执行完成后，局部变量就会被销毁。那么当打开窗时就会执行打印
        obj = QObject()
        obj.destroyed.connect(destroy_slot)

        # 当实例化一个 QObject 对象，并且这个对象绑定在了类对象中，只有类被销毁时这个对象才会被销毁，槽才会被执行，也就是关闭窗口时
        self.obj1 = QObject()
        self.obj1.destroyed.connect(destroy_self_slot)

    def QObject的信号操作_被修改名称时的信号(self):
        # 创建一个 QObject 对象，绑定一个修改名称的信号
        self.obj2 = QObject()
        self.obj2.objectNameChanged.connect(self._objectNameChanged_slot)

        # 修改一下名称，会触发槽函数
        self.obj2.setObjectName('xxx')

    def QObject的信号操作_判断信号是否已被阻断(self):
        '''
        下文中会有说明信号阻断函数，当信号被阻断后，信号即无法发出.
        signalsBlocked(self) 函数判断信号是否被阻断。

        返回值类型为布尔值，已阻断为 True，未阻断为 False。
        '''
        self.obj3 = QObject()
        self.obj3.objectNameChanged.connect(self._objectNameChanged_slot)
        print(self.obj2.signalsBlocked())  # 未被阻断，打印 False

    def QObject的信号操作_信号阻断(self):
        '''
        信号阻断函数

        blockSignals(self, bool)

        第二个参数传入布尔值，True表示阻断，False表示取消阻断(同判断信号阻断函数)
        '''
        self.obj4 = QObject()
        # 信号临时阻断
        self.obj4.blockSignals(True)
        print(self.obj4.signalsBlocked())  # 已被阻断，打印 True
        self.obj4.setObjectName('xx2')  # 不会触发槽函数

        self.obj4.blockSignals(False)
        print(self.obj4.signalsBlocked())  # 阻断已关闭，打印 False
        self.obj4.setObjectName('xx3')  # 会触发槽函数

    def QObject的信号操作_信号与槽取消连接(self):
        '''
        disconnect(信号) -- 将与信号连接的槽取消连接
        '''
        self.obj5 = QObject()
        self.obj5.objectNameChanged.connect(self._objectNameChanged_slot)

        self.obj5.objectNameChanged.disconnect()

        print(self.obj5.signalsBlocked())  # 取消连接，仅表示信号与槽的关联关系取消了，不表示信息不能发出，所以会打印出 False

        # 修改对象名称，测试信号与槽是否已经取消连接
        # 会触发信号，但是已经没有绑定的槽了，所以没有任何程序执行
        self.obj2.setObjectName('ooo')

    def QObject的信号操作_获取信号连接的槽的数量(self):
        '''
        receibers(self, PYQT_SIGNAL)
        第二个参数必须是信息对象
        返回内容就是信号连接的槽的数量，类型为 int
        '''
        self.obj6 = QObject()
        print(self.obj6.receivers(self.obj6.objectNameChanged))  # 0

        self.obj6.objectNameChanged.connect(self._objectNameChanged_slot)
        print(self.obj6.receivers(self.obj6.objectNameChanged))  # 1

    def _objectNameChanged_slot(self, name):
        '''
        objectNameChanged 的槽信号，第一个参数意思是修改后的对象名称(str)
        '''
        print("对象名称修改为%s" % (name))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
