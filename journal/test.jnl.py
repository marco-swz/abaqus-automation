# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.Model(modelType=STANDARD_EXPLICIT, name='Hutprofil')
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_1', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_1'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_1'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_1'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_1'].Line(point1=(25, 215), point2=(
    53.45, 215))
mdb.models['Hutprofil'].sketches['Sketch_1'].Line(point1=(53.45, 215), point2=(
    64.9, 216.01))
mdb.models['Hutprofil'].sketches['Sketch_1'].Line(point1=(64.9, 216.01), 
    point2=(63.95, 230.13))
mdb.models['Hutprofil'].sketches['Sketch_1'].Line(point1=(63.95, 230.13), 
    point2=(57, 256))
mdb.models['Hutprofil'].sketches['Sketch_1'].Line(point1=(57, 256), point2=(25, 
    256))
mdb.models['Hutprofil'].sketches['Sketch_1'].Line(point1=(25, 256), point2=(25, 
    215))
mdb.models['Hutprofil'].sketches['Sketch_1'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_1'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_1'].geometry[4], nearPoint1=(25, 
    215), nearPoint2=(64.9, 216.01), radius=5)
mdb.models['Hutprofil'].sketches['Sketch_1'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_1'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_1'].geometry[5], nearPoint1=(
    53.45, 215), nearPoint2=(63.95, 230.13), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_1'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_1'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_1'].geometry[6], nearPoint1=(64.9, 
    216.01), nearPoint2=(57, 256), radius=11)
mdb.models['Hutprofil'].sketches['Sketch_1'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_1'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_1'].geometry[7], nearPoint1=(
    63.95, 230.13), nearPoint2=(25, 256), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S1_U_R1', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S1_U_R1'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_1'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS1_U_R1', 
    part=mdb.models['Hutprofil'].parts['S1_U_R1'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS1_U_R1', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS1_U_R1', ), 
    vector=(275, 294.5, 0))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_2', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_2'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_2'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_2'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_2'].Line(point1=(25, 256), point2=(57, 
    256))
mdb.models['Hutprofil'].sketches['Sketch_2'].Line(point1=(57, 256), point2=(57, 
    289))
mdb.models['Hutprofil'].sketches['Sketch_2'].Line(point1=(57, 289), point2=(25, 
    289))
mdb.models['Hutprofil'].sketches['Sketch_2'].Line(point1=(25, 289), point2=(25, 
    256))
mdb.models['Hutprofil'].sketches['Sketch_2'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_2'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_2'].geometry[4], nearPoint1=(25, 
    256), nearPoint2=(57, 289), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_2'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_2'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_2'].geometry[5], nearPoint1=(57, 
    256), nearPoint2=(25, 289), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S1_U_R2', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S1_U_R2'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_2'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS1_U_R2', 
    part=mdb.models['Hutprofil'].parts['S1_U_R2'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS1_U_R2', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS1_U_R2', ), 
    vector=(275, 294.5, 0))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_3', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_3'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_3'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_3'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_3'].Line(point1=(25, 289), point2=(57, 
    289))
mdb.models['Hutprofil'].sketches['Sketch_3'].Line(point1=(57, 289), point2=(
    62.84, 305.01))
mdb.models['Hutprofil'].sketches['Sketch_3'].Line(point1=(62.84, 305.01), 
    point2=(63.47, 314.05))
mdb.models['Hutprofil'].sketches['Sketch_3'].Line(point1=(63.47, 314.05), 
    point2=(52.64, 315))
mdb.models['Hutprofil'].sketches['Sketch_3'].Line(point1=(52.64, 315), point2=(
    25, 315))
mdb.models['Hutprofil'].sketches['Sketch_3'].Line(point1=(25, 315), point2=(25, 
    289))
mdb.models['Hutprofil'].sketches['Sketch_3'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_3'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_3'].geometry[4], nearPoint1=(25, 
    289), nearPoint2=(62.84, 305.01), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_3'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_3'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_3'].geometry[5], nearPoint1=(57, 
    289), nearPoint2=(63.47, 314.05), radius=9)
mdb.models['Hutprofil'].sketches['Sketch_3'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_3'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_3'].geometry[6], nearPoint1=(
    62.84, 305.01), nearPoint2=(52.64, 315), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_3'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_3'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_3'].geometry[7], nearPoint1=(
    63.47, 314.05), nearPoint2=(25, 315), radius=5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S1_U_R3', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S1_U_R3'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_3'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS1_U_R3', 
    part=mdb.models['Hutprofil'].parts['S1_U_R3'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS1_U_R3', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS1_U_R3', ), 
    vector=(275, 294.5, 0))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_4', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_4'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_4'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_4'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_4'].Line(point1=(25, 196), point2=(
    84.3, 196))
mdb.models['Hutprofil'].sketches['Sketch_4'].Line(point1=(84.3, 196), point2=(
    94.63, 213.89))
mdb.models['Hutprofil'].sketches['Sketch_4'].Line(point1=(94.63, 213.89), 
    point2=(70.5, 216))
mdb.models['Hutprofil'].sketches['Sketch_4'].Line(point1=(70.5, 216), point2=(
    25, 216))
mdb.models['Hutprofil'].sketches['Sketch_4'].Line(point1=(25, 216), point2=(25, 
    196))
mdb.models['Hutprofil'].sketches['Sketch_4'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_4'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_4'].geometry[4], nearPoint1=(25, 
    196), nearPoint2=(94.63, 213.89), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_4'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_4'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_4'].geometry[5], nearPoint1=(84.3, 
    196), nearPoint2=(70.5, 216), radius=2.5)
mdb.models['Hutprofil'].sketches['Sketch_4'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_4'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_4'].geometry[6], nearPoint1=(
    94.63, 213.89), nearPoint2=(25, 216), radius=0.48)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S1_O_R1', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S1_O_R1'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_4'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS1_O_R1', 
    part=mdb.models['Hutprofil'].parts['S1_O_R1'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS1_O_R1', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS1_O_R1', ), 
    vector=(275, 432.5, 0))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_5', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_5'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_5'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_5'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_5'].Line(point1=(25, 216), point2=(
    71.07, 216))
mdb.models['Hutprofil'].sketches['Sketch_5'].Line(point1=(71.07, 216), point2=(
    73, 238))
mdb.models['Hutprofil'].sketches['Sketch_5'].Line(point1=(73, 238), point2=(25, 
    238))
mdb.models['Hutprofil'].sketches['Sketch_5'].Line(point1=(25, 238), point2=(25, 
    216))
mdb.models['Hutprofil'].sketches['Sketch_5'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_5'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_5'].geometry[4], nearPoint1=(25, 
    216), nearPoint2=(73, 238), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_5'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_5'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_5'].geometry[5], nearPoint1=(
    71.07, 216), nearPoint2=(25, 238), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S1_O_R2', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S1_O_R2'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_5'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS1_O_R2', 
    part=mdb.models['Hutprofil'].parts['S1_O_R2'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS1_O_R2', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS1_O_R2', ), 
    vector=(275, 432.5, 0))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_6', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_6'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_6'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_6'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_6'].Line(point1=(25, 250.9), point2=(
    79.5, 250.9))
mdb.models['Hutprofil'].sketches['Sketch_6'].Line(point1=(79.5, 250.9), point2=
    (79.5, 265.9))
mdb.models['Hutprofil'].sketches['Sketch_6'].Line(point1=(79.5, 265.9), point2=
    (25, 265.9))
mdb.models['Hutprofil'].sketches['Sketch_6'].Line(point1=(25, 265.9), point2=(
    25, 250.9))
mdb.models['Hutprofil'].sketches['Sketch_6'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_6'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_6'].geometry[4], nearPoint1=(25, 
    250.9), nearPoint2=(79.5, 265.9), radius=6.5)
mdb.models['Hutprofil'].sketches['Sketch_6'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_6'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_6'].geometry[5], nearPoint1=(79.5, 
    250.9), nearPoint2=(25, 265.9), radius=1)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S1_O_R3', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S1_O_R3'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_6'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS1_O_R3', 
    part=mdb.models['Hutprofil'].parts['S1_O_R3'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS1_O_R3', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS1_O_R3', ), 
    vector=(275, 432.5, 0))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_7', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_7'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_7'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_7'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_7'].Line(point1=(25, 278.9), point2=(
    79.5, 278.9))
mdb.models['Hutprofil'].sketches['Sketch_7'].Line(point1=(79.5, 278.9), point2=
    (79.5, 293.9))
mdb.models['Hutprofil'].sketches['Sketch_7'].Line(point1=(79.5, 293.9), point2=
    (25, 293.9))
mdb.models['Hutprofil'].sketches['Sketch_7'].Line(point1=(25, 293.9), point2=(
    25, 278.9))
mdb.models['Hutprofil'].sketches['Sketch_7'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_7'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_7'].geometry[4], nearPoint1=(25, 
    278.9), nearPoint2=(79.5, 293.9), radius=1)
mdb.models['Hutprofil'].sketches['Sketch_7'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_7'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_7'].geometry[5], nearPoint1=(79.5, 
    278.9), nearPoint2=(25, 293.9), radius=6.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S1_O_R4', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S1_O_R4'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_7'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS1_O_R4', 
    part=mdb.models['Hutprofil'].parts['S1_O_R4'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS1_O_R4', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS1_O_R4', ), 
    vector=(275, 432.5, 0))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_8', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_8'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_8'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_8'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_8'].Line(point1=(25, 297.4), point2=(
    61.46, 297.4))
mdb.models['Hutprofil'].sketches['Sketch_8'].Line(point1=(61.46, 297.4), 
    point2=(74.17, 298.51))
mdb.models['Hutprofil'].sketches['Sketch_8'].Line(point1=(74.17, 298.51), 
    point2=(72.83, 313.9))
mdb.models['Hutprofil'].sketches['Sketch_8'].Line(point1=(72.83, 313.9), 
    point2=(25, 313.9))
