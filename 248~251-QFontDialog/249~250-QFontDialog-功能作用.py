'''
249~250-QFontDialog-功能作用

构造函数
    QFontDialog(parent: QWidget = None)
    QFontDialog(QFont, parent: QWidget = None)
打开对话框
    open(self)
    open(PYQT_SLOT) -- 打开后, 会自动连接fontSelected信号与此处指定的槽函数
    exec() -> int
当前字体
    setCurrentFont(QFont)
    currentFont() -> QFont
最终选中字体
    selectedFont() -> QFont
选项控制
    setOption(QFontDialog.FontDialogOption, on=True)
        on = True -- 设置该选项
        on = False -- 取消该选项
    setOptions(QFontDialog.FontDialogOption) -- 设置多个选项
    testOption(QFontDialog.FontDialogOption) -- 测试某个选项是否生效
    options() -> QFontDialog.FontDialogOption -- 获取当前的选项
静态方法 (静态方法打开选择字体的对话框控件)
    getFont(parent: QWidget = None) -> Tuple[QFont, bool]  -- 返回值, 字体对象和是否点击了确认按钮
    getFont(QFont, parent: QWidget = None, caption: str = '', options: QFontDialog.FontDialogOption) -> Tuple[QFont, bool]
        参数: 1: 默认字体  2. 父控件  3. 对话框标题  4. 选项    返回值: (最终字体, 是否点击确认)

附:
    QFontDialog.FontDialogOption
        QFontDialog.NoButtons -- 不显示'确定'和'取消'按钮。（对“实时对话框”有用。）
        QFontDialog.DontUseNativeDialog -- 在Mac上使用Qt的标准字体对话框而不是Apple的原生字体面板。
        QFontDialog.ScalableFonts -- 显示可缩放字体
        QFontDialog.NonScalableFonts -- 显示不可缩放的字体
        QFontDialog.MonospacedFonts -- 显示等宽字体
        QFontDialog.ProportionalFonts -- 显示比例字体

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFontDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('249~250-QFontDialog-功能作用')
        self.resize(1000, 500)

        self.fd = QFontDialog(self)

        # 显示等宽字体
        self.fd.setOption(QFontDialog.MonospacedFonts, on=False)

        # 打开对话框, 并制定一个最终选择的槽函数, 在槽函数内, 获取最终选择的字体对象, 为了展示清楚, 展示字体家族名称
        self.fd.open(lambda: print('最终选择了:', self.fd.selectedFont().family()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
