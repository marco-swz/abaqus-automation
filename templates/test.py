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
# DELETED
# DELETED
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
# DELETED
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
#Blechgroesse
#breite = 15.0
#hoehe = 2.
#laenge = 150
#Vernetzung
#dickenelement = hoehe/2
#biegeelement = 2
#globalelement = 10
#Material
#material_Name = 'Stahl'
#Dichte = 0.00000000785 #kg/mm^3
#E_Modul = 210000 #MPa
#Poisson = 0.3 
#maxWeg = -20.0
Plastic = []
with open (material_path) as f: 
    reader = csv.reader(f, delimiter=',',quotechar='|')
    is_header = True
    for row in reader:
        if is_header:
            is_header = False
            continue
        Plastic.append([float(r) for r in row])


        
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
# DELETED
del mdb.models['Model-1'].sketches['__profile__']
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(-50.0, 1.25), point2=(55.0, -1.25))
s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-54.2282485961914, 
    0.0512466430664062), value=hoehe)
s.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(-43.1570777893066, 
    -3.84333610534668), value=laenge)
p = mdb.models['Model-1'].Part(name='Blech', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Blech']
p.BaseSolidExtrude(sketch=s, depth=breite)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Blech']
# DELETED
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Blech']
f1, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[3], sketchUpEdge=e[8], 
    sketchPlaneSide=SIDE1, origin=(25.0, 1.25, breite/2))
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
# DELETED
# DELETED
#Material festlegen
mdb.models['Model-1'].Material(name=material_Name)
mdb.models['Model-1'].materials[material_Name].Density(table=((Dichte, ), ))
mdb.models['Model-1'].materials[material_Name].Elastic(table=((E_Modul, Poisson), ))
mdb.models['Model-1'].materials[material_Name].Plastic(scaleStress=None, table=( Plastic))
mdb.models['Model-1'].HomogeneousSolidSection(name='Material', 
    material=material_Name, thickness=None)
p = mdb.models['Model-1'].parts['Blech']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#fff ]', ), )
region = p.Set(cells=cells, name='Blech')
p = mdb.models['Model-1'].parts['Blech']
p.SectionAssignment(region=region, sectionName='Material', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
# DELETED
# DELETED
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
# DELETED
# DELETED
# DELETED
# DELETED
a = mdb.models['Model-1'].rootAssembly
a.rotate(instanceList=('Stempel-1', 'Stempel-2', 'Stempel-3'), axisPoint=(0.0, 
    0.0, 100.0), axisDirection=(0.0, 0.0, -10.0), angle=90.0)
#: The instances were rotated by 90. degrees about the axis defined by the point 0., 0., 100. and the vector 0., 0., -10.
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('Stempel-3', ), vector=(25.0, 6.75, 30.0))
#: The instance Stempel-3 was translated by 25., 6.25, 30. with respect to the assembly coordinate system
a.translate(instanceList=('Stempel-3', ), vector=(0.0, -1, -(50-breite)/2))
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('Stempel-2', ), vector=(-35.0, -6.25, 30.0))
#: The instance Stempel-2 was translated by -35., -6.25, 30. with respect to the assembly coordinate system
a.translate(instanceList=('Stempel-2', ), vector=(0.0, 0.0, -(50-breite)/2))
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('Stempel-1', ), vector=(85.0, -6.25, 30.0))
#: The instance Stempel-1 was translated by 85., -6.25, 30. with respect to the assembly coordinate system
a.translate(instanceList=('Stempel-1', ), vector=(0.0, 0.0, -(50-breite)/2))
# DELETED
# DELETED
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Blech-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#56 ]', ), )
a.Set(cells=cells1, name='Auswertung')
#: The set 'Auswertung' has been created (4 cells).
# DELETED
# DELETED
# DELETED
# DELETED
mdb.models['Model-1'].StaticStep(name='Verformen', previous='Initial', 
    maxNumInc=1000000, initialInc=0.005, minInc=1e-15, nlgeom=ON)
# DELETED
mdb.models['Model-1'].StaticStep(name='Halten', previous='Verformen', 
    maxNumInc=100000, initialInc=0.05, minInc=1e-15)
# DELETED
mdb.models['Model-1'].StaticStep(name='Ausgansposition', previous='Halten', 
    maxNumInc=100000, initialInc=0.05, minInc=1e-15)
# DELETED
regionDef=mdb.models['Model-1'].rootAssembly.sets['Auswertung']
#mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(variables=(
#    'COOR1', 'COOR2', 'COOR3'), region=regionDef, sectionPoints=DEFAULT, 
#    rebar=EXCLUDE)
mdb.models['Model-1'].FieldOutputRequest(name='Auswerte_Variable', 
        createStepName='Verformen', variables=('S', 'RF', 'COORD'))
