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

# INSERT INTO personas (nombre, dni, fecha_nacimiento, sexo, estado, created_at) VALUES
#                      ('Patricio', '12964757', '1991-08-01', 'otro', true, now());  
print('INSERT INTO personas (nombre, apellidos, email) VALUES')
for i in range(100):
    myfirstname = objFaker.first_name()
    mylastname = objFaker.last_name()
    myemail = objFaker.free_email()

    print(f"('{myfirstname}','{mylastname}','{myemail}'),")

# INSERT INTO personas (nombre, dni, fecha_nacimiento, sexo, estado, created_at) VALUES
#                      ('Patricio', '12964757', '1991-08-01', 'otro', true, now());  