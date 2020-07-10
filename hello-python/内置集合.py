from collections import OrderedDict
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')


from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key2'] # N/A

from collections import Counter
c = Counter('programming') # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
c.update('programming') # Counter({'r': 4, 'g': 4, 'm': 4, 'p': 2, 'o': 2, 'a': 2, 'i': 2, 'n': 2})

class LastUpdatedOrderedDict(OrderedDict):
  def __init__(self, capacity):
    super().__init__()
    self._capacity = capacity
  
  def __setitem__(self, key, value):
    containsKey = 1 if key in self else 0
    if len(self) - containsKey >= self._capacity:
      last = self.popitem(last=False) 
      print('remove:', last)
    if containsKey:
      del self[key]
      print('set:', (key, value))
    else:
      print('add:', (key, value))
    
    super().__setitem__(key, value)


fifo = LastUpdatedOrderedDict(3)
fifo['a'] = 2
fifo['b'] = 3
fifo['c'] = 4
fifo['d'] = 5
print(fifo)

