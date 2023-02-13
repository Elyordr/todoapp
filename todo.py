from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

todos = {}
id_counter = 0

class TodoResource(Resource):
    def get(self, todo_id):
        if todo_id in todos:
            return {
                "id": todo_id,
                "data": todos[todo_id]['data'],
                "completed": todos[todo_id]['completed'],
                "error": "null"
            }
        else:
            return {"error": "Todo not found"}, 200

    def put(self, todo_id):
            completed = request.form.get('completed', "False")
            if completed not in ["True", "False", "true", "false"]:
                return {"error": "completed field should be either true or false(boolean)"}, 400
            completed = True if completed in ["True", "true"] else False
            global id_counter
            if todo_id == "":
                todo_id = id_counter
                id_counter += 1
            todos[todo_id] = {
                "data": request.form['data'],
                "completed": completed
            }
            return {
                "id": todo_id,
                "data": todos[todo_id]['data'],
                "completed": todos[todo_id]['completed'],
                "status": "Your new ToDo successfully created"
            }

api.add_resource(TodoResource, '/todo/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)