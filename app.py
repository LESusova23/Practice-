from flask import Flask, render_template, request, redirect, url_for
from models import db, Ship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iara.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Используем .get для безопасности
        ship_name = request.form.get('name', '')
        reg_num = request.form.get('reg_number', '')
        captain_name = request.form.get('captain', '')

        new_ship = Ship(name=ship_name, reg_number=reg_num, captain=captain_name)
        db.session.add(new_ship)
        db.session.commit()
        return redirect(url_for('index'))

    ships = Ship.query.all()
    return render_template('index.html', ships=ships)


@app.route('/delete/<int:ship_id>', methods=['GET', 'POST'])
def delete_ship(ship_id: int):
    # Теперь переменная называется ship_id, конфликтов нет
    ship = Ship.query.get_or_404(ship_id)
    db.session.delete(ship)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)