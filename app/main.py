from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.environ.get('APP_VERSION', "1.0")
    hostname = os.environ.get('HOSTNAME', "unknown") # K8s provides this
    return f"Hello from GitOps on Pi! Version: {version}. Served by pod: {hostname}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

