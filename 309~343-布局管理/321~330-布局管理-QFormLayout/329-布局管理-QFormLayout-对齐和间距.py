'''
329-布局管理-QFormLayout-对齐和间距

对齐方式:
    setFormAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) -- 设置表单的对齐方式
    formAlignment(self)->Qt.Alignment -- 获取表单的对齐方式
    setLabelAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) -- 设置标签的对齐方式
    labelAlignment(self)->Qt.Alignment -- 获取标签的对齐方式
间距:
    setVerticalSpacing(int) -- 设置垂直方向的间距
    verticalSpacing()->int -- 获取垂直方向的间距
    setHorizontalSpacing(int) -- 设置水平方向的间距
    horizontalSpacing()->int -- 获取水平方向的间距
    spacing()->int
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QFormLayout
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('329-布局管理-QFormLayout-对齐和间距')
        self.resize(1000, 500)

        fl = QFormLayout()
        fl.addRow('标签1', QLineEdit())
        fl.addRow('标签2', QLineEdit())

        '''设置对齐方式'''
        fl.setFormAlignment(Qt.AlignRight | Qt.AlignTop)

        '''设置间距'''
        fl.setVerticalSpacing(40)
        fl.setHorizontalSpacing(400)

        self.setLayout(fl)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
