from flask import Flask
from urllib.parse import unquote
app = Flask(__name__)
@app.route("/<code>")
def execute(code):
  return eval(unquote(code))