mdb.models['Hutprofil'].sketches['Sketch_8'].Line(point1=(25, 313.9), point2=(
    25, 297.4))
mdb.models['Hutprofil'].sketches['Sketch_8'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_8'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_8'].geometry[4], nearPoint1=(25, 
    297.4), nearPoint2=(74.17, 298.51), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_8'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_8'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_8'].geometry[5], nearPoint1=(
    61.46, 297.4), nearPoint2=(72.83, 313.9), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_8'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_8'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_8'].geometry[6], nearPoint1=(
    74.17, 298.51), nearPoint2=(25, 313.9), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S1_O_R5', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S1_O_R5'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_8'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS1_O_R5', 
    part=mdb.models['Hutprofil'].parts['S1_O_R5'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS1_O_R5', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS1_O_R5', ), 
    vector=(275, 432.5, 0))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_9', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_9'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_9'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_9'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_9'].Line(point1=(25, 313.9), point2=(
    71, 313.9))
mdb.models['Hutprofil'].sketches['Sketch_9'].Line(point1=(71, 313.9), point2=(
    97.59, 316.23))
mdb.models['Hutprofil'].sketches['Sketch_9'].Line(point1=(97.59, 316.23), 
    point2=(75.64, 328.9))
mdb.models['Hutprofil'].sketches['Sketch_9'].Line(point1=(75.64, 328.9), 
    point2=(25, 328.9))
mdb.models['Hutprofil'].sketches['Sketch_9'].Line(point1=(25, 328.9), point2=(
    25, 313.9))
mdb.models['Hutprofil'].sketches['Sketch_9'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_9'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_9'].geometry[4], nearPoint1=(25, 
    313.9), nearPoint2=(97.59, 316.23), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_9'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_9'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_9'].geometry[5], nearPoint1=(71, 
    313.9), nearPoint2=(75.64, 328.9), radius=2)
mdb.models['Hutprofil'].sketches['Sketch_9'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_9'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_9'].geometry[6], nearPoint1=(
    97.59, 316.23), nearPoint2=(25, 328.9), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S1_O_R6', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S1_O_R6'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_9'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS1_O_R6', 
    part=mdb.models['Hutprofil'].parts['S1_O_R6'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS1_O_R6', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS1_O_R6', ), 
    vector=(275, 432.5, 0))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_10', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_10'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_10'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_10'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_10'].Line(point1=(25, 217), point2=(
    58.52, 217))
mdb.models['Hutprofil'].sketches['Sketch_10'].Line(point1=(58.52, 217), point2=
    (74.68, 219.85))
mdb.models['Hutprofil'].sketches['Sketch_10'].Line(point1=(74.68, 219.85), 
    point2=(72.46, 233.85))
mdb.models['Hutprofil'].sketches['Sketch_10'].Line(point1=(72.46, 233.85), 
    point2=(56.95, 255.6))
mdb.models['Hutprofil'].sketches['Sketch_10'].Line(point1=(56.95, 255.6), 
    point2=(25, 255.6))
mdb.models['Hutprofil'].sketches['Sketch_10'].Line(point1=(25, 255.6), point2=(
    25, 217))
mdb.models['Hutprofil'].sketches['Sketch_10'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_10'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_10'].geometry[4], nearPoint1=(25, 
    217), nearPoint2=(74.68, 219.85), radius=2)
mdb.models['Hutprofil'].sketches['Sketch_10'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_10'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_10'].geometry[5], nearPoint1=(
    58.52, 217), nearPoint2=(72.46, 233.85), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_10'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_10'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_10'].geometry[6], nearPoint1=(
    74.68, 219.85), nearPoint2=(56.95, 255.6), radius=4)
mdb.models['Hutprofil'].sketches['Sketch_10'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_10'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_10'].geometry[7], nearPoint1=(
    72.46, 233.85), nearPoint2=(25, 255.6), radius=1)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S2_U_R1', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S2_U_R1'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_10'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS2_U_R1', 
    part=mdb.models['Hutprofil'].parts['S2_U_R1'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS2_U_R1', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS2_U_R1', ), 
    vector=(275, 292.5, 400))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_11', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_11'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_11'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_11'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_11'].Line(point1=(25, 255.6), point2=(
    57, 255.6))
mdb.models['Hutprofil'].sketches['Sketch_11'].Line(point1=(57, 255.6), point2=(
    57, 289.6))
mdb.models['Hutprofil'].sketches['Sketch_11'].Line(point1=(57, 289.6), point2=(
    25, 289.6))
mdb.models['Hutprofil'].sketches['Sketch_11'].Line(point1=(25, 289.6), point2=(
    25, 255.6))
mdb.models['Hutprofil'].sketches['Sketch_11'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_11'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_11'].geometry[4], nearPoint1=(25, 
    255.6), nearPoint2=(57, 289.6), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_11'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_11'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_11'].geometry[5], nearPoint1=(57, 
    255.6), nearPoint2=(25, 289.6), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S2_U_R2', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S2_U_R2'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_11'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS2_U_R2', 
    part=mdb.models['Hutprofil'].parts['S2_U_R2'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS2_U_R2', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS2_U_R2', ), 
    vector=(275, 292.5, 400))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_12', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_12'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_12'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_12'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_12'].Line(point1=(25, 289.6), point2=(
    57.18, 289.6))
mdb.models['Hutprofil'].sketches['Sketch_12'].Line(point1=(57.18, 289.6), 
    point2=(69.19, 301.4))
mdb.models['Hutprofil'].sketches['Sketch_12'].Line(point1=(69.19, 301.4), 
    point2=(70.58, 310.18))
mdb.models['Hutprofil'].sketches['Sketch_12'].Line(point1=(70.58, 310.18), 
    point2=(54.61, 313))
mdb.models['Hutprofil'].sketches['Sketch_12'].Line(point1=(54.61, 313), point2=
    (25, 313))
mdb.models['Hutprofil'].sketches['Sketch_12'].Line(point1=(25, 313), point2=(
    25, 289.6))
mdb.models['Hutprofil'].sketches['Sketch_12'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_12'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_12'].geometry[4], nearPoint1=(25, 
    289.6), nearPoint2=(69.19, 301.4), radius=1)
mdb.models['Hutprofil'].sketches['Sketch_12'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_12'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_12'].geometry[5], nearPoint1=(
    57.18, 289.6), nearPoint2=(70.58, 310.18), radius=3.5)
mdb.models['Hutprofil'].sketches['Sketch_12'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_12'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_12'].geometry[6], nearPoint1=(
    69.19, 301.4), nearPoint2=(54.61, 313), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_12'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_12'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_12'].geometry[7], nearPoint1=(
    70.58, 310.18), nearPoint2=(25, 313), radius=5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S2_U_R3', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S2_U_R3'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_12'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS2_U_R3', 
    part=mdb.models['Hutprofil'].parts['S2_U_R3'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS2_U_R3', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS2_U_R3', ), 
    vector=(275, 292.5, 400))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_13', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_13'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_13'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_13'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_13'].Line(point1=(25, 205.1), point2=(
    80, 205.1))
mdb.models['Hutprofil'].sketches['Sketch_13'].Line(point1=(80, 205.1), point2=(
    80, 216.66))
mdb.models['Hutprofil'].sketches['Sketch_13'].Line(point1=(80, 216.66), point2=
    (60.5, 220.1))
mdb.models['Hutprofil'].sketches['Sketch_13'].Line(point1=(60.5, 220.1), 
    point2=(25, 220.1))
mdb.models['Hutprofil'].sketches['Sketch_13'].Line(point1=(25, 220.1), point2=(
    25, 205.1))
mdb.models['Hutprofil'].sketches['Sketch_13'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_13'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_13'].geometry[4], nearPoint1=(25, 
    205.1), nearPoint2=(80, 216.66), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_13'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_13'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_13'].geometry[5], nearPoint1=(80, 
    205.1), nearPoint2=(60.5, 220.1), radius=1)
mdb.models['Hutprofil'].sketches['Sketch_13'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_13'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_13'].geometry[6], nearPoint1=(80, 
    216.66), nearPoint2=(25, 220.1), radius=1)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S2_O_R1', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S2_O_R1'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_13'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS2_O_R1', 
    part=mdb.models['Hutprofil'].parts['S2_O_R1'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS2_O_R1', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS2_O_R1', ), 
    vector=(275, 430.5, 400))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_14', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_14'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_14'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_14'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_14'].Line(point1=(25, 220.1), point2=(
    61.26, 220.1))
mdb.models['Hutprofil'].sketches['Sketch_14'].Line(point1=(61.26, 220.1), 
    point2=(66.76, 251.3))
mdb.models['Hutprofil'].sketches['Sketch_14'].Line(point1=(66.76, 251.3), 
    point2=(25, 251.3))
mdb.models['Hutprofil'].sketches['Sketch_14'].Line(point1=(25, 251.3), point2=(
    25, 220.1))
mdb.models['Hutprofil'].sketches['Sketch_14'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_14'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_14'].geometry[4], nearPoint1=(25, 
    220.1), nearPoint2=(66.76, 251.3), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_14'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_14'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_14'].geometry[5], nearPoint1=(
    61.26, 220.1), nearPoint2=(25, 251.3), radius=1)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S2_O_R2', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S2_O_R2'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_14'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS2_O_R2', 
    part=mdb.models['Hutprofil'].parts['S2_O_R2'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS2_O_R2', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS2_O_R2', ), 
    vector=(275, 430.5, 400))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_15', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_15'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_15'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_15'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_15'].Line(point1=(25, 251.3), point2=(
    75.47, 251.3))
mdb.models['Hutprofil'].sketches['Sketch_15'].Line(point1=(75.47, 251.3), 
    point2=(79.5, 256.27))
mdb.models['Hutprofil'].sketches['Sketch_15'].Line(point1=(79.5, 256.27), 
    point2=(79.5, 288.69))
