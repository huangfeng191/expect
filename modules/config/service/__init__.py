# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from service.comm import *
import ctx
config_ddic = CRUD(ctx.config_mdb, 'ddic')
a = config_ddic.get({})
print(a)

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
