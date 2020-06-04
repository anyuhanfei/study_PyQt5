'''
330-布局管理-QFormLayout-字段的增长策略

setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy)
fieldGrowthPolicy()->QFormLayout.FieldGrowthPolicy

附:
    QFormLayout.FieldsStayAtSizeHint -- 默认值
    QFormLayout.ExpandingFieldsGrow -- 水平大小策略为Expanding或MinimumExpanding的字段将增长以填充
    QFormLayout.AllNonFixedFieldsGrow -- 具有允许它们增长的大小策略的所有字段将增长已填充可用空间



'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('330-布局管理-QFormLayout-字段的增长策略')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
