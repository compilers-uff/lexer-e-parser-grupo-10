# Expressões aritméticas válidas
1 + 2 + 3
4 * 5 - 6
7 // 2
-10

# Atribuições válidas
x = 10
y = x + 5
z = x * y

# Atribuições múltiplas e encadeadas
a = b = c = 0
x = y = z = a + b
i = j = k = 1 + 2 * 3

# Atribuições com indexação e atributos
lista = [1, 2, 3]
lista[0] = lista[1] = 5
objeto = None
x = y = z = 42
x = y = objeto.atributo = 100
lista[0] = y = objeto.metodo = 200

# Estruturas de controle
if x > 0:
    print(x)

while i < 10:
    i = i + 1

for i in [1, 2, 3]:
    print(i)

# Chamadas de função
print("Hello")
soma(1, 2)

# Listas e indexação
lista = [1, 2, 3]
elemento = lista[0]