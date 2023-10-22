# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by fratschiller on Wed Oct 18 06:52:04 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=323.996887207031, 
    height=130.76481628418)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.rectangle(point1=(3.75, 20.0), point2=(12.5, -30.0))
s.DistanceDimension(entity1=g[2], entity2=g[5], textPoint=(20.7489471435547, 
    12.6530609130859), value=10.0)
s.DistanceDimension(entity1=g[2], entity2=g[3], textPoint=(3.16856384277344, 
    26.9387741088867), value=1.0)
s.delete(objectList=(d[0], ))
s.DistanceDimension(entity1=g[2], entity2=g[5], textPoint=(6.54154205322266, 
    8.57143020629883), value=5.0)
s.ObliqueDimension(vertex1=v[2], vertex2=v[3], textPoint=(15.8427886962891, 
    12.6530609130859), value=50.0)
p = mdb.models['Model-1'].Part(name='Stempel', dimensionality=THREE_D, 
    type=ANALYTIC_RIGID_SURFACE)
p = mdb.models['Model-1'].parts['Stempel']
p.AnalyticRigidSurfRevolve(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Stempel']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(-45.0, 1.25), point2=(35.0, -1.25))
s1.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(-21.9754867553711, 
    -4.7959156036377), value=150.0)
s1.DistanceDimension(entity1=g[5], entity2=g[3], textPoint=(-37.4094352722168, 
    -1.02040481567383), value=2.5)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(-50.0, 1.25), point2=(55.0, -1.25))
s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-54.2282485961914, 
    0.0512466430664062), value=2.5)
s.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(-43.1570777893066, 
    -3.84333610534668), value=150.0)
