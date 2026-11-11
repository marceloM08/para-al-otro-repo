from flask import Flask, render_template, request, redirect, url_for, flash
from datos import create_state, categories
from estructuras import get_neighbors, add_vertex, add_edge
from gastos import capture_data, undo_last, list_expenses, total_general, total_by_category, search_by_amount

app = Flask(__name__)
app.secret_key = "gastos_secret_key"

state = create_state()
last_search = []


def init_category_graph():
    # Inicializa el grafo de categorias con algunas relaciones
    for cat in categories:
        add_vertex(state["grafo"], cat)
    add_edge(state["grafo"], "Comida", "Ocio")
    add_edge(state["grafo"], "Transporte", "Servicios")
    add_edge(state["grafo"], "Salud", "Otros")
    add_edge(state["grafo"], "Comida", "Salud")


init_category_graph()


@app.route('/')
def index():
    expenses = list_expenses(state)
    total = total_general(state)
    totals_cat = total_by_category(state)
    graph_info = {cat: get_neighbors(state["grafo"], cat) for cat in categories}
    return render_template('index.html',
                           categories=categories,
                           expenses=expenses,
                           total=total,
                           totals_cat=totals_cat,
                           graph_info=graph_info,
                           search_results=last_search)


@app.route("/add", methods=["POST"])
def add_expense():
    try:
        amount = float(request.form["monto"])
        if amount <= 0:
            flash("El monto debe ser mayor que 0.")
            return redirect(url_for("index"))
        description = request.form["descripcion"]
        date = request.form["fecha"]
        category = request.form.get("categoria")
        moneda = request.form.get("moneda", "C$")
        capture_data(state, amount, description, date, category, moneda)
        flash(f'Gasto "{description}" ingresado y categorizado exitosamente.')
    except ValueError:
        flash("Error: Ingrese un numero valido porfavor.")
    return redirect(url_for("index"))


@app.route("/undo", methods=["POST"])
def undo():
    expense = undo_last(state)
    if expense:
        flash(f'Deshecho el gasto: {expense["descripcion"]}')
    else:
        flash("No hay nada que deshacer.")
    return redirect(url_for("index"))


@app.route("/search", methods=["POST"])
def search():
    global last_search
    try:
        amount = float(request.form["monto_busqueda"])
        last_search = search_by_amount(state, amount)
        flash(f"Busqueda completada. Encontrados {len(last_search)} resultados.")
    except ValueError:
        flash("Error: Ingrese un monto valido para buscar.")
        last_search = []
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
