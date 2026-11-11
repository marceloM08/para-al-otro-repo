from estructuras import enqueue, dequeue, push, pop, insert_end, delete_node, to_list, insert_bst, search_bst
from datos import create_expense

def capture_data(state, amount, description, date, category, moneda):
    # Captura un gasto, lo categoriza inmediatamente e inserta en lista y BST
    expense = create_expense(amount, description, date, category, moneda)
    node = insert_end(state["gastos"], expense)
    push(state["recientes"], node)
    insert_bst(state["bst"], expense)
    return expense

def categorize_next(state, category):
    # Categoriza el siguiente gasto pendiente e inserta en lista y BST
    expense = dequeue(state["pendientes"])
    if expense is None:
        return None
    expense["categoria"] = category
    node = insert_end(state["gastos"], expense)
    push(state["recientes"], node)
    insert_bst(state["bst"], expense)
    return expense

def undo_last(state):
    # Deshace el ultimo gasto categorizado
    node = pop(state["recientes"])
    if node is None:
        return None
    delete_node(state["gastos"], node)
    return node["dato"]

def list_expenses(state):
    # Lista todos los gastos
    return to_list(state["gastos"])

def total_general(state):
    # Calcula el total general en cordobas
    return sum(g["monto_cordobas"] for g in list_expenses(state))

def total_by_category(state):
    # Calcula totales por categoria en cordobas
    totals = {}
    for g in list_expenses(state):
        cat = g["categoria"]
        totals[cat] = totals.get(cat, 0) + g["monto_cordobas"]
    return totals

def search_by_amount(state, amount):
    # Busca gastos por monto usando el BST
    return search_bst(state["bst"], amount)
