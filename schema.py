__author__ = 'albmin'

import json
import os

"""
Initializer that will return a json schema object
"""
#TODO add add functionality separately (from a shell or program) with a persist option in the fn call
class Schema():


    """
    Constructor takes in an input json file and schema map (also JSON)
    """
    #TODO add error checking if not JSON, (i guess kinda already done)
    def __init__(self, input, schema_map):
        inp = self.read_json(input)
        dmap = self.read_json(schema_map)
        return self.json_map(inp, dmap)


    """
    Reads in the json file and returns the dict
    """
    def read_json(self, file):
        if not os.path.isfile(file):
            print 'File does not exist in this context, aborting'
            exit()
        try:
            with open(file) as f:
                return json.loads(f)
        except ValueError:
            print 'Error processing file, aborting'
            exit()


    """
    This is where the cool code lives, basically a json structure is created
    based on the input file and it's values, but the variables are assigned to
    the ones specified in the schema, if they don't exist in the schema, then the
    input variables are used
    """
    def json_map(self, inp, dmap):
        #construct the file via an iteration of the input
        output = {}
        for key in inp:
            if key in dmap:
                output[dmap[key]] = inp[key]
            else:
                output[key] = inp[key]

        return output
