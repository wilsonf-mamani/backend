import Prisma from "@prisma/client";
import { prisma } from "../prisma.js";
import { ArchivosService } from "./archivos.services.js";

export class ProductoService {
  static async crearProducto(data) {
    try {
      const nuevoProducto = await prisma.producto.create({
        data,
      });

      return { content: nuevoProducto };
    } catch (error) {
      console.log(error);
      if (error instanceof Prisma.Prisma.PrismaClientValidationError) {
        return {
          message: "error en la validacion de prisma",
        };
      }

      if (error instanceof Prisma.Prisma.PrismaClientKnownRequestError) {
        // https://www.prisma.io/docs/reference/api-reference/error-reference

        // el producto ya existe
        // la data es insuficiente
        // la fk del tipo de producto no existe
        // si es que queremos eliminar y ese registro tiene relacion con otra tabla no permitira la eliminacion
        return {
          message: "Error al crear el producto",
          content: error.message,
        };
      }
    }
  }


  static async devolverProducto(id) { 
    const producto = await prisma.producto.findUnique({
        where: { id: +id },
        inclued: { tipoProducto: true },
        rejectOnNotFound: false,
    });


    if (ProductoService === undefined) {
        return {
            message: `No existe el producto con el id ${id}`
        };
    }
    
    const productoConImagen = {
        ...producto,
        imagen: ArchivosService.devolverUrl(producto.imagen),
    };

    return{
        producto: productoConImagen
    }
 }   

 static async listarProductos() {
     const productos = await prisma.producto.findMany({
         include: { tipoProducto: true },
     });

     console.log(productos);
     const productosIterados = productos.map((producto)=>{
         return {
             ...producto, 
             imagen: producto.imagen && ArchivosService.devolverURL(producto.imagen),
        };
     })
     return { productos: productosIterados };
 }



}