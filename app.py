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




if __name__ == '__main__':
    app.run(debug=True)