# 这是本人学习设计模式过程中的一个记录仓库
----

### 第一章：监听模式
### 第二章：状态模式
我们从对象的角度来考虑会有哪个类，首先不管它是什么状态，对象始终是水（H2O），所以会有一个Water类；而它又有三种状态，
我们可以定义三个状态类：SolidState、LiquidState、GaseousState；从SolidState、LiquidState、GaseousState
这三个单词中我们会发现都有一个State后缀，于是我们会想它们之间是否有一些共性，能否提取出一个更抽象的类，这个类就是状态类
（State）。这些类之间的关系可用图表示，如图2-1所示。[插图]图2-1 水的三态相关类之间的关系
### 第三章：中介模式
中介模式主要有以下三个角色，在设计中介模式时要找到并区分这些角色：
（1）交互对象（InteractiveObject）：要进行交互的一系列对象。
（2）中介者（Mediator）：负责协调各个对象之间的交互。
（3）具体中介者（Mediator）：中介的具体实现