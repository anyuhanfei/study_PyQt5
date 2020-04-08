'''
230~231-QComboBox-综合案例

给定一些城市数据, 实现两级联动的效果
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QComboBox


class Window(QWidget):
    city_dict = {
        '北京': {"东城": "001", "西城": "002", "丰台": "003"},
        '上海': {"黄埔": "004", "徐汇": "005", "长宁": "006"},
        '广东': {"广州": "007", "深圳": "008", "佛山": "009"}
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('230~231-QComboBox-综合案例')
        self.resize(1000, 500)

        self._create_combobox()

        self.cb_level_one.currentIndexChanged[str].connect(self._set_item)

    def _create_combobox(self):
        '''创建两个 QComboBox 控件, 并给第一个控件添加条目'''
        # 添加第一个控件, 并添加条目
        self.cb_level_one = QComboBox(self)
        self.cb_level_one.move(10, 10)
        self.cb_level_one.addItem('请选则城市')
        for i in self.city_dict.keys():
            self.cb_level_one.addItem(i)
        # 添加第二个控件
        self.cb_level_two = QComboBox(self)
        self.cb_level_two.move(100, 10)

    def _set_item(self, str):
        '''给第二个控件赋值'''
        # 先删除旧条目
        self.cb_level_two.clear()
        # 然后添加新条目
        for key, value in self.city_dict[str].items():
            self.cb_level_two.insertItem(0, key, value)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
