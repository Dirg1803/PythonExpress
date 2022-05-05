mascota = 'conejo'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('tienes un perro')
elif mascota == 'pez':
    print('tienes un pez')
else:
    print('No sé que animal tienes')


edad=16
calificacion=9

if edad < 18:
    print('Eres menor de edad')
    if calificacion > 7:
        print('Has aprobado')
    else:
        print('reprobaste')
else:
    print('eres adulto')