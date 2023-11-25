#servidor REST
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/truck/api/", methods=["GET"])
def Get_Trucks():
    Trucks = [
        {"id": 1, "year": 2017, "model": ""},
        {"id": 2, "year": 2019, "model": ""},
        {"id": 3, "year": 2020, "model": ""},
        {"id": 4, "year": 2016, "model": ""},
    ]
    return jsonify(Trucks)


@app.route("/truck-details/api/", methods=["GET"])
def Truck_Details():
    Details = {"id": 2, "year": 2019, "model": ""}
    return Details


if __name__ == "__main__":
    app.run(debug=True)
