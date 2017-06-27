from flask import Flask, render_template, request, url_for, jsonify, send_from_directory
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
	print("Hello!")
	return send_from_directory("pages", "index.html")

@app.route("/<path:path>")
def open_file(path):
	return send_from_directory("static", path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4999)

