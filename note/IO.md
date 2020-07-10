### 文件读写
`open()`打开文件

`read()`读取文件的所有内容，可传入参数，指定每次最多读取size个字节的内容

`readline()`读取一行内容

`readlines()`一次读取所有内容并按行返回list

`close()`关闭文件，`with`语句来自动帮我们调用`close()`方法

`write()`写文件

`tell()`获取当前文件读取指针的位置

`seek()`移动文件读写指针到指定位置

```python
with open('/Users/lishiming/Desktop/react/test/App.js', 'r') as f:
  for line in f.readlines():
    print(line.strip())
```


### StringIO和BytesIO 内存中读写数据

### 操作文件和目录
`os.path.abspath()` 查看文件的绝对路径

`os.path.join()` 拼接路径

`os.mkdir` 创建目录

`os.rmdir` 删除目录

`os.path.split()` 拆分目录，把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名

`os.path.splitext()` 获取文件拓展名

`os.listdir()` 前目录下的文件和文件夹

`os.path.isdir()`

`os.path.isfile()` 


```python
import os
def searchFile(path, file):
  for sub in os.listdir(path):
    sub_path = os.path.join(path, sub)
    if (os.path.isfile(sub_path)) and file in sub:
      print(sub_path)
    elif (os.path.isdir(sub_path)):
      searchFile(sub_path, file)

```


### 序列化
#### pickle
`pickle.dumps()`方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法`pickle.dump()`直接把对象序列化后写入一个file-like Object

当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用`pickle.loads()`方法反序列化出对象，也可以直接用`pickle.load()`方法从一个file-like Object中直接反序列化出对象

#### JSON  json模块
`dumps()`方法返回一个str，内容就是标准的JSON。类似的，`dump()`方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象，用`loads()`或者对应的`load()`方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

##### class JSON序列化
`dumps()` 设置可选参数`default`，提供一个转换函数，用于告知Python怎么将对象转换成dict

标准化方式可简化成: `json.dumps(s, default=lambda obj: obj.__dict__)`，因为通常class的实例都有一个`__dict__`属性，它就是一个dict

#### class JSON反序列化
类似的，设置可选参数`object_hook`

`loads()`方法首先转换出一个dict对象，然后，我们传入的`object_hook`函数负责把dict转换为class实例


### urllib
操作URL
