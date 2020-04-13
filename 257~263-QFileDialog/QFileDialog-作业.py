'''
QFileDialog-作业

窗口有两个按钮和一个文本编辑器, 点击一个按钮可以让用户选择一个文件(应该是任意文件, 为了可编辑, 所以自我简化功能, 只能是 py 文件), 把文件内容展示到文本编辑器中, 当用户点击另一个按钮后, 可以另存为到另一个文件中
'''

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QPushButton, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QFileDialog-作业')
        self.resize(500, 800)

        self.create_widget()
        self.connect_function()

    def create_widget(self):
        '''创建两个按钮控件和一个文本编辑器控件'''
        self.open_btn = QPushButton(self)
        self.open_btn.move(50, 20)
        self.open_btn.setText('打开')

        self.save_btn = QPushButton(self)
        self.save_btn.move(400, 20)
        self.save_btn.setText('保存')

        self.text_edit = QTextEdit(self)
        self.text_edit.move(50, 70)
        self.text_edit.resize(400, 700)

    def connect_function(self):
        '''绑定两个按钮的信号函数'''
        self.open_btn.clicked.connect(self._open_file)

        self.save_btn.clicked.connect(self._save_file)

    def _open_file(self):
        '''打开一个文件(限制为 py 文件)
        将选中的文件输入到文本编辑器控件中
        '''
        # 打开一个文件
        self.open_file = QFileDialog.getOpenFileName(self, '请选择一个 python 文件', './', 'Python(*.py)', 'Python(*.py)')
        # 通过文件路径读取文件内容
        with open(self.open_file[0], 'r', encoding="utf-8") as f:
            self.text_edit.setText(f.read())

    def _save_file(self):
        '''另存为当前文本编辑器的内容'''
        # 获取要保存的文件名
        self.save_file = QFileDialog.getSaveFileName(self, '另存为', './', 'Python(*.py)', 'Python(*.py)')
        # 将内容输入到文件中
        with open(self.save_file[0], 'a+', encoding="utf-8") as f:
            f.write(self.text_edit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