mdb.models['Hutprofil'].sketches['Sketch_15'].Line(point1=(79.5, 288.69), 
    point2=(72.43, 295))
mdb.models['Hutprofil'].sketches['Sketch_15'].Line(point1=(72.43, 295), point2=
    (25, 295))
mdb.models['Hutprofil'].sketches['Sketch_15'].Line(point1=(25, 295), point2=(
    25, 251.3))
mdb.models['Hutprofil'].sketches['Sketch_15'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_15'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_15'].geometry[4], nearPoint1=(25, 
    251.3), nearPoint2=(79.5, 256.27), radius=1)
mdb.models['Hutprofil'].sketches['Sketch_15'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_15'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_15'].geometry[5], nearPoint1=(
    75.47, 251.3), nearPoint2=(79.5, 288.69), radius=3)
mdb.models['Hutprofil'].sketches['Sketch_15'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_15'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_15'].geometry[6], nearPoint1=(
    79.5, 256.27), nearPoint2=(72.43, 295), radius=3)
mdb.models['Hutprofil'].sketches['Sketch_15'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_15'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_15'].geometry[7], nearPoint1=(
    79.5, 288.69), nearPoint2=(25, 295), radius=10)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S2_O_R3', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S2_O_R3'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_15'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS2_O_R3', 
    part=mdb.models['Hutprofil'].parts['S2_O_R3'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS2_O_R3', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS2_O_R3', ), 
    vector=(275, 430.5, 400))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_16', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_16'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_16'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_16'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_16'].Line(point1=(25, 295), point2=(
    68.14, 295))
mdb.models['Hutprofil'].sketches['Sketch_16'].Line(point1=(68.14, 295), point2=
    (65.5, 310))
mdb.models['Hutprofil'].sketches['Sketch_16'].Line(point1=(65.5, 310), point2=(
    25, 310))
mdb.models['Hutprofil'].sketches['Sketch_16'].Line(point1=(25, 310), point2=(
    25, 295))
mdb.models['Hutprofil'].sketches['Sketch_16'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_16'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_16'].geometry[4], nearPoint1=(25, 
    295), nearPoint2=(65.5, 310), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_16'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_16'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_16'].geometry[5], nearPoint1=(
    68.14, 295), nearPoint2=(25, 310), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S2_O_R4', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S2_O_R4'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_16'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS2_O_R4', 
    part=mdb.models['Hutprofil'].parts['S2_O_R4'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS2_O_R4', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS2_O_R4', ), 
    vector=(275, 430.5, 400))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_17', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_17'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_17'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_17'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_17'].Line(point1=(25, 310), point2=(
    65, 310))
mdb.models['Hutprofil'].sketches['Sketch_17'].Line(point1=(65, 310), point2=(
    90, 314.41))
mdb.models['Hutprofil'].sketches['Sketch_17'].Line(point1=(90, 314.41), point2=
    (90, 330))
mdb.models['Hutprofil'].sketches['Sketch_17'].Line(point1=(90, 330), point2=(
    25, 330))
mdb.models['Hutprofil'].sketches['Sketch_17'].Line(point1=(25, 330), point2=(
    25, 310))
mdb.models['Hutprofil'].sketches['Sketch_17'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_17'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_17'].geometry[4], nearPoint1=(25, 
    310), nearPoint2=(90, 314.41), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_17'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_17'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_17'].geometry[5], nearPoint1=(65, 
    310), nearPoint2=(90, 330), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_17'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_17'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_17'].geometry[6], nearPoint1=(90, 
    314.41), nearPoint2=(25, 330), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S2_O_R5', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S2_O_R5'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_17'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS2_O_R5', 
    part=mdb.models['Hutprofil'].parts['S2_O_R5'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS2_O_R5', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS2_O_R5', ), 
    vector=(275, 430.5, 400))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_18', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_18'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_18'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_18'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_18'].Line(point1=(25, 223.5), point2=(
    67.31, 223.5))
mdb.models['Hutprofil'].sketches['Sketch_18'].Line(point1=(67.31, 223.5), 
    point2=(78.89, 224.51))
mdb.models['Hutprofil'].sketches['Sketch_18'].Line(point1=(78.89, 224.51), 
    point2=(77.91, 238.54))
mdb.models['Hutprofil'].sketches['Sketch_18'].Line(point1=(77.91, 238.54), 
    point2=(56.96, 255.5))
mdb.models['Hutprofil'].sketches['Sketch_18'].Line(point1=(56.96, 255.5), 
    point2=(25, 255.5))
mdb.models['Hutprofil'].sketches['Sketch_18'].Line(point1=(25, 255.5), point2=(
    25, 223.5))
mdb.models['Hutprofil'].sketches['Sketch_18'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_18'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_18'].geometry[4], nearPoint1=(25, 
    223.5), nearPoint2=(78.89, 224.51), radius=10)
mdb.models['Hutprofil'].sketches['Sketch_18'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_18'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_18'].geometry[5], nearPoint1=(
    67.31, 223.5), nearPoint2=(77.91, 238.54), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_18'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_18'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_18'].geometry[6], nearPoint1=(
    78.89, 224.51), nearPoint2=(56.96, 255.5), radius=2)
mdb.models['Hutprofil'].sketches['Sketch_18'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_18'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_18'].geometry[7], nearPoint1=(
    77.91, 238.54), nearPoint2=(25, 255.5), radius=1)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S3_U_R1', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S3_U_R1'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_18'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS3_U_R1', 
    part=mdb.models['Hutprofil'].parts['S3_U_R1'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS3_U_R1', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS3_U_R1', ), 
    vector=(275, 290.5, 800))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_19', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_19'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_19'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_19'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_19'].Line(point1=(25, 255.5), point2=(
    57, 255.5))
mdb.models['Hutprofil'].sketches['Sketch_19'].Line(point1=(57, 255.5), point2=(
    57, 289.5))
mdb.models['Hutprofil'].sketches['Sketch_19'].Line(point1=(57, 289.5), point2=(
    25, 289.5))
mdb.models['Hutprofil'].sketches['Sketch_19'].Line(point1=(25, 289.5), point2=(
    25, 255.5))
mdb.models['Hutprofil'].sketches['Sketch_19'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_19'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_19'].geometry[4], nearPoint1=(25, 
    255.5), nearPoint2=(57, 289.5), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_19'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_19'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_19'].geometry[5], nearPoint1=(57, 
    255.5), nearPoint2=(25, 289.5), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S3_U_R2', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S3_U_R2'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_19'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS3_U_R2', 
    part=mdb.models['Hutprofil'].parts['S3_U_R2'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS3_U_R2', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS3_U_R2', ), 
    vector=(275, 290.5, 800))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_20', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_20'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_20'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_20'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_20'].Line(point1=(25, 289.5), point2=(
    56.72, 289.5))
mdb.models['Hutprofil'].sketches['Sketch_20'].Line(point1=(56.72, 289.5), 
    point2=(72.43, 297.5))
mdb.models['Hutprofil'].sketches['Sketch_20'].Line(point1=(72.43, 297.5), 
    point2=(73.13, 306.4))
mdb.models['Hutprofil'].sketches['Sketch_20'].Line(point1=(73.13, 306.4), 
    point2=(54.85, 308))
mdb.models['Hutprofil'].sketches['Sketch_20'].Line(point1=(54.85, 308), point2=
    (25, 308))
mdb.models['Hutprofil'].sketches['Sketch_20'].Line(point1=(25, 308), point2=(
    25, 289.5))
mdb.models['Hutprofil'].sketches['Sketch_20'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_20'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_20'].geometry[4], nearPoint1=(25, 
    289.5), nearPoint2=(72.43, 297.5), radius=2)
mdb.models['Hutprofil'].sketches['Sketch_20'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_20'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_20'].geometry[5], nearPoint1=(
    56.72, 289.5), nearPoint2=(73.13, 306.4), radius=2)
mdb.models['Hutprofil'].sketches['Sketch_20'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_20'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_20'].geometry[6], nearPoint1=(
    72.43, 297.5), nearPoint2=(54.85, 308), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_20'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_20'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_20'].geometry[7], nearPoint1=(
    73.13, 306.4), nearPoint2=(25, 308), radius=5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S3_U_R3', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S3_U_R3'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_20'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS3_U_R3', 
    part=mdb.models['Hutprofil'].parts['S3_U_R3'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS3_U_R3', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS3_U_R3', ), 
    vector=(275, 290.5, 800))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_21', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_21'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_21'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_21'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_21'].Line(point1=(25, 190), point2=(
    85, 190))
mdb.models['Hutprofil'].sketches['Sketch_21'].Line(point1=(85, 190), point2=(
    85, 217.59))
mdb.models['Hutprofil'].sketches['Sketch_21'].Line(point1=(85, 217.59), point2=
    (71.44, 223.2))
mdb.models['Hutprofil'].sketches['Sketch_21'].Line(point1=(71.44, 223.2), 
    point2=(56.6, 224.5))
mdb.models['Hutprofil'].sketches['Sketch_21'].Line(point1=(56.6, 224.5), 
    point2=(25, 224.5))
mdb.models['Hutprofil'].sketches['Sketch_21'].Line(point1=(25, 224.5), point2=(
    25, 190))
mdb.models['Hutprofil'].sketches['Sketch_21'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_21'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_21'].geometry[4], nearPoint1=(25, 
    190), nearPoint2=(85, 217.59), radius=1)
mdb.models['Hutprofil'].sketches['Sketch_21'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_21'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_21'].geometry[5], nearPoint1=(85, 
    190), nearPoint2=(71.44, 223.2), radius=2)
mdb.models['Hutprofil'].sketches['Sketch_21'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_21'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_21'].geometry[6], nearPoint1=(85, 
    217.59), nearPoint2=(56.6, 224.5), radius=30)
