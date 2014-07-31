# -*- coding: utf-8 -*-

from gevent import monkey; monkey.patch_all()

from haven.contrib.ws_haven import WSHaven
from kola_box import KolaBox
from flask import Flask
from haven import logger
import logging

logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

flask_app = Flask(__name__)


@flask_app.route('/http')
def http():
    return u'http ok'

app = WSHaven(KolaBox, '/echo', flask_app)


@app.route(1)
def index(request):
    request.write(dict(
        ret=1,
        body='ok haha',
        address=request.address,
    ))


@app.repeat_timer(60)
def timer():
    logger.debug('timer')


if __name__ != '__main__':
    # 启动timer之类的
    app._before_run()

if __name__ == '__main__':
    app.run('127.0.0.1', 8000, workers=2)
