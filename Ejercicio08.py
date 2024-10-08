#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n = input('Inserte primer número')
m = input('Inserte segundo número')
x = int(n)
y = int(m)
Cociente = ((x // y))
Resto = ((x % y)) 
c = Cociente
r = Resto
print('El Cociente es igual a',(c))
print('El Resto es igual a',(r))