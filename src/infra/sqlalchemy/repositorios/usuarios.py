from src.infra.sqlalchemy.models import models
from src.schema import schemas
from .main import RepositorioBase


class RepositorioUsuario(RepositorioBase):

    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(nome=usuario.nome,
                                    telefone=usuario.telefone)
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario

    def listar(self):
        usuarios = self.db.query(models.Usuario).all()
        return usuarios



        
