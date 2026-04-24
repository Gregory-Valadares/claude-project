from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional

# Modelo — define a tabela no banco e valida os dados
class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
    idade: int

# Banco de dados
DATABASE_URL = "sqlite:///./usuarios.db"
engine = create_engine(DATABASE_URL)

def criar_tabelas():
    SQLModel.metadata.create_all(engine)

# App
app = FastAPI()

@app.on_event("startup")
def startup():
    criar_tabelas()

@app.get("/usuarios")
def listar_usuarios():
    with Session(engine) as session:
        usuarios = session.exec(select(Usuario)).all()
        return usuarios

@app.post("/usuarios", status_code=201)
def criar_usuario(usuario: Usuario):
    with Session(engine) as session:
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario

@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    with Session(engine) as session:
        usuario = session.get(Usuario, usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return usuario

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    with Session(engine) as session:
        usuario = session.get(Usuario, usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        session.delete(usuario)
        session.commit()
        return {"mensagem": "Usuário deletado"}