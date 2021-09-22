# En este script hacemos operaciones basicas
# Autor: Ivan Marin
# 15 de sept 2021
# repaso del 22 de septiembre

# Variable: un nombre que contiene un valor. Podemos hacer operaciones con ese nombre
suma = 5 + 2
resta = suma - 8.5
m1 = 32.5
m2 = 64
multiplicacion = m1 * m2
print("Este programa acaba de hacer algunas operaciones")
print('la suma dio como resultado: ')
print(suma)
print('la resta dio como resultado: ', resta) # la resta dio como resultado: -1.5
print('la multiplicacion dio como resultado: ', multiplicacion)
print(m2, "/", m1, " = ", m2/m1)

# operadores adicionales
# potencia
potencia = 12 ** 5 # doce a la potencia cinco
print(potencia)

# Modulo: es el residuo de una division de numeros enteros
mod1 = 12 % 3 # doce modulo 3, mod1 = 0
es_par = 3 % 2 # comprobar que 3 es par o no
print("Si 3 % 2 = 0 significa que 3 es par: ", es_par)

# division que solo devuelve el valor entero
print("Division entera ", m2 // m1) # da 1
print("Divsion normal", m2 / m1) # da 1.9692307692307693
