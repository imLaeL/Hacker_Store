import uuid
from sqlalchemy import Column, Integer, String
from .database import Base

class Produtos(Base):
    __tablename__ = "produtos"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    preco = Column(Integer, nullable=False)
    qtde = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Produto id={self.id} nome={self.nome}>"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "qtde": self.qtde
        }
