# python
#### 什么是python：Python（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象、解释型计算机程序设计语言。
#### python程序的组成
     1.程序由模块构成
     2.模块包含语句
     3.语句包含表达式
     4.表达式建立并处理对象
#### python关键字
     循环判断
     if elif else for while break continue and or is not in
     函数模块类
     from 从某个文件当中引入模块
     import 引入某些内容
     as 当做什么 生成新的对象用
     def 定义函数
     pass 空语句占位
     lambda 定义匿名函数
     return 函数返回函数返回值
     class 定义类
     异常
     try 异常检测
     except 异常处理
     finally 最终执行 异常执行
     raise 抛出异常
     其他
     del 删除一个变量
     global 声明使用全局变量
     with 形成一个新对象
     assert 断言处理
     yield 函数的终断返回
     nonlocal 闭包
     exec 形成新的进程
#### python的核心数据类型
     数字（包含整形Int和浮点型Float） 字符串（String） 列表（List） 字典(Dict) 元组(Tuple) 集合(Set) 文件
     其他类型 ： 类类型(object) None(Nonetype) 布尔型(Boolean)
     编程单元模块类型 ： 函数(function) 模块(module) 类(class)
#### 常量与变量
     常量：不能给被改变的量
     变量：人为设定有的标识符，用来标记常量，可以被重复利用赋值
#### 标识符明明规则
     1.标识符由一个或多个字母、数字或下划线组成
     2.标识符的第一个字符必须是字母或下划线
     3.标识符不能与关键字相同
     4.python语言是严格区分大小写的
     但是在python的标识符命名中还有一些默认规则
     1.以单一下划线开头的变量名（—x）不会被from module import ×语句导入
     2.前后双下划线的变量（————x————）为系统的默认变量
     3.前面两个下划线开头的变量（————x）为类的私有变量
#### python中0为假1为真
#### ‘’‘ 原样输出
#### #coding=utf-8设置在首行或者第二行 可以在python中输出中文
#### 字符串：零个或多个字符组成的有限串行
#### a|b 与 两个数2进制进行比较 只要有一个数是1就取1
#### a&b 或 两个数2进制进行比较，只要有一个数是0就为0
#### a^b 亦或 连个数2进制进行比较，相同取0，不同取1
#### 强制转换：
     a=1.234 int（a）=1 取整数
#### import math 引用math这个数学库
     math.sqrt(a):a开方
     math.pow(a,b):a的b次方
     math.trunc(a):如果a是小数，省去小数部分，或者int（a）函数，也可以省去小数部
     math.floor(a):对a向下求整，他的值小于或等于a
     math.cell(a):对a向上求整，她的值大于或等于a
     math.factorial(a):求a的阶乘
     math.exp(a):求e的a次方
#### import random 引入random模块（随机）
     random.random():随机生成一组数
     random.choice（数据类型）：在这个数据类型中随机挑选一个
#### 转义字符
     \n 换行
     \r 回车
     \t 水平制表
#### 字符串操作
     1 字符串的拼接和重复 （+和×）
     2 repr
     a.find('a')查找字符串a，找到返回索引值，找不到返回-1
     a.replace('a','sf'):对全局进行搜索和替换
     a.split(',')把，作为分隔符把他们分割成单一的部分
     a.upper()把a的字符全部都编程大写的
     a.isalpha()检查a中是否全部是字母，是返回true，否则返回false
     切片操作
     a='asdasd'
     a[1]: 's'
     a[-1]: 'd'
     a[1:3]: 'sd'
     a[1:]: 'sdasd'
     a[0:3]: 'asd'
     a[:-1]: 'asdas'
     a[:]: 'asdasd'
     a[::-1] 'dsadsa' 逆向取值 每一个取一个
     a[::-2] 'das' 　　逆向取值　每两个取一个
     a[-1:-5:-2]  'da'
     a[2::-2] 'da' 在２前边的每两个取一个
#### 输入输出
     input 输入
     print 输出 python2中不换后加，python3中不换行后加，end“
     %d 传入整型
     %s 传入字符串
     %f 传入浮点型
     %% 输入%