mdb.models['Hutprofil'].sketches['Sketch_21'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_21'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_21'].geometry[7], nearPoint1=(
    71.44, 223.2), nearPoint2=(25, 224.5), radius=5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S3_O_R1', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S3_O_R1'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_21'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS3_O_R1', 
    part=mdb.models['Hutprofil'].parts['S3_O_R1'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS3_O_R1', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS3_O_R1', ), 
    vector=(275, 428.5, 800))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_22', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_22'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_22'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_22'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_22'].Line(point1=(25, 224.5), point2=(
    57.25, 224.5))
mdb.models['Hutprofil'].sketches['Sketch_22'].Line(point1=(57.25, 224.5), 
    point2=(58.56, 239.5))
mdb.models['Hutprofil'].sketches['Sketch_22'].Line(point1=(58.56, 239.5), 
    point2=(25, 239.5))
mdb.models['Hutprofil'].sketches['Sketch_22'].Line(point1=(25, 239.5), point2=(
    25, 224.5))
mdb.models['Hutprofil'].sketches['Sketch_22'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_22'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_22'].geometry[4], nearPoint1=(25, 
    224.5), nearPoint2=(58.56, 239.5), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_22'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_22'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_22'].geometry[5], nearPoint1=(
    57.25, 224.5), nearPoint2=(25, 239.5), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S3_O_R2', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S3_O_R2'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_22'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS3_O_R2', 
    part=mdb.models['Hutprofil'].parts['S3_O_R2'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS3_O_R2', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS3_O_R2', ), 
    vector=(275, 428.5, 800))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_23', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_23'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_23'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_23'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_23'].Line(point1=(25, 239.5), point2=(
    58.55, 239.5))
mdb.models['Hutprofil'].sketches['Sketch_23'].Line(point1=(58.55, 239.5), 
    point2=(79.5, 256.46))
mdb.models['Hutprofil'].sketches['Sketch_23'].Line(point1=(79.5, 256.46), 
    point2=(79.5, 288.58))
mdb.models['Hutprofil'].sketches['Sketch_23'].Line(point1=(79.5, 288.58), 
    point2=(64.16, 296.4))
mdb.models['Hutprofil'].sketches['Sketch_23'].Line(point1=(64.16, 296.4), 
    point2=(25, 296.4))
mdb.models['Hutprofil'].sketches['Sketch_23'].Line(point1=(25, 296.4), point2=(
    25, 239.5))
mdb.models['Hutprofil'].sketches['Sketch_23'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_23'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_23'].geometry[4], nearPoint1=(25, 
    239.5), nearPoint2=(79.5, 256.46), radius=4)
mdb.models['Hutprofil'].sketches['Sketch_23'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_23'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_23'].geometry[5], nearPoint1=(
    58.55, 239.5), nearPoint2=(79.5, 288.58), radius=2)
mdb.models['Hutprofil'].sketches['Sketch_23'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_23'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_23'].geometry[6], nearPoint1=(
    79.5, 256.46), nearPoint2=(64.16, 296.4), radius=2)
mdb.models['Hutprofil'].sketches['Sketch_23'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_23'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_23'].geometry[7], nearPoint1=(
    79.5, 288.58), nearPoint2=(25, 296.4), radius=4)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S3_O_R3', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S3_O_R3'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_23'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS3_O_R3', 
    part=mdb.models['Hutprofil'].parts['S3_O_R3'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS3_O_R3', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS3_O_R3', ), 
    vector=(275, 428.5, 800))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_24', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_24'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_24'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_24'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_24'].Line(point1=(25, 296.4), point2=(
    64.07, 296.4))
mdb.models['Hutprofil'].sketches['Sketch_24'].Line(point1=(64.07, 296.4), 
    point2=(63.2, 306.4))
mdb.models['Hutprofil'].sketches['Sketch_24'].Line(point1=(63.2, 306.4), 
    point2=(25, 306.4))
mdb.models['Hutprofil'].sketches['Sketch_24'].Line(point1=(25, 306.4), point2=(
    25, 296.4))
mdb.models['Hutprofil'].sketches['Sketch_24'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_24'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_24'].geometry[4], nearPoint1=(25, 
    296.4), nearPoint2=(63.2, 306.4), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_24'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_24'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_24'].geometry[5], nearPoint1=(
    64.07, 296.4), nearPoint2=(25, 306.4), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S3_O_R4', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S3_O_R4'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_24'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS3_O_R4', 
    part=mdb.models['Hutprofil'].parts['S3_O_R4'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS3_O_R4', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS3_O_R4', ), 
    vector=(275, 428.5, 800))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_25', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_25'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_25'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_25'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_25'].Line(point1=(25, 306.4), point2=(
    62.79, 306.4))
mdb.models['Hutprofil'].sketches['Sketch_25'].Line(point1=(62.79, 306.4), 
    point2=(75.11, 307.48))
mdb.models['Hutprofil'].sketches['Sketch_25'].Line(point1=(75.11, 307.48), 
    point2=(85, 311.28))
mdb.models['Hutprofil'].sketches['Sketch_25'].Line(point1=(85, 311.28), point2=
    (85, 340))
mdb.models['Hutprofil'].sketches['Sketch_25'].Line(point1=(85, 340), point2=(
    25, 340))
mdb.models['Hutprofil'].sketches['Sketch_25'].Line(point1=(25, 340), point2=(
    25, 306.4))
mdb.models['Hutprofil'].sketches['Sketch_25'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_25'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_25'].geometry[4], nearPoint1=(25, 
    306.4), nearPoint2=(75.11, 307.48), radius=5)
mdb.models['Hutprofil'].sketches['Sketch_25'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_25'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_25'].geometry[5], nearPoint1=(
    62.79, 306.4), nearPoint2=(85, 311.28), radius=30)
mdb.models['Hutprofil'].sketches['Sketch_25'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_25'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_25'].geometry[6], nearPoint1=(
    75.11, 307.48), nearPoint2=(85, 340), radius=2)
mdb.models['Hutprofil'].sketches['Sketch_25'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_25'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_25'].geometry[7], nearPoint1=(85, 
    311.28), nearPoint2=(25, 340), radius=1)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S3_O_R5', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S3_O_R5'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_25'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS3_O_R5', 
    part=mdb.models['Hutprofil'].parts['S3_O_R5'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS3_O_R5', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS3_O_R5', ), 
    vector=(275, 428.5, 800))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_26', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_26'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_26'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_26'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_26'].Line(point1=(25, 220), point2=(
    80.33, 220))
mdb.models['Hutprofil'].sketches['Sketch_26'].Line(point1=(80.33, 220), point2=
    (80.72, 242.5))
mdb.models['Hutprofil'].sketches['Sketch_26'].Line(point1=(80.72, 242.5), 
    point2=(55.86, 256))
mdb.models['Hutprofil'].sketches['Sketch_26'].Line(point1=(55.86, 256), point2=
    (25, 256))
mdb.models['Hutprofil'].sketches['Sketch_26'].Line(point1=(25, 256), point2=(
    25, 220))
mdb.models['Hutprofil'].sketches['Sketch_26'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_26'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_26'].geometry[4], nearPoint1=(25, 
    220), nearPoint2=(80.72, 242.5), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_26'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_26'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_26'].geometry[5], nearPoint1=(
    80.33, 220), nearPoint2=(55.86, 256), radius=1.5)
mdb.models['Hutprofil'].sketches['Sketch_26'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_26'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_26'].geometry[6], nearPoint1=(
    80.72, 242.5), nearPoint2=(25, 256), radius=2)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S4_U_R1', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S4_U_R1'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_26'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS4_U_R1', 
    part=mdb.models['Hutprofil'].parts['S4_U_R1'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS4_U_R1', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS4_U_R1', ), 
    vector=(275, 290.5, 1200))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_27', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_27'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_27'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_27'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_27'].Line(point1=(25, 256), point2=(
    57, 256))
mdb.models['Hutprofil'].sketches['Sketch_27'].Line(point1=(57, 256), point2=(
    57, 289))
mdb.models['Hutprofil'].sketches['Sketch_27'].Line(point1=(57, 289), point2=(
    25, 289))
mdb.models['Hutprofil'].sketches['Sketch_27'].Line(point1=(25, 289), point2=(
    25, 256))
mdb.models['Hutprofil'].sketches['Sketch_27'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_27'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_27'].geometry[4], nearPoint1=(25, 
    256), nearPoint2=(57, 289), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_27'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_27'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_27'].geometry[5], nearPoint1=(57, 
    256), nearPoint2=(25, 289), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S4_U_R2', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S4_U_R2'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_27'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS4_U_R2', 
    part=mdb.models['Hutprofil'].parts['S4_U_R2'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS4_U_R2', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS4_U_R2', ), 
    vector=(275, 290.5, 1200))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_28', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_28'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_28'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_28'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_28'].Line(point1=(25, 289), point2=(
    53.53, 289))
mdb.models['Hutprofil'].sketches['Sketch_28'].Line(point1=(53.53, 289), point2=
    (74.08, 293.93))
mdb.models['Hutprofil'].sketches['Sketch_28'].Line(point1=(74.08, 293.93), 
    point2=(73.8, 310))
mdb.models['Hutprofil'].sketches['Sketch_28'].Line(point1=(73.8, 310), point2=(
    25, 310))
mdb.models['Hutprofil'].sketches['Sketch_28'].Line(point1=(25, 310), point2=(
    25, 289))
mdb.models['Hutprofil'].sketches['Sketch_28'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_28'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_28'].geometry[4], nearPoint1=(25, 
    289), nearPoint2=(74.08, 293.93), radius=2)
mdb.models['Hutprofil'].sketches['Sketch_28'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_28'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_28'].geometry[5], nearPoint1=(
    53.53, 289), nearPoint2=(73.8, 310), radius=1.5)
