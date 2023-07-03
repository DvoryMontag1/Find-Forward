import os
import pickle
# import datetime

class searchResults:
    def __init__(self, date="", camera="", numCamera=0, TimeRangeStart="", TimeRangeEnd="", Description="",Bargain_time="", pathImage="", pathVideo=""):
        self.date = date
        self.camera = camera
        self.numCamera = numCamera
        self.TimeRangeStart = TimeRangeStart
        self.TimeRangeEnd = TimeRangeEnd
        self.Description = Description
        self.Bargain_time=Bargain_time
        self.pathImage = pathImage
        self.pathVideo = pathVideo

# יצירת אינסטנס אחד של המחלקה searchResults כמשתנה גלובלי עם ערכים ריקים
global_variable = searchResults()


# קובץ המכיל את האובייקטים
file_path = "objects.pkl"

# # טעינת האובייקטים מהקובץ אם הקובץ קיים
# if os.path.exists(file_path):
#     with open(file_path, "rb") as file:
#         objects = pickle.load(file)
# else:
#     objects = []

# # יצירת אובייקט חדש והוספתו לרשימה
# new_object = searchResults(datetime.date.today(),"camera A","5","01/05/23 03:00","02/05/23 06:00",None,"resource/img/תמונות חתוכות/object2z15.jpg","output.mp4")
# objects.append(new_object)

# # שמירת הרשימה חזרה לקובץ
# with open(file_path, "wb") as file:
#     pickle.dump(objects, file)

# # הדפסת האובייקטים ברשימה
# for obj in objects:
#     print(obj.date , obj.camera)

def add_search_result(new_object):
    # טעינת האובייקטים מהקובץ אם הקובץ קיים
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            objects = pickle.load(file)
    else:
        objects = []
    objects.append(new_object)
    # שמירת הרשימה חזרה לקובץ
    with open(file_path, "wb") as file:
        pickle.dump(objects, file)




def get_all_searches():
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            objects = pickle.load(file)
            return objects
    else:
        return None





# def add_search_result(date, camera, numCamera, TimeRangeStart, TimeRangeEnd, Description, pathImage, pathVideo):
#     file_path = "objects.pkl"

#     # טעינת האובייקטים מהקובץ אם הקובץ קיים
#     if os.path.exists(file_path):
#         with open(file_path, "rb") as file:
#             objects = pickle.load(file)
#     else:
#         objects = []

#     # יצירת אובייקט חדש והוספתו לרשימה
#     new_object = searchResults(date, camera, numCamera, TimeRangeStart, TimeRangeEnd, Description, pathImage, pathVideo)
#     objects.append(new_object)

#     # שמירת הרשימה חזרה לקובץ
#     with open(file_path, "wb") as file:
#         pickle.dump(objects, file)