#### 列表
     定义：列表表示一种容器类型，是任意对象的有序集合，通过索引访问其中的元素。
     表达符号：[]
     append 增加 append（‘a’）向列表的末端加入a
     extend 合并列表 extend（[5,6]）合并两个列表
     insert 在某个位置插入一个元素 insert(3,2)在下标为3的位置插入2
     index 定位 index(5)显示5的下标
     count 计数
     sort 排序 （默认从小到大）sort（cmp=numsort）从大到小
     reverse 反转
     del 删除
     remove 删除
     pop 弹出
#### 元组
     定义：元组是一种容器类型，是任意对象的有序集合，通过索引访问其中的元素
     长度固定，对象不可变
     表达符号：（）
     元组的操作
     元组的用法几乎与列表一致，唯一不同的是元组不可修改，这在一些特殊需求的时候有意义。只是元组的定义中用圆括号，  
     在初始化的时候可以用括号也可以不用。
     用途
     元组的存在看似多余但是在有些地方不可替代
     1.作为键使用的时候
     2.作为一些内建函数或者方法的返回值，不希望被修改
#### 字典：通过键值对来实现元素的存取，是一种无序的集合，容器可变，可改变的，没有运算
     键：可以是数字或字符串，值什么类型都可以，内部查找是散列查找
     d.keys() 列出所有的键
     d.values() 列出所有的值
     d.items() 列出所有的键和值，每一对形成一个元组
     d.get("a") 获取键a的值
     d.update(d2) 合并
     d.pop(key) 弹出某一个 字典中弹出的一个消失
     del d[key] 删除 用中括号
     a = dict(zip(x,y))两个元组x,y或者其他转换成字典
#### 集合：无序排列，可包含不同的数据类型，支持成员关系测试，花括号{}，只能整体使用不可以取数，不可以有重复的项
     s = {[1,2]} 定义一个集合
     s = set([]) 定义一个空集合
     s = {1,2} 定义一个集合
     s = frozenset({1,2,3}) frozenset 定义的列表不可变
#### 集合方法：
     s.add(5) 添加一个值
     s.pop() 随机弹出
     s.cleat() 清空集合
     s.remove() 删除集合中某个数
     s.diffrence(s1) 列出s中有s1没有的项
     s.union(s1) 合并s和s1 相同的只取一项
     s.update(s1) 合并s和s1 相同的只取一项
#### 集合运算：
     s - s1  减去s1中和s中重复的项
     s | s1 合并（并集）
     s & s1 相同的（交集）
     s ^ s1 不相同的|（补集）
#### 数据类型总结：
     bool：true false 逻辑运算得到的结果为bool类型
     nonetype：none用做空，占位变量
     数字类型 整型 不可变的 数学运算位运算等
     浮点型
     字符串类型  有序的  不可变的 + * 运算  属性方法 切片操作 in逻辑
     列表       有序的  可变的   + * 运算  属性方法 切片操作 in逻辑
     元组       有序的  不可变的 + * 运算  属性方法 切片操作 in逻辑
     字典       无序的  可变的            属性方法         in逻辑
     集合  set  无序的  可变的 -|^&运算   属性方法         in逻辑
     frozenset 无序的  不可变的 -|^&运算  属性方法         in逻辑
#### import copy
     如果对copy中的属性进行修改，会对copy有影响，不会影响deepcopy
     d = [1,2,[3,4],5]对d进行任何操作都会影响m对【3，4】操作会影响m l 不会影响k
     m=d
     l = copy.copy(d)
     k = deepcopy(d)
#### import random引入随机模块
     import.randint（1，10）随机出现1到10之间的数
#### 语句结构 分支（选择）结构 if else elif 循环结构 for in while else break continue
#### if 判断条件：
     执行内容/pass pass：占位符 什么都不执行
     if 判断条件：
     执行内容
     else：如果if条件不成立时执行这个
     执行内容
#### 三元运算：
     x if 判断条件 else z 如果判断条件是真返回x，如果判断条件是假返回z
     range 快速生成一个序列
     range(i,j,[步进值])：i：起始值 j：终止值但不包括
     range（10）生成一个0到10的序列
     srange（10）：形成一个迭代对象
#### for i in n: n可以使字符串 元组 序列 表达式 等
     执行代码内容
     迭代指重复执行一个命令
     []
#### while判断语句：
     执行内容
     else：
     执行内容
     break：循环结构
     continue：跳出本次循环，执行下次判断，再循环
