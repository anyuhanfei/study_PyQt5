'''
365~367-QSS-声明-背景属性

属性:
    background-color -- 背景颜色, 可以填写颜色单词, 也可以使用 rgb, 也可以使用 16 位的颜色符(#FFFFFF)
    background-image -- 背景图片, 例: url('./xxx.png')
    background-repeat -- 重复填充, no-repeat 不重复填充, repeat-x, repeat-y 单方向重复填充, repeat-xy 两个方向都重复填充
    background-position -- 对齐方式, top, left, right, bottom, 使用多个需要空格隔开
    background-origin -- 位置参照, padding (默认)内边距, content 内容, border 边框
    background-clip -- 裁剪, padding 裁剪内边距的背景, content 裁剪内容中的背景, border 裁剪外边距的背景
    background-attachment -- 是否跟随控件多余部分滚动而滚动, scroll (默认)滚动, fixed 不滚动, 适用于多行文本编辑器
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('365~367-QSS-声明-背景属性')
        self.resize(1000, 500)

        self.btn = QPushButton(self)
        self.btn.move(10, 10)
        self.btn.resize(33, 43)
        self.btn.setStyleSheet("""
            background-image: url('./puke.png');
            background-origin: content;
            background-clip: padding;

            padding-left: -69px;
            padding-top: -182px;
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
