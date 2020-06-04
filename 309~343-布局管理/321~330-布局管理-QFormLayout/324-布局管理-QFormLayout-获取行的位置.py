'''
324-布局管理-QFormLayout-获取行的位置

getWidgetPosition(self, QWidget)->Tuple[int, QFormLayout.ItemRole]
getLyaoutPosition(self, QLayout)->Tuple[int, QFormLayout, ItemRole]

rowCount()->int -- 行的总数


附:
    QFormLayout.ItemRole -- 角色
        QFormLayout.LabelRole -- 标签 0
        QFormLayout.FieldRole -- 输入框 1
        QFormLayout.SpanningRole -- 跨越标签和输入框的控件 2
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFormLayout, QPushButton, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('324-布局管理-QFormLayout-获取行的位置')
        self.resize(1000, 500)

        fl = QFormLayout()

        label_1 = QLabel('标签1')
        le_1 = QLineEdit()
        le_2 = QLineEdit()
        button = QPushButton('确认')

        fl.addRow(label_1, le_1)
        fl.addRow('标签2', le_2)
        fl.addRow(button)

        self.setLayout(fl)

        '''行数'''
        print(fl.rowCount())

        '''获取行位置'''
        print(fl.getWidgetPosition(le_1))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
