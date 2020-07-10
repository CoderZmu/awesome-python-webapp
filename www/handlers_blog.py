'''
blog url handlers
'''

import json, re, hashlib, logging

from aiohttp import web

from coroweb import get, post
from models import Blog, User
from config import configs
from apis import APIError, APIValueError, APIPermissionError, Page

def check_admin(request):
    if request.__user__ is None:
        raise APIPermissionError

def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p

@get('/blog/info')
async def get_blog_info(*, id):
    blog = await Blog.find(id)
    return blog

@get('/blog/list')
async def get_blog_list(*, page='1', size='10'):
    page_index = get_page_index(page)
    num = await Blog.findNumber('count(id)')
    p = Page(num, page_index, int(size))
    if num == 0:
        return dict(page=p, blogs=())
    blogs = await Blog.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)


@post('/blog/add')
async def add_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty')
    
    user = request.__user__
    blog = Blog(user_id=user.id, user_name=user.name, user_image=user.image, name=name, sumary=summary, content=content)
    await blog.save()
    return blog



