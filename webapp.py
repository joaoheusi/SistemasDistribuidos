from flask import Flask
from flask import request
import services.readWorkoutsService
import services.createWorkoutService
app = Flask(__name__)




@app.route("/workouts", methods=['GET'])
def workouts():
  if request.method == 'GET':
    return services.readWorkoutsService.find_all()
  else:
    return {"Error":"InvalidMethod", "Description": "The method used is invalid doesnt exist."}

@app.route("/workout/<id>", methods=['GET'])
def workout(id= None):
  return services.readWorkoutsService.find_one(id)

@app.route("/createWorkout", methods=['POST'])
def createWorkout():
  created_index = services.createWorkoutService.post(request.json)
  if created_index:
    return services.readWorkoutsService.find_one(created_index)
  return {"Error":"Not Created", "Description": "The workout was not created"}