import { hashSync } from "bcrypt";

export default async(prisma) => {

    const password = hashSync ('Welcome123', 10)

    await prisma.usuario.upsert({
        create: {
            nombre :'Eduardo',
            correo : 'ederiveroman@gmail.com',
            password : password,
            tipoUsuario: 'ADMIN',
        },
        update: {
            password : password,
        },
        where: {
            correo: 'ederiveroman@gmail.com'
        },
    });
};

