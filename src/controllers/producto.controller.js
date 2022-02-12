import { productoDto } from "../services/dtos/request/producto.dto.js";
import { ProductoService } from "../services/producto.service.js";

export async function crear(req, res) {
    try{
        const data = productoDto(req.body);
        const resultado = await ProductoService.crearProducto(data);
        return res.status(201).json(resultado);
    } catch (error) {
        return res.status(400).json({
            message: error.message,
        });
    }

}

export async function devolver(req, res) {
    const { id } = req.params;
    const resultado = await ProductoService.devolverProducto(id);

    return res.json(resultado);
}

export async function devolverProductos(req, res) {
    const resultado = await ProductoService.listarProductos();

    return res.json(resultado);
}