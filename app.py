from flask import Flask, render_template, request, redirect, url_for
from models import db, Ship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iara.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        ship_name = request.form['name']
        reg_num = request.form['reg_number']
        captain_name = request.form['captain']

        new_ship = Ship(name=ship_name, reg_number=reg_num, captain=captain_name)

        db.session.add(new_ship)
        db.session.commit()
        return redirect(url_for('index'))

    ships = Ship.query.all()
    return render_template('index.html', ships=ships)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)