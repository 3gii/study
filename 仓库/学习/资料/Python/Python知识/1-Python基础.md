[TOC]

#### 1. Python中的编码

Python2中默认的编码格式是ASCII格式，在读取中文时会报错，解决方案

在文件开头加入`# -*- coding: utf-8 -*-`或者`#coding=utf-8`

注意：第二种方式`=`两边不能有空格

>在Pycharm里设置文件的编码 file>Settings>Editor>File encodings

#### 2. 设置文件可执行

- 文件开头添加`#!/usr/bin/pythn`
- 文件开头添加`#!/usr/bin/env python`

#### 3. 语法规则

* 在同一行写多条语句时用`;`隔开

#### 4. 数据类型

**1) 数字类型**

* int

  > 在Python2.2以后的版本中，int类型数据溢出后会自动转为long类型。在Python3中long类型被移除，用int代替

* float
* complex
  `3.14+5j`
* bool

  > Python2中没有bool类型，它用数字0表示False，用1表示True。在Python3中，True和False被定义成关键字，但值依然是1和0，可以和数字相加。

**2) 非数字类型** 

* str

* tuple

* list

* dict

  > 字典的键必须唯一，且是不可变类型。字典是无序的

* set

**3) 判断数据类型** 

* type()

  不会认为子类是一种父类类型

* isinstance()

  会认为子类是一种父类类型

####5. 运算符

**1) 算术运算符**

* +
* -
* *
* /
  真正的除法，非地板除
* %
* **
* //
  用于地板除

**2) 比较运算符**

* ==
* !=
* \>
* <
* \>=
* <=

**3) 赋值运算**

* =
* +=
* -=
* *=
* /=
* %=
* **=
* //=

**4) 位运算符**

* &
* |
* ^
* ~
  `~x`类似于`~x-1`
* \>>
* <<

**5) 逻辑运算符**

* and
  `x and y` 如果`x`为`False`, 返回`False`否则返回`y`的计算值
* or 
  `x or y` 如果`x`为`True`, 返回`x`的值，否则返回`y`的计算值
* not

**6) 成员运算符**

* in 
* not in

**7) 身份运算符**

* is
  `x is y`类似` id(x) == id(y)`如果引用的是同一个对象返回`True`,否则返回`False`

* not is

  `x not is y`类似` id(x) != id(y)`如果引用的不是同一个对象返回`True`,否则返回`False`

* 与`==`或`!=`的区别

  `is`和`not is`判断的是两个变量引用对象，`==`和`!=`判断的是引用变量的值

**8) 运算符优先级**

| 运算符                   | 描述                                                   |
| ------------------------ | ------------------------------------------------------ |
| **                       | 指数 (最高优先级)                                      |
| ~ + -                    | 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@) |
| * / % //                 | 乘，除，取模和取整除                                   |
| + -                      | 加法减法                                               |
| >> <<                    | 右移，左移运算符                                       |
| &                        | 位 'AND'                                               |
| ^ \|                     | 位运算符                                               |
| <= < > >=                | 比较运算符                                             |
| <> == !=                 | 等于运算符                                             |
| = %= /= //= -= += *= **= | 赋值运算符                                             |
| is is not                | 身份运算符                                             |
| in not in                | 成员运算符                                             |
| and or not               | 逻辑运算符                                             |

#### 6. 数字(Number)

**1) 常见数字类型举例**

| int    | float      | complex    |
| ------ | ---------- | ---------- |
| 10     | 0.0        | 3.14j      |
| 100    | 15.20      | 45.j       |
| -786   | -21.9      | 9.322e-36j |
| 080    | 32.3+e18   | .876j      |
| -0490  | -90.       | -.6545+0J  |
| -0x260 | -32.54e100 | 3e+26J     |
| 0x69   | 70.2-E12   | 4.53e-7j   |

**2) 数字类型之间的转换**

* int(x)
* float(x)
* complex(x)
  将`x`转到一个复数，实部为`x`，虚部为`0`
* complex(x, y)
  将`x`和`y`转换到一个复数，实部为`x`，虚部为`y`, `x`和`y`是数字表达式

**3) 运算**

* // 
  得到的并不一定是整数，与分母和分子的数据类型有关系

* 在不同的机器上浮点数运算的结果可能不同
* 在交互模式中，最后被输出的表达式结果被赋值给变量`_`

**4) 随机数函数**

