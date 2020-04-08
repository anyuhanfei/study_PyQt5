'''
226-QComboBox-数据的限制

API:
    setMaxCount(int max) -- 设置最大数量 (超出不新增, 而不是移除旧的)
    maxCount() -- 获取最大数量
    setMaxVisibleItems(int maxItems) -- 设置可见的最大条目个数
    maxVisibleItems() -- 获取可见的最大条目个数
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QComboBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('226-QComboBox-数据的限制')
        self.resize(1000, 500)

        cb = QComboBox(self)
        cb.move(10, 10)
        cb.addItems(['1', '2', '3', '4', '5'])

        '''最大数量设置'''
        cb.setMaxCount(4)
        print('最大数量设置:', cb.maxCount())

        '''可见的最大条目个数'''
        cb.setMaxVisibleItems(2)
        print('可见的最大条目个数:', cb.maxVisibleItems())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
