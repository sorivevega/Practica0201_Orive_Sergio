#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
Peso = input('¿Cuanto pesas?')
Estatura = input('¿Cuanto mides?')
x = float(Peso)
y = float(Estatura)
z = ((x)/(y ** 2))
imc = round(z, 2)
print('Tu índice de masa corporal es',(imc))