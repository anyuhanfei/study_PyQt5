'''
103-QRadioButton-多组互斥

若需要多组单选按钮，现阶段可以创建空白的 widget 控件，然后每组都继承一个这样的控件。在不同的父控件下，组与组之间单选按钮就不会互斥了。
(不是最优解，仅仅是现学习阶段的一个通过逻辑来解决问题的方法)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('103_QRadioButton_多组互斥')
        self.resize(1000, 500)

        '''初始化两组单选按钮'''
        # 若仅仅写以下代码，那么这四个单选按钮将互斥，这不是想要的结果
        rb_man = QRadioButton('男', self)
        rb_woman = QRadioButton('女', self)
        rb_man.move(10, 10)
        rb_woman.move(70, 10)

        rb_yes = QRadioButton('yes', self)
        rb_no = QRadioButton('no', self)
        rb_yes.move(10, 50)
        rb_no.move(70, 50)

        '''将每组单选按钮的父控件分离'''
        widget_sex = QWidget(self)
        widget_sex.resize(150, 100)
        widget_sex.move(0, 0)
        widget_judge = QWidget(self)
        widget_judge.resize(150, 100)
        widget_judge.move(0, 100)

        rb_man.setParent(widget_sex)
        rb_woman.setParent(widget_sex)
        rb_yes.setParent(widget_judge)
        rb_no.setParent(widget_judge)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
