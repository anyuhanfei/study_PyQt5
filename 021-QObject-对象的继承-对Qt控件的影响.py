'''
021-QObject-对象的继承-对Qt空间的影响

如果一个控件，没有任何父控件，那么就会被当成顶层控件(窗口)：
    多个顶层控件相互独立；

如果想要一个控件被包含在另外一个控件内部，就需要设置父子关系：
    显示位置受父控件约束；
    生命周期也被父对象接管；

案例：
    1. 创建两个独立的窗口，需要设置两个不同的标题
    2. 创建一个窗口，包含另两个子控件 QWidget，两个子空间必须在同一个窗口内部
    3. 创建一个窗口，包含多个子控件 QWidget 和 QLabel
        让所有 QLabel 子控件都设置背景颜色为 cyan，即使后续再增加新的 QLabel 子控件
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


app = QApplication(sys.argv)


'''1.'''
# 创建一个顶级控件
win1 = QWidget()
win1.setWindowTitle('an')
win1.show()
# 创建另一个顶级控件
win2 = QWidget()
win2.setWindowTitle('yu')
win2.show()

'''2.'''
# 创建顶级控件
win3 = QWidget()
win3.setWindowTitle('han')
win3.resize(500, 500)
# 创建两个 QWidget 子控件
win4 = QWidget(win3)
win4.setStyleSheet('background-color: red;')
win4.resize(100, 100)
win5 = QWidget()
win5.setParent(win3)
win5.setStyleSheet('background-color: green;')
win5.resize(100, 100)
win5.move(100, 100)

win3.show()

'''3.'''
# 创建顶级控件
win6 = QWidget()
win6.setWindowTitle('fei')
win6.resize(500, 500)
# 创建多个 QLabel 子控件
label1 = QLabel(win6)
label1.setText('111111')
label2 = QLabel(win6)
label2.setText('222222')
label2.move(0, 50)
# 创建多个 QWidget 子控件
win7 = QWidget(win6)
win7.resize(100, 100)
win7.move(0, 100)
win7.setStyleSheet('background-color: red;')
win8 = QWidget(win6)
win8.resize(100, 100)
win8.move(0, 200)
win8.setStyleSheet('background-color: green;')
# 遍历顶级控件中的 QLable 子控件，并对子对象的样式进行修改
for sub_obj in win6.findChildren(QLabel):
    sub_obj.setStyleSheet('background-color: cyan;')

win6.show()

sys.exit(app.exec_())
