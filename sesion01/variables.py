edades = [10,20,3,12,"edad", 14.5, False, [1,2]]
print(edades[-1])

curso = {
    'nombre': 'backend',
    'dificultad': 'dificil',
    'skills': [
        {
            'nombre': 'base de datos',
            'nivel': 'intermedio'
        },
        {
            'nombre': 'q4m',
            'nivel': 'avanzado'

        }
    ]

}

print(curso['skills'][0]['nivel'])