'''
167-QTextEdit-字体设置

API:
    字体家族
        setFontFamily(family_str) -- 设置字体家族
        fontFamily() -- 获取字体家族
        QFontDialog.getFont() -- 查看可用的字体
    字体粗细
        setFontWeight(int) -- 设置字体粗细
        fontWeight() -- 获取字体粗细
    字体斜体
        setFontItalic(bool) -- 设置字体是否是斜体
        fontItalic() -- 获取字体是否斜体
    字体尺寸
        setFontPointSize(float) -- 设置字体尺寸
        fontPointSize() -- 获取字体尺寸
    字体下划线
        setFontUnderline(bool) -- 设置是否有下划线
        fontUnderline() -- 获取是否有下划线
    统一设置QFont (功能全, 类似自定义)
        setCurrentFont(QFont) -- 设置 QFont
        currentFont() -> QFont -- 获取 QFont

附:
    QFont:
        QFont.ExtraLight
        QFont.Light
        QFont.ExtraBold
        QFont.Black
        QFont.Bold
        QFont.DemiBold
        QFont.Medium
        QFont.Normal
        QFont.Thin
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.Qt import QFontDialog, QFont


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('167-QTextEdit-字体设置')
        self.resize(1000, 500)

        # 查看字体家族
        QFontDialog.getFont()

        te = QTextEdit(self)

        '''设置字体家族'''
        te.setFontFamily('幼圆')

        '''设置字体粗细'''
        te.setFontWeight(20)

        '''设置字体是否是斜体'''
        te.setFontItalic(True)

        '''设置字体尺寸'''
        te.setFontPointSize(40)

        '''设置是否有下划线'''
        te.setFontUnderline(True)

        '''设置 QFont'''
        font = QFont()
        # te.setCurrentFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
