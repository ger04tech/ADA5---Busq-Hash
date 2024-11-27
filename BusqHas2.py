# Tamaño de la tabla hash
table_size = 5
hash_table = [[] for _ in range(table_size)]  # Cada posición será una lista enlazada

def hash_function(key):
    return key % table_size

def insert(key):
    index = hash_function(key)
    hash_table[index].append(key)

def search(key):
    index = hash_function(key)
    if key in hash_table[index]:
        return f"El número {key} está en la tabla en el índice {index}."
    return f"El número {key} no está en la tabla."

# Insertar valores
insert(12)
insert(7)
insert(22)
insert(15)
insert(32)

# Buscar valores
print(search(22))  # Debería estar en la tabla
print(search(10))  # No debería estar en la tabla
