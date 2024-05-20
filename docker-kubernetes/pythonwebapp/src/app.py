from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello World</p>"


@app.route("/health")
def health_status():
    return jsonify(
        status="up"
    )


def fetchDetails():
    host_name = socket.gethostname()
    #host_ip = socket.gethostbyname(host_name)
    return str(host_name)


@app.route("/details")
def details():
    host_name = fetchDetails()
    return render_template('index.html', host_name=host_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
