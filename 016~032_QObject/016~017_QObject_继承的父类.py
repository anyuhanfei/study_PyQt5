import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QObject


class Window(QWidget):
    x = 0
    y = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject-继承的父类')
        self.resize(700, 400)
        self.setup_ui()

    def setup_ui(self):
        self.QObject继承结构测试()
        self.QObject对象名称和属性操作()

    def QObject继承结构测试(self):
        self.x = 0

        self._setup_label('查看 QObject 的继承结构:')

        mros = QObject.mro()
        self.x += 20
        for mro in mros:
            self._setup_label(str(mro), 0, 15)

    def QObject对象名称和属性操作(self):
        self.x = 0

        # 设置和读取名称
        obj = QObject()
        obj.setObjectName('测试')

        self._setup_label('QObject对象名称: %s' % (obj.objectName()), 0, 30)

        # 设置和读取属性（相当于类属性或字典，键值对形式）
        obj.setProperty('notice_one_level', 'error')
        obj.setProperty('notice_two_level', 'warning')

        self._setup_label('读取 QObject 对象中已经设置的属性：', 0, 30)
        self._setup_label(obj.property('notice_one_level'), 20, 15)
        self._setup_label(obj.property('notice_two_level'), 0, 15)

        # 读取属性名（键名）
        self.x = 0
        self._setup_label('当前所有属性名：', 0, 30)
        self._setup_label(str(obj.dynamicPropertyNames()), 20, 15)

    def _setup_label(self, content, x=0, y=0):
        '''设置一个标签'''
        if x != 0:
            self.x += x
        if y != 0:
            self.y += y
        labels = QLabel(self)
        labels.setText(content)
        labels.move(self.x, self.y)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
