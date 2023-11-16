from odbAccess import *
#from abaqusConstants import *
#from symbolicConstants import *
import numpy as np
import json
            
odb = openOdb('data.odb')

def get_frames(odb):
    json.dumps('data.json')
    for step_name in odb.steps.keys():
        frames = odb.steps[step_name].frames

        print('Processing step `{}` ...'.format(step_name))
        frameMap = {}
        for i, frame in enumerate(frames):
            field = {}
            for field_output_key in frame.fieldOutputs.keys():
                print('\tProcessing field output `{}` ...'.format(field_output_key))
                field_output = frame.fieldOutputs[field_output_key]
                values = np.zeros((len(field_output.values), 3))

                for i, val in enumerate(field_output.values):
                    values[i,0] = val.mises
                    values[i,1] = val.inv3
                    values[i,2] = val.press

                field[field_output_key] = values

            frameMap[i] = field

    # TODO(marco): Store data

get_frames(odb)