mdb.models['Hutprofil'].sketches['Sketch_28'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_28'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_28'].geometry[6], nearPoint1=(
    74.08, 293.93), nearPoint2=(25, 310), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S4_U_R3', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S4_U_R3'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_28'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS4_U_R3', 
    part=mdb.models['Hutprofil'].parts['S4_U_R3'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS4_U_R3', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS4_U_R3', ), 
    vector=(275, 290.5, 1200))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_29', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_29'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_29'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_29'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_29'].Line(point1=(25, 205), point2=(
    55.75, 205))
mdb.models['Hutprofil'].sketches['Sketch_29'].Line(point1=(55.75, 205), point2=
    (55.75, 243.9))
mdb.models['Hutprofil'].sketches['Sketch_29'].Line(point1=(55.75, 243.9), 
    point2=(25, 243.9))
mdb.models['Hutprofil'].sketches['Sketch_29'].Line(point1=(25, 243.9), point2=(
    25, 205))
mdb.models['Hutprofil'].sketches['Sketch_29'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_29'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_29'].geometry[4], nearPoint1=(25, 
    205), nearPoint2=(55.75, 243.9), radius=0.5)
mdb.models['Hutprofil'].sketches['Sketch_29'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_29'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_29'].geometry[5], nearPoint1=(
    55.75, 205), nearPoint2=(25, 243.9), radius=0.5)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S4_O_R1', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S4_O_R1'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_29'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS4_O_R1', 
    part=mdb.models['Hutprofil'].parts['S4_O_R1'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS4_O_R1', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS4_O_R1', ), 
    vector=(275, 428.5, 1200))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_30', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_30'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_30'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_30'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_30'].Line(point1=(25, 243.9), point2=(
    56.26, 243.9))
mdb.models['Hutprofil'].sketches['Sketch_30'].Line(point1=(56.26, 243.9), 
    point2=(79.5, 256.52))
mdb.models['Hutprofil'].sketches['Sketch_30'].Line(point1=(79.5, 256.52), 
    point2=(79.5, 288.53))
mdb.models['Hutprofil'].sketches['Sketch_30'].Line(point1=(79.5, 288.53), 
    point2=(60.58, 292.9))
mdb.models['Hutprofil'].sketches['Sketch_30'].Line(point1=(60.58, 292.9), 
    point2=(25, 292.9))
mdb.models['Hutprofil'].sketches['Sketch_30'].Line(point1=(25, 292.9), point2=(
    25, 243.9))
mdb.models['Hutprofil'].sketches['Sketch_30'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_30'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_30'].geometry[4], nearPoint1=(25, 
    243.9), nearPoint2=(79.5, 256.52), radius=3)
mdb.models['Hutprofil'].sketches['Sketch_30'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_30'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_30'].geometry[5], nearPoint1=(
    56.26, 243.9), nearPoint2=(79.5, 288.53), radius=1.5)
mdb.models['Hutprofil'].sketches['Sketch_30'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_30'].geometry[5], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_30'].geometry[6], nearPoint1=(
    79.5, 256.52), nearPoint2=(60.58, 292.9), radius=1.5)
mdb.models['Hutprofil'].sketches['Sketch_30'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_30'].geometry[6], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_30'].geometry[7], nearPoint1=(
    79.5, 288.53), nearPoint2=(25, 292.9), radius=3)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S4_O_R2', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S4_O_R2'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_30'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS4_O_R2', 
    part=mdb.models['Hutprofil'].parts['S4_O_R2'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS4_O_R2', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS4_O_R2', ), 
    vector=(275, 428.5, 1200))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_31', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_31'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_31'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_31'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_31'].Line(point1=(25, 292.9), point2=(
    62.4, 292.9))
mdb.models['Hutprofil'].sketches['Sketch_31'].Line(point1=(62.4, 292.9), 
    point2=(62.4, 320.4))
mdb.models['Hutprofil'].sketches['Sketch_31'].Line(point1=(62.4, 320.4), 
    point2=(25, 320.4))
mdb.models['Hutprofil'].sketches['Sketch_31'].Line(point1=(25, 320.4), point2=(
    25, 292.9))
mdb.models['Hutprofil'].sketches['Sketch_31'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_31'].geometry[3], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_31'].geometry[4], nearPoint1=(25, 
    292.9), nearPoint2=(62.4, 320.4), radius=1)
mdb.models['Hutprofil'].sketches['Sketch_31'].FilletByRadius(curve1=
    mdb.models['Hutprofil'].sketches['Sketch_31'].geometry[4], curve2=
    mdb.models['Hutprofil'].sketches['Sketch_31'].geometry[5], nearPoint1=(
    62.4, 292.9), nearPoint2=(25, 320.4), radius=2)
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='S4_O_R3', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['S4_O_R3'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_31'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aS4_O_R3', 
    part=mdb.models['Hutprofil'].parts['S4_O_R3'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aS4_O_R3', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aS4_O_R3', ), 
    vector=(275, 428.5, 1200))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_32', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_32'].rectangle(point1=(0.0, 0.0), 
    point2=(100, 1.5))
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='Blech', type=
    DEFORMABLE_BODY)
mdb.models['Hutprofil'].parts['Blech'].BaseSolidExtrude(depth=600, sketch=
    mdb.models['Hutprofil'].sketches['Sketch_32'])
mdb.models['Hutprofil'].parts['Blech'].Chamfer(edgeList=(
    mdb.models['Hutprofil'].parts['Blech'].edges[0], ), length=10)
mdb.models['Hutprofil'].parts['Blech'].Chamfer(edgeList=(
    mdb.models['Hutprofil'].parts['Blech'].edges[13], ), length=10)
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aBlech', 
    part=mdb.models['Hutprofil'].parts['Blech'])
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aBlech', ), 
    vector=(490, 351.5, -630))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_32', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_32'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_32'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_32'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_32'].Line(point1=(10, 0), point2=(100, 
    0))
mdb.models['Hutprofil'].sketches['Sketch_32'].Line(point1=(100, 0), point2=(
    100, 110))
mdb.models['Hutprofil'].sketches['Sketch_32'].Line(point1=(100, 110), point2=(
    10, 110))
mdb.models['Hutprofil'].sketches['Sketch_32'].Line(point1=(10, 110), point2=(
    10, 0))
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='FS_OW', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['FS_OW'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_32'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aFS_OW', 
    part=mdb.models['Hutprofil'].parts['FS_OW'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aFS_OW', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aFS_OW', ), 
    vector=(485, 453, -300))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(540, 453, -300))
mdb.models['Hutprofil'].RigidBody(name='RBE_FS_OW', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[67], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aFS_OW'].faces.getSequenceFromMask(
    mask=('[#f ]', ), )))
mdb.models['Hutprofil'].ConstrainedSketch(name='Sketch_33', sheetSize=250.0)
mdb.models['Hutprofil'].sketches['Sketch_33'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Hutprofil'].sketches['Sketch_33'].FixedConstraint(entity=
    mdb.models['Hutprofil'].sketches['Sketch_33'].geometry[2])
mdb.models['Hutprofil'].sketches['Sketch_33'].Line(point1=(10, 0), point2=(100, 
    0))
mdb.models['Hutprofil'].sketches['Sketch_33'].Line(point1=(100, 0), point2=(
    100, 110))
mdb.models['Hutprofil'].sketches['Sketch_33'].Line(point1=(100, 110), point2=(
    10, 110))
mdb.models['Hutprofil'].sketches['Sketch_33'].Line(point1=(10, 110), point2=(
    10, 0))
mdb.models['Hutprofil'].sketches['Sketch_33'].Line(point1=(10, 0), point2=(10, 
    0))
mdb.models['Hutprofil'].Part(dimensionality=THREE_D, name='FS_UW', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Hutprofil'].parts['FS_UW'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Hutprofil'].sketches['Sketch_33'])
mdb.models['Hutprofil'].rootAssembly.Instance(dependent=ON, name='aFS_UW', 
    part=mdb.models['Hutprofil'].parts['FS_UW'])
mdb.models['Hutprofil'].rootAssembly.rotate(angle=-90.0, axisDirection=(0, 0, 
    1), axisPoint=(0, 0, 0), instanceList=('aFS_UW', ))
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aFS_UW', ), 
    vector=(485, 251.5, -300))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(540, 251.5, -300))
