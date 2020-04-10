'''
235-QDialog-模态与非模态

QDialog 可能是模态的或非模态对话框

模态对话框:
    应用程序级别 (是默认值) (exec())
        当该种模态的对话框出现时，用户必须首先对对话框进行交互，直到关闭对话框，然后才能访问程序中其他的窗口
    窗口级别 (open())
        该模态仅仅阻塞与对话框关联的窗口，但是依然允许用户与程序中其它窗口交互
非模态对话框:
    不会阻塞与对话框关联的窗口以及与其他窗口进行交互 (show())

    结合setModal(True)也可以实现模态对话框
    结合setWindowModality(Qt.WindowModal)也可以实现模态对话框 (Qt.WindowModal or Qt.ApplicationModal)

QDialogs可以提供返回值，它们可以有默认按钮
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('235-QDialog-模态与非模态')
        self.resize(1000, 500)

        self.d = QDialog(self)

        btn = QPushButton(self)
        btn.move(10, 10)
        btn.setText('弹框')
        btn.clicked.connect(self._btn_clicked)

    def _btn_clicked(self):
        '''应用程序级别'''
        self.d.exec()
        '''窗口级别'''
        self.d.open()
        '''非模态对话框'''
        self.d.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
