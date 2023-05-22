

#Proyecto: Calculadora de I.M.C

import sys 
print('Bienvenido, si deseas saber tu I.M.C, ingresa los siguientes datos')
nombre = input('Nombre(s): ')
if nombre == '':
    print('Es necesario este dato')
while nombre == '':
    nombre = input('Nombre(s): ')
apellido1 = input('Apellido paterno: ')
if apellido1 == '':
    print('Es necesario este dato')
while apellido1 == '':
    apellido1 = input('Apellido paterno: ')
apellido2 = input('Apellido materno: ')
if apellido2 == '':
    print('Es necesario este dato')
    apellido2 = input('Apellido materno: ')
while apellido2 == '':
    if apellido2== '':
        sys.exit(-1)    
edad = int(input('Edad: ' ))   
peso = float(input('Peso (kg): '))   
estatura = float(input('Estatura (m): '))

imc = peso/estatura**2
print(f'{nombre} {apellido1} {apellido2} tiene {edad} años, un peso de {peso:.2f} kg y una estatura de: {estatura:.2f} m\nSu I.M.C. es: ',imc)
if imc < 20:
    print('Tiene un peso bajo')
elif imc >=20 and imc< 25:
        print('Tiene un peso normal')
elif imc >=25 and imc <30:
    print('Tiene Sobrepeso')
elif imc >=30 and imc <40:
    print('Tiene obesidad')
else:
    print('Tiene obesidad morbida')