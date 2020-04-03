'''
124~126-QLineEdit-文本内容限制-验证器

API:
    setValidator(QValidator) -- 设置验证器
    setInputMask(mask_str) -- 掩码验证

QValidator:
    用于验证用户输入数据的合法性
    如果一个输入框设置了验证器,到时用户在文本框中输入内容时,首先会将内容传递给验证器进行验证,如果输入框结束输入后, 上述的验证状态并非有效, 则会调用修复方法

    是一个抽象类，无法直接使用，可以自定义子类，也可以使用系统提供的子类

    validate(self, input_text, pos) -- 验证方法
        return (QValidator.Acceptable,  input_text, pos) -- 验证通过
        return (QValidator.Intermediate,  input_text, pos) -- 暂不作判定是否通过验证
        return (QValidator.Invalid,  input_text, pos) -- 验证不通过

    fixup(self, input_text) -- 修复方法
        return 修正后文本
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from PyQt5.QtGui import QValidator, QIntValidator


class MyValidator(QValidator):
    '''验证器'''
    def __init__(self):
        super().__init__()

    def validate(self, input_text, pos):
        '''验证方法
        Args:
            input_text: 输入框中的值
            pos: 光标位置
        return:
            tuple, 包含验证结果、输入框中的值，光标位置
        '''
        # 在这里写验证逻辑代码，这里用打印代替了
        print(input_text, pos)

        # return (QValidator.Acceptable, input_text, pos)
        return (QValidator.Intermediate,  input_text, pos)

    def fixup(self, input_text):
        '''修复方法
        会在结束输入时的验证方法返回非通过状态时调用， 在返回结果后，会再次调用 validate() 方法进行验证，如果验证通过，则将返回值展示在输入框中，如果验证未通过，则不做任何操作。
        Args:
            input_text: 输入框中的值
        return:
            返回修正后的文本
        '''
        print('aa', input_text)

        return '18'


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('126_QLineEdit_文本内容限制_验证器')
        self.resize(1000, 500)

        le = QLineEdit(self)

        '''创建一个验证器'''
        validator = MyValidator()

        '''将验证器绑定到文本框控件上'''
        le.setValidator(validator)

        '''整型数据验证器'''
        ler = QLineEdit(self)
        ler.move(0, 30)
        ler.setValidator(QIntValidator(10, 100))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
