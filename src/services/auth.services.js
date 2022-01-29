import { compareSync } from "bcrypt";
import { prisma } from "../prisma.js";
import jwt from "jsonwebtoken";

export class AuthService {
    static async login({ correo, password}) {
        // SELECT password, tipo_usuario FROM USUARIO WHERE correo = ...
        // sino lo encuentra se mostrará un error de not found
        const usuarioEncontrado = await prisma.usuario.findUnique({
            where: { correo },
            select: { password: true, tipoUsuario: true},
            rejectOnNotFound: true,
        });

        const resultado = compareSync(password, usuarioEncontrado.password);

        if (resultado) {
            const token = jwt.sign(
                { id:usuarioEncontrado.id, mensaje_oculto: "hola soy un mensaje"},
                process.env.jwt_secret,
                { expiresIn: 100}
            )
            return { message: "Si es el usuario", token };
        } else {
            return { message: "Credenciales incorrectas" };
        }
    }
}