'''
211-QDateTimeEdit-简单使用

附:
    QDateTime:
        日期时间对象
        它是 QDate 和 QTime 类的组合
        包括 年月日 时分秒毫秒

        功能作用:
            日期时间对象构造:
                QDateTime()
                QDateTime(QDateTime)
                QDateTime(QDate)
                QDateTime(QDate,  QTime, Qt.TimeSpec = Qt.LocalTime)
                QDateTime(int, int, int, int, int, second: int = 0, msec: int = 0, timeSpec: int = 0)
                QDateTime(QDate, QTime, Qt.TimeSpec, int)
                QDateTime(QDate, QTime, QTimeZone)
                currentDateTime() -- 当前时间 (静态方法)
                currentDateTimeUtc() -- 世界标准时间 (静态方法)
            调整日期时间:
                addYears(int) -- 添加年
                addMonths(int) -- 添加月
                addDays(int) -- 添加天
                addSecs(int) -- 添加秒
                addMSecs(int) -- 添加毫秒
                setDate(const QDate &date) -- 设置日期
                setTime(const QTime &time) -- 设置时间
            计算时间差:
                offsetFromUtc() -- 与世界标准时间的时间差
                secsTo(QDateTime) -- 与另一个时间间隔的秒数
                msecsTo(QDateTime) -- 与另一个时间间隔的毫秒数

    QDate:
        日期对象
        包括年月日

        功能作用:
            日期对象的构造:
                QDate()
                QDate(int y, int m, int d)
                currentDate()
            调整日期:
                setDate(int year, int month, int day)
                addYears(int nyears)
                addMonths(int nmonths)
                addDays(qint64 ndays)
            计算时间差:
                daysTo(const QDate &d)
            获取时间:
                day() -- 这一个月的第几日
                month() -- 第几月
                year() -- 第几年
                dayOfWeek() -- 这一周 第几日
                dayOfYear() -- 这一年 第几日
                daysInMonth() -- 这一月总共多少天
                daysInYear() -- 这一年总共多少天

    QTime:
        时间对象
        包括时分秒毫秒

        功能作用:
            时间对象构造:
                QTime()
                QTime(int h, int m, int s = 0, int ms = 0)
                currentTime()
            调整时间:
                addSecs(int s)
                addMSecs(int ms)
            计算时间差:
                secsTo(QTime t)
            计时:
                 start()
                 restart()
                 elapsed()
            获取时间:
                hour()
                minute()
                second()
                msec()
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit
from PyQt5.QtCore import QDateTime, QDate, QTime


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('211-QDateTimeEdit-简单使用')
        self.resize(1000, 500)

        dt = QDateTime(2020, 1, 1, 1, 1)  # 2020年1月1日 1时1分
        dt = dt.addYears(2)  # 不是修改对象自身, 而是返回一个新的对象

        QDateTimeEdit(dt, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
