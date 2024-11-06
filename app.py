from flask import Flask
from urllib.parse import unquote
from urllib.requests import urlopen
from urllib.error import URLError
import subprocess
app = Flask(__name__)
@app.route("/")
def homepage():
  return '<h1 style="text-align:center;"><a href="https://utility-bot-94wf.onrender.com/">Special service made for this thing</a></h1>'
  
@app.route("/calc/<path:code>")
def execute(code):
  try:
    f = open("code.py", "w")
    f.write(f"from math import*\nimport sympy\nfrom sympy.abc import x, y, z\nimport random\ntry:\n\tprint({unquote(code)})\nexcept BaseException as e:\n\tprint(repr(e))")
    f.close()
    carr = ["timeout", "-s", "SIGKILL", "10s", "python3", "code.py"]
    return subprocess.check_output(carr).decode("utf-8")
  except BaseException as e:
    return repr(e)

@app.route("/run/<pastebin_id>")
def execute_code(pastebin_id):
  try:
    code = urlopen(f"https://pastebin.com/").read().decode('utf-8')
    f = open("code.py", "w")
    f.write(code)
    f.close()
    carr = ["timeout", "-s", "SIGKILL", "10s", "python3", "code.py"]
    return subprocess.check_output(carr).decode("utf-8")
  except URLError as e:
    return "An error occured while fetching pastebin text."
  except BaseException as e:
    return repr(e)
