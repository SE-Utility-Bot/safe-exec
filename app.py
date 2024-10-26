from flask import Flask
from urllib.parse import unquote
import subprocess
app = Flask(__name__)
@app.route("/<path:code>")
def execute(code):
  try:
    f = open("code.py", "w")
    f.write(f"from math import*\nimport sympy\ntry:\n\tprint({unquote(code)})\nexcept BaseException as e:\n\tprint(repr(e))")
    f.close()
    carr = ["timeout", "-s", "SIGKILL", "10s", "python3", "code.py"]
    return subprocess.check_output(carr).decode("utf-8").replace("\n", "")
  except BaseException as e:
    return repr(e)
