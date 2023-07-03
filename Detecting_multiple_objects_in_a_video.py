import cv2
import numpy as np
from PIL import Image
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename
import One_bounding_box
from TST_tree_LinkedListNode import LinkedListNode
import TST_tree_LinkedListNode
import Search_in_an_index 
import Single_object_tracking as Strack  # מעקב אובייקט בודד
import search_results
import math
import imageio

# פילוח אובייקט
def Object_segmentation(img, x, y, w, h):

    # צור מסכה של אפסים עם אותה צורה כמו תמונת הקלט
    mask = np.zeros(img.shape[:2], np.uint8)

    # צור מערך זמני של אפסים עם אותה צורה כמו תמונת הקלט
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # הגדר את אזור התיבה התוחמת כחזית
    rect = (x, y, w, h)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    # צור מסכה עם אזור החזית הסביר
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # הכפל את המסכה עם תמונת הקלט כדי לחלץ את החזית
    img = img*mask2[:, :, np.newaxis]
    cv2.imshow('ff', img)
    cv2.waitKey(0)

    # שמור את תמונת החזית שחולצה
    cv2.imwrite('resource/img/objects/output_image{}.jpg'.format(x), img)
    # cv2.imwrite('resource/img/objects/carrrr', img)

g=0
center_points_prv_frame=[]
tracking_objects={}
tracking_cordinates={}
track_id=0
maxDisappeared=13


# זיהוי הקטגוריה לחיפוש
def Identify_the_category_to_search_for(filename):
    img = Image.open("{}".format(filename))
    img = img.convert("RGB")
    np_img = np.array(img)
    (class_ids, scores, bbox) = model.detect(np_img)
    final_boxes =One_bounding_box.one_box(bbox, scores,np_img.shape[0],np_img.shape[1])
    return class_ids[final_boxes[0]]


# פרוק הסרטה לפריימים
def video_detect(filename,firstFrame,category,head_list):
    # מרכזי אובייקטים בפריים הקודם
    global center_points_prv_frame
    # האובייקים המזוהים
    global tracking_objects
    global track_id
    # מספר פריימים שיכול להיעלם ודיין נחשב קיים
    global maxDisappeared
    # total_distance = 0
    # num_pairs = 0
    

