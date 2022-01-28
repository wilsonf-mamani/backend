import express, { json } from "express";
import morgan from "morgan"
import { authRouter } from "./routes/auth.routes.js";

const app = express();
app.use(morgan("dev"));
app.use(json());

//definir rutas
app.use(authRouter);

const PORT = process.env.PORT ?? 3000;

app.listen(PORT, () => {
    console.log(`servidor corriendo exitosamente en el puerto ${PORT}`);
})