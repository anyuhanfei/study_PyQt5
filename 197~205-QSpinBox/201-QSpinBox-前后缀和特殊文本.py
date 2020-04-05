'''
201-QSpinBox-前后缀和特殊文本

API:
    setPrefix(str) -- 设置前缀作为展示
    prefix() -> str -- 获取前缀
    setSuffix(str) -- 设置后缀作为展示
    suffix() -> str -- 获取后缀

    setSpecialValueText(str) -- 最小值特殊文本 (父类中的方法) (没有前后缀)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('201-QSpinBox-前后缀和特殊文本')
        self.resize(1000, 500)

        sb = QSpinBox(self)

        '''前缀'''
        # 设置
        sb.setPrefix('周')
        # 获取
        print('前缀:', sb.prefix())

        '''后缀'''
        # 设置
        sb.setSuffix('月')
        # 获取
        print('后缀:', sb.suffix())

        '''最小值特殊文本'''
        sb.setSpecialValueText('最小值')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
