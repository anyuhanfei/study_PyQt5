'''
126_QLineEdit_文本内容限制_掩码限制

掩码可以指定固定位置的固定数据类型, 达到一个格式上的限制

掩码由一串掩码字符和分隔符组成  可选的分号; 和 空白占位字符

API:
    setInputMask(mask_str) -- 设置掩码

掩码详情见 http://note.youdao.com/noteshare?id=9ea49c7dd9bcb74b1e5f87194cc60cd7&sub=20C0107B61AD4AF5BCC11E2A717B29C2
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('126_QLineEdit_文本内容限制_掩码限制')
        self.resize(1000, 500)

        le = QLineEdit(self)

        '''添加掩码验证'''
        le.setInputMask('>A-9')  # 参数是掩码规则，这里的意思是第一个字符要输入大写字母，第二个字符是 -，第三字符是数字


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
