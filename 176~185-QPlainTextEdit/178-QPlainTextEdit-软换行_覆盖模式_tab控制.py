'''
178-QPlainTextEdit-软换行_覆盖模式_tab控制

API:
    lineWrapMode() -> QPlainTextEdit.LineWrapMode -- 获取软换行模式
    setLineWrapMode(QPlainTextEdit.LineWrapMode) -- 设置软换行模式

    overwriteMode() -> bool -- 获取覆盖模式
    setOverwriteMode(bool) -- 设置覆盖模式(单字符输入有效)

    setTabChangesFocus(bool) -- 控制 tab 的作用: True 切换焦点, False 普通制表符
    setTabStopDistance(distance_float) -- 设置制表符宽度
    tabChangesFocus() -> bool -- 获取 tab 的作用
    tabStopDistance() -> float -- 获取制表符宽度

附:
    QPlainTextEdit.LineWrapMode
        QPlainTextEdit.NoWrap -- 没有软换行
        QPlainTextEdit.WidgetWidth -- 超出控件宽度进行自动换行
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPlainTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('178-QPlainTextEdit-软换行_覆盖模式_tab控制')
        self.resize(1000, 500)

        pte = QPlainTextEdit(self)

        '''软换行'''
        # 开启软换行
        pte.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        # 获取软换行模式
        print('获取软换行模式:', pte.lineWrapMode())

        '''覆盖模式'''
        # 设在为覆盖模式
        pte.setOverwriteMode(True)
        # 获取是否是覆盖模式
        print('获取是否是覆盖模式:', pte.overwriteMode())

        '''tab'''
        # 将 tab 键改为普通制表符
        pte.setTabChangesFocus(False)
        # 修改制表符宽度
        pte.setTabStopDistance(160)
        # 获取 tab 键的作用:
        print('获取 tab 键的作用:', pte.tabChangesFocus())
        # 获取制表符宽度
        print('获取制表符宽度:', pte.tabStopDistance())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
