# 376~385-QTDesigner

普通情况下, 搭建 GUI 界面是通过手写代码创建的一个一个控件并填写样式等等, 这样做若工作量大或界面复杂时, 代码会比较混乱和庞大.

可以通过可视化的设计工具, 来按照所见即所得的方式进行设计界面, 然后"自然转换成代码". 这样做直观, 高效, 鼠标拖拖点点就完成了. 并且工作量小, 方便修改调试, 而且界面和逻辑是分离的. 在正规开发中都使用这种方式.

## 介绍

QTDesigner 中的操作方式十分灵活, 其通过拖拽的方式放置控件可以随时查看控件效果.

QTDesigner 的设计符合 MVC 的架构, 实现了视图和逻辑的分离, 从而实现了开发的便捷

QTDesigner 生成的 .ui 文件(实质上是 XML 格式的文件), 可以直接使用 (from PyQt5.uic import loadUi    loadUi("login.ui", self)), 也可以通过 pyuic5 工具转换成 .py 文件

## 安装

pip install PyQt5-tools -i https://pypi.douban.com/simple

注: 安装位置在使用 pip 安装时, 最后的几行中有说明

```
Requirement already satisfied: click in c:\users\administrator\appdata\local\programs\python\python37\lib\site-packages (from PyQt5-tools) (7.0)
```

上面其实不是包安装的位置, 但是可以知道 python 安装的位置, 然后在 python 安装根目录下进入 script 目录, 这里就是第三方库的安装目录.(当前, 若有设置环境变量, 就不需要找到这个位置, 只需要知道执行文件的名字就可以执行)

#### 设计工具--designer

搭建界面

#### ui转py--pyuic5

pyuic5 $FileName$ -o ui_$FileNameWithoutExtension$.py -x


#### qrc资源转换--pyrcc5

pyrcc5 $FileName$ -o $FileNameWithoutExtension$_rc.py

## 界面初识

自上而下, 分别是菜单栏和工具栏. 再往下, 是三个栏目在同一高度上.

那么在这里, 自左向右, 分别是控件盒子(widget box), 中间是界面区, 在这里对界面进行操作, 右边是一竖排栏目.

在右边竖排栏目中, 最上面是对象树(object inspector), 属性编辑器(property Editor).

在右边竖排栏目中, 最下面是三个栏目的合集, 通过 tab 按钮来转换, 分别是 signal/Slot Editor(信号与槽), Action Edition(行为管理器), Resource Browser(资源管理器)

## 控件操作

#### 添加控件

从控件盒子(widget box)中拖拽控件到界面区

#### 修改控件

- 双击修改控件内容
- 控件四周的八个点是修改控件尺寸的, 点击拖拽即可

#### 删除控件

选中控件按 `backspace`

#### 创建父子关系

将界面区的一个控件拖拽到某个盒子控件中.

#### 控件要放到与盒子控件重合位置但不创建父子关系

若直接拖拽控件到指定位置, 因为那个位置是有盒子控件, 所以使用拖拽则肯定会创建父子关系, 可以通过右边的属性编辑器来编辑 x, y 轴的坐标.

#### 控制控件的层级

右键控件, 有 `send to back`(下移一层) 和 `bring to front`(上移一层) 两个选项, 可以控制此控件的层级. (右边的对象树(object inspector)也可以做此操作)

#### 属性操作

选中控件后, 右侧的属性编辑器(property Editor)就会展示出与此控件相关的所有属性, 可以直接在属性编辑器(property Editor)中修改属性.

一些常见和通用的属性操作在右键控件中可以直接操作.

点击属性编辑器(property Editor)中的`加号`可以添加自定义属性.

## 样式表

右键控件选择`change styleSheet...` 即可打开 `Edit Style Sheet` 窗口来修改控件样式.

选中控件, 在右边属性编辑器(property Editor)中找到 `styleSheet` 属性, 可以在列表里直接修改样式, 也可以点击输入框后的 `...` 按钮打开 `Edit Style Sheet` 窗口.

## 资源管理器

#### 创建资源管理文件

在右下角的 `Resource Browser`(资源管理器)中, 点击铅笔样式的按钮进行资源的管理.(在 `Edit Style Sheet` 窗口中, 点击 `Add Resource` 或其下拉菜单下的任何一个按钮也都可以弹出此窗口)

再次点击铅笔样式的按钮(这次点击窗口内的), 出现一个资源管理文件的管理窗口, 左下角可以新建或打开一个 `qrc` 文件.

创建 `qrc` 文件完成后, 需要创建一个前缀, 点击文件夹带加号的图标, 会新增一个前缀, 修改名称即可.

在然后点击 `add files` 文件, 添加图片资源(可多选), 添加完成后点击 `OK`

注:
    资源管理的层级比较多, `qrc` 文件相当于一个容器, 在容器内创建前缀(可多个)相当于在容器内隔开了一个个独立的空间, 在前缀中添加图片资源相当于在独立的空间中放一个个物品.

#### 打开资源管理文件

也可以打开一个已经存在的资源管理文件, 按钮在添加资源管理文件旁边. 之后的操作就相同了.


## 提升控件类型

当基础控件无法满足需求, 并且已经写好了一个自定义的控件(继承了某个控件). 那么如果在 designer 中使用呢?

首先拖拽一个控件(自定义控件继承的那个控件)到界面上, 然后右键此控件, 选择 `promote to...`.

分别填写 `promoted class name` 和 `Header file` 表单. 其中, `promoted class name` 是自定义控件的名称, `header file` 是存放这个自定义控件的文件的文件名(不要填写后缀名)

填写后点击 `Add` 按钮添加到列表中, 然后选中这一列, 点击 `Promote` 按钮提升完成.

注:
    自定义控件在软件内预览时不会有任何的效果, 必须保存后执行文件才会出现预期的效果.

## 布局管理器操作

对窗口控件设置一个布局, 通过拖拽控件盒子(widget box)中的布局控件到界面或对象树(object inspector)的窗口控件上, 都是无法对窗口控件设置布局的, 这样的操作会创建一个窗口控件下的子布局.

正确的操作是: 选中对象树(object inspector)的窗口控件, 然后点击工具栏的布局按钮, 这样就为窗口控件设置了一个布局.