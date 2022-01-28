import { prisma } from "../prisma.js";

export class AuthService {
    static async login({ correo, password}) {
        // SELECT password, tipo_usuario FROM USUARIO WHERE correo = ...
        // sino lo encuentra se mostrará un error de not found
        const usuarioEncontrado = await prisma.usuario.findUnique({
            where: { correo },
            select: { password: true, tipoUsuario: true},
            rejectOnNotFound: true,
        });

        return { message : "Si existe"}
    }
}