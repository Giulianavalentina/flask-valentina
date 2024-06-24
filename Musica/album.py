from flask import Blueprint, render_template
from . import db
bp = Blueprint('album', __name__, url_prefix= '/album')
@bp.route('/')
def albums():
    base_de_datos = db.get_db()
    consulta = """
         SELECT Title, AlbumId FROM albums
        ORDER by Title;
    """
    resultado = base_de_datos.execute(consulta, (id,))
    lista_de_resultado = resultado.fetchall()
    return render_template("album.html",albums=lista_de_resultado)

@bp.route('detalle/<int:id>')
def album(id):
    base_de_datos = db.get_db()
    consulta = """
        SELECT Title, AlbumId FROM albums
        WHERE AlbumId = ?
        ORDER by Title;
        
    """
    consulta2 = """
        SELECT t.name, t.tracksId FROM tracks t
        WHERE t.AlbumId = ?
        ORDER by Title;
    """
    resultado = base_de_datos.execute(consulta, (id,))
    albums = resultado.fetchone()
    resultado = base_de_datos.execute(consulta, (id,))
    lista_album = resultado.fetchall()
    pagina = render_template("detalle_album.html",  
    album = albums,
    canciones = lista_album)
    return pagina

