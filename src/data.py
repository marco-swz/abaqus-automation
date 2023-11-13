from abaqus import *
from abaqusConstants import *
import numpy as np
            
odb = session.openOdb(name='test.odb')

def get_frames(odb):
    for step_name in odb.steps.keys():
        frames = odb.steps[step_name].frames

        values = []
        for frame in frames:
            for output in frame.fieldOutputs:
                field = np.zeros((output.dim, output.dim2, 3))
                for val in output.values:
                    field[,,0] = val.mises
                values.append(field)



