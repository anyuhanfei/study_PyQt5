'''
276-QCalendarWidget-信号

activated(QDate date) -- 只要用户按下Return或Enter键或双击日历小部件中的日期，就会发出此信号。
clicked(QDate date) -- 单击有效日期时才会发出信号
currentPageChanged(int year, int month) -- 当前显示的月份更改时会发出此信号。新的一年和一个月作为参数传递。
selectionChanged() -- 当前选择的日期更改时会发出此信号
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('276-QCalendarWidget-信号')
        self.resize(1000, 500)

        cw = QCalendarWidget(self)

        '''确认日期'''
        cw.activated.connect(lambda date_obj: print('确认日期:', date_obj))

        '''点击日期'''
        cw.clicked.connect(lambda date_obj: print('选择日期:', date_obj))

        '''更改月份'''
        cw.currentPageChanged.connect(lambda year, month: print('更改月份: %s年%s月' % (year, month)))

        '''更改当前选择'''
        cw.selectionChanged.connect(lambda: print('更改了当前选择的日期'))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
