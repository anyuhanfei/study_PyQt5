'''
325-布局管理-QFormLayout-设置行

setLayout(self, int, QFormLayout.ItemRole, QLayout)
setWidget(self, int, QFormLayout.ItemRole, QWidget)

注意:
    根据行号和角色, 设置相关控件或布局, 如果有必要会延长布局
    如果单元格已被占用, 则不会设置成功 (包括占据整行)

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFormLayout, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('325-布局管理-QFormLayout-设置行')
        self.resize(1000, 500)

        label_1 = QLabel('标签1')
        label_2 = QLabel('标签2')
        le_1 = QLineEdit()
        le_2 = QLineEdit()

        fl = QFormLayout()

        fl.setWidget(0, QFormLayout.LabelRole, label_1)
        fl.setWidget(0, QFormLayout.FieldRole, le_1)

        '''设置一个右边的行'''
        fl.setWidget(1, QFormLayout.FieldRole, le_2)

        '''设置一个单元格占用'''
        fl.setWidget(0, QFormLayout.LabelRole, label_2)

        self.setLayout(fl)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
