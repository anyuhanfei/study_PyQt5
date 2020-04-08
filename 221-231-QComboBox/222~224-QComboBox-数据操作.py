'''
222~224-QComboBox-数据操作

API:
    添加条目项:
        addItem(str, userData: Any = None)
        addItem(QIcon, str, userData: Any = None)
        addItems(Iterable[str])
    插入条目项:
        insertItem(int, str, userData: Any = None)
        insertItem(int, QIcon, str, userData: Any = None)
        insertItems(int, Iterable[str])
    设置条目项:
        setItemIcon(int, QIcon)
        setItemText(int, str)
        setItemData(int, Any, role: int = Qt.UserRole) -- 设置数据, 下节使用了
    删除条目项
        removeItem(int index)
    插分割线
        insertSeparator(int index)
    设置当前选定条目项
        setCurrentIndex(int index)
        setCurrentText(QString text)
    编辑当前选定条目项
        setEditText(QString text) -- 结合设置可被编辑(setEditable)

(了解)
模型操作:
    setModel(QAbstractItemModel model)
    setModelColumn(int visibleColumn)
    setRootModelIndex(QModelIndex index)
    model()
    modelColumn()
    rootModelIndex()
视图操作:
    setView(QAbstractItemView *itemView)
    view()
代理设置:
    setItemDelegate(QAbstractItemDelegate *delegate)

注:
    from PyQt5.QtWidgets import QTreeView  -- 树形视图
    from PyQt5.QtGui import QStandardItemModel  -- 模型对象的抽象父类
    from PyQt5.QtCore import QAbstractItemModel  -- 一种模型对象
    from PyQt5.QtGui import QIcon, QStandardItem  -- 实例化模型对象
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QTreeView
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import QAbstractItemModel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('222~224-QComboBox-数据操作')
        self.resize(1000, 500)

        cb = QComboBox(self)
        cb.move(10, 10)

        '''添加条目项'''
        # 单条信息
        cb.addItem('选项一')
        # 单条信息, 有图标
        cb.addItem(QIcon('./xxx.png'), '选项二')
        # 多条信息
        cb.addItems(['选项3', '选项4'])

        '''插入条目项'''
        # 单条信息
        cb.insertItem(2, '插入一')
        # 单条信息, 有图标
        cb.insertItem(2, QIcon('./xxx.png'), '插入二')
        # 多条信息
        cb.insertItems(2, ['插入三', '插入四'])

        '''设置条目项'''
        # 设置条目项图标
        cb.setItemIcon(0, QIcon('./xxx.png'))
        # 设置条目项内容
        cb.setItemText(0, '设置一')

        '''删除条目项'''
        cb.insertItem(0, '被删除项')
        cb.removeItem(0)

        '''插入分割线'''
        cb.insertSeparator(2)

        '''设置当前选定条目项'''
        # cb.setCurrentIndex(2)
        cb.setCurrentText('插入三')

        '''编辑当前选定条目项'''
        cb.setEditable(True)
        cb.setEditText('被编辑了')

        '''查看模型'''
        print('当前模型:', QAbstractItemModel.__subclasses__())

        cb_two = QComboBox(self)
        cb_two.move(150, 10)
        cb_two.resize(100, 30)

        # 创建一个模型对象
        model = QStandardItemModel()
        # 创建一些条目
        item1 = QStandardItem('item1')
        item2 = QStandardItem('item2')
        item22 = QStandardItem('item22')
        # 添加到结果中, 父子关系
        item2.appendRow(item22)
        model.appendRow(item1)
        model.appendRow(item2)
        # 将模型对象设置到控件中
        cb_two.setModel(model)
        # 修改视图
        cb_two.setView(QTreeView(cb))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
