'''
281-QLabel-小伙伴

在自身上绑定一个快捷键, 当设置了一个伙伴控件后, 按下快捷键, 这个伙伴控件就会得到焦点.

QLabel 绑定快捷键必须设置伙伴控件后才会有效果

按下 alt 键后, QLabel 的快捷键那个字母下会出现下划线, 在按钮这个键, 伙伴控件就会得到焦点

API:
    buddy() -> QWidget
    setBuddy(QWidget buddy)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('281-QLabel-小伙伴')
        self.resize(1000, 500)

        label = QLabel(self)
        label.setText('输入(&s):')
        label.move(10, 10)

        le = QLineEdit(self)
        le.move(100, 10)

        le2 = QLineEdit(self)  # 转移焦点用
        le2.move(400, 10)

        '''设置伙伴控件'''
        label.setBuddy(le)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
