# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:16:48 2024

@author: wills
"""


from ApoapsisFunction import delVreq

## Global Variables
mu = 398600
rF = 6563
rI = 6563

ARI = int(input("Initial Apoapsis Altitude (excluding radius of Earth): "))
ARF = int(input("Final Apoapsis Altitude (excluding radius of Earth): "))

## Global Variables
aI = ((6378+185)+(6378+ARI))/2
aF = ((6378+185)+(6378+ARF))/2


print("The change in apoapsis from " + str(ARI) + " km to " + str(ARF) + " km requries an additional dV of " + str(round(delVreq(mu,rF,rI,aF,aI),7)) + " km/s!")