#### 序列
     序列：是指列表，字符串，元组三个类型
     特点：1.可以通过索引来抓取特定的项目
          2.可以切片
      max(x):返回最大值，返回x中最大的值
      min(x):返回最小值，返回x中最小的值
      cmp(x,y):比较两个序列值是否相等。字母的字符串长于数字的字符串1表示前面长于后面 -1表示后面长于前面 0表示相等
#### 继承：继承描述了基类的属性如果“遗传”给派生类。一个子类可以继承它的基类的任何属性，不管是数据属性还是方法。
     简单总结继承的意图或者好处：
     1.可以实现代码重用，但不是仅仅实现代码重用，有时候根本就没有重用。
     2.实现属性和方法继承
     3.一个类在继承父类的同时也有自己特有的方法和属性，当与父类重名的时候会覆盖掉父类的方法和属性。
#### 多重继承
#### 继承检测
     可以使用issubclass()函数来检测一个类是否继承于另一个类>>>issubclass(Class1,Class2)
#### super函数
     初始化
     函数的继承分一般方法的继承还有点不同，在子类中无法直接使用父类中的初始化函数。在子类覆盖父类  
     的方法后如果海西哪个要使用父类中的方法就需要借助super函数。这个函数的目的就是帮组程序员找出  
     相应的父类，然后方便调用相关的属性。一般情况下，程序员可能仅仅采用非绑定方式调用祖先类方法。使用
     super()可以简化搜索一个合适祖先的任务，并且在调用它时，替你传入实例或类型对象。 
#### super函数的参数，第一个是当前子类的类的名字，第二个self，然后是点号，点号后面是所要调用的父类的方法。
#### 封装
     继承。封装和多态被认为是面向对象编程的三个重要特征。但是封装和多态无论在理解上还是实践上都是有争议的话题。这些争议多来自于对同意现象的不同  
     理解，还有不同的编程语言的事项和对多态封装的诠释角度不同。不管有多少不同的理解方式，我们都药对这两个概念有所了解，这也是编程水平进阶的必须。
#### 封装和私有化
     在程序设计中，封装是对对象的一种抽象，即将某些部分隐藏起来，对程序（或者模块）外部不可见，无法调用。  
     封装离不开“私有化”。就是将类或者函数中的某些属性限制在某个区域之内，外部无法调用。Python中私有化的  
     方法比较简单，就是在准备私有化的属性（方法或者数据）名字前面加上双下划线。
#### 多态
     多态是值面向对象程序执行时，相同的信息可能会送给多个不同的类别对象，系统可依据对象所属类别，引发对应  
     类别的方法而又不同的行为。简单来说就是相同的信息给予不同的对象会引发不同的动作。
#### 魔法方法、属性和迭代器
     在Python中，有的方法和属性名称前后都会有两个下划线，这种写法很特别，在之前我们提到过，我们跟这种方法  
     或者属性叫做特殊方法（属性）夜叫做魔法方法（属性）。一般这种方法都是由系统定义的，有特殊的含义，可以  
     通过dir（）函数进行查看一个对象有什么魔法方法（属性）。
     class A（）：
     a.__doc__ 文档说明
     a.__class__ 类名
     a.__dict__ 字典
     __getattr__ 调用一个不存在的变量时会调用getattr
     __setattr__ 给一个不存在的属性赋值时会调用setattr
#### 迭代器和生成器
     迭代器
```python
     #class TestIter:
     def __init__(self,a):
         self.a = a
     def __iter__(self):
         return self
     def __next__（self）:
         self.a += 1
         return self.a ** 2
     a = TestIter(2)
     print (next(a))
     print (a.__next__()) 与上一行表达意思相同，python2，3都可以使用
```
     生成器
     生成器是一次生成一个值的特殊类型函数。可以将其视为可恢复函数。调用该函数将返回一个可用于生成连续x值的生成器，简单的说就是在函数的执行过程
     yield语句会把你需要的值返回给调用生成器的地方，然后退出函数，下一次调用生成器函数的时候又从上次中断的地方开始执行，而生成器内的素有变量参数
     都会被保存下来供下一次使用。
     ```python
     #def fib(max):
         a,b=0,1
         while a<max:
             yield a
             a,b = b,a+b
     for i in fib(20):
          print(i)
     ```
