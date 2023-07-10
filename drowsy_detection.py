from flask import Flask, render_template, Response, jsonify
import threading
import cv2
import time
import numpy as np
from keras.models import load_model
import torch
from facenet_pytorch import MTCNN


# flask
app = Flask(__name__)

# global variables
camera_frame = None
drowsy_detected_count = 0


# The function of drowsy detection
def drowsy_detection() :
    # variables
    global camera_frame
    global drowsy_detected_count  # '연달아' 졸음이라 예측한 횟수 (최종적인 졸음 판단 기준)
    prev_time = 0
    fps = 1

    # device
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print('Running on device : {}'.format(device))

    # webcam
    webcam = cv2.VideoCapture(0)

    # detectors
    face_detector = MTCNN(keep_all = True, device = device)
    drowsy_detector = load_model('./vgg_16_train_B3K1_taein12_juhyang12_epoch4_seed30.h5')

    while True:
        ret, frame = webcam.read()

        # when a frame is captured
        if ret == True :
            time_interval = time.time() - prev_time
            
            # face detection and crop
            boxes, _ = face_detector.detect(frame)
        
            try : 
                if boxes.size > 0 :
                    start_x = int(boxes[0][0])
                    start_y = int(boxes[0][1])
                    end_x = int(boxes[0][2])
                    end_y = int(boxes[0][3])
                    
                    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255, 0, 0), 2)
                    cropped_face = frame[start_y : end_y, start_x : end_x]
                    cropped_face = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2RGB)  # opencv는 BGR이므로 RGB로 바꾸기
                    cropped_face = cv2.resize(cropped_face, (100, 100))
                        
                    # when time has elapsed as long as fps, do drowsy detection
                    if time_interval >= 1 / fps :
                        prev_time = time.time()

                        # drowsy detection
                        cropped_face = np.expand_dims(cropped_face, axis = 0)
                        result = drowsy_detector.predict(cropped_face)
                        predicted_label = result.argmax()

                        if predicted_label == 1 :
                            drowsy_detected_count += 1
                        else :
                            drowsy_detected_count = 0
                            
                        # print('predicted label =>', predicted_label, ', drowsy detected count =>', drowsy_detected_count)

                        if drowsy_detected_count >= 3 :
                            cv2.putText(frame, 'Drowsy!', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
                        else :
                            cv2.putText(frame, 'Not Drowsy', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)

            except :
                pass

            # copy frame
            camera_frame = frame.copy()


# 이 url을 입력하면, 웹캠 영상이 스트리밍됨.
@app.route('/')
def main() :
    return render_template('main.html')


# 이 url을 입력하면, 졸음 예측 함수가 실행됨.
@app.route('/start_drowsy_detection')
def start_drowsy_detection() :
    t = threading.Thread(target = drowsy_detection)
    t.start()

    return 'start drowsy detection'


# 프레임을 인코딩한 후 반환하는 함수
def get_frame() :
    global camera_frame

    while True :
        if camera_frame is not None :
            ret, buffer = cv2.imencode('.jpg', camera_frame)
            frame = buffer.tobytes()

            if ret == True :
                yield (b'--frame\r\n' 
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# 이 url을 입력하면, 웹캠의 프레임을 반환함.
@app.route('/video_feed')
def video_feed() :
    return Response(get_frame(), mimetype = 'multipart/x-mixed-replace; boundary=frame')


# 이 url을 입력하면, 졸음 예측 결과를 반환함.
@app.route('/drowsy_detection_result')
def show_drowsy_detection_result() :
    global drowsy_detected_count
    
    if drowsy_detected_count >= 3 :
        return jsonify(1)
    else :
        return jsonify(0)


# Flask 앱 실행
if __name__ == '__main__' :
    app.run(host = '0.0.0.0', port = 5000, debug = True)