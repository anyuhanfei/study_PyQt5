'''
一切的开始，hello world

pyqt5 安装
pip install PyQt5 -i https://pypi.douban.com/simple
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel  # 导入需要使用的控件

'''创建应用程序'''
# sys.argv 列表类型，可接收命令行执行代码时自身的文件路径和其后跟随的以空格隔开的一个或多个参数
# QApplication() 实例化一个PyQt的实例化对象，可将命令行参数列表传入到此实例化对象中，这样可以在实例化对象中根据命令行参数做一些功能。可以通过 app.arguments() 函数获取到实例化对象中保存的命令行参数
app = QApplication(sys.argv)

'''控件操作'''
# 小知识：当创建的控件没有父控件时，系统会自动将它当作顶层控件，也就是窗口控件。系统会自动给窗口添加一些装饰，如标题栏，并且具备了窗口控件的特性，如设置标题
window = QWidget()  # 创建空白控件，无父控件
window.setWindowTitle('暗语寒飞')  # 设置窗口标题
window.resize(500, 500)  # 设置控件大小，参数一为宽，参数二为高
window.move(400, 200)  # 移动控件位置，参数一为 x 轴坐标，参数二为 y 轴坐标，原点坐标在父控件的左上角，x 轴向右为正方向，y 轴向下为正方向（无父控件的控件的坐标原点在屏幕左上角）

label = QLabel(window)  # 创建标签控件，父控件是 window
label.setText('Hello World')  # 设置标签内容
label.move(200, 200)

window.show()  # 展示此控件。前提：没有父控件；原因：没有父控件的控件默认不展示，需要手动展示

'''开始执行应用程序并进入消息循环'''
# sys.exit() 系统退出，可手动填写参数表示状态码，一般情况下，状态码为0是为系统自动退出，其他则为程序错误
# app.exec_() 保证了在窗口关闭前不会关闭进程（关闭进程后窗口也会关闭）,会无限循环获取窗口状态，信号等
sys.exit(app.exec_())
