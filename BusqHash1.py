# Tamaño de la tabla hash
table_size = 10
hash_table = [None] * table_size

def hash_function(key):
    return key % table_size

def insert(key):
    index = hash_function(key)
    # Resolución lineal en caso de colisión
    while hash_table[index] is not None:
        index = (index + 1) % table_size
    hash_table[index] = key

def search(key):
    index = hash_function(key)
    start_index = index  # Para evitar bucles infinitos
    while hash_table[index] is not None:
        if hash_table[index] == key:
            return f"El número {key} está en la tabla en el índice {index}."
        index = (index + 1) % table_size
        if index == start_index:  # Si vuelve al inicio, el número no está
            break
    return f"El número {key} no está en la tabla."

# Insertar valores
insert(34)
insert(25)
insert(89)
insert(56)
insert(17)

# Buscar valores
print(search(56))  # Debería estar en la tabla
print(search(100))  # No debería estar en la tabla
