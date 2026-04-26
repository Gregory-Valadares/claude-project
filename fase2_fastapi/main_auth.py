from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional
from auth import hash_senha, verificar_senha, criar_token, verificar_token

app = FastAPI()

DATABASE_URL = "sqlite:///./auth.db"
engine = create_engine(DATABASE_URL)

def criar_tabelas():
    SQLModel.metadata.create_all(engine)

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
    senha_hash: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.on_event("startup")
def startup():
    criar_tabelas()

@app.post("/cadastrar", status_code=201)
def cadastrar(nome: str, email: str, senha: str):
    with Session(engine) as session:
        existente = session.exec(select(Usuario).where(Usuario.email == email)).first()
        if existente:
            raise HTTPException(status_code=400, detail="Email já cadastrado")
        usuario = Usuario(nome=nome, email=email, senha_hash=hash_senha(senha))
        session.add(usuario)
        session.commit()
        return {"mensagem": f"Usuário {nome} cadastrado com sucesso!"}

@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    with Session(engine) as session:
        usuario = session.exec(select(Usuario).where(Usuario.email == form.username)).first()
        if not usuario or not verificar_senha(form.password, usuario.senha_hash):
            raise HTTPException(status_code=401, detail="Credenciais inválidas")
        token = criar_token({"sub": usuario.email})
        return {"access_token": token, "token_type": "bearer"}

@app.get("/perfil")
def perfil(token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")
    email = payload.get("sub")
    with Session(engine) as session:
        usuario = session.exec(select(Usuario).where(Usuario.email == email)).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return {"nome": usuario.nome, "email": usuario.email}