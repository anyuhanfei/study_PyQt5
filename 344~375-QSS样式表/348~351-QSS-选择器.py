'''
348~351-QSS-选择器

 选择器           例                                说明

通用选择器      *                         匹配所有控件
类型选择器      QPushButton               通过控件类型来匹配控件(包含子类)
类选择器        .QPushButton              通过控件类型来匹配控件(不包含子类)
ID选择器        #objectName               通过 objectName 来匹配控件 (setObjectName)
属性选择器      控件类型[属性名="属性值"]  通过属性值来匹配控件 (setProperty)
后代选择器      父控件 子控件             通过父控件(直接或间接)子控件来筛选控件
子选择器        父控件>子控件              通过父控件(直接)子控件来筛选控件
子控件选择器    复合控件::子控件           筛选一个复合控件上的子控件

注: 选择器可以组合使用, 需要用逗号隔开

附:
    常见的符合控件及其子控件
        QCheckBox, QRadioButton -- ::indicator
        QComboBox -- ::drop-down
        QSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit -- ::up-button  ::down-button  ::up-arrow  ::down-arrow
        QProgressBar -- ::chunk
        QScrollBar -- ::sub-line  ::add-line  ::sub-page  ::add-page  ::up-arrow  ::down-arrow  ::left-arrow  ::right-arrow
        QGroupBox -- ::title  ::indicator
        QTableView -- ::item
            QHeaderView, QTableCornerButton -- ::section
        QTreeView -- ::item  ::branch
            QHeaderView -- ::section
        QTabWidget -- ::pane  ::tab-bar
            QTabBar -- ::tab  ::close-button  ::tear  ::scroller
            QTabBar, QToolButton -- ::left-arrow  ::right-arrow
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('348~351-QSS-选择器')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
