# -*- coding: utf-8 -*-

from service import *
from service.comm import *
import ctx
config_ddic=CRUD(ctx.config_mdb,'ddic')
a=config_ddic.get({})
print(a)