# DELETED
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
# DELETED
# DELETED
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
# DELETED
# DELETED
# DELETED
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
    thickness=ON, interactionProperty='Reibung', adjustMethod=OVERCLOSED, 
    initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#: The interaction "Stempel" has been created.
# DELETED
mdb.models['Model-1'].TabularAmplitude(name='StempelWeg', timeSpan=TOTAL, 
    smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 20.0), (2.0, 20.0), (3.0, 
    0.0)))
# DELETED
# DELETED
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
# DELETED
# DELETED
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
# DELETED
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
# DELETED
#Verfahren Stempel
mdb.models['Model-1'].boundaryConditions['Stempel'].setValuesInStep(
    stepName='Verformen', u2=1.0, amplitude='StempelWeg')
mdb.models['Model-1'].amplitudes['StempelWeg'].setValues(timeSpan=TOTAL, 
    smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, maxWeg), (2.0, maxWeg), (3.0, 
    0.0)))
#Eigengewicht
#mdb.models['Model-1'].Gravity(comp2=-9810.0, createStepName='Verformen', 
#   distributionType=UNIFORM, field='', name='Eigengewicht')
# DELETED
# DELETED
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Blech-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#40000 ]', ), )
region = regionToolset.Region(vertices=verts1)
mdb.models['Model-1'].ZsymmBC(name='BlechZ', createStepName='Initial', 
    region=region, localCsys=None)
# DELETED
# DELETED
p = mdb.models['Model-1'].parts['Blech']
# DELETED
# DELETED
# DELETED
p = mdb.models['Model-1'].parts['Blech']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
# DELETED
# DELETED
# DELETED
# DELETED
p = mdb.models['Model-1'].parts['Blech']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#90441104 #81021010 #28 ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=dickenelement, deviationFactor=0.1, 
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
#p.generateMesh()
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
# DELETED
# DELETED
# DELETED
#pathFile = getcwd
#fullpathFile = pathFile+'/3Punkt_Biegen'
mdb.saveAs('3Punkt_Biegen')
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".
# DELETED
mdb.save()
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".
# DELETED
# DELETED
# DELETED
p = mdb.models['Model-1'].parts['Blech']
# DELETED
p = mdb.models['Model-1'].parts['Stempel']
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
p = mdb.models['Model-1'].parts['Stempel']
p.ReferencePoint(point=(0.0, 0.0, 0.0))
# DELETED
# DELETED
# DELETED
# DELETED
#: 
#: Point 1: 0., 0., 0.  Point 2: 0., -30., 0.
#:    Distance: 30.  Components: 0., -30., 0.
p = mdb.models['Model-1'].parts['Stempel']
p.features['RP'].setValues(yValue=-5.0)
p = mdb.models['Model-1'].parts['Stempel']
p.regenerate()
# DELETED
# DELETED
p = mdb.models['Model-1'].parts['Stempel']
p.regenerate()
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
# DELETED
# DELETED
# DELETED
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
# DELETED
mdb.models['Model-1'].boundaryConditions['Stempel'].setValuesInStep(
    stepName='Verformen', u2=1.0, amplitude='StempelWeg')
# DELETED
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Blech-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#40000 ]', ), )
region = regionToolset.Region(vertices=verts1)
mdb.models['Model-1'].ZsymmBC(name='BlechZ', createStepName='Initial', 
    region=region, localCsys=None)
# DELETED
mdb.save()
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".


a = mdb.models['Model-1'].rootAssembly
# DELETED
# DELETED
# DELETED
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
# DELETED
# DELETED
# DELETED
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
    thickness=ON, interactionProperty='Reibung', adjustMethod=OVERCLOSED, 
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
    thickness=ON, interactionProperty='Reibung', adjustMethod=OVERCLOSED, 
    initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#: The interaction "AuflageB" has been created.
