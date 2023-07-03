
# # מעבר על עץ ההסרטות

# import os
# import shutil
# from datetime import datetime, timedelta
# import Detecting_multiple_objects_in_a_video


# # חיפוש הקטגוריה בעץ אינדקס ואם קיים לחפש לפי מה שקיים ברשימה המקושרת בטווח התאריך והשעה המבוקשים ורק אם לא מצא ישלח לפונקציה
# # להוסיף כאן קטגוריה חדשה שלא היתה
# def iterate_folders(start_date, start_time,end_date,end_time,class_id,head_list):
#     # current_date = datetime.strptime(start_date, "%d-%m-%Y")
#     current_time = datetime.strptime(start_time, "%H-%M")
#     # end_date = datetime.strptime(end_date, "%d-%m-%Y")
#     end_time = datetime.strptime(end_time,  "%H-%M")


#     while True:
#         # folder_name = os.path.join("01-05-2023_07-05-2023", current_date.strftime("%d-%m-%y"), current_time.strftime("%H-%M"))
#         folder_name = os.path.join("01-05-2023_07-05-2023", start_date, current_time.strftime("%H-%M"))

# ######################
#         # for filename in os.listdir(folder_name):
#         #     file_path = os.path.join(folder_name, filename)
#         #     try:
#         #         if os.path.isfile(file_path) or os.path.islink(file_path):
#         #            Detecting_multiple_objects_in_a_video.video_detect(file_path, class_id)
#         #         elif os.path.isdir(file_path):
#         #             shutil.rmtree(file_path)
#         #     except Exception as e:
#         #         print('Failed to delete %s. Reason: %s' % (file_path, e))
# #######################

#         # # קבלת רשימת כל הקבצים בתיקייה
#         files = os.listdir(folder_name)

#         # # סינון הקבצים כך שנשארו רק סוגי הקבצים שהם סרטונים (לדוגמה, עם סיומת .mp4)
#         # video_files = [file for file in files if file.endswith('.mp4')]
        
#         # # שליחת  הסרטונים
#         for video_file in files:
#             file_path = os.path.join(folder_name, video_file)
#             Detecting_multiple_objects_in_a_video.video_detect(file_path, class_id,head_list)
         
#         # Move to the next time
#         current_time += timedelta(hours=1)

#         # Move to the next date if the current time exceeds 23:00
#         if current_time.hour == 7 : # לשנות ל 23
#             folder="01-05-2023_07-05-2023\\"+ start_date+"\\" +current_time.strftime("%H-%M")
#             video_file= os.listdir(folder)
#             for video in video_file:
#                Detecting_multiple_objects_in_a_video.video_detect(folder+"\\"+video, class_id,head_list)
#             start_date += timedelta(days=1)
#             current_time = datetime.strptime("01:00", "%H:%M")  # לשנות ל00:00    

#         # Stop the iteration if the current date exceeds the current date
#         if start_date  > end_date or (start_date==end_date and current_time >end_time):
#            break
             


import os
import shutil
from datetime import datetime, timedelta
import Detecting_multiple_objects_in_a_video


# מקבל גם מערך המייצג זמנים המכיל מספר פריים ממנו להתחיל בסרטונים
def iterate_folders(start_date, start_time, end_date, end_time,my_array, class_id, head_list): 
    current_date = datetime.strptime(start_date, "%d-%m-%y")
    current_time = datetime.strptime(start_time, "%H-%M")
    end_date = datetime.strptime(end_date, "%d-%m-%y")
    end_time = datetime.strptime(end_time, "%H-%M")

    while True:
        numFrame=0
       # בודקת אם הסרטון הופיע ברשימה
        if my_array:  
            existing_item =next((item for item in my_array if item["date"] == current_date.strftime("%d-%m-%y") and item["time"] == current_time.strftime("%H-%M")), None)
            if existing_item:
                numFrame=existing_item["numFrame"]

        folder_name = os.path.join("01-05-2023_07-05-2023", current_date.strftime("%d-%m-%y"), current_time.strftime("%H-%M"))

        files = os.listdir(folder_name)

        for video_file in files:
            file_path = os.path.join(folder_name, video_file)
            finish=Detecting_multiple_objects_in_a_video.video_detect(file_path,numFrame, class_id, head_list)      
            if finish:
                print("לגמור כאן הכל")           

        current_time += timedelta(hours=1)

        if current_time.hour == 23:
            folder = os.path.join("01-05-2023_07-05-2023", current_date.strftime("%d-%m-%y"), current_time.strftime("%H-%M"))
            video_files = os.listdir(folder)
            for video in video_files:
                file_path = os.path.join(folder, video)
                Detecting_multiple_objects_in_a_video.video_detect(file_path,numFrame, class_id, head_list)

                    

            current_date += timedelta(days=1)
            current_time = datetime.strptime("00:00", "%H:%M")

        if current_date > end_date or (current_date == end_date and current_time > end_time):
            break
