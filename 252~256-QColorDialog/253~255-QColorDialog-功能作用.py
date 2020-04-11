'''
253~255-QColorDialog-功能作用

构造函数:
    QColorDialog(parent: QWidget = None)
    QColorDialog(Union[QColor, Qt.GlobalColor, QGradient], parent: QWidget = None)
打开对话框:
    open(self)
    open(PYQT_SLOT) -- 打开后, 会自动连接colorSelected信号与此处指定的槽函数
    exec() -> int
当前颜色:
    setCurrentColor(QColor())
    currentColor() -> QColor
最终选中颜色:
    selectedColor()
选项控制:
    setOption(self, QColorDialog.ColorDialogOption, on: bool = True)
    setOptions(self, Union[QColorDialog.ColorDialogOptions, QColorDialog.ColorDialogOption])
    testOption(self, QColorDialog_ColorDialogOption)
静态方法:
    customCount() -> int
    setCustomColor(int index, QColor color)
    customColor(int index) -> QColor
    setStandardColor(int index, QColor color)
    standardColor(int index) -> QColor
    getColor(initial: Union[QColor, Qt.GlobalColor, QGradient] = Qt.white, parent: QWidget = None, title: str = '', options: Union[QColorDialog.ColorDialogOptions, QColorDialog.ColorDialogOption] = QColorDialog.ColorDialogOptions()) -> QColor

附:
    QColorDialog.ColorDialogOption
        QColorDialog.ShowAlphaChannel -- 允许用户选择颜色的alpha分量。
        QColorDialog.NoButtons -- 不显示“ 确定”和“ 取消”按钮。（对“实时对话框”有用。）
        QColorDialog.DontUseNativeDialog -- 使用Qt的标准颜色对话框而不是操作系统原生颜色对话框。
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QColorDialog
from PyQt5.QtGui import QPalette


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('253~255-QColorDialog-功能作用')
        self.resize(1000, 500)

        self.cd = QColorDialog(self)

        self.cd.open(self._color)

    def _color(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, self.cd.selectedColor())
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
