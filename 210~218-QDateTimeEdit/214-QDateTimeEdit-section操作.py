'''
214-QDateTimeEdit-section操作

QDateTimeEdit 控件中的内容分别代表各个时间的部分, 这些部分都是 section, 它们的索引默认从 0 开始, 从左至右.

API:
    sectionCount() -> int -- 获取section个数
    setCurrentSectionIndex(int) -- 设置当前的section索引(不是修改当前索引的值, 而是修改当前指定的索引)
    currentSectionIndex() -> int -- 获取section索引
    setCurrentSection(QDateTimeEdit.Section) -- 设置当前操作的日期时间section (可以在各个section顺序混乱时正确指定到)
    currentSection() -> QDateTimeEdit.Section -- 获取当前的section部分
    sectionAt(index_int) -> QDateTimeEdit.Section -- 获取指定索引位置的section
    sectionText(QDateTimeEdit.Section) -> str -- 获取指定section的文本内容

附:
    QDateTimeEdit.Section:
        QDateTimeEdit.NoSection
        QDateTimeEdit.AmPmSection
        QDateTimeEdit.MSecSection
        QDateTimeEdit.SecondSection
        QDateTimeEdit.MinuteSection
        QDateTimeEdit.HourSection
        QDateTimeEdit.DaySection
        QDateTimeEdit.MonthSection
        QDateTimeEdit.YearSection
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('214-QDateTimeEdit-section操作')
        self.resize(1000, 500)

        self.dte = QDateTimeEdit(self)

        '''获取section个数'''
        print('section个数:', self.dte.sectionCount())

        '''获取section索引'''
        btn = QPushButton('获取索引', self)
        btn.move(0, 50)
        btn.clicked.connect(lambda: print('当前位置的索引:', self.dte.currentSectionIndex()))

        '''设置section索引'''
        btn = QPushButton('设置索引', self)
        btn.move(80, 50)
        btn.clicked.connect(lambda: self.dte.setCurrentSectionIndex(3))

        '''设置当前操作的日期时间section'''
        btn = QPushButton('设置section', self)
        btn.move(160, 50)
        btn.clicked.connect(lambda: self.dte.setCurrentSection(QDateTimeEdit.DaySection))

        '''获取当前的section部分'''
        btn = QPushButton('获取section', self)
        btn.move(240, 50)
        btn.clicked.connect(lambda: print('获取当前的section部分', self.dte.currentSection()))

        '''获取指定索引位置的section'''
        btn = QPushButton('获取指定索引的section', self)
        btn.move(00, 90)
        btn.clicked.connect(lambda: print('获取指定索引位置的section', self.dte.sectionAt(1)))

        '''获取指定section的文本内容'''
        btn = QPushButton('获取指定section的文本内容', self)
        btn.move(00, 130)
        btn.clicked.connect(lambda: print('获取指定section的文本内容', self.dte.sectionText(QDateTimeEdit.DaySection)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
