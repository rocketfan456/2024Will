# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:16:48 2024

@author: wills
"""

import numpy as np


def visviva(mu,r,a):
    '''
    Calculate the velocity at point in orbit.

    Parameters
    ----------
    mu : int
        Gravitational Constant (km^2/s^2).
    r : int
        Distance from center body (km).
    a : int
        semi-major axis (km).

    Returns
    -------
    v : float
        velocity at specifies orbit point.
    '''
    
    v = np.sqrt(mu*((2/r)-(1/a)))
    
    return v




def delVreq(ApogeeChange):
    '''
    Calculate the difference in velocities at given points in orbit.
    
    Parameters
    ----------
    mu : int
        Gravitational Constant (km^2/s^2).
    rF : int
        Final distance from center body (km).
    aF : int
        Final semi-major axis (km).
    rI : int
        Initial distance from center body (km).
    aI : int
        Initial semi-major axis (km).

    Returns
    -------
    v : float
        dV necessary to change from specified apogees.
    '''
    mu = 398600
    rF = 6563
    rI = 6563

    aI = ((6378+185)+(6378+185))/2
    aF = ((6378+185)+(6378+ApogeeChange))/2
    
    delV = visviva(mu,rF,aF) - visviva(mu,rI,aI)

    return delV
