# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:54:08 2020

@author: Daniel.Feeney
"""

import spm1d
import matplotlib.pyplot as plt

dataset    = spm1d.data.uv1d.t1.Random()
Y,mu       = dataset.get_data()  #Y is (10x100), mu=0

plt.plot(Y)
plt.close

t  = spm1d.stats.ttest(Y, mu)  #mu is 0 by default
ti = t.inference(alpha=0.05, two_tailed=False, interp=True)
ti.plot()