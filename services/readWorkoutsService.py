import json
from pathlib import Path
from datetime import datetime
import os

file_path = os.path.dirname(os.path.realpath(__file__))
workouts_path = Path(file_path).parent.joinpath("documents").joinpath("workouts.json")

def find_all():
  with open(workouts_path, 'r') as f:
    workouts = json.load(f)
  
  print(workouts)
  return workouts

def find_one(id = None):
  with open(workouts_path, 'r') as f:
    workouts = json.load(f)
    try:
      return workouts[id]
    except KeyError:
      return {"Error":"KeyError", "Description": "The id informed doesnt exist."}