mdb.models['Hutprofil'].RigidBody(name='RBE_FS_UW', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[72], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aFS_UW'].faces.getSequenceFromMask(
    mask=('[#f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(510.5, 294.5, 0))
mdb.models['Hutprofil'].RigidBody(name='RBE_S1_U_R1', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[75], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_U_R1'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(547.5, 294.5, 0))
mdb.models['Hutprofil'].RigidBody(name='RBE_S1_U_R2', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[78], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_U_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(577, 294.5, 0))
mdb.models['Hutprofil'].RigidBody(name='RBE_S1_U_R3', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[81], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_U_R3'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(481, 432.5, 0))
mdb.models['Hutprofil'].RigidBody(name='RBE_S1_O_R1', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[84], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R1'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(502, 432.5, 0))
mdb.models['Hutprofil'].RigidBody(name='RBE_S1_O_R2', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[87], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(533.4, 432.5, 0))
mdb.models['Hutprofil'].RigidBody(name='RBE_S1_O_R3', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[90], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R3'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(561.4, 432.5, 0))
mdb.models['Hutprofil'].RigidBody(name='RBE_S1_O_R4', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[93], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R4'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(580.65, 432.5, 0))
mdb.models['Hutprofil'].RigidBody(name='RBE_S1_O_R5', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[96], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R5'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(596.4, 432.5, 0))
mdb.models['Hutprofil'].RigidBody(name='RBE_S1_O_R6', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[99], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R6'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(511.3, 292.5, 400))
mdb.models['Hutprofil'].RigidBody(name='RBE_S2_U_R1', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[102], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_U_R1'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(547.6, 292.5, 400))
mdb.models['Hutprofil'].RigidBody(name='RBE_S2_U_R2', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[105], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_U_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(576.3, 292.5, 400))
mdb.models['Hutprofil'].RigidBody(name='RBE_S2_U_R3', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[108], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_U_R3'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(487.6, 430.5, 400))
mdb.models['Hutprofil'].RigidBody(name='RBE_S2_O_R1', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[111], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_O_R1'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(510.7, 430.5, 400))
mdb.models['Hutprofil'].RigidBody(name='RBE_S2_O_R2', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[114], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_O_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(548.15, 430.5, 400))
mdb.models['Hutprofil'].RigidBody(name='RBE_S2_O_R3', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[117], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_O_R3'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(577.5, 430.5, 400))
mdb.models['Hutprofil'].RigidBody(name='RBE_S2_O_R4', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[120], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_O_R4'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(595, 430.5, 400))
mdb.models['Hutprofil'].RigidBody(name='RBE_S2_O_R5', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[123], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_O_R5'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(514.5, 290.5, 800))
mdb.models['Hutprofil'].RigidBody(name='RBE_S3_U_R1', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[126], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_U_R1'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(547.5, 290.5, 800))
mdb.models['Hutprofil'].RigidBody(name='RBE_S3_U_R2', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[129], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_U_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(573.75, 290.5, 800))
mdb.models['Hutprofil'].RigidBody(name='RBE_S3_U_R3', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[132], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_U_R3'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(482.25, 428.5, 800))
mdb.models['Hutprofil'].RigidBody(name='RBE_S3_O_R1', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[135], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_O_R1'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(507, 428.5, 800))
mdb.models['Hutprofil'].RigidBody(name='RBE_S3_O_R2', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[138], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_O_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(542.95, 428.5, 800))
mdb.models['Hutprofil'].RigidBody(name='RBE_S3_O_R3', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[141], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_O_R3'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(576.4, 428.5, 800))
mdb.models['Hutprofil'].RigidBody(name='RBE_S3_O_R4', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[144], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_O_R4'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(598.2, 428.5, 800))
mdb.models['Hutprofil'].RigidBody(name='RBE_S3_O_R5', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[147], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_O_R5'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(513, 290.5, 1200))
mdb.models['Hutprofil'].RigidBody(name='RBE_S4_U_R1', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[150], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_U_R1'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(547.5, 290.5, 1200))
mdb.models['Hutprofil'].RigidBody(name='RBE_S4_U_R2', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[153], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_U_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(574.5, 290.5, 1200))
mdb.models['Hutprofil'].RigidBody(name='RBE_S4_U_R3', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[156], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_U_R3'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(499.45, 428.5, 
    1200))
mdb.models['Hutprofil'].RigidBody(name='RBE_S4_O_R1', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[159], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_O_R1'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(543.4, 428.5, 1200))
mdb.models['Hutprofil'].RigidBody(name='RBE_S4_O_R2', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[162], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_O_R2'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )))
mdb.models['Hutprofil'].rootAssembly.ReferencePoint(point=(581.65, 428.5, 
    1200))
mdb.models['Hutprofil'].RigidBody(name='RBE_S4_O_R3', refPointRegion=Region(
    referencePoints=(mdb.models['Hutprofil'].rootAssembly.referencePoints[165], 
    )), surfaceRegion=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_O_R3'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )))
mdb.models['Hutprofil'].Material(name='Mat')
mdb.models['Hutprofil'].materials['Mat'].Density(table=((7.8e-09, ), ))
mdb.models['Hutprofil'].materials['Mat'].Elastic(table=((210000, 0.3), ))
mdb.models['Hutprofil'].materials['Mat'].Plastic(table=((186.2712, 0), (
    225.6347, 0.005), (246.211, 0.01), (260.697, 0.015), (272.0399, 0.02), (
    281.4356, 0.025), (289.4961, 0.03), (296.5791, 0.035), (302.9127, 0.04), (
    308.652, 0.045), (313.9075, 0.05), (318.7608, 0.055), (323.274, 0.06), (
    327.4956, 0.065), (331.464, 0.07), (335.2105, 0.075), (338.7607, 0.08), (
    342.136, 0.085), (345.3541, 0.09), (348.4305, 0.095), (351.3781, 0.1), (
    354.2082, 0.105), (356.9308, 0.11), (359.5544, 0.115), (362.0866, 0.12), (
    364.5341, 0.125), (366.903, 0.13), (369.1985, 0.135), (371.4256, 0.14), (
    373.5885, 0.145), (375.6912, 0.15), (377.7373, 0.155), (379.73, 0.16), (
    381.6723, 0.165), (383.5669, 0.17), (385.4163, 0.175), (387.2228, 0.18), (
    388.9886, 0.185), (390.7156, 0.19), (392.4057, 0.195), (394.0605, 0.2)))
mdb.models['Hutprofil'].HomogeneousSolidSection(material='Mat', name=
    'Section Blech', thickness=None)
mdb.models['Hutprofil'].parts['Blech'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Hutprofil'].parts['Blech'].cells.getSequenceFromMask(
    mask=('[#1 ]', ), )), sectionName='Section Blech', thicknessAssignment=
    FROM_SECTION)
mdb.models['Hutprofil'].ImplicitDynamicsStep(description='entry', name='entry', 
    nlgeom=ON, previous='Initial')
mdb.models['Hutprofil'].ContactProperty('Kontakt_nofric')
mdb.models['Hutprofil'].interactionProperties['Kontakt_nofric'].NormalBehavior(
    allowSeparation=ON, clearanceAtZeroContactPressure=0.0, 
    constraintEnforcementMethod=AUGMENTED_LAGRANGE, contactStiffness=1000, 
    contactStiffnessScaleFactor=1.0, pressureOverclosure=HARD)
mdb.models['Hutprofil'].interactionProperties['Kontakt_nofric'].TangentialBehavior(
    absoluteDistance=0.01, dependencies=0, directionality=ISOTROPIC, 
    elasticSlipStiffness=None, formulation=PENALTY, maximumElasticSlip=
    ABSOLUTE_DISTANCE, pressureDependency=OFF, shearStressLimit=None, 
    slipRateDependency=OFF, table=((0, ), ), temperatureDependency=OFF)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aFS_OW'].faces.getSequenceFromMask(
    mask=('[#f ]', ), )), name='Kontakt FS_OW', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aFS_UW'].faces.getSequenceFromMask(
    mask=('[#f ]', ), )), name='Kontakt FS_UW', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R1'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )), name='Kontakt S1_O_R1_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S1_O_R2_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R3'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S1_O_R3_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R4'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S1_O_R4_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R5'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )), name='Kontakt S1_O_R5_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_O_R6'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )), name='Kontakt S1_O_R6_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_U_R1'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S1_U_R1_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_U_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S1_U_R2_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS1_U_R3'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S1_U_R3_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_O_R1'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )), name='Kontakt S2_O_R1_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_O_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S2_O_R2_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_O_R3'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S2_O_R3_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_O_R4'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S2_O_R4_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_O_R5'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )), name='Kontakt S2_O_R5_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_U_R1'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S2_U_R1_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_U_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S2_U_R2_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS2_U_R3'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S2_U_R3_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_O_R1'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S3_O_R1_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_O_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S3_O_R2_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_O_R3'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S3_O_R3_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_O_R4'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S3_O_R4_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_O_R5'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S3_O_R5_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_U_R1'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S3_U_R1_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_U_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S3_U_R2_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS3_U_R3'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S3_U_R3_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_O_R1'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S4_O_R1_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_O_R2'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), name='Kontakt S4_O_R2_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_O_R3'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S4_O_R3_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_U_R1'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )), name='Kontakt S4_U_R1_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_U_R2'].faces.getSequenceFromMask(
    mask=('[#3f ]', ), )), name='Kontakt S4_U_R2_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='entry', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Kontakt_nofric', master=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aS4_U_R3'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )), name='Kontakt S4_U_R3_entry', slave=Region(
    side1Faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), sliding=FINITE, thickness=ON)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_FS_OW', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[67], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_FS_UW', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[72], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R1', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[84], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R2', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[87], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R3', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[90], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R4', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[93], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R5', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[96], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R6', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[99], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_U_R1', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[75], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_U_R2', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[78], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_U_R3', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[81], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_O_R1', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[111], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_O_R2', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[114], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_O_R3', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[117], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_O_R4', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[120], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_O_R5', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[123], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_U_R1', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[102], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_U_R2', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[105], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_U_R3', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[108], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_O_R1', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[135], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_O_R2', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[138], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_O_R3', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[141], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_O_R4', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[144], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_O_R5', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[147], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_U_R1', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[126], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_U_R2', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[129], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_U_R3', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[132], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_O_R1', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[159], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_O_R2', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[162], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_O_R3', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[165], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_U_R1', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[150], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_U_R2', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[153], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_U_R3', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[156], )), u1=0.0, u2=
    0.0, u3=0.0, ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R1_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[84], )), u1=UNSET, u2=
    UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R2_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[87], )), u1=UNSET, u2=
    UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R3_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[90], )), u1=UNSET, u2=
    UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R4_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[93], )), u1=UNSET, u2=
    UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R5_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[96], )), u1=UNSET, u2=
    UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_O_R6_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[99], )), u1=UNSET, u2=
    UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_U_R1_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[75], )), u1=UNSET, u2=
    UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_U_R2_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[78], )), u1=UNSET, u2=
    UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S1_U_R3_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[81], )), u1=UNSET, u2=
    UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_O_R1_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[111], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_O_R2_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[114], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_O_R3_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[117], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_O_R4_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[120], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_O_R5_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[123], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_U_R1_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[102], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_U_R2_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[105], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S2_U_R3_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[108], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_O_R1_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[135], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_O_R2_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[138], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_O_R3_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[141], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_O_R4_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[144], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_O_R5_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[147], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_U_R1_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[126], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_U_R2_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[129], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S3_U_R3_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[132], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_O_R1_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[159], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_O_R2_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[162], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_O_R3_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[165], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_U_R1_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[150], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_U_R2_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[153], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_S4_U_R3_entry', region=Region(referencePoints=(
    mdb.models['Hutprofil'].rootAssembly.referencePoints[156], )), u1=UNSET, 
    u2=UNSET, u3=UNSET, ur1=0.0, ur2=UNSET, ur3=UNSET)
