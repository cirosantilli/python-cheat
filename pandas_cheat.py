#!/usr/bin/env python

import pandas as pd

s = pd.Series([1, 2, 4])
s.iloc[-1]
# TODO compare.
s.rolling(2, min_periods=1).mean() == [1, 1.5, 3.5]
# s.rolling(2, min_periods=1).mean()[-1]
