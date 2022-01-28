import validator from "validator";

export function loginDto({correo, password}){
    if (!validator.isEmail(correo)) {
        throw Error('el correo debe ser un correo válido');
    }

    if (!validator.isStrongPassword(password)) {
        throw Error(
            'la contraseña no es lo suficientemente segura'
            );
    }
    return { correo, password};
}