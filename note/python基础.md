#### 字符串
以单引号'或双引号"括起来的任意文本

##### 转义字符
用r''表示''内部的字符串默认不转义

##### 模板字符串 
'''...'''格式表示多行内容

##### 编码方式
内存中以Unicode表示，网络传输或者磁盘，保存为UTF-8编码

`\u4e2d\u6587` 等价于 `中文`

`ord()`获取字符的整数表示

`chr()`把编码转换成对应的字符

`encode()` 将Unicode表示的str编码为指定的字节流bytes(UTF-8编码)

```python
'中文'.encode('utf-8')
# b'\xe4\xb8\xad\xe6\x96\x87'
```

`decode()` 字节流转换str

```python
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
```

`len()` 计算字符数或者字节数

##### 格式化
%运算符就是用来格式化字符串的。

在字符串内部，%s表示用字符串替换，%d表示用整数替换，%f浮点数，%x十六进制。

有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

```python
'Hello, %s' % 'world'
'Hi, %s, you have $%d.' % ('Michael', 1000000)
```

格式化整数和浮点数还可以指定是否补0和整数与小数的位数

```python
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
```

如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

```python
'Age: %s. Gender: %s' % (25, True)
# 'Age: 25. Gender: True'
```

#### 布尔值
True、False两种值，用and、or和not运算

非零数值、非空字符串、非空list等，就判断为True，否则为False

### 变量
动态语言，变量本身类型不固定

可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的值

#### 常量
约定用全部大写的变量名表示

### list
可变的有序列表

可用负数做索引 逆序获取元素

`len()`获取元素个数

`append()`追加元素到末尾

`insert()`插入元素到指定位置

`pop()`删除指定位置元素 不传索引则删除末尾元素

### tuple
不可变的有序列表

空的tuple，可以写成()

只有1个元素的tuple定义时必须加一个逗号,

### 循环
range() 用于生成整数序列

```python
list(range(5))
# [0, 1, 2, 3, 4]
```

### dict
通过下标方式取值，如果key不存在，dict就会报错

`get()` 如果key不存在，可以返回None，或者自己指定的value

`pop()` 删除key

dict的key必须是不可变对象，因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）

### set
一组key的集合，没有重复的key，重复元素在set中自动被过滤

通过list初始化

```python
s = set([1, 2, 3])
# {1, 2, 3}
```
`add()`添加元素

`remove()`删除元素

### 函数
#### 内置函数
`abs()` 求绝对值

`max()` 求最大值，接受任意多个参数

##### 数据类型转换
`int()`

`float()`

`str()`

`bool()`

`hex()`

##### 类型检查
`isinstance()`

```python
isinstance(x, (int, float))
isinstance(x, int)
```

#### 定义函数
定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

##### 空函数
什么事都不做的函数 使用pass语句

##### 返回多个值
使用tuple，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值

#### 函数的参数
##### 默认参数
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

可不按顺序提供部分默认参数，但是需要把参数名写上

默认参数必须指向不变对象！

```python
def enroll(name, gender, age=6, city='Beijing'):
    pass
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
```


##### 可变参数
在参数前面加一个*号，自动组装为一个tuple

在list或tuple前面加一个*号，可将list或tuple的元素变成可变参数

```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

##### 关键字参数
允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

