import itertools

def pi(N):
  naturals = itertools.count(1, 2)
  odds = itertools.takewhile(lambda x: x < 2 * N, naturals)
  return sum([(-1)**(x//2)*4/x for x in odds])


print(pi(10))