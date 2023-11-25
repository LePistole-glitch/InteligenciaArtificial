from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>Hola Mundo!</p>"


@app.route("/json/", methods=["GET"])
def json():
    Details = {"id_texto": "Hola", "texto": "Mundo",}
    return Details


if __name__ == "__main__":
    app.run(debug=True)