#### 数据结构
#### 1.数据
     数据即信息的载体，是能够输入到计算机中并且能被计算机识别、存储和处理的符号总称。
     
#### 2.数据元素
     数据元素是数据的基本单位，又称之为记录。一般，数据元素由若干基本项（或称字段、域、属性）组成。
#### 3.数据类型
     数据类型是对数据元素取值范围与运算的限定。
#### 4.数据结构（DS）可用形式化语言描述，即DS是一个二元组
#### 逻辑结构和存储结构
     逻辑结构：表示数据运算之间的抽象关系（如邻接关系、从属关系等），按每个元素可能具有的直接前趋数和直接后继数将逻辑结构分为”线性结构“和”非线性结构
     存储结构：逻辑结构在计算机中的具体实现方法，分为顺序存储方法、链接存储方法、索引存储方法、散列存储方法。
     数据运算：对数据进行的操作，如插入、删除、查找、排序等。
#### 逻辑结构
     如果只是描述数据结构中数据元素之间的联系规律，即逻辑关系，则称此时的数据结构为数据的逻辑机构。它是从具体问题中抽象出来的数学模型，与机器无关。
     线性结构
     对于数据结构课程而言，简单地说，线性结构式n个数据元素的有序集合。
     集合中比存在唯一的一个”第一个元素“
     结合中必存在唯一的一个”最后的元素“
     除最后元素之外，其它数据元素均有唯一的”后继“
     除第一元素外，其它数据元素均有唯一的”前驱“
     树形结构（层次结构）
     树形结构指的是数据元素之间存在着”一对多“的树形关系的数据结构，是一类重要的非线性数据结构。
     在树形结构中，树根结点没有前驱结点，其余每个结点有且只有一个前驱结点。叶子结点没有后续结点，其余每个结点的后续结点数可以是一个也可以是多个。
     图状结构（网状结构）
     图是一种比较复杂的数据结构。在图结构中任意两个元素之间都可能有关系，也就是说这是一种多对多的关系。
     其他结构
     除了以上集中常见的逻辑结构外，数据结构中还包含其他的结构，比如集合等。有时根据实际情况抽象的模型不止是简单的某一种，也可能拥有更多的特征。
#### 存储结构
     数据的存储结构指的是数据的逻辑结构在计算机存储器中的映像。存储结构是通过计算机语言所编制的程序来实现的，因而是依赖于具体的计算机语言的。
     1.顺序存储：将数据结构中各元素按照其逻辑顺序存放于存储器一片连续的存储空间中
     2.链式存储：将数据结构中各元素分不到存储器的不同点，用地址（或链指针）方式建立它们之间的联系，由此得到的存储结构为链式存储结构。
     3.索引存储：在存储数据的同时，建立一个附加的索引表，即索引存储结构=数据文件+素引表
     4.散列存储：根据数据元素的特殊字段（称为关键字key），计算数据元素的存放地址，然后数据元素按地址存放，所得到的存储结构为散列存储结构
#### 运算
     数据元素包含的许多值是非数值型的（如文字、日期等数据），对其进行的操作（或运算）也不再是+-*/等数学运算，而是注入增删改查这样的运算。
#### 算法
     数据结构 + 算法 = 程序
     算法设计：取决于决定的逻辑结构
     算法实现：依赖于采用的存储结构
###  算法基础
     算法是一个有穷规则（或语句、指令）的有序集合。它确定了解决某一个问题的一个运算序列。对于问题的初始输入，通过算法有限步的运行，产生一个或多个数出
###  算法的特性
     有穷性 ———— 算法执行的步骤（或规则）是有限的
     确定性 ———— 每个计算步骤无二义性
     可行性 ———— 每个计算步骤能够在有限的时间内完成
     输入   ———— 算法有一个或多个外部输入
     输出   ———— 算法有一个或多个输出
###  评价算法好坏的方法
     正确性：运行正确是一个算法的前提
     可读性：容易理解，同意编程和调试、容易维护。
     健壮性：考虑情况全面，不容易出现运行错误
     时间效率高：算法小号的时间少
     储存量低：占用较少的存储空间