p = mdb.models['Model-1'].Part(name='Blech', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Blech']
p.BaseSolidExtrude(sketch=s, depth=50.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Blech']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Blech']
f1, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[3], sketchUpEdge=e[8], 
    sketchPlaneSide=SIDE1, origin=(25.0, 1.25, 25.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=316.23, gridSpacing=7.9, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Blech']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.ConstructionLine(point1=(-75.0, 0.0), point2=(75.0, 0.0))
s1.HorizontalConstraint(entity=g[6], addUndoState=False)
s1.Line(point1=(-75.0, 1.975), point2=(75.0, 1.975))
s1.HorizontalConstraint(entity=g[7], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[7], addUndoState=False)
s1.CoincidentConstraint(entity1=v[4], entity2=g[2], addUndoState=False)
s1.CoincidentConstraint(entity1=v[5], entity2=g[5], addUndoState=False)
s1.Line(point1=(-75.0, -1.975), point2=(75.0, -1.975))
s1.HorizontalConstraint(entity=g[8], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[8], addUndoState=False)
s1.CoincidentConstraint(entity1=v[6], entity2=g[2], addUndoState=False)
s1.CoincidentConstraint(entity1=v[7], entity2=g[5], addUndoState=False)
s1.Line(point1=(-63.2, 25.0), point2=(-63.2, -25.0))
s1.VerticalConstraint(entity=g[9], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[9], addUndoState=False)
s1.CoincidentConstraint(entity1=v[8], entity2=g[3], addUndoState=False)
s1.CoincidentConstraint(entity1=v[9], entity2=g[4], addUndoState=False)
s1.Line(point1=(0.0, 25.0), point2=(0.0, -25.0))
s1.VerticalConstraint(entity=g[10], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[10], addUndoState=False)
s1.CoincidentConstraint(entity1=v[10], entity2=g[3], addUndoState=False)
s1.EqualDistanceConstraint(entity1=v[2], entity2=v[1], midpoint=v[10], 
    addUndoState=False)
s1.CoincidentConstraint(entity1=v[11], entity2=g[4], addUndoState=False)
s1.EqualDistanceConstraint(entity1=v[0], entity2=v[3], midpoint=v[11], 
    addUndoState=False)
s1.Line(point1=(59.25, 25.0), point2=(59.25, -25.0))
s1.VerticalConstraint(entity=g[11], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[11], addUndoState=False)
s1.CoincidentConstraint(entity1=v[12], entity2=g[3], addUndoState=False)
s1.CoincidentConstraint(entity1=v[13], entity2=g[4], addUndoState=False)
s1.SymmetryConstraint(entity1=g[7], entity2=g[8], symmetryAxis=g[6])
s1.DistanceDimension(entity1=g[7], entity2=g[8], textPoint=(-49.4136734008789, 
    -4.43361473083496), value=4.0)
s1.DistanceDimension(entity1=g[9], entity2=g[2], textPoint=(-72.7072982788086, 
    22.0706367492676), value=15.0)
s1.DistanceDimension(entity1=g[11], entity2=g[5], textPoint=(70.2707214355469, 
    12.716194152832), value=15.0)
p = mdb.models['Model-1'].parts['Blech']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#8 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e1[8], faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Blech']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e = p.edges
pickedEdges =(e[0], e[4], e[11], e[14], e[17], e[21], e[27], e[29])
p.PartitionCellBySweepEdge(sweepPath=e[31], cells=pickedCells, 
    edges=pickedEdges)
p = mdb.models['Model-1'].parts['Blech']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#7 ]', ), )
e1 = p.edges
pickedEdges =(e1[29], e1[30], e1[32], e1[35], e1[36], e1[39], e1[40], e1[43], 
    e1[45])
p.PartitionCellBySweepEdge(sweepPath=e1[15], cells=pickedCells, 
    edges=pickedEdges)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Aluminium')
mdb.models['Model-1'].materials['Aluminium'].Elastic(table=((70000.0, 0.3), ))
mdb.models['Model-1'].materials['Aluminium'].Plastic(scaleStress=None, table=((
    305.0, 0.0), (309.0, 0.001125), (320.0, 0.013996), (331.0, 0.118731), (
    340.0, 0.281615), (350.0, 0.481607), (360.0, 0.78642), (370.0, 1.18941)))
mdb.models['Model-1'].HomogeneousSolidSection(name='Material', 
    material='Aluminium', thickness=None)
p = mdb.models['Model-1'].parts['Blech']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#fff ]', ), )
region = p.Set(cells=cells, name='Blech')
p = mdb.models['Model-1'].parts['Blech']
p.SectionAssignment(region=region, sectionName='Material', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Blech']
a.Instance(name='Blech-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Stempel']
a.Instance(name='Stempel-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Stempel']
a.Instance(name='Stempel-2', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Stempel']
a.Instance(name='Stempel-3', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
a.rotate(instanceList=('Stempel-1', 'Stempel-2', 'Stempel-3'), axisPoint=(0.0, 
    0.0, 0.0), axisDirection=(10.0, 0.0, 0.0), angle=90.0)
#: The instances were rotated by 90. degrees about the axis defined by the point 0., 0., 0. and the vector 10., 0., 0.
session.viewports['Viewport: 1'].view.setValues(nearPlane=293.356, 
    farPlane=459.022, width=96.8193, height=40.9118, viewOffsetX=8.27466, 
    viewOffsetY=17.8716)
session.viewports['Viewport: 1'].view.setValues(nearPlane=295.865, 
    farPlane=463.263, width=97.6476, height=41.2618, cameraPosition=(394.685, 
    87.3424, 17.0752), cameraUpVector=(-0.484507, 0.513369, -0.708312), 
    cameraTarget=(33.228, 0.505234, 26.3875), viewOffsetX=8.34545, 
    viewOffsetY=18.0245)
session.viewports['Viewport: 1'].view.setValues(nearPlane=292.12, 
    farPlane=467.007, width=148.674, height=62.8234, viewOffsetX=5.41143, 
    viewOffsetY=13.8575)
session.viewports['Viewport: 1'].view.setValues(nearPlane=309.593, 
    farPlane=456.273, width=157.567, height=66.5811, cameraPosition=(119.749, 
    164.684, -322.83), cameraUpVector=(-0.243225, 0.680324, 0.691376), 
    cameraTarget=(35.4925, -7.21526, -4.03557), viewOffsetX=5.73511, 
    viewOffsetY=14.6864)
a = mdb.models['Model-1'].rootAssembly
a.rotate(instanceList=('Stempel-1', 'Stempel-2', 'Stempel-3'), axisPoint=(0.0, 
    0.0, 100.0), axisDirection=(0.0, 0.0, -10.0), angle=90.0)
#: The instances were rotated by 90. degrees about the axis defined by the point 0., 0., 100. and the vector 0., 0., -10.
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('Stempel-3', ), vector=(25.0, 6.25, 30.0))
#: The instance Stempel-3 was translated by 25., 6.25, 30. with respect to the assembly coordinate system
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('Stempel-2', ), vector=(-35.0, -6.25, 30.0))
#: The instance Stempel-2 was translated by -35., -6.25, 30. with respect to the assembly coordinate system
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('Stempel-1', ), vector=(85.0, -6.25, 30.0))
#: The instance Stempel-1 was translated by 85., -6.25, 30. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=295.13, 
    farPlane=357.326, width=242.098, height=102.3, viewOffsetX=18.4895, 
    viewOffsetY=-3.352)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Blech-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#56 ]', ), )
a.Set(cells=cells1, name='Auswertung')
#: The set 'Auswertung' has been created (4 cells).
session.viewports['Viewport: 1'].view.setValues(nearPlane=273.965, 
    farPlane=378.65, width=224.736, height=94.964, cameraPosition=(-3.85777, 
    -278.846, -142.019), cameraUpVector=(-0.146953, -0.490412, 0.859012), 
    cameraTarget=(24.757, 1.24004, 22.7782), viewOffsetX=17.1635, 
    viewOffsetY=-3.11161)
session.viewports['Viewport: 1'].view.setValues(nearPlane=271.783, 
    farPlane=385.004, width=222.946, height=94.2078, cameraPosition=(3.21549, 
    -102.492, -286.247), cameraUpVector=(0.0397775, -0.953026, 0.300266), 
    cameraTarget=(25.2118, -3.84763, 23.9316), viewOffsetX=17.0268, 
    viewOffsetY=-3.08683)
session.viewports['Viewport: 1'].view.setValues(nearPlane=267.735, 
    farPlane=387.081, width=219.626, height=92.8048, cameraPosition=(-11.6535, 
    -111.958, -280.494), cameraUpVector=(0.019624, -0.942508, 0.333607), 
    cameraTarget=(25.1105, -3.11889, 24.8385), viewOffsetX=16.7732, 
    viewOffsetY=-3.04086)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Verformen', previous='Initial', 
    maxNumInc=1000000, initialInc=0.005, minInc=1e-15, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Verformen')
mdb.models['Model-1'].StaticStep(name='Halten', previous='Verformen', 
    maxNumInc=100000, initialInc=0.05, minInc=1e-15)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Halten')
mdb.models['Model-1'].StaticStep(name='Ausgansposition', previous='Halten', 
    maxNumInc=100000, initialInc=0.05, minInc=1e-15)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='Ausgansposition')
