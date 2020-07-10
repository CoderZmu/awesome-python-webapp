import time, functools
def metric(fn):
  @functools.wraps(fn)
  def print_time(*args, **kw):
    start = time.time()
    result = fn(*args, **kw)
    end = time.time()
    print('%s executed in %s ms' % (fn.__name__, end - start))
    return result
  return print_time

print(__name__)
if __name__=='__main__':
  print('hello, python')

