from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total Request Count')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

app.run(host='0.0.0.0', port=5000)