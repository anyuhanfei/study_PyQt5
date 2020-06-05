'''
352~354-QSS-伪状态

限制状态只能在某种状态下, 被样式表作用

语法:
    选择器:伪状态

常见伪状态
    :checked -- button 控件被选中
    :unchecked -- button 控件未被选中
    :hover -- 控件被鼠标放在上面
    :pressed -- 控件被按下
    :focus -- 控件获取焦点
    :disable -- 控件失效
    :enable -- 控件有效
    :indeterminate -- checkBox 或者 radioButton 被部分选中
    :on -- 控件处于 on 状态
    :off -- 控件处于 off 状态

注意:
    不同的控件可能有某种特定的伪状态, 无法通用, 具体查看官方文档
    ! 可以否定
    可以连接使用
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('352~354-QSS-伪状态')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