mdb.models['Hutprofil'].parts['Blech'].DatumPlaneByPrincipalPlane(offset=340, 
    principalPlane=XYPLANE)
mdb.models['Hutprofil'].parts['Blech'].PartitionCellByDatumPlane(cells=
    mdb.models['Hutprofil'].parts['Blech'].cells, datumPlane=
    mdb.models['Hutprofil'].parts['Blech'].datums[5])
mdb.models['Hutprofil'].parts['Blech'].DatumPlaneByPrincipalPlane(offset=260, 
    principalPlane=XYPLANE)
mdb.models['Hutprofil'].parts['Blech'].PartitionCellByDatumPlane(cells=
    mdb.models['Hutprofil'].parts['Blech'].cells, datumPlane=
    mdb.models['Hutprofil'].parts['Blech'].datums[7])
mdb.models['Hutprofil'].parts['Blech'].DatumPlaneByPrincipalPlane(offset=380, 
    principalPlane=XYPLANE)
mdb.models['Hutprofil'].parts['Blech'].PartitionCellByDatumPlane(cells=
    mdb.models['Hutprofil'].parts['Blech'].cells, datumPlane=
    mdb.models['Hutprofil'].parts['Blech'].datums[9])
mdb.models['Hutprofil'].parts['Blech'].DatumPlaneByPrincipalPlane(offset=220, 
    principalPlane=XYPLANE)
mdb.models['Hutprofil'].parts['Blech'].PartitionCellByDatumPlane(cells=
    mdb.models['Hutprofil'].parts['Blech'].cells, datumPlane=
    mdb.models['Hutprofil'].parts['Blech'].datums[11])
mdb.models['Hutprofil'].parts['Blech'].DatumPlaneByPrincipalPlane(offset=5, 
    principalPlane=YZPLANE)
mdb.models['Hutprofil'].parts['Blech'].PartitionCellByDatumPlane(cells=
    mdb.models['Hutprofil'].parts['Blech'].cells[3], datumPlane=
    mdb.models['Hutprofil'].parts['Blech'].datums[13])
mdb.models['Hutprofil'].parts['Blech'].DatumPlaneByPrincipalPlane(offset=15, 
    principalPlane=YZPLANE)
mdb.models['Hutprofil'].parts['Blech'].PartitionCellByDatumPlane(cells=
    mdb.models['Hutprofil'].parts['Blech'].cells[4], datumPlane=
    mdb.models['Hutprofil'].parts['Blech'].datums[15])
mdb.models['Hutprofil'].parts['Blech'].DatumPlaneByPrincipalPlane(offset=25, 
    principalPlane=YZPLANE)
mdb.models['Hutprofil'].parts['Blech'].PartitionCellByDatumPlane(cells=
    mdb.models['Hutprofil'].parts['Blech'].cells[5], datumPlane=
    mdb.models['Hutprofil'].parts['Blech'].datums[17])
mdb.models['Hutprofil'].parts['Blech'].PartitionFaceByDatumPlane(datumPlane=
    mdb.models['Hutprofil'].parts['Blech'].datums[17], faces=
    mdb.models['Hutprofil'].parts['Blech'].faces.getSequenceFromMask(mask=(
    '[#0 #400 ]', ), ))
mdb.models['Hutprofil'].parts['Blech'].PartitionFaceByDatumPlane(datumPlane=
    mdb.models['Hutprofil'].parts['Blech'].datums[17], faces=
    mdb.models['Hutprofil'].parts['Blech'].faces.getSequenceFromMask(mask=(
    '[#0 #20 ]', ), ))
mdb.models['Hutprofil'].parts['Blech'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8I, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT), ), regions=(
    mdb.models['Hutprofil'].parts['Blech'].cells, ))
mdb.models['Hutprofil'].parts['Blech'].seedPart(minSizeFactor=0.1, size=1)
mdb.models['Hutprofil'].parts['Blech'].generateMesh()
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_ylock', region=Region(
    faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#0 #1000 ]', ), )), u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=
    UNSET, ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_zstart_entry', region=Region(
    faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#0 #40 ]', ), )), u1=UNSET, u2=UNSET, u3=40, ur1=UNSET, ur2=UNSET, 
    ur3=UNSET)
mdb.models['Hutprofil'].DisplacementBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC_ylock_entry', region=Region(
    faces=mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    mask=('[#0 #40 ]', ), )), u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, 
    ur3=UNSET)
del mdb.models['Model-1']
mdb.models['Hutprofil'].parts['Blech'].features['Solid extrude-1'].setValues(
    depth=2000.0)
mdb.models['Hutprofil'].parts['Blech'].regenerate()
mdb.models['Hutprofil'].parts['Blech'].features['Datum plane-1'].setValues(
    offset=1040.0)
mdb.models['Hutprofil'].parts['Blech'].regenerate()
mdb.models['Hutprofil'].parts['Blech'].features['Datum plane-2'].setValues(
    offset=960.0)
mdb.models['Hutprofil'].parts['Blech'].regenerate()
mdb.models['Hutprofil'].parts['Blech'].features['Datum plane-3'].setValues(
    offset=1080.0)
mdb.models['Hutprofil'].parts['Blech'].regenerate()
mdb.models['Hutprofil'].parts['Blech'].features['Datum plane-4'].setValues(
    offset=920.0)
mdb.models['Hutprofil'].parts['Blech'].regenerate()
mdb.models['Hutprofil'].rootAssembly.regenerate()
mdb.models['Hutprofil'].rootAssembly.translate(instanceList=('aBlech', ), 
    vector=(0.0, 0.0, -1400.0))
mdb.models['Hutprofil'].parts['Blech'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8I, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Hutprofil'].parts['Blech'].cells.getSequenceFromMask(('[#ff ]', 
    ), ), ))
mdb.models['Hutprofil'].parts['Blech'].generateMesh()
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Hutprofil'].rootAssembly.regenerate()
mdb.models['Hutprofil'].rootAssembly.regenerate()
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Hutprofil'].boundaryConditions['BC_ylock'].move('entry', 'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_ylock_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_zstart_entry'].move('entry', 
    'Initial')
#* ValueError: Non-zero boundary condition in initial step.
mdb.models['Hutprofil'].boundaryConditions['BC_S4_U_R3_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_U_R3'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_U_R2_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_U_R2'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_U_R1_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_FS_OW'].move('entry', 'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_FS_UW'].move('entry', 'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R1'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R1_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R2'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R2_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R3'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R3_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R4'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R4_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R5'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R5_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R6'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R6_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_U_R1'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_U_R1_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_U_R2'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_U_R2_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_U_R3'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S1_U_R3_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R1'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R1_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R2'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R2_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R3'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R3_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R4'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R4_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R5'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R5_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_U_R1'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_U_R1_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_U_R2'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_U_R2_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_U_R3'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S2_U_R3_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R1'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R1_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R2'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R2_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R3'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R3_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R4'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R4_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R5'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R5_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_U_R1'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_U_R1_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_U_R2'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_U_R2_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_U_R3'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S3_U_R3_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_O_R1'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_O_R1_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_O_R2'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_O_R2_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_O_R3'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_O_R3_entry'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].boundaryConditions['BC_S4_U_R1'].move('entry', 
    'Initial')
mdb.models['Hutprofil'].interactions['Kontakt FS_OW'].move('entry', 'Initial')
mdb.models['Hutprofil'].interactions['Kontakt FS_UW'].move('entry', 'Initial')
mdb.models['Hutprofil'].interactions['Kontakt FS_OW'].setValues(adjustMethod=
    OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, enforcement=
    SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, thickness=ON, 
    tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt FS_UW'].setValues(adjustMethod=
    OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, enforcement=
    SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, thickness=ON, 
    tied=OFF)
mdb.models['Hutprofil'].ImplicitDynamicsStep(initialInc=10000.0, minInc=0.1, 
    name='move', previous='entry', timePeriod=10000.0)
mdb.models['Hutprofil'].steps['move'].setValues(initialInc=1.0, maxNumInc=
    100000000)
mdb.models['Hutprofil'].boundaryConditions['BC_zstart_entry'].setValuesInStep(
    stepName='move', u3=2000.0)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R1_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R2_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R3_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R4_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R5_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S2_U_R1_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S2_U_R2_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S2_U_R3_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R1_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R2_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R3_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R4_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R5_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S3_U_R1_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S3_U_R2_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S3_U_R3_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S4_O_R1_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S4_O_R2_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S4_O_R3_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S4_U_R1_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S4_U_R2_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S4_U_R3_entry'].move('entry', 
    'move')
mdb.models['Hutprofil'].interactions['Kontakt S4_U_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R4_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R5_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R6_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_U_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_U_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_U_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R4_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R5_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_U_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_U_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_U_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R4_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R5_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_U_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_U_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_U_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_O_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_O_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_O_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_U_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_U_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, sliding=FINITE, 
    thickness=ON, tied=OFF)
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Hutprofil'].parts['Blech'].deleteMesh(regions=
    mdb.models['Hutprofil'].parts['Blech'].cells.getSequenceFromMask(('[#90 ]', 
    ), ))
mdb.models['Hutprofil'].ConstrainedSketch(gridSpacing=100.12, name=
    '__profile__', sheetSize=4004.99, transform=
    mdb.models['Hutprofil'].parts['Blech'].MakeSketchTransform(
    sketchPlane=mdb.models['Hutprofil'].parts['Blech'].faces[34], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Hutprofil'].parts['Blech'].edges[74], 
    sketchOrientation=RIGHT, origin=(50.0, 1.5, 1539.503083)))
