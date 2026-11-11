from estructuras import create_queue, create_stack, create_list, create_bst, create_graph

categories = ["Comida", "Transporte", "Servicios", "Ocio", "Salud", "Otros"]

counter = {"id": 0}

TASA_CAMBIO = 36.62 

def create_expense(amount, description, date, category, moneda="C$"):
    # Crea un gasto unico con su respectiva conversion a cordobas
    counter["id"] += 1
    monto_cordobas = amount if moneda == "C$" else amount * TASA_CAMBIO
    return {
        "id": counter["id"],
        "monto": amount,
        "moneda": moneda,
        "monto_cordobas": round(monto_cordobas, 2),
        "descripcion": description,
        "fecha": date,
        "categoria": category,
    }

def create_state():
    # Crea el estado inicial del sistema
    return {
        "pendientes": create_queue(),
        "recientes": create_stack(),
        "gastos": create_list(),
        "bst": create_bst(),
        "grafo": create_graph(),
    }
