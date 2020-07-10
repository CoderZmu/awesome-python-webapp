'''
async web application
'''

import logging, asyncio, os, json, time
from datetime import datetime

from aiohttp import web

import orm
from coroweb import add_routes, add_static
from user_cookie import checkCookie, COOKIE_NAME

logging.basicConfig(level=logging.INFO)

async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        return (await handler(request))

    return logger

async def auth_factory(app, handler):
    async def auth(request):
        logging.info('check user: %s %s' % (request.method, request.path))
        request.__user__ = None
        cookie_str = request.cookies.get(COOKIE_NAME)
        if cookie_str:
            user = await checkCookie(cookie_str)
            if user:
                logging.info('set current user: %s' % user.email)
                request.__user__ = user
        
        if request.path.startswith('/manage/') and (request.__user__ is None or not request.__user__.admin):
            return web.HTTPFound('/signin')
        
        return (await handler(request))
    return auth

async def response_factory(app, handler):
    async def response(request):
        logging.info('Response handles...')
        r = await handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
            resp.content_type = 'application/json;charset=utf-8'
            return resp
        if isinstance(r, list) or isinstance(r, tuple):
            resp = web.Response(body=json.dumps(r, ensure_ascii=False).encode('utf-8'))
            resp.content_type = 'application/json;charset=utf-8'
            return resp
            
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp

    return response


async def init(loop):
    await orm.create_pool(user='www-data',
                          password='www-data',
                          db='awesome',
                          loop=loop)
    app = web.Application(loop=loop,
                          middlewares=[logger_factory, auth_factory, response_factory])
    add_routes(app, 'handlers_user')
    add_routes(app, 'handlers_blog')
    add_static(app)
    runner = web.AppRunner(app)
    await runner.setup()
    srv = await loop.create_server(runner.server, '127.0.0.1', 9999)
    logging.info('server started at http://127.0.0.1:9999...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
