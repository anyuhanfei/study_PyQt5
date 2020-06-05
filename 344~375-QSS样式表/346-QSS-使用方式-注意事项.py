'''
346-QSS-使用方式-注意事项

在实际开发中, 一般不会再这里写 qss 样式, 原因是当控件过多时会太过混乱, 可以通过读取文件的方式来加载 qss 文件
甚至可以将加载 qss 文件这步操作封装成一个工具类或工具方法

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication

from Tools import Tools


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('346-QSS-使用方式-注意事项')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    Tools.set_qss_to_obj('./text.qss', app)

    sys.exit(app.exec_())
