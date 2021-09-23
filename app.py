#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, json, render_template, Response, request, jsonify
from flask.wrappers import Request

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera
from robo_controller import PIROBO
# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)
robo_controller = PIROBO()

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' +
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/control_handler", methods=["POST"])
def control_handler():
    data = request.json
    if(robo_controller.send_action(data["action"])):
        return jsonify({"status": "Success", "action": data["action"]})
    else:
        return jsonify({"status": "Failed", "action": data["action"]})


@app.route("/tunnel_address")
def get_tunnel_address():
    return jsonify({"URL": ngrok_tunnel.public_url})


if __name__=="__main__":
    from pyngrok import ngrok, conf
    ngrok_tunnel = ngrok.connect(8080)
    print(ngrok_tunnel)
    app.run(host="localhost", port=8080)