regionDef=mdb.models['Model-1'].rootAssembly.sets['Auswertung']
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(variables=(
    'COOR1', 'COOR2', 'COOR3'), region=regionDef, sectionPoints=DEFAULT, 
    rebar=EXCLUDE)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].ContactProperty('Reibung')
mdb.models['Model-1'].interactionProperties['Reibung'].TangentialBehavior(
    formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
    pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((
    0.15, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
    fraction=0.005, elasticSlipStiffness=None)
mdb.models['Model-1'].interactionProperties['Reibung'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)
#: The interaction property "Reibung" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Verformen')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
#: Warning: Some of the entities selected belong to an analytical rigid part instance. All selected entities must belong to that instance.
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Stempel-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#f ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Blech-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#30c3000 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='AuflageA', 
    createStepName='Initial', main=region1, secondary=region2, sliding=FINITE, 
    thickness=ON, interactionProperty='Reibung', adjustMethod=NONE, 
    initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#: The interaction "AuflageA" has been created.
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Stempel-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#f ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Blech-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4104000 #4000c ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='AuflageB', 
    createStepName='Initial', main=region1, secondary=region2, sliding=FINITE, 
    thickness=ON, interactionProperty='Reibung', adjustMethod=NONE, 
    initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#: The interaction "AuflageB" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Verformen')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].view.setValues(nearPlane=274.358, 
    farPlane=392.688, width=225.059, height=95.1006, cameraPosition=(104.02, 
    292.796, -114.386), cameraUpVector=(-0.780109, -0.118625, -0.614295), 
    cameraTarget=(30.9288, 11.0073, 32.8486), viewOffsetX=17.1881, 
    viewOffsetY=-3.11608)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Stempel-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#f ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Blech-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #11d200 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Stempel', 
    createStepName='Initial', main=region1, secondary=region2, sliding=FINITE, 
    thickness=ON, interactionProperty='Reibung', adjustMethod=NONE, 
    initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#: The interaction "Stempel" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
mdb.models['Model-1'].TabularAmplitude(name='StempelWeg', timeSpan=TOTAL, 
    smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 20.0), (2.0, 20.0), (3.0, 
    0.0)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=273.429, 
    farPlane=396.006, width=224.297, height=94.7787, cameraPosition=(68.7552, 
    89.7251, 344.491), cameraUpVector=(-0.00543934, 0.961964, -0.273123), 
    cameraTarget=(24.7163, 1.20903, 33.6038), viewOffsetX=17.1299, 
    viewOffsetY=-3.10553)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Stempel-2'].edges
