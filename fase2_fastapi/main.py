from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à API do Greg!"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/usuarios/{nome}")
def saudacao(nome: str):
    return {"mensagem": f"Olá, {nome}!"}

@app.get("/soma/{a}/{b}")
def soma(a: int, b: int):
    return {"resultado": a + b}