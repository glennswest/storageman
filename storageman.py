from flask import Flask, render_template, send_from_directory
from nvmetarget import nvmelib

app = Flask(__name__)


@app.route('/js/<path:path>')
def send_js(path):
    return(send_from_directory('js', path))

@app.route('/css/<path:path>')
def send_css(path):
    return(send_from_directory('css', path))

@app.route('/api/v1/devices')
def get_devices():
    data = nvme.targets()
    return(data)

@app.route("/")
def index():
    return render_template('index.html')

nvme = nvmelib.NvmeTarget()
