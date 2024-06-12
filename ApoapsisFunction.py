# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:16:48 2024

@author: wills
"""

import numpy as np


def visviva(mu,r,a):
    
    v = np.sqrt(mu*((2/r)-(1/a)))
    
    return v




def delVreq(mu,rF,rI,aF,aI):
    
    delV = visviva(mu,rF,aF) - visviva(mu,rI,aI)

    return delV