a.ReferencePoint(point=a.instances['Stempel-2'].InterestingPoint(edge=e1[2], 
    rule=CENTER))
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['Stempel-3'].edges
a.ReferencePoint(point=a.instances['Stempel-3'].InterestingPoint(edge=e21[2], 
    rule=CENTER))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Stempel-1'].edges
a.ReferencePoint(point=a.instances['Stempel-1'].InterestingPoint(edge=e1[2], 
    rule=CENTER))
session.viewports['Viewport: 1'].view.setValues(nearPlane=227.833, 
    farPlane=412.295, width=186.895, height=78.9739, cameraPosition=(-162.458, 
    154.798, -186.07), cameraUpVector=(0.201999, 0.871034, 0.447767), 
    cameraTarget=(54.5618, 5.52695, 6.40333), viewOffsetX=14.2734, 
    viewOffsetY=-2.58767)
session.viewports['Viewport: 1'].view.setValues(nearPlane=255.876, 
    farPlane=397.23, width=209.899, height=88.6945, cameraPosition=(-47.187, 
    111.396, -275.208), cameraUpVector=(0.0559785, 0.942775, 0.328696), 
    cameraTarget=(56.4552, 4.09343, 14.9128), viewOffsetX=16.0302, 
    viewOffsetY=-2.90617)
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['Stempel-2'].edges
a.ReferencePoint(point=a.instances['Stempel-2'].InterestingPoint(edge=e21[1], 
    rule=CENTER))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Stempel-3'].edges
a.ReferencePoint(point=a.instances['Stempel-3'].InterestingPoint(edge=e1[1], 
    rule=CENTER))
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['Stempel-1'].edges
a.ReferencePoint(point=a.instances['Stempel-1'].InterestingPoint(edge=e21[1], 
    rule=CENTER))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[17], r1[19], r1[20], r1[22], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].EncastreBC(name='Auflager', createStepName='Initial', 
    region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[18], r1[21], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].DisplacementBC(name='Stempel', createStepName='Initial', 
    region=region, u1=SET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Verformen')
mdb.models['Model-1'].boundaryConditions['Stempel'].setValuesInStep(
    stepName='Verformen', u2=1.0, amplitude='StempelWeg')
mdb.models['Model-1'].amplitudes['StempelWeg'].setValues(timeSpan=TOTAL, 
    smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, -20.0), (2.0, -20.0), (3.0, 
    0.0)))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Halten')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Blech-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#40000 ]', ), )
region = regionToolset.Region(vertices=verts1)
mdb.models['Model-1'].ZsymmBC(name='BlechZ', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Blech']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Blech']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=270.072, 
    farPlane=421.912, width=163.814, height=69.3927, cameraPosition=(218.243, 
    78.4905, -251.163), cameraUpVector=(-0.523674, 0.796555, 0.302102))
session.viewports['Viewport: 1'].view.setValues(nearPlane=289.669, 
    farPlane=393.417, width=175.7, height=74.4279, cameraPosition=(-37.8521, 
    129.411, -284.827), cameraUpVector=(-0.236569, 0.662919, 0.710334), 
    cameraTarget=(29.0369, -4.72681, 23.52))
session.viewports['Viewport: 1'].view.setValues(nearPlane=273.315, 
    farPlane=408.197, width=165.781, height=70.2258, cameraPosition=(-110.97, 
    115.324, -265.458), cameraUpVector=(-0.0270924, 0.710034, 0.703646), 
    cameraTarget=(29.3165, -4.67295, 23.4459))
session.viewports['Viewport: 1'].view.setValues(nearPlane=252.555, 
    farPlane=425.899, width=153.189, height=64.8917, cameraPosition=(-229.074, 
    77.1465, -186.201), cameraUpVector=(0.172886, 0.758654, 0.628135), 
    cameraTarget=(30.0417, -4.43852, 22.9592))
