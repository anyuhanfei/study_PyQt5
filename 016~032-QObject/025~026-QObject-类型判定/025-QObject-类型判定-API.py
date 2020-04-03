'''
025-QObject-类型判定-API

可以判定一个对象是否是一个控件，也可以判定这个对象是否是继承某个类(包括直接和间接继承)；

主要用于判定和筛选控件
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtCore import QObject


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('025_QObject_类型判定_API')
        self.resize(700, 800)
        self.set_ui()

    def set_ui(self):
        self.QObject类型判定()

    def QObject类型判定(self):
        obj = QObject()
        w = QWidget()
        btn = QPushButton()
        label = QLabel()

        pyqt_dict = {'QObject': obj, 'QWidget': w, 'QPushButton': btn, 'QLabel': label}

        '''
        obj.isWidgetType -- 判断对象是否是控件
        '''
        y = 10
        for key, value in pyqt_dict.items():
            for_l = QLabel(self)
            for_l.setText('%s 是否是控件: %s' % (key, value.isWidgetType()))
            for_l.move(10, y)
            y += 30

        '''
        obj.inherits(p_str) -- 判断对象是否继承自某个类

        参数一表示与 类名相同的字符串类型 的数据
        '''
        y = 200
        for key, value in pyqt_dict.items():
            for_l = QLabel(self)
            for_l.setText('%s 是否继承自 QWidget: %s' % (key, value.inherits('QWidget')))
            for_l.move(10, y)
            y += 30


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
