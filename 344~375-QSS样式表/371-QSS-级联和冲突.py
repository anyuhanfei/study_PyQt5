'''
371-QSS-级联和冲突

级联:
    QSS 可以在 QApplication, 父控件, 子控件中设置
    一个控件的最终样式, 会受到父控件和 QApplication 的影响
冲突:
    如果一个控件, 作为后代控件, 被多个祖先控件影响, 则会不同属性产生叠加, 相同属性产生覆盖
    特异性强的优先级高(也就是指令包含的控件越少特异性越高)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('371-QSS-级联和冲突')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
