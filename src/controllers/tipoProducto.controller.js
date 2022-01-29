import  jwt from "jsonwebtoken";
import { TipoProductoService } from "../services/tipoProducto.service.js";




export async function crearTipoProducto(req, res) {
    console.log(req.headers)
    const { authorization } = req.headers;

    if (!authorization){
        return res.status(403).json({
            message:
                "No tienes privilegios suficientes para realizar esta acción en tipoProducto.controller"
        })
    }
    const token = authorization.split(' ')[1];
    try {
        const data = jwt.verify(token, process.env.jwt_secret)
        console.log(data);
        const resultado = await TipoProductoService.crearTipoProducto({
            nombreProducto: "",
            usuarioId:1,
        });
    
        return res.json(resultado);
    } catch (error) {
        console.log(error);
        return res.status(403).json({
            message: "token invalida en tipoProducto.controller"
        })
    }


}