# DELETED
# DELETED
# DELETED
# DELETED
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Blech-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#40000 ]', ), )
region = regionToolset.Region(vertices=verts1)
mdb.models['Model-1'].DisplacementBC(name='BlechX', createStepName='Initial', 
    region=region, u1=SET, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
mdb.models['Model-1'].boundaryConditions['BlechX'].deactivate('Halten')
mdb.models['Model-1'].boundaryConditions['BlechZ'].deactivate('Halten')
# DELETED
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
# DELETED
#: Model: C:/temp/Biegen.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     7
#: Number of Meshes:             7
#: Number of Element Sets:       3
#: Number of Node Sets:          9
#: Number of Steps:              3
# DELETED
# DELETED
# DELETED
# DELETED
a = mdb.models['Model-1'].rootAssembly
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
# DELETED
#: Job Biegen: Abaqus/Standard completed successfully.
#: Job Biegen completed successfully. 
# DELETED
# DELETED
#Entfernen der Partitionen
del mdb.models['Model-1'].parts['Blech'].features['Partition cell-1']
del mdb.models['Model-1'].parts['Blech'].features['Partition cell-2']
a = mdb.models['Model-1'].rootAssembly
# DELETED
#Hinzufügen neue Partition
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Blech'].features['Partition face-1'].sketch)
mdb.models['Model-1'].parts['Blech'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Blech'].features['Partition face-1'])
mdb.models['Model-1'].sketches['__edit__'].Line(point1=(-5.925, 7.5), point2=(
    -5.925, -7.5))
mdb.models['Model-1'].sketches['__edit__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__edit__'].geometry[12])
mdb.models['Model-1'].sketches['__edit__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__edit__'].geometry[3], entity2=
    mdb.models['Model-1'].sketches['__edit__'].geometry[12])
mdb.models['Model-1'].sketches['__edit__'].CoincidentConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__edit__'].vertices[14], 
    entity2=mdb.models['Model-1'].sketches['__edit__'].geometry[3])
mdb.models['Model-1'].sketches['__edit__'].CoincidentConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__edit__'].vertices[15], 
    entity2=mdb.models['Model-1'].sketches['__edit__'].geometry[4])
mdb.models['Model-1'].sketches['__edit__'].Line(point1=(5.925, 7.5), point2=(
    5.925, -7.5))
mdb.models['Model-1'].sketches['__edit__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__edit__'].geometry[13])
mdb.models['Model-1'].sketches['__edit__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__edit__'].geometry[3], entity2=
    mdb.models['Model-1'].sketches['__edit__'].geometry[13])
mdb.models['Model-1'].sketches['__edit__'].CoincidentConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__edit__'].vertices[16], 
    entity2=mdb.models['Model-1'].sketches['__edit__'].geometry[3])
mdb.models['Model-1'].sketches['__edit__'].CoincidentConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__edit__'].vertices[17], 
    entity2=mdb.models['Model-1'].sketches['__edit__'].geometry[4])
mdb.models['Model-1'].sketches['__edit__'].SymmetryConstraint(entity1=
    mdb.models['Model-1'].sketches['__edit__'].geometry[12], entity2=
    mdb.models['Model-1'].sketches['__edit__'].geometry[13], symmetryAxis=
    mdb.models['Model-1'].sketches['__edit__'].geometry[10])
mdb.models['Model-1'].sketches['__edit__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__edit__'].geometry[12], entity2=
    mdb.models['Model-1'].sketches['__edit__'].geometry[13], textPoint=(
    6.53984069824219, 13.1113624572754), value=12.0)
