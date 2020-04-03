'''
081-QAbstractButton-图标设置

图标设置的 API ：
    setIcon(QIcon(image_path)) -- 设置图标(QSize() 方法在 PyQt5.QtGui 类中)
    setIconSize(QSize(w, h)) -- 设置图标大小(QIcon() 方法在 PyQt5.QtCore 类中)
     () -- 获取图标
    iconSize() -- 获取图标大小
'''

import sys


from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('081_QAbstractButton_图标设置')
        self.resize(500, 500)

        self.btn = QPushButton(self)
        self.btn.resize(60, 100)

        '''设置按钮图标'''
        # 设置一个图标对象
        icon_obj = QIcon('./xxx.png')
        # 将图标对象设置为按钮图标
        self.btn.setIcon(icon_obj)

        '''设置按钮图标大小'''
        # 创建尺寸对象
        size_obj = QSize(60, 100)
        self.btn.setIconSize(size_obj)

        '''读取按钮图标信息'''
        # 获取图标对象
        icon_obj_get = self.btn.icon()

        self.label_one = QLabel(self)
        self.label_one.move(5, 110)
        self.label_one.setText('图标对象：' % (str(icon_obj_get)))

        # 获取图标尺寸对象
        icon_size_get = self.btn.iconSize()

        self.label_two = QLabel(self)
        self.label_two.move(5, 140)
        self.label_two.setText('图标尺寸对象：%s' % (str(icon_size_get)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
