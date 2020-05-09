'''
300-QProgressDialog-功能作用

API:
    setMinimumDuration(int ms) -- 设置展示延时时间(默认4秒)
    minimumDuration() -> int -- 获取展示延时时间
        备注: 如果在等待时间内, 进度已经完成了, 那么就不会再弹出了.
    open() -- 立即打开(非模态窗口)
    show() -- 立即打开(模态窗口)

    setAutoClose(bool) -- 是否自动关闭
    setAutoReset(bool) -- 满值时是否自动归零

    setWindowTitle(str) -- 设置标题
    setLabelText(str) -- 设置提示语
    labelText(str) -- 获取提示语
    setCancelButtonText(cancelButtonText_str) -- 设置取消按钮的文本
    wasCanceled() -- 判断是否已取消

    setBar(QProgressBar bar) -- 设置一个进度条空间
    setCancelButton(QPushButton cancelButton) -- 设置一个取消按钮
    setLabel(QLabel label) -- 设置一个标签(提示语)

    setMinimum(int minimum) -- 设置最小值
    minimum() -> int -- 获取最小值
    setMaximum(int maximum) -- 设置最大值
    maximum() -> int -- 获取最大值
    setRange(int minimum, int maximum) -- 设置范围
    setValue(int progress) -- 设置当前值
    value() -> int -- 获取当前值

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QProgressDialog
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('300-QProgressDialog-功能作用')
        self.resize(1000, 500)

        self.pd = QProgressDialog(self)
        self.pd.setMinimumDuration(1000)
        self.pd.setWindowTitle('标题')
        self.pd.setLabelText('提示语')
        self.pd.setCancelButtonText('取消按钮')
        self.pd.setRange(0, 10)
        self.pd.setValue(0)

        self.timer = QTimer(self.pd)
        self.timer.timeout.connect(self._timeout)
        self.timer.start(1000)

    def _timeout(self):
        if self.pd.value()+1 >= self.pd.maximum() or self.pd.wasCanceled():
            self.timer.stop()
        self.pd.setValue(self.pd.value() + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
