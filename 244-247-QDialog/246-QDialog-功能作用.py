'''
246-QDialog-功能作用

构造函数:
    QDialog(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
模态设置:
    setModal(bool) (结合show()方法一起使用)
    modal() -> bool
弹出:
    open()
    exec()
是否显示尺寸调整控件:
    setSizeGripEnabled(bool)
    isSizeGripEnabled() -> bool
常用操作槽:
    accept() -- 确认
    reject() -- 取消
    done(int r) -- 其他按钮
设置和获取数值:
    setResult(int)
    result() -> int
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('246-QDialog-功能作用')
        self.resize(1000, 500)

        d = QDialog(self)
        '''是否显示尺寸调整控件'''
        # 设置
        d.setSizeGripEnabled(True)

        '''常用操作槽'''
        # 确认按钮, 返回1, 会关闭弹框
        btn1 = QPushButton(d)
        btn1.move(10, 10)
        btn1.setText('确认')
        btn1.clicked.connect(lambda: d.accept())

        # 取消按钮, 返回0, 会关闭弹框
        btn2 = QPushButton(d)
        btn2.move(10, 60)
        btn2.setText('取消')
        btn2.clicked.connect(lambda: d.reject())

        # 其他按钮, 返回设置的值, 会关闭弹框
        btn3 = QPushButton(d)
        btn3.move(10, 110)
        btn3.setText('其他')
        btn3.clicked.connect(lambda: d.done(3))

        '''设置值'''
        # 不会关闭弹框
        btn4 = QPushButton(d)
        btn4.move(10, 160)
        btn4.setText('设置')
        btn4.clicked.connect(lambda: d.setResult(4))

        '''获取值'''
        # 不会关闭弹框
        btn5 = QPushButton(d)
        btn5.move(10, 210)
        btn5.setText('获取')
        btn5.clicked.connect(lambda: print('当前值:', d.result()))

        print(d.exec())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
