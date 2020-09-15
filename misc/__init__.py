
# -*- coding: utf-8 -*-
# Module  : 混杂的
# Author  : fengfeng
# Date    : 2017-7-15
# Version : 1.0
import logging
import time
import ctx


class event(object):

    def __init__(self, func):
        self._key = func.__name__

    def __get__(self, obj, cls):

        if self._key not in obj.__dict__:
            obj.__dict__[self._key] = BindEvent()

        return obj.__dict__[self._key]


class BindEvent(object):

    def __init__(self):
        self._fns = []

    def __iadd__(self, fn):
        self._fns.append(fn)
        return self

    def __isub__(self, fn):
        self._fns.remove(fn)
        return self

    def __call__(self, *args, **kwargs):

        for f in self._fns[:]:
            f(*args, **kwargs)


# mongodb 添加索引
def indexing(db=None, *indexes):

    if db and indexes:

        _indexes = set([]) if db.count(
        ) == 0 else db.index_information().keys()

        for idx in indexes:

            options = dict(idx).get('__options__', {})
            idx = [k for k in idx if k[0] != '__options__']
            options['background'] = True

            now = time.time()
            db.ensure_index(idx, **options)
            if time.time() - now > 1.0:
                logging.info("Ensured index %s->%s" % (repr(idx), repr(db)))
    return lambda func: func
