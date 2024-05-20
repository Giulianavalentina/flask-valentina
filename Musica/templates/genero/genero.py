from flask import Blueprint, render_template
from ... import db
bp = Blueprint('genero', __name__, url_prefix= '/genero')
@bp.route('/')
def generos():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres
        ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("genero/genero.html",generos=lista_de_resultado)

@bp.route('detalle/<init:id>')
def generos(id):
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres
        WHERE id = ?
        ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("genero/genero.html",generos=lista_de_resultado)