mdb.models['Hutprofil'].parts['Blech'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Hutprofil'].sketches['__profile__'])
mdb.models['Hutprofil'].sketches['__profile__'].Line(point1=(438.143279304687, 
    50.0), point2=(438.143279304687, -50.0))
mdb.models['Hutprofil'].sketches['__profile__'].VerticalConstraint(
    addUndoState=False, entity=
    mdb.models['Hutprofil'].sketches['__profile__'].geometry[44])
mdb.models['Hutprofil'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Hutprofil'].sketches['__profile__'].geometry[22], entity2=
    mdb.models['Hutprofil'].sketches['__profile__'].geometry[44])
mdb.models['Hutprofil'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Hutprofil'].sketches['__profile__'].vertices[22], entity2=
    mdb.models['Hutprofil'].sketches['__profile__'].geometry[22])
mdb.models['Hutprofil'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Hutprofil'].sketches['__profile__'].vertices[23], entity2=
    mdb.models['Hutprofil'].sketches['__profile__'].geometry[35])
mdb.models['Hutprofil'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Hutprofil'].sketches['__profile__'].geometry[37], entity2=
    mdb.models['Hutprofil'].sketches['__profile__'].geometry[44], textPoint=(
    448.892180671875, 30.9245986938477), value=20.0)
mdb.models['Hutprofil'].parts['Blech'].PartitionFaceBySketch(faces=
    mdb.models['Hutprofil'].parts['Blech'].faces.getSequenceFromMask((
    '[#0 #4 ]', ), ), sketch=mdb.models['Hutprofil'].sketches['__profile__'], 
    sketchUpEdge=mdb.models['Hutprofil'].parts['Blech'].edges[74])
del mdb.models['Hutprofil'].sketches['__profile__']
mdb.models['Hutprofil'].parts['Blech'].PartitionCellBySweepEdge(cells=
    mdb.models['Hutprofil'].parts['Blech'].cells.getSequenceFromMask(('[#80 ]', 
    ), ), edges=(mdb.models['Hutprofil'].parts['Blech'].edges[0], ), sweepPath=
    mdb.models['Hutprofil'].parts['Blech'].edges[67])
mdb.models['Hutprofil'].rootAssembly.regenerate()
mdb.models['Hutprofil'].steps['move'].setValues(maxNumInc=100000, minInc=1e-05, 
    timePeriod=100.0)
mdb.models['Hutprofil'].rootAssembly.Surface(name='BlechOben', side1Faces=
    mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    ('[#84102810 #1084 ]', ), ))
mdb.models['Hutprofil'].interactions['Kontakt FS_OW'].setValues(adjustMethod=
    OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, enforcement=
    SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].rootAssembly.Surface(name='BlechUnten', side1Faces=
    mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].faces.getSequenceFromMask(
    ('[#11090108 #4208 ]', ), ))
mdb.models['Hutprofil'].interactions['Kontakt FS_UW'].setValues(adjustMethod=
    OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, enforcement=
    SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R4_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R5_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_O_R6_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_U_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_U_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S1_U_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R4_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_O_R5_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_U_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_U_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S2_U_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R4_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_O_R5_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_U_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_U_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S3_U_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_O_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_O_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_O_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechOben'], sliding=FINITE, 
    thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_U_R1_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_U_R2_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactions['Kontakt S4_U_R3_entry'].setValues(
    adjustMethod=OVERCLOSED, bondingSet=None, contactTracking=TWO_CONFIG, 
    enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, slave=
    mdb.models['Hutprofil'].rootAssembly.surfaces['BlechUnten'], sliding=FINITE
    , thickness=ON, tied=OFF)
mdb.models['Hutprofil'].interactionProperties['Kontakt_nofric'].tangentialBehavior.setValues(
    absoluteDistance=0.01, dependencies=0, directionality=ISOTROPIC, 
    elasticSlipStiffness=None, formulation=PENALTY, maximumElasticSlip=
    ABSOLUTE_DISTANCE, pressureDependency=OFF, shearStressLimit=None, 
    slipRateDependency=OFF, table=((0.135, ), ), temperatureDependency=OFF)
mdb.models['Hutprofil'].interactionProperties['Kontakt_nofric'].tangentialBehavior.setValues(
    absoluteDistance=0.01, dependencies=0, directionality=ISOTROPIC, 
    elasticSlipStiffness=None, formulation=PENALTY, maximumElasticSlip=
    ABSOLUTE_DISTANCE, pressureDependency=OFF, shearStressLimit=None, 
    slipRateDependency=OFF, table=((0.15, ), ), temperatureDependency=OFF)
mdb.models['Hutprofil'].boundaryConditions['BC_FS_OW'].setValues(u2=UNSET)
mdb.models['Hutprofil'].boundaryConditions['BC_FS_UW'].setValues(u2=UNSET)
mdb.models['Hutprofil'].boundaryConditions['BC_FS_OW'].setValues(u2=SET)
mdb.models['Hutprofil'].boundaryConditions['BC_FS_UW'].setValues(u2=SET)
mdb.models['Hutprofil'].boundaryConditions['BC_FS_OW'].setValuesInStep(
    stepName='entry', u2=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_FS_UW'].setValuesInStep(
    stepName='entry', u2=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R1'].setValuesInStep(
    stepName='entry', u2=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_FS_OW'].setValuesInStep(
    stepName='entry', u2=0.0, ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_FS_UW'].setValuesInStep(
    stepName='entry', u2=0.0, ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R1'].setValuesInStep(
    stepName='entry', u2=0.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R1_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R2_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R3_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R4_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R5_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_O_R6_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_U_R1_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_U_R2_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S1_U_R3_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R1_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R1_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R2_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R3_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R4_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S2_O_R5_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S2_U_R1_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S2_U_R2_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S2_U_R3_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R1_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R2_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R3_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R4_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S3_O_R5_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S3_U_R1_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S3_U_R2_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S3_U_R1_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S3_U_R3_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S4_O_R1_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S4_O_R2_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S4_O_R3_entry'].setValuesInStep(
    stepName='entry', ur1=-15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S4_U_R1_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S4_U_R2_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_S4_U_R3_entry'].setValuesInStep(
    stepName='entry', ur1=15.0)
mdb.models['Hutprofil'].boundaryConditions['BC_ylock'].deactivate('entry')
mdb.models['Hutprofil'].boundaryConditions['BC_ylock_entry'].deactivate(
    'entry')
mdb.models['Hutprofil'].parts['Blech'].Set(cells=
    mdb.models['Hutprofil'].parts['Blech'].cells.getSequenceFromMask((
    '[#1ff ]', ), ), name='FullBlech')
mdb.models['Hutprofil'].parts['Blech'].sectionAssignments[0].setValues(region=
    mdb.models['Hutprofil'].parts['Blech'].sets['FullBlech'])
mdb.models['Hutprofil'].rootAssembly.regenerate()
mdb.models['Hutprofil'].boundaryConditions['BC_zstart_entry'].suppress()
mdb.models['Hutprofil'].VelocityBC(amplitude=UNSET, createStepName='entry', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Velo', 
    region=
    mdb.models['Hutprofil'].rootAssembly.instances['aBlech'].sets['FullBlech'], 
    v1=UNSET, v2=UNSET, v3=100.0, vr1=UNSET, vr2=UNSET, vr3=UNSET)
mdb.models['Hutprofil'].steps['entry'].setValues(initialInc=0.01, minInc=4e-06, 
    timePeriod=0.4)
mdb.models['Hutprofil'].steps['move'].setValues(timePeriod=10.0)
mdb.models['Hutprofil'].parts['Blech'].deleteMesh(regions=
    mdb.models['Hutprofil'].parts['Blech'].cells.getSequenceFromMask(('[#d8 ]', 
    ), ))
mdb.models['Hutprofil'].parts['Blech'].seedEdgeBySize(constraint=FINER, edges=
    mdb.models['Hutprofil'].parts['Blech'].edges.getSequenceFromMask((
    '[#15412a #2a20300 #420404 ]', ), ), size=0.8)
mdb.models['Hutprofil'].parts['Blech'].deleteMesh(regions=
    mdb.models['Hutprofil'].parts['Blech'].cells.getSequenceFromMask(('[#6 ]', 
    ), ))
mdb.models['Hutprofil'].parts['Blech'].seedEdgeBySize(constraint=FINER, edges=
    mdb.models['Hutprofil'].parts['Blech'].edges.getSequenceFromMask((
    '[#a2800000 #5c1d #3000 ]', ), ), size=1.0)
mdb.models['Hutprofil'].parts['Blech'].Set(edges=
    mdb.models['Hutprofil'].parts['Blech'].edges.getSequenceFromMask((
    '[#a2800000 #5c1d #3000 ]', ), ), name='TestStripe')
mdb.models['Hutprofil'].parts['Blech'].seedEdgeBySize(constraint=FINER, edges=
    mdb.models['Hutprofil'].parts['Blech'].edges.getSequenceFromMask((
    '[#28000 #0 #1c0070 ]', ), ), size=1.0)
mdb.models['Hutprofil'].parts['Blech'].Set(edges=
    mdb.models['Hutprofil'].parts['Blech'].edges.getSequenceFromMask((
    '[#28000 #0 #1c0070 ]', ), ), name='Beginning')
mdb.models['Hutprofil'].parts['Blech'].seedPart(minSizeFactor=0.1, size=5.0)
mdb.models['Hutprofil'].parts['Blech'].generateMesh()
mdb.models['Hutprofil'].parts['Blech'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8I, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Hutprofil'].parts['Blech'].cells.getSequenceFromMask((
    '[#1ff ]', ), ), ))
mdb.models['Hutprofil'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Hutprofil', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Impli', nodalOutputPrecision=SINGLE, 
    numCpus=4, numDomains=4, numGPUs=0, queue=None, resultsFormat=ODB, scratch=
    '', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
