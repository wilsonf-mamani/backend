from faker import Faker
from faker.providers import person, internet


objFaker = Faker()
objFaker.add_provider(person)
objFaker.add_provider(internet)


# print(objFaker.first_name())
# print(objFaker.last_name())
# print(objFaker.free_email())
# print(objFaker.name())

# cursos = ['COMUNICACION', 'CTA', 'INGLES', 'FRENCH']

# for curso in cursos:
#     print(f"INSERT INTO CURSOS (nombre) VALUES ('{curso}');")

# print('INSERT INTO alumnos (nombre, apellido, correo) VALUES')
# for i in range(100):
#     myfirstname = objFaker.first_name()
#     mylastname = objFaker.last_name()
#     myemail = objFaker.free_email()

#     print(f"('{myfirstname}','{mylastname}','{myemail}'),")



import pandas as pd

# Lista de alumnos y cursos
alumno_li = []
for i in range(1,101):
    for j in range(1,5):
        alumno_li.append([i, j])
# Desorden de datos, conversión lista/dataframe
df = pd.DataFrame(alumno_li, columns=['a','b'])
df1 = df.sample(frac=1).reset_index(drop=True)
# Impresión consulta
for m in range(200):
    alumno_id = df1.iloc[m+1,0]
    curso_id = df1.iloc[m+1,1]
    print(f"INSERT INTO alumnos_cursos (alumno_id, curso_id) VALUES({alumno_id},{curso_id});")
