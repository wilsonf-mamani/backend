from faker import Faker
from faker.providers import person, internet


objFaker = Faker()
objFaker.add_provider(person)
objFaker.add_provider(internet)


# print(objFaker.first_name())
# print(objFaker.last_name())
# print(objFaker.free_email())
# print(objFaker.name())

cursos = ['COMUNICACION', 'CTA', 'INGLES', 'FRENCH']

for curso in cursos:
    print(f"INSERT INTO CURSOS (nombre) VALUES ('{curso}');")

print('INSERT INTO alumnos (nombre, apellido, correo) VALUES')
for i in range(100):
    myfirstname = objFaker.first_name()
    mylastname = objFaker.last_name()
    myemail = objFaker.free_email()

    print(f"('{myfirstname}','{mylastname}','{myemail}'),")

