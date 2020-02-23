import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QObject


class Window(QWidget):
    y = 0
    obj0 = QObject()
    obj1 = QObject()
    obj2 = QObject()
    obj3 = QObject()
    obj4 = QObject()
    obj5 = QObject()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject对象的父子关系')
        self.resize(700, 800)
        self.setup_ui()

    def setup_ui(self):
        self._show_obj()
        self.QObject对象的父子关系()
        self.QObject读取父级对象()
        self.QObject根据条件查找子对象()

    def QObject对象的父子关系(self):
        '''创建多个QObject对象，将父子关系设置成以下关系
                obj1 - obj3
        obj0 <         obj4
                obj2 <
                       obj5
        '''
        self.obj1.setParent(self.obj0)  # 设置 obj1 的父级
        self.obj2.setParent(self.obj0)
        self.obj3.setParent(self.obj1)
        self.obj4.setParent(self.obj2)
        self.obj5.setParent(self.obj2)

        self._setup_label('QObject对象的父子关系: ', 0, 120)
        self._show_obj_tree(self.obj0)

    def QObject读取父级对象(self):

        self._setup_label('读取父级对象：', 0, 290)
        self._setup_label('obj0： %s' % (str(self.obj0)), 25, 310)
        self._setup_label('obj1： %s' % (str(self.obj1)), 25, 325)
        self._setup_label('obj1 的父级对象： %s' % (str(self.obj1.parent())), 25, 340)

    def QObject根据条件查找子对象(self):
        '''
        findChild(parmenter_1, parmenter_2, parmenter_3)  获取指定名称和类型的子对象（仅能获取符合条件的第一个子对象）
            parmenter_1: 类型或元组(元素为类型)
            parmenter_2: 名称，选填
            parmenter_3: 查找选项
                         Qt.FindChildrenRecursively -- 递归查找（默认选项）
                         Qt.FindDirectChildrenOnly -- 只查找一级子对象

        findChildren(parmenter_1, parmenter_2, parmenter_3)  与上方函数用法和意义都相同，只不过是可以查找到多个结果
        '''
        self.obj2.setObjectName('obj2')
        self.obj3.setObjectName('obj3')

        # obj6 = QLabel()
        # obj6.setParent(obj0)  # ✖ setParent(self, QWidget): argument 1 has unexpected type 'QObject'

        self._setup_label('QObject根据条件查找子对象:', 0, 380)
        self._setup_label('obj0： %s' % (str(self.obj0)), 25, 400)
        self._setup_label('obj1： %s' % (str(self.obj1)), 25, 425)
        self._setup_label('obj2： %s' % (str(self.obj2)), 25, 450)
        self._setup_label('查找 obj0 中是 QObject 的第一个子对象:  %s' % (self.obj0.findChild(QObject)), 25, 475)
        self._setup_label('查找 obj0 中是 QObject 类型并且名称为 "obj2" 的子对象： %s' % (self.obj0.findChild(QObject, 'obj2')), 25, 500)
        self._setup_label('查找 obj0 中是 QObject 类型并且名称为 "obj3" 的子对象： %s' % (self.obj0.findChild(QObject, 'obj3')), 25, 525)
        self._setup_label('查找 obj0 中是 QObject 的所有子对象:  %s' % (self.obj0.findChildren(QObject)), 25, 550)

    def _show_obj_tree(self, obj, level=1):
        '''展示对象继承关系树状图
        Args:
            obj: 父对象
            level: 当前层级
        '''
        self._setup_label(str(obj), level * 20, self.y)
        level += 1
        for child_obj in obj.children():  # obj.children() 获取对象的所有一级子对象
            self.y += 20
            self._show_obj_tree(child_obj, level)

    def _setup_label(self, text, x, y):
        '''更新对象间的继承关系'''
        label = QLabel(self)
        label.setText(text)
        label.move(x, y)

    def _show_obj(self):
        '''展示创建对象名称和id'''
        self._setup_label('obj0： %s' % (str(self.obj0)), 0, 0)
        self._setup_label('obj1： %s' % (str(self.obj1)), 0, 15)
        self._setup_label('obj2： %s' % (str(self.obj2)), 0, 30)
        self._setup_label('obj3： %s' % (str(self.obj3)), 0, 45)
        self._setup_label('obj4： %s' % (str(self.obj4)), 0, 60)
        self._setup_label('obj5： %s' % (str(self.obj5)), 0, 75)
        self.y = 140


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
