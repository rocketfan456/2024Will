import numpy as np

# This function will output a summary of each phase
def PrintData(phaseList):
    print('{0:25s}'.format("------------------------------------------------------------------------" ))
    print('{0:20s}{1:>11s}{2:>11s}{3:>11s}'.format("Phase Name", "DV (m/s)", "Mass0 (kg)", "MassF (kg)" ))
    print('{0:25s}'.format("------------------------------------------------------------------------" ))
    for curPhase in phaseList:
        print('{0:20s}{1:11.1f}{2:11.1f}{3:11.1f}'.format(curPhase.strName, curPhase.dvPhase, curPhase.mStart, curPhase.mEnd))

# This class will create a generic "phase" which will do propellant 
# calculations
class Phase:

    def __init__(self, strName, mStart, dvPhase, clsEng):
        # Check if this is a T/W phase. If so, 
        # update the dV and calculate the thrust-to-weight
        twPhase = clsEng.thrust / (mStart * 9.81)
        if dvPhase < 0:
            dvPhase = 4335 * np.exp(-(twPhase) * 20.25) + 1880

        # Calculate Impulse Propellant Using Rocket Equation   
        # We specify Impulse because we'll have other types later
        mPropImpulse = mStart - mStart / (np.exp(dvPhase / (9.81 * clsEng.isp)))

        # Determine Oxidizer and Fuel
        mPropImpulseOx = (mPropImpulse * clsEng.mr) / (1 + clsEng.mr)
        mPropImpulseFuel = mPropImpulse / (1 + clsEng.mr)
        
        mEnd = mStart - mPropImpulse 
        
        # Move data to class structure to save information
        self.mStart = mStart
        self.mEnd = mEnd
        self.dvPhase = dvPhase
        self.clsEng = clsEng
        self.mPropImpulse = mPropImpulse
        self.strName = strName
        self.twPhase = twPhase
        self.mPropImpulseOx = mPropImpulseOx
        self.mPropImpulseFuel = mPropImpulseFuel

# This class creates a summary of the entire mission - summing things up across
# phases         
class MissionSummary:
    def __init__(self, tupPhases):
        """
        Inputs:
            tupPhases: list of phase classes
        """
        # Initialize variables 
        mPropImpulse = 0
        mPropImpulseOx = 0
        mPropImpulseFuel = 0

        # sum up the usages by phase
        for curPhase in tupPhases:
            mPropImpulse += curPhase.mPropImpulse 
            mPropImpulseOx += curPhase.mPropImpulseOx
            mPropImpulseFuel += curPhase.mPropImpulseFuel

        # Stuff everything into self    
        self.mPropImpulse = mPropImpulse
        self.mPropImpulseOx = mPropImpulseOx
        self.mPropImpulseFuel = mPropImpulseFuel

# This builds up an engine, with an assumed thrust, specific impulse, and 
# mixture ratio
class Engine:
    def __init__(self, isp, thrust, mr):
        self.isp = isp
        self.thrust = thrust
        self.mr = mr

# Example usage:
engine = Engine(isp=300, thrust=5000, mr=2.5)
phase1 = Phase("Boost Phase", 10000, 3000, engine)
phase2 = Phase("Cruise Phase", 8000, 1500, engine)
phases = [phase1, phase2]

PrintData(phases)

mission_summary = MissionSummary(phases)
print("Mission Summary:")
print("Total Propellant: {:.1f} kg".format(mission_summary.mPropImpulse))
print("Total Oxidizer: {:.1f} kg".format(mission_summary.mPropImpulseOx))
print("Total Fuel: {:.1f} kg".format(mission_summary.mPropImpulseFuel))
