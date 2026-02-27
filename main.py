import cowsay
import flask
import torch

app = flask.Flask(__name__)

@app.route("/")
def index():
    msg = cowsay.get_output_string("cow", "Hello from Docker!")
    return f"<pre><code>{msg}</code></pre>"

@app.route("/gpu")
def gpu():
    return torch.cuda.get_device_name()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
