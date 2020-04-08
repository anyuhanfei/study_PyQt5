'''
232-QFontComboBox

组合框中填充了按字母顺序排列的字体系列名称列表
让用户选择字体家族

继承自 QComboBox

API:
    设置和获取当前字体:
        setCurrentFont(QFont f)
        currentFont() -> QFont
    设置和获取过滤器:
        setFontFilters(QFontComboBox.FontFilters)
        fontFilters() -> QFontComboBox.FontFilters

信号: (大多是继承自 QComboBox)
    currentFontChanged(QFont font)

附:
    QFontComboBox.FontFilters
        QFontComboBox.AllFonts -- 显示所有字体
        QFontComboBox.ScalableFonts -- 显示可缩放字体
        QFontComboBox.NonScalableFonts -- 显示不可缩放的字体
        QFontComboBox.MonospacedFonts -- 显示等宽字体
        QFontComboBox.ProportionalFonts -- 显示比例字体
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFontComboBox, QLabel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('232-QFontComboBox')
        self.resize(1000, 500)

        fcb = QFontComboBox(self)

        '''信号'''
        label = QLabel(self)
        label.move(100, 10)
        label.setText('测试字体')
        fcb.currentFontChanged.connect(lambda val: label.setFont(val))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