###  时间复杂度的计算
     1、将表达式中所要运行的次数加和
     2、如果没有不定项，那么她的常量为o（1），如果有不定项，取不定项的最高次幂
     3、如果最高次幂前有系数，去掉系数，最高次幂为时间复杂度
#### 线性表
     线性表是信息表的一种形式，表中数据元素之间满足线性关系（或线性结构），是一种最基本、最简单的数据结构类型。线性表的定义是描述其逻辑结构，增删改查
     我们通常对一个数据模型的分析也是从逻辑结构、存储结构、运算三个部分来进行分析。
###  顺序存储结构的特点：
     1.逻辑上相邻的元素ai，ai+1，其存储位置也是相邻的；
     2.对数据元素ai的存取为随机存取或按地址存取
     3，存储密度高
###  顺序存储结构的不足：
     对表的插入和删除等运算时间复杂度较差
#### 线性表的链式存储
     相对于顺序存储，链式存储更加接近我们传统意义的列表，通常也叫做链表。
     将线性表中各元素分布在存储器的不同存储快，称为结点，每个结点（尾结点除外）中都持有一个指向下一个结点的引用，这样所得到的存储结构为链表结构
#### 双向循环列表
     在单链表中，查找后继，耗时仅为o（1），因为取之后继的引用即可。单查找其前驱，则需从链表的头指针开始，找到其结点前一结点既是。故运算时间复杂度
     依赖表厂n，耗时为o（n）。另外，若链表中有一指针被破坏，则整个链表脱节。这是单链表的不足，为此，引入双向链表
#### 栈
     栈是限制在一段进行插入操作和删除操作的线性表（俗称堆栈），允许进行操作的一段称为”栈顶“，另一端称为”栈底“，当栈中没有元素是为”空站“。
     特点：后进先出或者叫后进先出
     栈的操作有入栈（压栈），出栈（弹栈），判断栈的空满等操作。
#### 队列
     队列是限制在两端进行插入操作和删除操作的线性表，允许进行存入操作的一端称为”队尾“，允许进行删除操作的一端称为”队头“。当线性表中没有元素
     称为”空队“。特点：先进先出
     队列的操作有入队，出队，判断队列的空满等操作。
     from collections import deque
     queue = deque
     queue.append('')
     queue.popleft()左弹出
#### 树
     树的概念
     树是n个节点的有限集合T，它满足两个条件：有且仅有一个特定的称为根的节点；其余的节点可以分为m个互不相交的有限集合，其中每一个集合又是一棵树
     并称为其根的字数
     表示方法
     树形表示法、目录表示法
###  基本概念
     一个节点的字数的个数称为该节点的度数，一棵树的度数是指该树中节点的最大度数
     度数为零的节点称为输液或终端节点，度数不为零的节点称为分支节点，除根节点外的分支节点称为内部节点。
     一个节点的子树之根节点称为该节点的子节点，该节点称为它们的福节点，同一节点的各个子节点之间称为兄弟节点。一棵树的根节点没有父节点
     节点的层数等于父节点层数加一，根节点的层数定义为一。树中节点层数的最大值称为该树的高度或深度。
     若树种每个节点的各个子树的排列为从左到右，不能交换，即兄弟之间是有序的，则该树称为有序树。一般的树是有序树。
     m棵互不相交的树的集合称为森林。树去掉根节点就成为森林，森林加上一个新的根节点就成为树。
     树的逻辑结构：树中任何节点都可以有零个或多个直接后继节点（子节点），但至多只有一个直接前趋节点（父节点），根节点没有前趋节点，叶节点没有后继节点
     输的存储结构：比较综合的存储方式
###  二叉树
     是n个节点的有限集合，它或者是空集（n=0），或者是由一个根节点以及两棵互不相交的、分别称为左子树和右子树的二叉树组成。
     二叉树与普通有序树不同，二叉树严格区分左右孩子，即使只有一个子节点也要区分左右。
###  二叉树的性质
     二叉树第i（i>=1）时有2k-1个节点的二叉树
     深度为k（K>=1）DE二叉树最多有2k-1个节点
     在任意一颗二叉树中，树叶的数目比度数为2的节点的数目多一
     总节点数为各类节点之和：n = n0 +2*n2+1-->n0 = n2 +1
     满二叉树：深度为k(k>=1)时有2k-1个节点的二叉树
     完全二叉树：只有最下面两层有度数小于2的节点，且最下面一层的叶节点集中在最左边的若干位置上。
     具有n个节点的完全二叉树的深度为log2n +1
