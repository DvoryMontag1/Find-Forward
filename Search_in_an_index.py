
# חיפושים של קטגוריות בעץ אינדקס
# אולי אני יצרף את זה בסוף עם דף אחר

import cv2
import os
import imageio
from datetime import datetime, timedelta
import TST_tree_node as node
import Detecting_multiple_objects_in_a_video as classes_objects
import showImage
import pickle
import Beyond_the_filming_tree
from PIL import Image



# טעינת העץ והרשימה מהקובץ באמצעות Pickle
with open("data.pickle", "rb") as file:
    loaded_data = pickle.load(file)


# loaded_data = loaded_data["root"]  # השמת העץ הטעון למשתנה root


# הצגת פריים המכיל אוביקט השייך לקטגוריה הנמצא באינדקס
def display_specific_frame(video_path, frame_number,location):
    file_video = os.listdir(video_path)
    video_path1 = os.path.join(video_path, file_video[0])
    video_reader = imageio.get_reader(video_path1)

    # Check if the video has at least one frame
    if len(video_reader) == 0:
        print("The video is empty")
        return

    # Check if the frame number is within the valid range
    if frame_number < 0 or frame_number >= len(video_reader):
        print("Invalid frame number")
        return

    # Read the desired frame
    frame = video_reader.get_data(frame_number)
    

    x1, y1, w, h = location
    cv2.rectangle(frame, (x1, y1), (x1+w, y1+h), (255, 0, 0), 3)
    pil_image = Image.fromarray(frame)
    found=showImage.show(pil_image)
    return found

 
def check_in_index(start_date,start_time,end_date,end_time,class_id):
    found=False
    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    start_date = start_date.strftime("%d-%m-%y")
    end_date = datetime.strptime(end_date, "%d-%m-%Y")
    end_date = end_date.strftime("%d-%m-%y")
    my_array=[]

    head_list= node.searchTST( loaded_data, classes_objects.classes[class_id]) 
    if head_list:  # If the category is already indexed
        current = head_list.next
        #  while current is not None:
        while current and  current.date<=end_date :
              if (start_date < current.date < end_date) or(start_date==current.date and
                                                        current.time>=start_time) or (end_date==current.date and end_date!=current.date and current.time <= end_time):

                  found= display_specific_frame("01-05-2023_07-05-2023\\"+current.date+'\\'+current.time,current.numFrame,current.location)
                  if found: #  אם נמצא האובייקט אפשר לעצור את הלולאה
                      break

                  # Check if the item already exists in the array
                  existing_item = next((item for item in my_array if item["date"] == current.date and item["time"] == current.time), None)
                  if existing_item:
                      # Update the numFrame value
                      existing_item["numFrame"] = current.numFrame
                  else:
                      # Add the new item to the array
                      new_item = {"date": current.date, "time": current.time, "numFrame": current.numFrame}  
                      my_array.append(new_item)
                      
              current = current.next

       
         # מעבר על עץ ההסרטות מינוס איפה שכבר הופיע ברשימה
        Beyond_the_filming_tree.iterate_folders(start_date,start_time,end_date,end_time,my_array, class_id,head_list)
        

    else:
        node.insert( loaded_data, classes_objects.classes[class_id]) # הוספת קטגוריה חדשה לאינדקס
        head_list= node.searchTST( loaded_data, classes_objects.classes[class_id]) 
        Beyond_the_filming_tree.iterate_folders(start_date,start_time,end_date,end_time,None, class_id,head_list)

         # שמירת העץ והרשימה לקובץ באמצעות Pickle
    with open("data.pickle", "wb") as file:
         pickle.dump( loaded_data, file)
         print("finish")




