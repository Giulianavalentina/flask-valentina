from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from.import db
    db.init_app(app)

@app.route('/canciones')
def musica():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM tracks
        ;
        """

    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    return render_template("musica.html", musica=lista_de_resultados)