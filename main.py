from fastapi import FastAPI
import calculadora


app = FastAPI()


@app.get("/")
def home():
    return 'deu certo'

@app.get("/conta/{expressao}")
def calcular(expressao: str):
    resultado = calculadora.calcular(expressao)
    return {"Resultado": resultado}






