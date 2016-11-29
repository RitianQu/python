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
#### 转义字符
     \n 换行
     \r 回车
     \t 水平制表
#### 字符串操作
     1 字符串的拼接和重复 （+和×）
     2 repr
#### 输入输出
     input 输入
     print 输出
     %d 传入整型
     %s 传入字符串
     %f 传入浮点型
     %% 输入%
#### 列表
     定义：列表表示一种容器类型，是任意对象的有序集合，通过索引访问其中的元素。
     表达符号：[]
     addend 增加
     extend 合并列表
     insert 在某个位置插入一个元素
     index 定位
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
     元组的用法几乎与列表一致，唯一不同的是元组不可修改，这在一些特殊需求的时候有意义。只是元组的定义中用圆括号，在初始化的时候可以用括号也可以不用。
     用途
     元组的存在看似多余但是在有些地方不可替代
     1.作为键使用的时候
     2.作为一些内建函数或者方法的返回值，不希望被修改
