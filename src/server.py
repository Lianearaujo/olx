from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import SessionLocal, engine, get_db, criar_bd
from src.infra.sqlalchemy.models import models
from src.schema import schemas
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuarios import RepositorioUsuario
from fastapi import FastAPI, Depends, status
from typing import List

# Criar banco de dados
criar_bd()

app = FastAPI()



#USUARIOS

@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=schemas.UsuarioSimples)
def criar_usuario(usuario: schemas.Usuario, session: Session = Depends(get_db)):
    return RepositorioUsuario(session).criar(usuario)


@app.get('/usuarios',response_model=List[schemas.Usuario])
def listar_usuarios(session: Session = Depends(get_db)):
    return RepositorioUsuario(session).listar()


#PRODUTOS

@app.post('/produtos', status_code=status.HTTP_200_OK , response_model=schemas.Produto)
def criar_produto(produto: schemas.Produto, session: Session = Depends(get_db)):
    return RepositorioProduto(session).criar(produto)


@app.get('/produtos', response_model=List[schemas.Produto])
def listar_produtos(session: Session = Depends(get_db)):
    return RepositorioProduto(session).listar()
