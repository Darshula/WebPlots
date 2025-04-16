from routes.python_runner import python_runner
from routes.r_runner import r_runner
from flask import Flask

from flask_cors import CORS

app = Flask(__name__, static_folder="static", static_url_path="/static")

CORS(app)

app.register_blueprint(r_runner, url_prefix="/r_runner")
app.register_blueprint(python_runner, url_prefix="/python_runner")

if __name__ == "__main__":
    app.run(debug=True, port=65535)
