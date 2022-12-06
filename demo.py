from ai_core import PyObjectDetection


obj = PyObjectDetection("video")
obj.initModel()
obj.video_detection("main_video.mp4", "result")
