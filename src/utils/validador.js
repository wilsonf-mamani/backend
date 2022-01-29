import jwt from 'jsonwebtoken';

export function verificarToken(token){
    try {
        const payload = jwt.verify(token,process.env.jwt_secret);
        return payload;
    } catch (error) {
        return error;
    }
}

export function validarUsuario (req, res, next) {
    if(!req.headers.authorization){
        return res.status(401).json({
            message: "se necesita una token para realizar esta solicitud en validador.js",
        })
    }

    const token = req.headers.authorization.split(" ")[1]
    const resultado = verificarToken(token);
    
    if (resultado instanceof jwt.JsonWebTokenError){
        return res.status(403).json({
            menssage: "La token es invalida, intentar nuevamente en validador.js"
        });
    }
    next();
}