| 函数                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [choice(seq)](http://www.runoob.com/python3/python3-func-number-choice.html) | 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。 |
| [randrange ([start,\] stop [,step])](http://www.runoob.com/python3/python3-func-number-randrange.html) | 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1 |
| [random()](http://www.runoob.com/python3/python3-func-number-random.html) | 随机生成下一个实数，它在[0,1)范围内。                        |
| [seed(\[x])](http://www.runoob.com/python3/python3-func-number-seed.html) | 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。 |
| [shuffle(lst)](http://www.runoob.com/python3/python3-func-number-shuffle.html) | 将序列的所有元素随机排序                                     |
| [uniform(x, y)](http://www.runoob.com/python3/python3-func-number-uniform.html) | 随机生成下一个实数，它在[x,y]范围内。                        |

**5) 三角函数**

| 函数                                                         | 描述                                              |
| ------------------------------------------------------------ | ------------------------------------------------- |
| [acos(x)](http://www.runoob.com/python3/python3-func-number-acos.html) | 返回x的反余弦弧度值。                             |
| [asin(x)](http://www.runoob.com/python3/python3-func-number-asin.html) | 返回x的反正弦弧度值。                             |
| [atan(x)](http://www.runoob.com/python3/python3-func-number-atan.html) | 返回x的反正切弧度值。                             |
| [atan2(y, x)](http://www.runoob.com/python3/python3-func-number-atan2.html) | 返回给定的 X 及 Y 坐标值的反正切值。              |
| [cos(x)](http://www.runoob.com/python3/python3-func-number-cos.html) | 返回x的弧度的余弦值。                             |
| [hypot(x, y)](http://www.runoob.com/python3/python3-func-number-hypot.html) | 返回欧几里德范数 sqrt(x*x + y*y)。                |
| [sin(x)](http://www.runoob.com/python3/python3-func-number-sin.html) | 返回的x弧度的正弦值。                             |
| [tan(x)](http://www.runoob.com/python3/python3-func-number-tan.html) | 返回x弧度的正切值。                               |
| [degrees(x)](http://www.runoob.com/python3/python3-func-number-degrees.html) | 将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0 |
| [radians(x)](http://www.runoob.com/python3/python3-func-number-radians.html) | 将角度转换为弧度                                  |

**6) 数字常亮**

| 常量 | 描述                                  |
| ---- | ------------------------------------- |
| pi   | 数学常量 pi（圆周率，一般以π来表示）  |
| e    | 数学常量 e，e即自然常数（自然常数）。 |

#### 7. 字符串

**1) 切片**

`str[start:end:step]` 字符串反转[::-1]  还可以用在`tuple`和`list`

**2) 获取**

* str[index]
* str.index[sub_str]

**3) 判断**

- isalpha()
  都是字符
- isdecimal()
  都是数字
- islower()
  都是小写字符
- isupper()
  都是大写字符
- startswith(str)
  是否以str开头
- endswith(str)
  是否以str结尾

**4) 查找替换**

- find(str, start=0, end=len(string))
- rfind(str, start=0, end=len(string))
- index(str, start=0, end=len(string))
- rindex(str, start=0, end=len(string))
- replace(old_str, new_str, num=string.count(old))

**5) 拆分连接**

- partition(str)
  将字符串分成三个元组（str前，str，str后）
- rpartition(str)
- split(str="",num)
  num有指定值时，分割num+1个字符串​
- splitlines()
  按照("\r", "\n", "\r\n")分割
- str1 + str2
- str.join(seq)
  以str作为分隔符，将seq中的所有元素合并成一个新的字符串

**6) 大小写转换**

- lower()
- upper()

**7) 文本对齐**

​	长度不够时空格填充

- ljust(width)
- rjust(width)
- center(width)

**8) 去除空白**

- lstrip()
- rstrip()
- strip()

**9) 重复**

* \* 还可以用在`list`和`tuple`

**10) 转换可运算类型**

* eval(str)

**11) 转义字符**

| 转义字符     | 描述                                         |
| ------------ | -------------------------------------------- |
| \\(在行尾时) | 续行符                                       |
| \\\          | 反斜杠符号                                   |
| \\'          | 单引号                                       |
| \\"          | 双引号                                       |
| \a           | 响铃                                         |
| \b           | 退格(Backspace)                              |
| \e           | 转义                                         |
| \000         | 空                                           |
| \n           | 换行                                         |
| \v           | 纵向制表符                                   |
| \t           | 横向制表符                                   |
| \r           | 回车                                         |
| \f           | 换页                                         |
| \oyy         | 八进制数，yy代表的字符，例如：\o12代表换行   |
| \xyy         | 十六进制数，yy代表的字符，例如：\x0a代表换行 |
| \other       | 其它的字符以普通格式输出                     |

**12) 原始字符串**

* r/R'str'

**13) 字符串格式化**

| 符   号 | 描述                                 |
| ------- | ------------------------------------ |
| %c      | 格式化字符及其ASCII码                |
| %s      | 格式化字符串                         |
| %d      | 格式化整数                           |
| %u      | 格式化无符号整型                     |
| %o      | 格式化无符号八进制数                 |
| %x      | 格式化无符号十六进制数               |
| %X      | 格式化无符号十六进制数（大写）       |
| %f      | 格式化浮点数字，可指定小数点后的精度 |
| %e      | 用科学计数法格式化浮点数             |
| %E      | 作用同%e，用科学计数法格式化浮点数   |
| %g      | %f和%e的简写                         |
| %G      | %f 和 %E 的简写                      |
| %p      | 用十六进制数格式化变量的地址         |

格式化操作符辅助指令:

| 符号  | 功能                                                         |
| ----- | ------------------------------------------------------------ |
| *     | 定义宽度或者小数点精度                                       |
| -     | 用做左对齐                                                   |
| +     | 在正数前面显示加号( + )                                      |
| <sp>  | 在正数前面显示空格                                           |
| #     | 在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X') |
| 0     | 显示的数字前面填充'0'而不是默认的空格                        |
| %     | '%%'输出一个单一的'%'                                        |
| (var) | 映射变量(字典参数)                                           |
| m.n.  | m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)        |

