import os
import time
import cv2
from PIL import Image
from imageai.Detection import ObjectDetection, VideoObjectDetection

execution_path = os.getcwd()
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()

detector.setModelPath(os.path.join(
    execution_path, "./Models/yolo.h5"))
detector.loadModel()

detections = detector.detectObjectsFromVideo(
    input_file_path=os.path.join(execution_path, "video.mp4"),
    output_file_path=os.path.join(execution_path, "video-result"),
    frames_per_second=30,
    log_progress=True
)


print("-"*50)
for num, eachObjeect in enumerate(detections, start=1):
    print(
        f'{num}) {eachObjeect["name"]}: {eachObjeect["percentage_probability"]}')


print("Done with successfully!")

time.sleep(2)
img = Image.open("result.jpg")
img.show()
