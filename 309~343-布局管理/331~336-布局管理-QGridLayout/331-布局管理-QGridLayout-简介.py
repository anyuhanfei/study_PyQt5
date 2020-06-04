'''
331-布局管理-QGridLayout-简介

网格布局, 取可用空间(通过其父布局或parentWidget()), 将其划分为行和列
并将其管理的每个窗口小控件放入正确的单元格中.
每列/行具有最小宽度和拉伸系数. 最小宽度是使用 set xxx MinimumVidth(), 拉伸因子使用 set xxx Stretch()

构造函数:
    QGridLayout(QWidget)
    QGridLayout()

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('331-布局管理-QGridLayout-简介')
        self.resize(1000, 600)

        gl = QGridLayout()

        label_1 = QLabel()
        label_1.setStyleSheet('background-color: red;')
        label_2 = QLabel()
        label_2.setStyleSheet('background-color: yellow;')
        label_3 = QLabel()
        label_3.setStyleSheet('background-color: blue;')

        gl.addWidget(label_1)
        gl.addWidget(label_2)
        gl.addWidget(label_3)

        self.setLayout(gl)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
