from flask import Flask, send_file
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # Use 0 for the default camera

@app.route('/')
def index():
    return 'Welcome to the still image capture server!'

@app.route('/capture')
def capture_image():
    success, frame = camera.read()
    if success:
        cv2.imwrite('captured_image.jpg', frame)
        return send_file('captured_image.jpg', mimetype='image/jpeg')
    else:
        return 'Error capturing image'

if __name__ == '__main__':
    app.run(debug=True)