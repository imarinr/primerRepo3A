# Este programa calcula el año de retiro laboral
# Tambien calcula cuantos años quedan para retirarse
# 14 de octubre de 2021
# Autor: Ivan Marin Roldan

anio_actual = 2021
print("Cual es tu edad?")
edad_actual = int(input())
print("A que edad deseas retirarte?")
edad_de_retiro = int(input())
anios_para_retiro = edad_de_retiro - edad_actual
anio_de_retiro = anio_actual + anios_para_retiro
print("Tienes ", anios_para_retiro, " años antes de que te puedas retirar")
print("Lo podras hacer en el año ", anio_de_retiro)