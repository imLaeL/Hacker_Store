from flask import Blueprint, request, jsonify
from .database import session
from .models import Produtos

routes = Blueprint("routes", __name__)

@routes.route("/produtos", methods=["GET"])
def get_produtos():
    data = session.query(Produtos).all()
    return jsonify([produto.to_dict() for produto in data])


@routes.route("/produtos", methods=["POST"])
def create_produto():
    data = request.json

    produto = Produtos(
        nome=data["nome"],
        preco=data["preco"],
        qtde=data["qtde"]
    )

    session.add(produto)
    session.commit()

    return jsonify(produto.to_dict()), 201


@routes.route("/produtos/<string:id>", methods=["DELETE"])
def delete_produto(id):
    produto = session.query(Produtos).filter_by(id=id).first()

    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    session.delete(produto)
    session.commit()

    return jsonify({"mensagem": "Produto deletado"})


@routes.route("/produtos/<string:id>", methods=["PUT"])
def update_produto(id):
    data = request.json
    produto = session.query(Produtos).filter_by(id=id).first()

    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    produto.nome = data["nome"]
    produto.preco = data["preco"]
    produto.qtde = data["qtde"]

    session.commit()

    return jsonify(produto.to_dict())
