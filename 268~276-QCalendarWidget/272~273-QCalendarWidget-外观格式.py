'''
272~273-QCalendarWidget-外观格式

导航条:
    isNavigationBarVisible() -> bool -- 获取导航栏是否可见
    setNavigationBarVisible(bool) -- 设置导航栏是否可见
一周的第一天:
    setFirstDayOfWeek(Qt.DayOfWeek dayOfWeek) -- 设置一周的第一天
    firstDayOfWeek() -> Qt.DayOfWeek -- 获取一周的第一天
    isGridVisible() -> bool
网格显示:
    isGridVisible() -> bool -- 获取是否添加网格
    setGridVisible(bool) -- 设置是否添加网格
文本格式:
    setHeaderTextFormat(QTextCharFormat format) -- 设置头部文件样式修改(水平和垂直)
    headerTextFormat() -> QTextCharFormat 获取头部文件样式(水平和垂直)
    setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat format) -- 设置水平标头
    horizontalHeaderFormat() -> QCalendarWidget.HorizontalHeaderFormat
    setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat format) -- 设置垂直标头
    verticalHeaderFormat() -> QCalendarWidget.VerticalHeaderFormat
    setWeekdayTextFormat(self, Qt.DayOfWeek, QTextCharFormat)
    weekdayTextFormat(Qt.DayOfWeek dayOfWeek) -> QTextCharFormat
    setDateTextFormat(QDate date, QTextCharFormat format)
    dateTextFormat(self, Union[QDate, datetime.date]) -> QTextCharFormat
    dateTextFormat(self) -> object

附:
    QCalendarWidget.HorizontalHeaderFormat
        QCalendarWidget.SingleLetterDayNames -- 周
        QCalendarWidget.ShortDayNames -- 周一
        QCalendarWidget.LongDayNames -- 星期一
        QCalendarWidget.NoHorizontalHeader -- 不显示
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('272~273-QCalendarWidget-外观格式')
        self.resize(1000, 500)

        cw = QCalendarWidget(self)

        '''设置导航栏是否可见'''
        cw.setNavigationBarVisible(False)

        '''设置一周的第一天'''
        cw.setFirstDayOfWeek(Qt.Sunday)

        '''设置是否添加网格'''
        cw.setGridVisible(True)

        '''设置水平标头'''
        cw.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
