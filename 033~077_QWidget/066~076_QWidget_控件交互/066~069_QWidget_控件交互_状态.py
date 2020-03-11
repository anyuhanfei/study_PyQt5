'''
066~069_QWidget_控件交互_状态
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('066~069_QWidget_控件交互_状态')
        self.resize(700, 700)
        self.move(500, 500)

        '''禁用'''
        btn_one = QPushButton(self)
        btn_one.setEnabled(False)  # True 正常  False 禁用
        btn_one.move(10, 10)
        label_one = QLabel(self)
        label_one.move(60, 15)
        label_one.setText('<-当前按钮是禁用状态')

        '''是否可见
        obj.setVisible(bool)  设置是否可见
        obj.setHidden(bool)  设置是否隐藏

        控件类中的 paintEvent() 即绘制方法
        '''
        btn_two = QPushButton(self)
        btn_two.setVisible(False)  # True 可见  False 隐藏
        btn_two.move(10, 50)
        label_two = QLabel(self)
        label_two.move(60, 55)
        label_two.setText('<-当前按钮是隐藏状态')

        '''判断是否随父控件的显示而显示
        如果能随着widget控件的显示和隐藏, 而同步变化, 则返回True
        '''
        btn_three = QPushButton(self)  # 如果不设置显示状态，就是随父控件同步变化
        btn_three.move(10, 90)
        label_three = QLabel(self)
        label_three.move(60, 95)
        label_three.setText('<-当前按钮是跟随父类显示而显示')

        '''获取控件最终状态是否可见'''
        btn_four = QPushButton(self)
        btn_four.move(10, 130)
        label_four = QLabel(self)
        label_four.move(60, 135)
        label_four.setText('<-当前按钮最终状态是可见')

        '''判定控件是否隐藏'''
        btn_five = QPushButton(self)
        btn_five.move(10, 170)
        label_five = QLabel(self)
        label_five.move(60, 175)
        label_five.setText('<-当前按钮是可见的')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