p = mdb.models['Model-1'].parts['Blech']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#90441104 #81021010 #28 ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=0.5, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
    kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
    hourglassControl=DEFAULT, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Blech']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#fff ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['Blech']
p.generateMesh()
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.saveAs(pathName='C:/temp/3Punkt_Biegen')
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".
# DELETED
mdb.save()
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Blech']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Stempel']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=93.1062, 
    farPlane=173.421, width=100.679, height=42.5427, cameraPosition=(-0.587794, 
    128.256, -1.79512), cameraUpVector=(-0.757334, -0.3354, -0.560315), 
    cameraTarget=(-0.895859, -3.20828, -0.895859))
session.viewports['Viewport: 1'].view.setValues(nearPlane=94.2583, 
    farPlane=172.282, width=101.925, height=43.0692, cameraPosition=(0.180808, 
    128.227, -3.63319), cameraUpVector=(-0.760433, -0.338681, -0.554109), 
    cameraTarget=(-0.885502, -3.20867, -0.920627))
session.viewports['Viewport: 1'].view.setValues(nearPlane=100.974, 
    farPlane=165.567, width=26.4171, height=11.1628, viewOffsetX=-0.0828445, 
    viewOffsetY=-0.651588)
session.viewports['Viewport: 1'].view.setValues(nearPlane=101.987, 
    farPlane=164.394, width=26.6821, height=11.2748, cameraPosition=(-30.4747, 
    107.921, 63.7298), cameraUpVector=(-0.638895, -0.126968, -0.758744), 
    cameraTarget=(-1.25769, -3.28195, -0.0203297), viewOffsetX=-0.0836757, 
    viewOffsetY=-0.658126)
session.viewports['Viewport: 1'].view.setValues(nearPlane=100.292, 
    farPlane=166.09, width=48.715, height=20.5849, viewOffsetX=-0.565142, 
    viewOffsetY=-0.0411775)
session.viewports['Viewport: 1'].view.setValues(nearPlane=121.55, 
    farPlane=145.157, width=59.0409, height=24.9482, cameraPosition=(-52.5049, 
    -9.02347, 122.525), cameraUpVector=(-0.738497, 0.110992, -0.665058), 
    cameraTarget=(-1.94516, -4.43755, 1.25452), viewOffsetX=-0.684932, 
    viewOffsetY=-0.0499057)
session.viewports['Viewport: 1'].view.setValues(nearPlane=120.681, 
    farPlane=146.027, width=58.6186, height=24.7698, viewOffsetX=-0.680033, 
    viewOffsetY=-0.0495488)
session.viewports['Viewport: 1'].view.setValues(nearPlane=115.136, 
    farPlane=150.615, width=55.9254, height=23.6317, cameraPosition=(-0.172633, 
    -38.9798, 128.464), cameraUpVector=(-0.936596, 0.208131, -0.281902), 
    cameraTarget=(-1.17074, -4.88705, 1.49708), viewOffsetX=-0.648788, 
    viewOffsetY=-0.0472722)
p = mdb.models['Model-1'].parts['Stempel']
p.ReferencePoint(point=(0.0, 0.0, 0.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=121.386, 
    farPlane=144.588, width=58.9613, height=24.9146, cameraPosition=(-20.2421, 
    0.251863, 131.339), cameraUpVector=(-0.884927, 0.01649, -0.465437), 
    cameraTarget=(-1.45788, -4.44583, 1.30488), viewOffsetX=-0.684008, 
    viewOffsetY=-0.0498384)
session.viewports['Viewport: 1'].view.setValues(nearPlane=121.143, 
    farPlane=144.831, width=58.8431, height=24.8646, cameraPosition=(-20.2215, 
    0.252462, 131.342), cameraUpVector=(-0.883657, 0.042571, -0.466196), 
    cameraTarget=(-1.43728, -4.44523, 1.30783), viewOffsetX=-0.682636, 
    viewOffsetY=-0.0497385)
session.viewports['Viewport: 1'].view.setValues(nearPlane=121.142, 
    farPlane=144.831, width=58.8427, height=24.8645, cameraPosition=(-20.2533, 
    0.251297, 131.337), cameraUpVector=(-0.885318, 0.00228915, -0.464981), 
    cameraTarget=(-1.46908, -4.44639, 1.30328), viewOffsetX=-0.682631, 
    viewOffsetY=-0.0497382)
session.viewports['Viewport: 1'].view.setValues(nearPlane=114.237, 
    farPlane=151.645, width=55.4888, height=23.4473, cameraPosition=(-5.84056, 
    -42.802, 127.326), cameraUpVector=(-0.930485, 0.126336, -0.343855), 
    cameraTarget=(-1.30258, -4.96833, 1.50223), viewOffsetX=-0.643722, 
    viewOffsetY=-0.0469032)
#: 
#: Point 1: 0., 0., 0.  Point 2: 0., -30., 0.
#:    Distance: 30.  Components: 0., -30., 0.
p = mdb.models['Model-1'].parts['Stempel']
p.features['RP'].setValues(yValue=-5.0)
p = mdb.models['Model-1'].parts['Stempel']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=120.864, 
    farPlane=145.087, width=58.7079, height=24.8075, cameraPosition=(-16.7055, 
    -12.2151, 131.731), cameraUpVector=(-0.895016, 0.0948064, -0.435843), 
    cameraTarget=(-1.38578, -4.59859, 1.38204), viewOffsetX=-0.681065, 
    viewOffsetY=-0.0496241)
