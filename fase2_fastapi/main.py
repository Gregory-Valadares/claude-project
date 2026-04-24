from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# "Banco de dados" em memória
usuarios = {}
proximo_id = 1

class Usuario(BaseModel):
    nome: str
    email: str
    idade: int

@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à API do Greg!"}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    if usuario_id not in usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuarios[usuario_id]

@app.post("/usuarios", status_code=201)
def criar_usuario(usuario: Usuario):
    global proximo_id
    usuarios[proximo_id] = usuario
    proximo_id += 1
    return {"id": proximo_id - 1, "dados": usuario}

@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario: Usuario):
    if usuario_id not in usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuarios[usuario_id] = usuario
    return {"mensagem": "Usuário atualizado", "dados": usuario}

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    if usuario_id not in usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    del usuarios[usuario_id]
    return {"mensagem": "Usuário deletado"}