###  二叉树的遍历
     遍历：沿某条搜索路径周游二叉树，对树中的每一个节点访问且仅访问一次
     由于二叉树的递归性质，遍历算法也是递归的。四种基本的遍历算法如下：
     先序遍历：先访问树根，再访问左子树，最后访问右子树；
     中序遍历：先访问左子树，再访问树根，最后访问右子树；
     后序遍历：先访问左子树，再访问右子树，最后访问树根
     层次遍历，从根节点开始，逐层从左向右进行遍历
###  哈弗曼树（最优二叉树）
     哈弗曼树，又称为最优树，是带权路径长度最短的树，有着广泛的应用。
     从树中一个节点到另外一个节点的分支构成一条路径，分支的数目称为路径的长度。树的路径长度是指从树根到每个节点的路径长度之和。
#### 图的基本概念
     图是一种非线性数据结构。
     有向图：
     设v1、v2为图中的两个顶点，若关系v1，v2存在方向性，则称相应的图为有向图。<v1,v2>∈R，表示从顶点v1到v2的一条弧。v1为弧尾，v2为弧头
     无向图：
     设v1、v2为图中的两个顶点，若关系无方向性，即：当∈R时，必有∈R，则称此图为无向图。
     稀疏图和稠密图弧或边的条数很少的图称为稀疏图，繁殖称为稠密图。
     网：若在图的关系或(v1,v2)上附加一个值w：
     称w为弧后边上的权。带权的图称为网。权w的具体含义视图在不同领域的应用而定，如顶点表示城市，权w可以为两个城市间的距离等等。
     子图：
     设图G=(V,R)、G1=(V1,R1),若G1属于G，则称G1为G的子图
     顶点的度：
     设E为无向图G中的边的集合，V、V1为图中的顶点。若(V,V1)∈E,则称V和V1互为邻接点，或称V与V1相邻接，边(V,V1)与V、V1相关联。
     某顶点V的度记为D（V），代表与V相关联的边的条数。
     路径：
     若从顶点V出发，经过某些顶能到达另一顶点V1，则称V与V1之间存在一条路径。由于图中两顶点间的关系是任意的，且可能存在回路，故两定点间可能存在
     多条路径（树中根到叶节点的路径是唯一的）。无向图中，顶点V到V1的第i条路径是一个顶点序列。路径上边的条数定义为该路径的长度。无向图中路径的
     （V0,V1,V2,V5,V3）长度为4.有向图中，两顶点间的路径也是有向的。路径(v0,v1lv2lvv5,v3)的长度为4.另外若路径（v1,v2...vn)中顶点不重复
     出现，则称其为简单路径；若路径中止呕第一顶点v1与最后一个顶点vn相同，则称其为简单回路或简单环。
     连通性：
     在无向图中，两顶点v与v1间存在路径，称v与v1是连通的；若图中任意两顶点都连通，则称该图为无向连通图。
     图的表示方法
     由于图中顶点键的关系（弧或边）无规律，故对图的存储较之表和树药复杂写，需要根据图的具体应用来构造图的存储结构。常用的存储表示有‘数组表示法’
     ‘邻接表’‘十字链表’和‘邻接多重表’等方法。在python也可以简单的使用字典和列表共同标识图的关系。
#### 图的遍历
     图的遍历是树的遍历的推广，是按照某种规则（或次序）访问图中各顶点一次且仅一次的操作，亦是将网状结构按某种规则线性化的过程
     由于图存在回路，为区别一顶点是否被访问过和避免顶点被多次访问，在遍历过程中，应记下每个访问过的顶点，即每个顶点对应有一个标识位，
     初始为False，一旦该顶点被访问，就将其置为True，以后若有碰到该顶点时，视其标识位的状态，而决定是否对齐访问。
     对图的遍历通常有‘深度优先搜索’和‘广度优先搜索’方法