session.viewports['Viewport: 1'].view.setValues(nearPlane=121.653, 
    farPlane=143.897, width=59.091, height=24.9694, cameraPosition=(4.31033, 
    -8.18838, 132.673), cameraUpVector=(-0.95587, 0.0192974, -0.293155), 
    cameraTarget=(-1.19307, -4.55335, 1.37174), viewOffsetX=-0.685509, 
    viewOffsetY=-0.0499479)
p = mdb.models['Model-1'].parts['Stempel']
p.regenerate()
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)

session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
del mdb.models['Model-1'].boundaryConditions['Auflager']
del mdb.models['Model-1'].boundaryConditions['BlechZ']
del mdb.models['Model-1'].boundaryConditions['Stempel']
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['Stempel-1'].referencePoints
refPoints1=(r1[2], )
r2 = a.instances['Stempel-2'].referencePoints
refPoints2=(r2[2], )
region = regionToolset.Region(referencePoints=(refPoints1, refPoints2, ))
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Initial', 
    region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['Stempel-3'].referencePoints
refPoints1=(r1[2], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].DisplacementBC(name='Stempel', createStepName='Initial', 
    region=region, u1=SET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Verformen')
mdb.models['Model-1'].boundaryConditions['Stempel'].setValuesInStep(
    stepName='Verformen', u2=1.0, amplitude='StempelWeg')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Blech-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#40000 ]', ), )
region = regionToolset.Region(vertices=verts1)
mdb.models['Model-1'].ZsymmBC(name='BlechZ', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.save()
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".


a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Stempel-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#f ]', ), )
a.Surface(side1Faces=side1Faces1, name='Stempel')
#: The surface 'Stempel' has been created (4 faces).
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Blech-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #11ffc0 ]', ), )
a.Surface(side1Faces=side1Faces1, name='BlechOben')
#: The surface 'BlechOben' has been created (12 faces).
mdb.models['Model-1'].ContactStd(name='Test', createStepName='Initial')
mdb.models['Model-1'].interactions['Test'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
r11=mdb.models['Model-1'].rootAssembly.surfaces['Stempel']
r12=mdb.models['Model-1'].rootAssembly.surfaces['BlechOben']
mdb.models['Model-1'].interactions['Test'].excludedPairs.setValuesInStep(
    stepName='Initial', addPairs=((r11, r12), ))
mdb.models['Model-1'].interactions['Test'].contactPropertyAssignments.appendInStep(
    stepName='Initial', assignments=((GLOBAL, SELF, 'Reibung'), ))
#: The interaction "Test" has been created.
del mdb.models['Model-1'].interactions['AuflageA']
del mdb.models['Model-1'].interactions['AuflageB']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=279.878, 
    farPlane=381.937, width=229.588, height=97.0144, cameraPosition=(52.3755, 
    -79.2308, -296.774), cameraUpVector=(0.369119, 0.90354, -0.21764), 
    cameraTarget=(57.361, -4.7697, 20.8046), viewOffsetX=17.5339, 
    viewOffsetY=-3.17878)
session.viewports['Viewport: 1'].view.setValues(nearPlane=278.239, 
    farPlane=383.546, width=228.244, height=96.4463, cameraPosition=(53.6551, 
    -125.162, -281.695), cameraUpVector=(0.416722, 0.84483, -0.335566), 
    cameraTarget=(57.1409, -6.22816, 22.0617), viewOffsetX=17.4312, 
    viewOffsetY=-3.16017)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Stempel-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#f ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Blech-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#71c7000 #4000c ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='Blech_unten')
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='AuflageA', 
    createStepName='Initial', main=region1, secondary=region2, sliding=FINITE, 
    thickness=ON, interactionProperty='Reibung', adjustMethod=NONE, 
    initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#: The interaction "AuflageA" has been created.
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Stempel-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#f ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
region2=a.surfaces['Blech_unten']
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='AuflageB', 
    createStepName='Initial', main=region1, secondary=region2, sliding=FINITE, 
    thickness=ON, interactionProperty='Reibung', adjustMethod=NONE, 
    initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#: The interaction "AuflageB" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=257.558, 
    farPlane=398.048, width=211.279, height=89.2776, cameraPosition=(-38.0318, 
    3.70019, -298.293), cameraUpVector=(0.237487, 0.96973, -0.0567758), 
    cameraTarget=(55.5745, -0.927977, 14.1847), viewOffsetX=16.1355, 
    viewOffsetY=-2.92528)
session.viewports['Viewport: 1'].view.setValues(nearPlane=258.926, 
    farPlane=396.68, width=212.401, height=89.7519, cameraPosition=(-37.9911, 
    5.84127, -298.273), cameraUpVector=(0.141136, 0.989605, -0.0276184), 
    cameraTarget=(55.6152, 1.2131, 14.2042), viewOffsetX=16.2212, 
    viewOffsetY=-2.94082)
session.viewports['Viewport: 1'].view.setValues(nearPlane=278.269, 
    farPlane=382.833, width=228.269, height=96.4569, cameraPosition=(40.1726, 
    1.03339, -306.754), cameraUpVector=(0.0138026, 0.999861, -0.00937048), 
    cameraTarget=(56.5639, 3.86152, 19.051), viewOffsetX=17.433, 
    viewOffsetY=-3.16052)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Blech-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#40000 ]', ), )
region = regionToolset.Region(vertices=verts1)
mdb.models['Model-1'].DisplacementBC(name='BlechX', createStepName='Initial', 
    region=region, u1=SET, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
mdb.models['Model-1'].boundaryConditions['BlechX'].deactivate('Halten')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.save()
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".
# DELETED
mdb.save()
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".
# DELETED
#: The job input file has been written to "Biegen.inp".
mdb.save()
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".
# DELETED
#: The job input file "Biegen.inp" has been submitted for analysis.
#: Job Biegen: Analysis Input File Processor completed successfully.
o3 = session.openOdb(name='C:/temp/Biegen.odb')
#: Model: C:/temp/Biegen.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     7
#: Number of Meshes:             7
#: Number of Element Sets:       3
#: Number of Node Sets:          9
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=301.56, 
    farPlane=394.804, width=215.474, height=91.0504, cameraPosition=(13.7081, 
    20.2597, 372.16), cameraUpVector=(0.0117581, 0.914276, -0.404921), 
    cameraTarget=(29.9225, -6.62005, 24.9366))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/Biegen.odb'])
o3 = session.openOdb(name='C:/temp/Biegen.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Verformen', frame=14)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Verformen', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Ausgansposition', frame=9)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Ausgansposition', frame=17)
#: Job Biegen: Abaqus/Standard completed successfully.
#: Job Biegen completed successfully. 
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Ausgansposition', frame=20)
session.odbs['C:/temp/Biegen.odb'].close()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.save()
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".

job = mdb.Job(
    name='test', 
    model='Model-1', 
    description='', 
    type=ANALYSIS, 
    atTime=None, 
    waitMinutes=0, 
    waitHours=0, 
    queue=None, 
    memory=4000, 
    memoryUnits=MEGA_BYTES, 
    getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, 
    echoPrint=OFF, 
    modelPrint=OFF, 
    contactPrint=OFF, 
    historyPrint=OFF, 
    userSubroutine='', 
    scratch='', 
    resultsFormat=ODB, 
    numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, 
    numCpus=1, 
    numDomains=4, 
    numGPUs=0
)

job.submit(consistencyChecking=OFF)
job.waitForCompletion()
    