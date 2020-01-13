'''
QOject的属性设置读取功能的应用实例

案例：
    创建多个用于信息提示的QLabel
要求：
    1. 凡是提示的QLabel控件，都要求设置：字体大小为25px，字体颜色为灰色，边框圆角为8px
    2. 信息提示分为多级：
        - 正常(normal)：绿色边框，绿色字体
        - 警告(warning)：黄色边框，黄色字体
        - 错误(error)：红色边框，红色字体
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, qApp


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QOject的属性设置读取功能的应用实例')
        self.resize(700, 400)
        self.setup_ui()

    def setup_ui(self):
        # 导入pss样式
        with open('./index.pss', 'r') as f:
            qApp.setStyleSheet(f.read())
        self._setup_label('normal', 'notice', {'notice_level': 'normal'}, 30)
        self._setup_label('warning', 'notice', {'notice_level': 'warning'}, 60)
        self._setup_label('error', 'notice', {'notice_level': 'error'}, 90)

    def _setup_label(self, text, object_name, propertys, y):
        '''创建标签控件
        Args:
            text: 标签展示文字
            object_name: 标签名称
            propertys: 标签的属性（列表）
            y: y轴位置
        '''
        label = QLabel(self)
        label.move(0, y)
        label.setObjectName(object_name)
        for key, value in propertys.items():
            label.setProperty(key, value)
        label.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
