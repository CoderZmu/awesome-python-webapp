'''
user url handlers
'''

import json, re, hashlib, logging

from aiohttp import web

from coroweb import get, post
from models import User, next_id
from apis import APIError, APIValueError
from user_cookie import generateCookie, COOKIE_NAME


@get('/user/list')
async def users(request):
    return (await User.findAll(orderBy='created_at desc'))

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

@post('/user/register')
async def register_user(*, email, name, passwd):
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not passwd or not _RE_SHA1.match(passwd):
        raise APIValueError('passwd')

    users = await User.findAll('email=?', [email])
    if len(users) > 0:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid, passwd)
    user = User(id=uid, name=name, email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(), image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())
    await user.save()

    user.passwd = '****'
    r = web.Response()
    r.set_cookie(COOKIE_NAME, generateCookie(user, 86400), max_age=86400, httponly=True)
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

@post('/user/login')
async def authenticate(*, email, passwd):
    if not email:
        raise APIValueError('email', 'Invalid email.')
    if not passwd:
        raise APIValueError('passwd', 'Invalid password.')

    users = await User.findAll('email=?', [email])
    if not len(users):
        raise APIValueError('email', 'Email not exist.')
    
    user = users[0]
    sha1_passwd = '%s:%s' % (user.id, passwd)
    sha1_passwd = hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
    if user.passwd != sha1_passwd:
        raise APIValueError('passwd', 'Invalid password.')

    r = web.Response()
    r.set_cookie(COOKIE_NAME, generateCookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '****'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


@get('/user/signout')
def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    r.set_cookie(COOKIE_NAME, '-deleted-', max_age=0, httponly=True)
    logging.info('user signed out.')
    return r


