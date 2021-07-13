import jsonschema
import json
from jsonschema import validate
from pathlib import Path
from datetime import datetime
import os


file_path = os.path.dirname(os.path.realpath(__file__))
workouts_path = Path(file_path).parent.joinpath("documents").joinpath("workouts.json")


""" workoutSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "datetime": {"type": "string"},
        "exercises": {"type": "list",
                      "items": [
                          {"type": "object",
                           "properties": {
                           "name": {"type": "string"},
                           "sets": {"type": "list",
                           "items": [
                             {"type": "object",
                              "properties": {
                              "reps": {"type": "number"},
                              "weight": {"type": "number"}
                           }}
                           ]}
                          }},
                      ]
                      }
    }
} """

""" def validate_json(jsonData):
  try:
    validate(instance=jsonData, schema=workoutSchema)
  except jsonschema.exceptions.ValidationError as err:
    return False
  return True """

""" def validate_schema(jsonData):
  try:
    validate(instance=jsonData, schema= workoutSchema)
  except jsonschema.exceptions.SchemaError as err:
    return False
  return True """



def post(jsonData):
  """   valid_json = validate_json(jsonData)
    print(valid_json)
    valid_schema = validate_schema(jsonData)
    print(valid_schema)
    if valid_schema and valid_json: """
    

  with open(workouts_path, "r") as f:
    workouts = json.load(f)
    print(workouts)
    new_index = str(int(max(workouts)) + 1)
    print(new_index)
    with open(workouts_path,mode='w') as w:
      workouts.update({new_index: jsonData})
      print(workouts)
      json.dump(workouts,w,indent=4)
    return new_index
  """ except: """
  """ return False """
      