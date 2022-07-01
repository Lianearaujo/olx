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



@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=schemas.UsuarioSimples)
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    return RepositorioUsuario(db).criar(usuario)


@app.get('/usuarios', status_code=status.HTTP_202_ACCEPTED, response_model=List[schemas.Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    return RepositorioUsuario(db).listar()


@app.post('/produtos', status_code=status. , response_model=schemas.Produto)
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
    return RepositorioProduto(db).criar(produto)


@app.get('/produtos', response_model=List[schemas.Produto])
def listar_produtos(db: Session = Depends(get_db)):
    return RepositorioProduto(db).listar()
