from __future__ import print_function
from odbAccess import *
import numpy as np
import json
            
odb = openOdb('data.odb')

def store_as_json(odb):
    stepMap = {}
    for step_name in odb.steps.keys():
        frames = odb.steps[step_name].frames

        frame_map = {}
        for i, frame in enumerate(frames):
            print(' '*100, end='\r')
            print('Processing step `{}` {}/{} ... '.format(step_name, i+1, len(frames)), end='\r')

            field = {}
            for field_output_key in frame.fieldOutputs.keys():
                field_output = frame.fieldOutputs[field_output_key]

                values = []
                for i, val in enumerate(field_output.values):
                    if val.precision == SINGLE_PRECISION:
                        data = val.data
                    else:
                        data = val.dataDouble

                    if (isinstance(data, np.ndarray)):
                        data = data.tolist()

                    values.append(data)

                field[field_output_key] = values
            frame_map[i] = field
        step_map[step_name] = frame_map

        print('Processing step `{}` {}/{} ... done'.format(step_name, len(frames), len(frames)), end='\r')
        print('')

    print('Storing data ... ', end='')

    with open('data.json', 'w') as fp:
        json.dump(stepMap, fp)
            
    print('done')

store_as_json(odb)

