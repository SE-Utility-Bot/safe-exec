from flask import Flask
from urllib.parse import unquote
import subprocess
app = Flask(__name__)
@app.route("/<path:code>")
def execute(code):
  try:
    carr = ["timeout", "-s", "SIGKILL", "10s", "python3", "-c", f"print({unquote(code)})"]
    return subprocess.check_output(carr).decode("utf-8").replace("\n", "")
  except BaseException as e:
    return repr(e)
