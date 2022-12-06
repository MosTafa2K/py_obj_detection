"""
Project Name: Object Detection Programm In Python
Version: 1.0.3
Authors: M.Rezaee Jamkarani & M.Mohammadzadeh
Technologies:
    * ImageAi: An Standalone Package for Object Detection
    * Tensorflow
    * keras
    * numpy: For Calculate Points In Image
    * matplotlib: For Drawing Colored box
    * Pillow: For Open And Working With Image


How To Use:

1- Create an 'object' from 'PyObjectDetection' class
>>> obj = PyObjectDetection()

2- Use one of 'PyObjectDetection' object methods
>>> obj.detect_image("param1", "param2")

* Notic:
    - Param1: Input Image
    - Param2: Output Image
    Example:
        obj.detect_image("Image1.jpg", "Image1_result.jpg")
    
    ** Put your input images in 'Images' folder in then put it name in self place
    ** The result will be save as your fav name in 'Out' folder 
"""
import os
import datetime
from abc import ABC, abstractmethod
import colorama
from imageai.Detection import ObjectDetection, VideoObjectDetection


class BaseDetection(ABC):

    @abstractmethod
    def initModel(self):
        pass


class ImageDetection(BaseDetection):

    def __init__(self):
        self.image_detector = ObjectDetection()

    def initModel(self):
        self.image_detector.setModelTypeAsYOLOv3()
        self.image_detector.setModelPath(
            os.path.join(execution_path, "./Models/yolo.h5"))
        self.image_detector.loadModel()

        # Image Detection

    def detect_image(self, inp_image: str):
        out_file = "result_" + inp_image.split(".")[0]
        out_file_ext = inp_image.split(".")[1]
        self.detections = self.image_detector.detectObjectsFromImage(
            input_image=os.path.join(execution_path, f"./Images/{inp_image}"),
            output_image_path=os.path.join(
                execution_path, f"./Out/{out_file + '.' + out_file_ext}")
        )

        print("-"*50)
        for num, eachObjeect in enumerate(self.detections, start=1):
            print(
                f'{num}) {eachObjeect["name"]}: {eachObjeect["percentage_probability"]}')
        print("Done with successfully!")


class VideoDetection(BaseDetection):

    def __init__(self) -> None:
        self.video_detector = VideoObjectDetection()

    def initModel(self):
        self.video_detector.setModelTypeAsYOLOv3()
        self.video_detector.setModelPath(
            os.path.join(execution_path, "./Models/yolo.h5"))
        self.video_detector.loadModel()

    def video_detection(self, inp_video: str):
        print(
            f"{colorama.Fore.GREEN}[+] {colorama.Fore.RESET}Detection Started at: {datetime.datetime.now()}")
        vid_name = inp_video.split(".")[0]
        self.video_detector.detectObjectsFromVideo(
            input_file_path=f"./Videos/{inp_video}",
            output_file_path=f"./Out/{'result_' + vid_name}",
            frames_per_second=30,
            log_progress=True
        )
        print(
            f"{colorama.Fore.GREEN}[+] {colorama.Fore.RESET}Detection Ended at: {datetime.datetime.now()}")


# Get Current Directory
execution_path = os.getcwd()
colorama.init()


def main():
    """ Puts your code here """
    pass


if __name__ == "__main__":
    main()
