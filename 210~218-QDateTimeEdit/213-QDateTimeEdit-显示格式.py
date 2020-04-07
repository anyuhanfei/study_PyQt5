'''
213-QDateTimeEdit-显示格式

API:
    setDisplayFormat(format_str) -- 设置日期时间显示格式
    displayFormat() -> str -- 获取日期时间显示格式

附:
    时间日期格式符
        日期
            d -- 没有前导零的数字的日期（1到31）
            dd -- 有前导零的数字的日期（01到31）
            ddd -- 缩写的本地化日期名称（例如'Mon'到'Sun'
            dddd -- 完整本地化的日期名称（例如“星期一”到“星期日”）
            M -- 没有前导零的数字的月份（1-12）
            MM -- 月份为前导零的数字（01-12）
            MMM -- 缩写的本地化月份名称（例如'Jan'到'Dec'）
            MMMM -- 完整的本地化月份名称（例如“1月”到“12月”）
            yy -- 年份为两位数字（00-99）
            yyyy -- 年份为四位数字
        时间
            h -- 没有前导零的小时（如果显示AM / PM，则为0到23或1到12）
            hh -- 前导零的小时（如果AM / PM显示，则为00到23或01到12）
            H -- 没有前导零的小时（0到23，即使有AM / PM显示）
            HH -- 前导零的小时（00到23，即使有AM / PM显示）
            m -- 没有前导零的分钟（0到59）
            mm -- 前导零（00到59）的分钟
            s -- 整个秒没有前导零（0到59）
            ss -- 带有前导零（00到59）
            z -- 第二个小数部分, 没有尾随零的毫秒（0到999）
            zzz -- 第二个小数部分, 有尾随零的毫秒（000到999）
            AP / A -- 使用AM / PM显示
            ap / a -- 使用am / pm显示
            t -- 时区
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('213-QDateTimeEdit-显示格式')
        self.resize(1000, 500)

        dte = QDateTimeEdit(self)

        '''设置日期时间显示格式'''
        dte.setDisplayFormat('yy-MMMM-ddd')

        '''获取日期时间显示格式'''
        print(dte.displayFormat())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
