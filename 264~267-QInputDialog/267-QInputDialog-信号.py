'''
267-QInputDialog-信号

intValueChanged(int value) -- 值被修改, 下同
intValueSelected(int value) -- 值被选中, 下同
doubleValueChanged(double value)
doubleValueSelected(double value)
textValueChanged(text_str)
textValueSelected(text_str)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('267-QInputDialog-信号')
        self.resize(1000, 500)

        input_d = QInputDialog(self)
        input_d.setInputMode(QInputDialog.IntInput)

        input_d.intValueChanged.connect(lambda val: print('值被修改', val))
        input_d.intValueSelected.connect(lambda val: print('值被选中', val))

        input_d.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
