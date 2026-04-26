from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# Configurações
SECRET_KEY = "sua-chave-secreta-troque-em-producao"
ALGORITHM = "HS256"
EXPIRACAO_MINUTOS = 30

# Contexto de criptografia
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash: str) -> bool:
    return pwd_context.verify(senha, hash)

def criar_token(dados: dict) -> str:
    payload = dados.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRACAO_MINUTOS)
    payload.update({"exp": expiracao})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None