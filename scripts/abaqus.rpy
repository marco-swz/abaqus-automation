# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by fratschiller on Mon Dec 18 14:00:32 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=169.0625, 
    height=152.055572509766)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('R:/CPS_Projekt/abaqus-automation/scripts/test.py', __main__.__dict__)
#* SyntaxError: ('invalid syntax', 
#* ('R:/CPS_Projekt/abaqus-automation/scripts/test.py', 18, 44, 'from 
#* driverUtils import executeOnCaeStartup^\n'))
