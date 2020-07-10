from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
  def fn(x, y):
    return x * 10 + y

  def char2num(s):
    return DIGITS[s]
  
  return reduce(fn, map(char2num, s))

def normalize(name):
  def fn(s):
    return s[:1].upper() + s[1:].lower()
  return map(fn, name)


def prod(L):
  def fn(x, y):
    return x * y
  return reduce(fn, L)

def count():
  def f(j):
    def g():
      return j * j
    return g
  return [f(i) for i in range(1, 4)]


def test(num, *args, **kwargs):
  print(args)
  print(kwargs)

gl_nums = (1,2,3)
gl_xiaoming = { "name": "小明", "age": '18' }
test(*gl_nums, **gl_xiaoming)



def addEnd(L=None):
  print(id(L))
  if L is None:
    print('2222')
    L = []
  print(id(L))
  L.append('END')
  return L

print(addEnd())
print(addEnd())
print(addEnd())

def triangles():
  L = [1]
  yield L
  while True:
    L=[1] + [L[i] + L[i+1] for i in range(len(L) - 1)] + [1]
    yield L



print(count())
f1,f2,f3 = count()
print(f1()) 
print(f2())


class Student(object):
  __slots__ = ('name', 'set_age', 'age')

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性

def set_age(self, age):
  self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(27)
print(s.age)

def set_score(self, score):
  self.score = score

# 给class绑定方法后，所有实例均可调用
Student.set_score = set_score


class Student2(object):
  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer!')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 ~ 100!')
    self._score = value


s = Student2()
s.score = 88
print(s.score,s.__str__)
s.__str__()


class Fib(object):
  def __init__(self):
    self.a, self.b = 0, 1 # 初始化两个计数器a，b
  
  def __iter__(self):
    return self # 实例本身就是迭代对象，故返回自己

  def __next__(self):
    self.a, self.b = self.b, self.a + self.b
    while self.a > 100000:
      raise StopIteration()
    return self.a

  def __getitem__(self, n):
    if isinstance(n, int):
      a, b = 0, 1
      for x in range(n+1):
        a, b = b, a + b
      return a
    if isinstance(n, slice):
      start, stop = n.start, n.stop
      if start is None:
        start = 0
      a, b = 0, 1
      L = []
      for x in range(stop):
        a, b = b, a + b
        if (x >= start):
          L.append(a)
      return L

f = Fib()
print(f.__dict__)
print(f[90:100])