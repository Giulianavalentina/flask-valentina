@bp.route('/new', methods =('GET', 'POST'))
def nuevo():
   if request.method == 'POST':
       name = request.form['name']
       con = db.get_db()
       consulta = """
               INSERT INTO artists(name)
               VALUES(?)
           """
       con.execute(consulta, (name,))
       con.commit()
       return redirect(url_for('artista.artista'))
   else:
       pagina = render_template('nuevo_artista.html',)
       return pagina