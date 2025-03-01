from flask import Flask,request, jsonify

app = Flask(__name__)

cars = [
    {
        'id': 1,
        'License plate': 3478932,
        'company': "Mazda",
        'model': "2",
        'color': "black",
        'year': 2017
    },
    {
        'id': 2,
        'License plate': 2627610,
        'company': "Mazda",
        'model': "3",
        'color': "blue",
        'year': 2020
    },
    {
        'id': 3,
        'License plate': 4578924,
        'company': "BMW",
        'model': "x2",
        'color': "grey",
        'year': 2025
    },
    {
        'id': 4,
        'License plate': 6490142,
        'company': "Audi",
        'model': "3",
        'color': "yellow",
        'year': 1990
    },
    {
        'id': 5,
        'License plate': 5647835,
        'company': "BMW",
        'color': "i8",
        'color': "green",
        'year': 1999
    }
]


@app.get("/cars")
def all_cars():
    return cars

@app.get("/new_cars")
def new_cars():
    new_cars_list = []
    for car in cars:
        if car["year"] >= 2020:
            new_cars_list.append(car)
    return new_cars_list

@app.get("/mazda")
def mazda():
    mazda_cars_list = []
    for car in cars:
        if car["company"] == "Mazda":
            mazda_cars_list.append(car)
    return mazda_cars_list


@app.post("/cars")
def create_car():
    create_car = request.json
    if validate_car_properties(create_car):
        if not exists_car(create_car):
            create_car["id"] = len(cars)+1
            cars.append(create_car)
            return "new car added", 201
        else:
            return f"car {create_car["License plate"]} already exists", 409
    else:
        return "missing data", 400

def exists_car(create_car):
    for car in cars:
        if car["License plate"] == create_car["License plate"]:
            return True
    return False


def validate_car_properties(create_car):
    if "License plate" not in create_car.keys() or\
        "company" not in create_car.keys() or\
        "year" not in create_car.keys() or\
        "model" not in create_car.keys() or\
        "color" not in create_car.keys():            
        return False
    else:
        return True



if __name__ == "__main__":
    app.run(port=8037, debug=True)