from flask import Flask
from urllib.parse import unquote
app = Flask(__name__)
@app.route("")
def hello():
  return "To evaluate code, please go to, for example, https://safe-exec.onrender.com/1+1<br/>That will give you the value of 1+1, which is 2."
@app.route("/<code>")
def execute(code):
  try:
    return str(eval(unquote(code)))
  except BaseException as e:
    return repr(e)
