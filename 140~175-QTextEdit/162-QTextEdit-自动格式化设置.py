'''
162-QTextEdit-自动格式化设置

API:
    setAutoFormatting(QTextEdit.AutoFormatting) -- 设置自动格式化
    autoFormatting() -> QTextEdit.AutoFormatting -- 获取自动格式化设置

附:
    QTextEdit.AutoFormatting
        QTextEdit.AutoNone -- 不要做任何自动格式化。
        QTextEdit.AutoBulletList -- 自动创建项目符号列表（例如，当用户在最左侧列中输入星号（'*'）时，或在现有列表项中按Enter键。
        QTextEdit.AutoAll -- 应用所有自动格式。目前仅支持自动项目符号列表。
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('162-QTextEdit-自动格式化设置')
        self.resize(1000, 500)

        te = QTextEdit(self)

        '''设置自动格式化'''
        te.setAutoFormatting(QTextEdit.AutoAll)
        # 设置后, 在输入框中输入 * 号就有效果 (必须是英文输入法)

        '''获取自动格式化'''
        print('获取自动格式化:', te.autoFormatting())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
