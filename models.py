from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    reg_number = db.Column(db.String(50), unique=True, nullable=False)
    captain = db.Column(db.String(100))

    def __repr__(self):
        return f'<Ship {self.name}>'