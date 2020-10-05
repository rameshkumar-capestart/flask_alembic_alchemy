from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:thispassword@localhost:5432/learning_alembic_sqlalchemy"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"


class CarsCompany(db.Model):
    __tablename__ = 'cars_company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    car = relationship("CarsModel", backref=db.backref("cars", uselist=False))

    def __init__(self, name, car_id):
        self.name = name
        self.car_id = car_id

    def __repr__(self):
        return f"<Car {self.name}>"



@app.route('/cars', methods=['POST', 'GET'])
def handle_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])
            db.session.add(new_car)
            db.session.commit()
            print(new_car.id)
            new_company = CarsCompany(name=data["name"],car_id=new_car.id)
            db.session.add(new_company)
            db.session.commit()

            return {"message": f"car {new_car.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        cars = CarsModel.query.all()
        results = [
            {
                "name": car.name,
                "model": car.model,
                "doors": car.doors
            } for car in cars]

        return {"count": len(results), "cars": results}