# לשלב ספריית זיהוי פנים טובה  (נכון לרגע זה אין אחת כזו טובה מספיק)
# לשלב ספריית השוואת אובייקטים טובה  (נכון לרגע זה אין אחת כזו טובה מספיק)

    # קריאה לקובץ הסרטה
    cap = cv2.VideoCapture(filename)

    # בדיקה אם הקובץ נפתח כראוי
    if not cap.isOpened():
        print("Error opening video file")
        exit()

    # חישוב מספר הפריימים בסרטה
    # frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # # הדפסת מידע על הסרטה
    # print("Video file:", filename)
    # print("Number of frames:", frame_count)

    numFrame = 0
    # בשביל לבדוק כל פריים שישי
    num=0
    finish = None  


    # לולאה למעבר לפריים הרצוי
    while cap.isOpened() and numFrame < firstFrame:
        ret, frame = cap.read()
        numFrame += 1
    

    # פתיחת לולאה לקריאת הפריימים 
    while cap.isOpened():
        ret, frame = cap.read()
        thisFrame=int(cap.get(cv2.CAP_PROP_POS_FRAMES))
       
        # בדיקה אם הפריים נקראו כראוי
        if not ret:
            break
 
        if num%6==0:

            #  נקודות המסגרת הנוכחית
            center_points_cur_frame=[]

            # הדפסת זמן ודקות עבור הפריים הנוכחי
            # מוסיפה אפסים בתחילת המחרוזת כדי להשלים אותה לאורך המבוקש zfill הפעולה

            # seconds = count / cap.get(cv2.CAP_PROP_FPS)
            # minutes = int(seconds // 60)
            # seconds %= 60
            # print("{} {} {} ",count,minutes,seconds)
 

            # המרת הפריים לגווני אפור
            cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            (class_ids, scores, bboxes) = model.detect(frame)
            
            # התיבה האמיתית עבור כל אוביקט
            final_boxes =One_bounding_box.one_box(bboxes, scores,frame.shape[0],frame.shape[1])
            
            for i in final_boxes:
                if (class_ids[i]== category):
                    x1, y1, w, h = bboxes[i]
                    cx = int((x1+x1 + w) / 2)
                    cy = int((y1 +y1+ h) / 2)
                    center_points_cur_frame.append({"center_point":(cx,cy),"box":(x1, y1, w, h),"disappeared":0} )
                    # cv2.putText(frame,str(classes[class_ids[i]])  + str(scores[i]*100), (x1, y1-5),
                    #                 cv2.FONT_HERSHEY_PLAIN, 1, (120, 50, 190), 2)
                    # cv2.rectangle(frame, (x1, y1), (x1+w, y1+h), (0, 0, 0), 2)

            if num<=12:
                for pt in center_points_cur_frame:    
                    for pt2 in center_points_prv_frame:
                        distance = math.hypot(pt2["center_point"][0] - pt["center_point"][0], pt2["center_point"][1] - pt["center_point"][1])
                        # total_distance+=distance # את זה הוספתי
                        # num_pairs+=1  # את זה הוספתי
                        if distance<600:
                            tracking_objects[track_id]=pt
                            track_id+=1
                            # box=pt["box"][0],pt["box"][1],pt["box"][0]+pt["box"][2],pt["box"][1]+pt["box"][3]    
                          
                            # אם זו פעם ראשונה שמחפש בהסרטה הזאת
                            if firstFrame==0:
                                  # ברגע שמוצא אוביקט מעדכן ברשימה בעץ נתיב ההסרטה ומספר פריים
                                result= TST_tree_LinkedListNode.search_linked_list(head_list, filename[22:30],filename[31:36],thisFrame) 
                                if result is None:
                                    newObject=LinkedListNode(filename[22:30],filename[31:36],thisFrame,bboxes[i])
                                    TST_tree_LinkedListNode.add_sorted(head_list,newObject)
                                found= Search_in_an_index.display_specific_frame("\\".join(filename.split("\\")[:-1]),thisFrame,bboxes[i])
                                if found:
                                    print("-----נצרך מעקב----")
                                    finish=Strack.objectTrack(filename,thisFrame,bboxes[i])
                                    if not finish:
                                        # מתחילים בחיפוש שוב מסוף המעקב
                                        while cap.isOpened() and numFrame < Strack.global_object_end_frame:
                                            ret, frame = cap.read()
                                            numFrame += 1
                                        continue
                                        # Search_in_an_index.check_in_index(start_date,start_time,end_date,end_time,category)
                                    #  בשביל לעצור את הלולאה
                                    else :
                                        return finish
            else:
                tracking_objects_copy = tracking_objects.copy()
                center_points_cur_frame_copy = center_points_cur_frame.copy()
                for object_id, pt2 in tracking_objects_copy.items():
                    object_exists = False
                    for pt in center_points_cur_frame_copy:
                        distance = math.hypot(pt2["center_point"][0] - pt["center_point"][0], pt2["center_point"][1] - pt["center_point"][1])

                        # total_distance+=distance # את זה הוספתי
                        # num_pairs+=1  # את זה הוספתי
                        # oעדכון מיקום מזהי
                        if distance < 600:
                            tracking_objects[object_id] = pt
                            object_exists = True
                            if pt in center_points_cur_frame:
                                center_points_cur_frame.remove(pt)
                            continue
                    # הסר תעודות זהות שאבדו
                    if not object_exists:
                        pt2["disappeared"] += 1
                        if pt2["disappeared"] > maxDisappeared:
                           tracking_objects.pop(object_id)
                # הוסף מזהים חדשים שנמצאו
                for  pt in center_points_cur_frame:
                    tracking_objects[track_id] = pt
                    track_id += 1
         
                    # בדיקה אם האובייקט הזה כבר קיים ברשימה מקושרת
                    result= TST_tree_LinkedListNode.search_linked_list(head_list, filename[22:30],filename[31:36],thisFrame) 
                    # אם לא נוסיף את זה לרשימה
                    if result is None:
                        # ברגע שמוצא אוביקט מעדכן ברשימה בעץ נתיב ההסרטה ומספר פריים  
                        newObject=LinkedListNode(filename[22:30],filename[31:36],thisFrame,bboxes[i])
                        TST_tree_LinkedListNode.add_sorted(head_list,newObject)

                    # אם קיים אז לא צריך להוסיף אותו - רק מציגים למשתמש את האובייקט ומאשר אם התכוון לזה
                    # להציג לאישור המשתמש
                    found= Search_in_an_index.display_specific_frame("\\".join(filename.split("\\")[:-1]),thisFrame,bboxes[i])
                    if found:
                        finish=Strack.objectTrack(filename,thisFrame,bboxes[i])
                        if not finish:
                            while cap.isOpened() and numFrame < Strack.global_object_end_frame:
                                ret, frame = cap.read()
                                numFrame += 1
                            continue

                        else :
                             return finish
                        # בשביל לעצור את הלולאה
                       
                # for object_id,pt in tracking_objects.items():
                #     cv2.circle(frame,pt["center_point"],5,(0,0,255),-1)
                #     cv2.putText(frame,str(object_id),(pt["center_point"][0],pt["center_point"][1]-7),0,1,(0,0,255),2)


            # צור העתק של הנקודות
            center_points_prv_frame=center_points_cur_frame.copy()

            key= cv2.waitKey(1)
            if key==27:
                break
        num += 1

    # if  total_distance>0 and num_pairs>0:  # חישוב המרחק בממצוע בין נקודות מרכז אובייקט בפריימים עוקבים בדילוגים 
    #     average_distance = total_distance / num_pairs
    #     print(average_distance)

    cap.release()
    print("Done!")




# opencv DNN
net = cv2.dnn.readNet("resource/model/dnn_model/yolov4-tiny.weights",
                      "resource/model/dnn_model/yolov4-tiny.cfg")

# מודל זהוי אוביקט
model = cv2.dnn_DetectionModel(net)
# השורה הזאת מגדירה את הפרמטרים של קלט המודל
model.setInputParams(size=(320, 320), scale=1/255)

# load classes list
classes = []
with open("resource/model/dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)




