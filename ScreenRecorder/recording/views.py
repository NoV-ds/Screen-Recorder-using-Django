from recording import Video_Record
from django.shortcuts import render
from Video_Record import Screen_Recorder, ScreenSize
import cv2 as cv
import threading
# Create your views here.
def index(request):
    return render(request, 'index.html')

def record(request):
    frame_size = ScreenSize()
    fourcc = cv.VideoWriter_fourcc(*"XVID") #file compresing according to video format
    out_video = cv.VideoWriter("media/Recording.mp4", fourcc, 24.0, frame_size) 
    return Screen_Recorder(out_video)

def start_recording(self):
    pass