mdb.models['Model-1'].parts['Blech'].features['Partition face-1'].setValues(
    sketch=mdb.models['Model-1'].sketches['__edit__'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].parts['Blech'].checkGeometry()
mdb.models['Model-1'].parts['Blech'].backup()
mdb.models['Model-1'].parts['Blech'].regenerate()
mdb.models['Model-1'].parts['Blech'].PartitionCellBySweepEdge(cells=
    mdb.models['Model-1'].parts['Blech'].cells.getSequenceFromMask(('[#1 ]', ), 
    ), edges=(mdb.models['Model-1'].parts['Blech'].edges[4], 
    mdb.models['Model-1'].parts['Blech'].edges[13], 
    mdb.models['Model-1'].parts['Blech'].edges[20], 
    mdb.models['Model-1'].parts['Blech'].edges[31], 
    mdb.models['Model-1'].parts['Blech'].edges[35], 
    mdb.models['Model-1'].parts['Blech'].edges[43]), sweepPath=
    mdb.models['Model-1'].parts['Blech'].edges[45])
mdb.models['Model-1'].parts['Blech'].PartitionCellBySweepEdge(cells=
    mdb.models['Model-1'].parts['Blech'].cells.getSequenceFromMask(('[#2 ]', ), 
    ), edges=(mdb.models['Model-1'].parts['Blech'].edges[18], 
    mdb.models['Model-1'].parts['Blech'].edges[26], 
    mdb.models['Model-1'].parts['Blech'].edges[32], 
    mdb.models['Model-1'].parts['Blech'].edges[38], 
    mdb.models['Model-1'].parts['Blech'].edges[41], 
    mdb.models['Model-1'].parts['Blech'].edges[50]), sweepPath=
    mdb.models['Model-1'].parts['Blech'].edges[53])
mdb.models['Model-1'].parts['Blech'].PartitionCellBySweepEdge(cells=
    mdb.models['Model-1'].parts['Blech'].cells.getSequenceFromMask(('[#7 ]', ), 
    ), edges=(mdb.models['Model-1'].parts['Blech'].edges[44], 
    mdb.models['Model-1'].parts['Blech'].edges[51], 
    mdb.models['Model-1'].parts['Blech'].edges[54]), sweepPath=
    mdb.models['Model-1'].parts['Blech'].edges[62])
mdb.models['Model-1'].parts['Blech'].PartitionCellBySweepEdge(cells=
    mdb.models['Model-1'].parts['Blech'].cells.getSequenceFromMask(('[#1c ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Blech'].edges[65], 
    mdb.models['Model-1'].parts['Blech'].edges[69], 
    mdb.models['Model-1'].parts['Blech'].edges[70]), sweepPath=
    mdb.models['Model-1'].parts['Blech'].edges[11])
mdb.models['Model-1'].parts['Blech'].PartitionCellBySweepEdge(cells=
    mdb.models['Model-1'].parts['Blech'].cells.getSequenceFromMask(('[#8c ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Blech'].edges[75], 
    mdb.models['Model-1'].parts['Blech'].edges[77], 
    mdb.models['Model-1'].parts['Blech'].edges[79]), sweepPath=
    mdb.models['Model-1'].parts['Blech'].edges[11])
mdb.models['Model-1'].parts['Blech'].PartitionCellBySweepEdge(cells=
    mdb.models['Model-1'].parts['Blech'].cells.getSequenceFromMask(('[#8c ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Blech'].edges[86], 
    mdb.models['Model-1'].parts['Blech'].edges[88], 
    mdb.models['Model-1'].parts['Blech'].edges[89]), sweepPath=
    mdb.models['Model-1'].parts['Blech'].edges[11])
mdb.models['Model-1'].parts['Blech'].PartitionCellBySweepEdge(cells=
    mdb.models['Model-1'].parts['Blech'].cells.getSequenceFromMask(('[#1c ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Blech'].edges[97], 
    mdb.models['Model-1'].parts['Blech'].edges[98], 
    mdb.models['Model-1'].parts['Blech'].edges[100]), sweepPath=
    mdb.models['Model-1'].parts['Blech'].edges[11])
#Mesh
mdb.models['Model-1'].parts['Blech'].seedEdgeBySize(constraint=FINER, 
    deviationFactor=0.1, edges=
    mdb.models['Model-1'].parts['Blech'].edges.getSequenceFromMask((
    '[#0 #ebc01400 #40003e00 ]', ), ), minSizeFactor=0.1, size=biegeelement)
mdb.models['Model-1'].parts['Blech'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=globalelement)
mdb.models['Model-1'].parts['Blech'].generateMesh()
#Reselect Surface
mdb.models['Model-1'].rootAssembly.Surface(name='Blech_unten', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Blech-1'].faces.getSequenceFromMask(
    ('[#19054130 #1119054 #1000 ]', ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='BlechOben', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Blech-1'].faces.getSequenceFromMask(
    ('[#0 #fc000000 #47ff ]', ), ))
#Reattach BounderyCondition
mdb.models['Model-1'].rootAssembly.Set(name='Mittelpunkt_Unten', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Blech-1'].vertices.getSequenceFromMask(
    ('[#20000000 ]', ), ))
mdb.models['Model-1'].boundaryConditions['BlechX'].setValues(region=
    mdb.models['Model-1'].rootAssembly.sets['Mittelpunkt_Unten'])
mdb.models['Model-1'].boundaryConditions['BlechZ'].setValues(region=
    mdb.models['Model-1'].rootAssembly.sets['Mittelpunkt_Unten'])
#Reselect Part for Material
mdb.models['Model-1'].parts['Blech'].Set(cells=
    mdb.models['Model-1'].parts['Blech'].cells.getSequenceFromMask((
    '[#3ffff ]', ), ), name='Blech')
#Reselect Auswertebereich
mdb.models['Model-1'].rootAssembly.Set(cells=
    mdb.models['Model-1'].rootAssembly.instances['Blech-1'].cells.getSequenceFromMask(
    ('[#c24a ]', ), ), name='Auswertung')
mdb.save()
#: The model database has been saved to "C:\temp\3Punkt_Biegen.cae".
print('Starting simulation')

    