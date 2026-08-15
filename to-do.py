from flask import Flask, render_template, request, redirect, url_for

from model import TodoModel
from controller import TodoController


# ==========================================
# CONFIGURACIÓN DE FLASK
# ==========================================

app = Flask(__name__)


# ==========================================
# CREACIÓN DEL MODELO Y CONTROLADOR
# ==========================================

todo_model = TodoModel()

todo_controller = TodoController(todo_model)


# ==========================================
# RUTA PRINCIPAL
# ==========================================

@app.route("/")
def index():

    tasks = todo_controller.get_tasks()

    return render_template(
        "index.html",
        tasks=tasks
    )


# ==========================================
# AGREGAR TAREA
# ==========================================

@app.route("/add", methods=["POST"])
def add_task():

    task_name = request.form.get("task")

    todo_controller.add_task(task_name)

    return redirect(url_for("index"))


# ==========================================
# ELIMINAR TAREA
# ==========================================

@app.route("/delete/<int:index>", methods=["POST"])
def delete_task(index):

    todo_controller.delete_task(index)

    return redirect(url_for("index"))


# ==========================================
# EJECUTAR APLICACIÓN
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)