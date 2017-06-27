from flask import Flask, render_template, request, url_for, jsonify, send_from_directory
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#mysql = MySQL()
#app.config['MYSQL_DATABASE_USER'] = '6s08'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'dome-crawler'
#app.config['MYSQL_DATABASE_DB'] = '6s08'
#app.config['MYSQL_DATABASE_HOST'] = 'domecrawl.us'
#mysql.init_app(app)

@app.route("/")
def hello():
    return send_from_directory("static", "index.html")

@app.route("/<path:path>")
def open_file(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4999, threaded=True)