Python2.6 开始，新增了一种格式化字符串的函数 [str.format()](http://www.runoob.com/python/att-string-format.html)，它增强了字符串格式化的功能。

**14) Unicode字符串**

在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 **u**。

#### 8. 列表

**1) 添加**

- insert(索引, 数据)
  指定的位置前有空元素时会补位
- append(数据)
  将数据作为整体追加到列表
- extend(iterable)
  将可迭代数据拆包后追加到尾部，相当于list1 += iterable

**2) 删除**

- del 列表[索引]
  直接从内存中删除，同del() 还可以用在其它类型数据
- 列表.remove(数据)
  删除第一次出现的元素
- 列表.pop(索引)
  不指定索引时，删除最后一个元素
- 列表.clear()
  清空列表，列表本身还在

**3) 修改**

- 列表[索引] = 数据
  索引不存在会报错

**4) 查询**

- 列表[索引]
- 列表.index(数据)
  查询第一次出现的元素的位置.没有会报错
- 列表.count(数据)
- if 数据 in 列表
- len(列表)

**5) 排序**

- 列表.sort()
  默认升序，列表.sort(reverse=True) 降序
- 列表.reverse()

#### 9. 元组

> 只包含一个元素时，需要用逗号隔开

- 查询
  - 元组[索引]
  - 元组.index(数据)
  - 元组.count(数据)
  - len(列表)
  - if 数据 in 元组

####10. 字典

**1) 添加**

- 字典[键] = 数据

**2) 删除**

- del 字典[键]
- 字典.pop(键)
  pop(键, None) 键不存在时不报错，第二个参数为具体的某个值时，会在键不存在时返回该值
- 字典.clear()

**3) 修改**

- 字典[键] = 数据
- 字典.get(键)
  键值不存在不会报错
- 字典.keys()
- 字典.values()
- 字典.items()

#### 11. 语句

**1)  条件控制**

* `if`
* `if else`
* `if elif else`
* `x if ... else ...`

**2) 循环语句**

* `while`
  `while ... else...`

* `for`

  `for ... in...else... `

* 循环控制

  `break` 和`continue`

#### 12. 常用函数

**1) len()**

**2) max()**

**3) min()**

**4) sum()**

#### 13. 可变与不可变类型

**1) 可变类型**
可以被修改，list，dict，set

**2) 不可变类型**
不可以被修改，str，int，float，bool，tuple

**3) 注意**
对可变类型与不可变类型通过函数操作时，需要开辟新的空间，可变类型原空间数据不变
对可变类型调用相应的方法进行操作时，不会重新分配空间，原数据发生变化
对不可变类型调用相应方法操作时，需要重新分配空间
如：lists = [6, 2, 3, 5] sort(lists) 返回 [2, 3, 5, 6] lists不变 lists.sort() 无返回 lists 变成 [2, 3, 5, 6]

#### 14. 函数

- 参数必须使用关键字
  def func(a, *,name) 函数在调用时 name参数必须以关键字参数传入
- 参数定义时出现的位置
  位置参数 > *args > 关键字参数 > **kwargs （如果关键字与kwargs中的键值不重复，可以将关键字参数放在kwargs参数后）
- 匿名函数
  lambda 参数: 表达式 lambda 只是一个表达式，而不是一个语句块

#### 15. 文件

**1) 打开文件**

open(file_name, mode)

- 访问模式
  - r
    只读，文件指针在文件开头，默认模式
  - w
    只写，存在时覆盖，不存在时创建新文件
  - a
    追加模式，文件不存在时创建文件
  - rb
  - wb
  - ab
  - r+
  - w+
  - a+
  - rb+
  - wb+
  - ab+
  - 总结
    文件不存在时创建文件，w， w+，a，a+，wb，wb+，ab，ab+

**2) 读取数据**

- read()
  f.read(num) 不写参数时表示读取所有的数据
- readlines()
  f.readlines() 按照行一次性读取所有的数据，返回的是一个列表
- readline()
  一次读取一行数据

**3) 写入数据**

- write()

**4) 关闭文件**

* f.close()

**5) 文件定位读写**

* tell() 获取当前位置 seek(offset, from) 设置位置
* offset：偏移量
* from：方向 0 表示文件开头 1 表示当前位置 2 表示文件末尾

**6) os 文件操作**

- 文件重命名
  os.rename(需要修改的文件, 新的文件名)
- 删除文件
  os.remove(文件)
- 创建文件夹
  os.mkdir(文件夹名)
- 获取当前目录
  os.getcwd()
- 改变默认目录
  os.chdir("test") 跳转到当前路径的test子目录中
- 获取目录列表
  os.listdir()
- 删除文件夹
  os.rmdir() 目录非空
- 判断文件是否存在
  os.path.exists(文件)

#### 16. 面向对象

#### 17. 异常

