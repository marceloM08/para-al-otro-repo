def create_queue():
    # Crea una cola vacia
    return []

def enqueue(queue, item):
    # Encola un elemento al final
    queue.append(item)

def dequeue(queue):
    # Desencola el primer elemento
    return queue.pop(0) if queue else None

def is_empty(queue):
    # Verifica si la cola esta vacia
    return len(queue) == 0

def peek_front(queue):
    # Ve el frente de la cola sin eliminarlo
    return queue[0] if queue else None

def create_stack():
    # Crea una pila vacia
    return []

def push(stack, item):
    # Apila un elemento
    stack.append(item)

def pop(stack):
    # Desapila el tope
    return stack.pop() if stack else None

def peek_top(stack):
    # Ve el tope de la pila
    return stack[-1] if stack else None

def is_empty_stack(stack):
    # Verifica si la pila esta vacia
    return len(stack) == 0

def create_list():
    # Crea una lista doble enlazada vacia
    return {"cabeza": None, "cola": None, "actual": None, "tamaño": 0}

def insert_end(lista, dato):
    # Inserta un nodo al final
    nodo = {"dato": dato, "ant": lista["cola"], "sig": None}
    if lista["cola"] is None:
        lista["cabeza"] = nodo
        lista["actual"] = nodo
    else:
        lista["cola"]["sig"] = nodo
    lista["cola"] = nodo
    lista["tamaño"] += 1
    return nodo

def delete_node(lista, nodo):
    # Elimina un nodo de la lista
    if nodo["ant"]:
        nodo["ant"]["sig"] = nodo["sig"]
    else:
        lista["cabeza"] = nodo["sig"]
    if nodo["sig"]:
        nodo["sig"]["ant"] = nodo["ant"]
    else:
        lista["cola"] = nodo["ant"]
    if lista["actual"] is nodo:
        lista["actual"] = nodo["sig"] or nodo["ant"]
    lista["tamaño"] -= 1

def advance(lista):
    # Avanza el puntero actual
    if lista["actual"] and lista["actual"]["sig"]:
        lista["actual"] = lista["actual"]["sig"]
    return lista["actual"]

def to_list(lista):
    # Convierte la lista a lista normal
    datos, nodo = [], lista["cabeza"]
    while nodo:
        datos.append(nodo["dato"])
        nodo = nodo["sig"]
    return datos

def create_bst():
    # Crea un arbol binario de busqueda
    return {"root": None}

def _create_node(data):
    return {"data": data, "left": None, "right": None}

def insert_bst(tree, expense):
    # Inserta un gasto en el BST ordenado por monto
    def insert(node, expense):
        if node is None:
            return _create_node(expense)
        if expense["monto"] < node["data"]["monto"]:
            node["left"] = insert(node["left"], expense)
        else:
            node["right"] = insert(node["right"], expense)
        return node
    tree["root"] = insert(tree["root"], expense)

def search_bst(tree, monto):
    # Busca gastos por monto en el BST
    results = []
    def search(node, monto):
        if node is None:
            return
        if abs(node["data"]["monto"] - monto) < 0.01:
            results.append(node["data"])
        if monto <= node["data"]["monto"]:
            search(node["left"], monto)
        if monto >= node["data"]["monto"]:
            search(node["right"], monto)
    search(tree["root"], monto)
    return results

def inorder_bst(tree):
    # Recorrido inorden del BST
    result = []
    def inorder(node):
        if node:
            inorder(node["left"])
            result.append(node["data"])
            inorder(node["right"])
    inorder(tree["root"])
    return result

def create_graph():
    # Crea un grafo vacio
    return {}

def add_vertex(graph, vertex):
    # Agrega un vertice al grafo
    if vertex not in graph:
        graph[vertex] = []

def add_edge(graph, v1, v2):
    # Agrega una arista no dirigida
    add_vertex(graph, v1)
    add_vertex(graph, v2)
    if v2 not in graph[v1]:
        graph[v1].append(v2)
    if v1 not in graph[v2]:
        graph[v2].append(v1)

def get_neighbors(graph, vertex):
    # Obtiene los vecinos de un vertice
    return graph.get(vertex, [])

def bfs(graph, start):
    # Recorrido en anchura del grafo
    from collections import deque
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result
