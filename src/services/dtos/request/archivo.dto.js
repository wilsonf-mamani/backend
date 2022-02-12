import validator from "validator";
export function archivoDto({productoId, contentType, ext, filename}) {
    if(!validator.isNumeric(productoId.toString())){
        throw Error('El productId debe ser numérico')
    }

    if(
        contentType !== "image/png" &&
        contentType !== "image/jpg" &&
        contentType !== "image/jpeg"
    ){
        throw Error('El contentType solo puede ser: image/png, image/jpg, image/jpeg');
    }

    if(
        !validator.equals(ext, "png") &&
        !validator.equals(ext, "jpg") &&
        !validator.equals(ext, "jpeg") 
        ){
        throw Error('La extensión solo puede ser: png, jpg, jpeg');
    }    

    if( validator.isEmpty(filename) ){
        throw Error('El filename no puede estar vacio');
    }    

    return { productoId, contentType, ext, filename}
}