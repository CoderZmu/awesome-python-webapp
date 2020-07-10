import asyncio

import orm
from models import User, Blog, Comment

loop = asyncio.get_event_loop()
async def test():
  await orm.create_pool(user='www-data', password='www-data', db='awesome', loop=loop)  
#   u = User(name='Test02', email='test02@example.com', passwd='1234567890', image='about:blank')  
#   await u.save()

  rs = await User.findAll()
  print(rs)
  rs[0].name = 'zmu233'
  await rs[0].update()
  rs = await User.findAll()
  print(rs[0])
loop.run_until_complete(test())