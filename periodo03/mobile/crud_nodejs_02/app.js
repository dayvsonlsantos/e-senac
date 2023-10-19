const express = require("express")
const app = express()
const port = 3000

path = require('path')

const bodyParser = require("body-parser")
cors = require('cors')

// Importando Mongo
const mongoose = require("mongoose")

// Important Rotas
const projectRouter = require('./routes/projects.route')

// Important .env
require('dotenv').config();


const connect = () => {
    mongoose.connect(`mongodb+srv://${process.env.DB_USER}:${process.env.DB_PASS}@crud.rdluv7o.mongodb.net/projects_db?retryWrites=true&w=majority`)

    const connection = mongoose.connection;

    connection.on("error", () => {
        console.error("Erro ao conectar com o MongoDB")
    })

    connection.on("open", () => {
        console.log("Conectado ao MongoDB com sucesso!")
    })

}

connect();

module.exports = mongoose;

// Iniciando Servidor
app.listen(process.env.PORT, () => {
    try {
        console.log(`Servido está rodando na porta ${port}`)
    } catch (e) {
        console.log('Servidor Offline')
    }
})

app.use(bodyParser.json())
app.use(cors())
app.use('/project', projectRouter)

app.get('/', (req, res) => {
    res.send('Hello World!')
})