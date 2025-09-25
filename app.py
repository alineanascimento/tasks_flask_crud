from tarfile import data_filter
from flask import Flask, jsonify, request
from models.task import Task

app = Flask(__name__)


#CRUD
# Create, Read, Update, Delete = criar, ler, atualizar, deletar

# Tabela : Tarefa, cliente, produto, pedido, funcionário
#lista
tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json() # recuperar o que o cliente enviou
    new_task = Task(id = task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks_list =[task.to_dict() for task in tasks]
    
    output = {
                "tasks": tasks_list,
                "total_tasks": len(tasks_list)
             }
    return jsonify(output)


#recuperar um item específico
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"message": "Não foi possível encontrar a tarefa."}), 404


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):

    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)

    if task is None:
        return jsonify({"message": "Não foi possível encontrar a tarefa."}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso!"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        print(t.to_dict())
        if t.id == id:
            task = t
            break
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso!"})


    if task is None:
        return jsonify({"message": "Não foi possível encontrar a tarefa."}), 404






"""@app.route('/user/<username>')
def show_user(username):
    print(username)
    print(type(username))
    return username
"""

#estudar documentação do flask
#https://flask.palletsprojects.com/en/2.3.x/quickstart
if __name__ == '__main__':
    app.run(debug=True)