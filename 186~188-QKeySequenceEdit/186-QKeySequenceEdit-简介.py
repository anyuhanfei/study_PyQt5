'''
186-QKeySequenceEdit-简介

采集键的序列(可多个)

控件允许输入QKeySequence, 它通常用作快捷方式。
当控件收到焦点时开始录制，并在用户释放最后一个关键字后一秒钟结束录制

继承自 QWidget


附:
    QKeySequence
    用来描述一个键位序列
    键位序列描述了必须一起使用以执行某些操作的键组合

    构造函数:
        QKeySequence(key_str) -- 创建一个自定义键位序列(字符串)
        QKeySequence(QKeySequence.StandardKey key) -- 创建一个标准键位序列
        QKeySequence(int k1, int k2 = 0, int k3 = 0, int k4 = 0) -- 创建一个自定义键位序列(枚举值)
        fromString(key_str)  -- 这个是静态方法

    API:
        toString() -> str -- 转换成可读字符串
        count() -- 键位个数

    1. 优先使用标准键位序列
    2. 自定义键位序列, 保证可读, 尽可能不用枚举值对应的整形数据

    键位序列分类
        自定义键位序列:
            字符串 例如: "Ctrl+S"
            枚举值 例如: Qt.Ctrl + Qt.Key_S

        标准键位序列(QKeySequence.):
            HelpContents	F1
            WhatsThis	Shift+F1
            Open	Ctrl+O
            Close	Ctrl+F4, Ctrl+W
            Save	Ctrl+S
            Quit		Ctrl+Q
            SaveAs		Ctrl+Shift+S
            New	Ctrl+N
            Delete	Del
            Cut	Ctrl+X, Shift+Del
            Copy	Ctrl+C, Ctrl+Ins
            Paste	Ctrl+V, Shift+Ins
            Preferences		Ctrl+,
            Undo	Ctrl+Z, Alt+Backspace
            Redo	Ctrl+Y, Shift+Ctrl+Z, Alt+Shift+Backspace
            Back	Alt+Left, Backspace
            Forward	Alt+Right, Shift+Backspace
            Refresh	             F5
            ZoomIn	Ctrl+Plus
            ZoomOut	Ctrl+Minus
            FullScreen	F11, Alt+Enter
            Print	Ctrl+P
            AddTab	Ctrl+T
            NextChild	Ctrl+Tab, Forward, Ctrl+F6
            PreviousChild	Ctrl+Shift+Tab, Back, Ctrl+Shift+F6
            Find	Ctrl+F
            FindNext	F3, Ctrl+G
            FindPrevious	Shift+F3, Ctrl+Shift+G
            Replace	Ctrl+H
            SelectAll	Ctrl+A
            Deselect	Ctrl+Shift+A
            Bold	Ctrl+B
            Italic	Ctrl+I
            Underline	Ctrl+U
            MoveToNextChar	Right
            MoveToPreviousChar	Left
            MoveToNextWord	Ctrl+Right
            MoveToPreviousWord	Ctrl+Left
            MoveToNextLine	Down
            MoveToPreviousLine	Up
            MoveToNextPage	PgDown
            MoveToPreviousPage	PgUp
            MoveToStartOfLine	Home
            MoveToEndOfLine	End
            MoveToStartOfDocument	Ctrl+Home
            MoveToEndOfDocument	Ctrl+End
            SelectNextChar	Shift+Right
            SelectPreviousChar	Shift+Left
            SelectNextWord	Ctrl+Shift+Right
            SelectPreviousWord	Ctrl+Shift+Left
            SelectNextLine	Shift+Down
            SelectPreviousLine	Shift+Up
            SelectNextPage	Shift+PgDown
            SelectPreviousPage	Shift+PgUp
            SelectStartOfLine	Shift+Home
            SelectEndOfLine	Shift+End
            SelectStartOfDocument	Ctrl+Shift+Home
            SelectEndOfDocument	Ctrl+Shift+End
            DeleteStartOfWord	Ctrl+Backspace
            DeleteEndOfWord	Ctrl+Del
            InsertParagraphSeparator	Enter
            InsertLineSeparator	Shift+Enter
            Cancel	Escape
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QKeySequenceEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('186-QKeySequenceEdit-简介')
        self.resize(1000, 500)

        '''创建 QKeySequenceEdit 控件'''
        QKeySequenceEdit(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