###  深度优先遍历
     算法描述：
     （1）访问初始顶点v并标记顶点v已访问。 
     （2）查找顶点v的第一个邻接顶点w。 
     （3）若顶点v的邻接顶点w存在，则继续执行；否则回溯到v，再找v的另外一个未访问过的邻接点。 
     （4）若顶点w尚未被访问，则访问顶点w并标记顶点w为已访问。 
     （5）继续查找顶点w的下一个邻接顶点wi，如果v取值wi转到步骤（3）。直到连通图中所有顶点全部访问过为止。
###  广度优先遍历
     算法描述：
     （1）顶点v入队列。 
     （2）当队列非空时则继续执行，否则算法结束。 
     （3）出队列取得队头顶点v；访问顶点v并标记顶点v已被访问。 
     （4）查找顶点v的第一个邻接顶点col。 
     （5）若v的邻接顶点col未被访问过的，则col入队列。 
     （6）继续查找顶点v的另一个新的邻接顶点col，转到步骤（5）。直到顶点v的所有未被访问过的邻接点处理完。转到步骤（2）。
#### 图的相关算法
     最短路径问题
     其中，顶点A～E表示城市，边上权可为两城市间的里程、乘车速度、耗费等等。咨询系统要解决的基本问题是：从某城市到另一城市，如何选择一条周转次数
     最少的路线。即如何寻找从一顶点到另一顶点所含边数最少的路径。可以从指定的顶点出发，对图作广度优先搜索，一旦遇到目标顶点就终止，由此得出两点
     间边数最少路径。例如从图中顶点A出发，寻找到达顶点C的边数最少路径，为（A,B,C），周转次数最少为1。但是显然，从（A,B,C）改为从(A,D,C)为好，
     即除了考虑周转次数外，还应考虑里程、费用、速度等问题，它们是赋在边上的权。此时，两顶点间路径长度L定义为路径上边的权值之和。两顶点间可能存在
     多条路径，路径长度最短的那条路径为最短路径（Shortest Path）。
     解决带权有向图中两顶点间最短路径问题有两个经典算法，分别为Dijkstra（迪杰斯特拉）算法和Floyd（弗洛伊德）算法。
#### 拓扑排序
     有向无环图是一种重要的数据结构，在实际中有着重要的应用，它是描述一项工程或系统的进行过程的有力工具。 对一项工程而言，可分为若干个子工程，
     子工程之间通常受着一定条件的制约。人们关心的是工程是否能够顺利进行，这就可以转化为检测一个有向图是否存在环的问题，通常采用拓扑排序的方法来检测。
     拓扑排序的算法思想是:
     (1)在有向图中选择一个没有前驱的顶点并且输出。
     (2)从图中删除该顶点和所有以它为尾的弧。重复上述两步 , 直到图中全部顶点均已输出，或者图中不存在无前驱的顶点为止。后一种情况说明图中存在环。
     在计算机中实现时 ,我们采用邻接表作为图的存储结构。为实现方便起见,在头结点中另设一个存放顶点入度的数组,则入度为 0的顶点为无前驱的顶点，
     另外，删除顶点和所有以它为尾的弧的操作,可以转换为让弧头顶点的入度减一来实现。为重复检查入度为0的顶点,需要另设一个栈来存放所有入度为零的顶点。
#### 排序
     1.冒泡排序
     2.选择排序
     3.插入排序
     4.快速排序
#### 查找
     二分法查找
     当数据量很大适宜采用该方法。采用二分法查找时，数据需是排好序的。主要思想是：设查找的数组取件为array[low,hgih]
     1.确定该期间的中间位置k
     2.将查找的值t与array[k]比较。若相等，查找成功返回次位置；否则确定新的查找区域，继续二分查找。
#### 哈希算法介绍
     哈希算法将任意长度的二进制映射为较短的固定长度的二进制值，这个小的二进制值称为哈希值。哈希值是一段数据唯一且及其紧凑的数值表示形式。
     如果散列一段明文而且哪怕只更改该段落的一个字母，随后的哈希都将产生不同的值。要找到散列为同一个值的两个不同的输入，在计算上是不可能的，
     所以数据的哈希值可以检验数据的完整性。一般用于快速查找和加密算法。
     Hash表，又称散列表。在前面讨论的顺序、折半、分块查找和树表的查找中，其ASL的量级在O（n）～O（log2n）之间。不论ASL在哪个量级，
     都与记录长度n有关。随着n的扩大，算法的效率会越来越低。
