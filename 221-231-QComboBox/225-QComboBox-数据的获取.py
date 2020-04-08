'''
225-QComboBox-数据的获取

API:
    count() -> int -- 条目总数
    itemIcon(int index) -> QIcon -- 指定条目的图标
    itemText(int index) -> str -- 指定条目的内容
    itemData(int index) -> Any -- 指定条目的数据
    currentIndex() -> int -- 当前的索引
    currentText() -> str -- 当前的内容
    currentData() -> any -- 当前的数据
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QComboBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('225-QComboBox-数据的获取')
        self.resize(1000, 500)

        cb = QComboBox(self)
        cb.addItems(['a', 'b', 'c', 'd'])
        cb.setItemData(2, {"age": "18"})
        cb.setItemData(3, {"name": "anyuhanfei"})
        cb.setCurrentIndex(2)

        '''条目总数'''
        print('条目总数:', cb.count())

        '''指定条目的内容'''
        print('指定条目的内容:', cb.itemText(3))

        '''指定条目的数据'''
        print('指定条目的数据:', cb.itemData(3))

        '''当前的索引'''
        print('当前的索引:', cb.currentIndex())

        '''当前的内容'''
        print('当前的内容:', cb.currentText())

        '''当前的数据'''
        print('当前的数据:', cb.currentData())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
