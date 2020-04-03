'''
094-QCommandLinkButton-使用

命令链接是 Windows Vista 引入的新控件

它的用途类似于单选按钮的用途，因为它用于在一组互斥选项之间进行选择

命令链接按钮不应单独使用，而应作为向导和对话框中单选按钮的替代选项

外观通常类似于平面按钮的外观，但除了普通按钮文本之外，它还允许描述性文本
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCommandLinkButton
from PyQt5.QtGui import QIcon


class Window(QWidget):
    widget = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('094_QCommandLinkButton_使用')
        self.resize(1000, 500)

        clb = QCommandLinkButton(self)
        # clb = QCommandLinkButton('标题', self)
        # clb = QCommandLinkButton('标题', '描述', self)

        '''设置标题'''
        clb.setText('标题')
        '''设置描述'''
        clb.setDescription('描述')
        '''获取描述'''
        print(clb.description())
        '''修改图标'''
        icon = QIcon('./xxx.png')
        clb.setIcon(icon)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
