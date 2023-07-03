
import cv2
import numpy as np
import os
from search_results import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


global_finish=None
global_object_end_frame= -1

def cut_video(input_file, output_file, start_time, end_time):
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

def is_object_moving(next_pts, prev_center):
    distance = np.linalg.norm(next_pts[0] - prev_center, ord=2)
    print(distance)
    if distance > 6:
        return True
    else:
        return False

def is_object_out_of_bounds(pts, frame_width, frame_height, padding=10):
    next_pts = pts[0] + padding
    return (
        next_pts[0] < 0 or
        next_pts[0] >= frame_width or
        next_pts[1] < 0 or
        next_pts[1] >= frame_height
    )

def objectTrack(filename, thisFrame, bbox):
    global global_object_end_frame
    global_object_end_frame=-1
    cap = cv2.VideoCapture(filename)
    frame_counter = 0
    object_start_frame = -1
    # object_end_frame = -1

    for _ in range(thisFrame):
        ret, frame = cap.read()
        if not ret:
            print("Failed to read video")
            break
        frame_counter += 1

    start = False
    x, y, w, h = bbox
    prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    prev_center = np.array([x + w / 2, y + h / 2], dtype=np.float32)

    lk_params = dict(winSize=(15, 15),
                     maxLevel=2,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    while True:
        ret, frame = cap.read()

        if not ret:
            break
        frame_counter += 1

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        next_pts, status, _ = cv2.calcOpticalFlowPyrLK(prev_gray, gray, np.array([prev_center]), None, **lk_params)

        if start and object_start_frame == -1 and is_object_moving(next_pts, prev_center):
            object_start_frame = frame_counter
        
        height, width, channels = frame.shape
        if start and is_object_out_of_bounds(next_pts, width, height):
            global_object_end_frame = frame_counter
            break

        prev_center = next_pts[0].flatten()

        # center = tuple(map(int, prev_center))
        # cv2.circle(frame, center, 5, (0, 0, 255), -1)
        # cv2.putText(frame, f"Center: {center}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # cv2.imshow('Tracking', frame)

        if cv2.waitKey(1) == 27:
            break
        start = True

        prev_gray = gray.copy()

    # אם האובייקט נשאר כל הזמן באותו מקום אין צורך להציג אותו
    if global_object_end_frame == -1 and object_start_frame == -1:
        return False

    # אם נגמרה ההסרטה והאובייקט קיים עדיין לעדכן עד הפריים האחרון 
    if global_object_end_frame == -1 and object_start_frame != -1:
         global_object_end_frame=frame_counter
    frame_rate = 30
    object_start_time = round(object_start_frame / frame_rate) 
    object_end_time = round(global_object_end_frame / frame_rate) 
    
    cut_video(filename, "C:/ProgramData/security camera footage/CutVideo.mp4", object_start_time, object_end_time)

    date=filename[22:30]
    clock=int(filename[31:33]) 

    # זמן התחלה
    # חישוב הזמן הכולל בשניות
    # total_time_seconds = object_start_time / frame_rate
    # total_time_seconds = int(total_time_seconds * 1000) // 100
    # חלוקת הזמן הכולל לדקות ושניות
    startMinutes =round(object_start_time // 60) 
    startSeconds =round(object_start_time % 60) 
    formatted_start_time = "{:02d}:{:02d}:{:02d}".format(int(clock), startMinutes, startSeconds)
    # זמן סיום
    # total_time_seconds = object_end_time / frame_rate
    # total_time_seconds = int(total_time_seconds * 1000) // 100

    # חלוקת הזמן הכולל לדקות ושניות
    endtMinutes =round(object_end_time // 60) 
    endSeconds =round(object_end_time % 60) 
    formatted_end_time = "{:02d}:{:02d}:{:02d}".format(clock, endtMinutes, endSeconds)

    search1 = search_results()
    search1.display_screen(date, formatted_start_time,formatted_end_time, "C:/ProgramData/security camera footage/CutVideo.mp4")
    search1.root.mainloop()

    cap.release()
    cv2.destroyAllWindows()

    # print(thisFrame) 
    # print("Object start frame:", object_start_frame)
    # print("Object end frame:", global_object_end_frame)


    return Single_object_tracking.global_finish

    