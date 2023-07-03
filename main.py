# כאן אני מנסה עכשיו לעבוד על תמונות

import cv2
import numpy as np
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename


import One_bounding_box
# import matplotlib.pyplot as plt


def non_max_suppression(outputs, confidence_threshold=0.5, iou_threshold=0.4):
    # convert outputs to numpy arrays
    bbox_list = np.array(outputs[0])
    conf_list = np.array(outputs[1])
    class_list = np.array(outputs[2])

    # apply confidence threshold
    indices = np.where(conf_list > confidence_threshold)[0]
    bbox_list = bbox_list[indices]
    conf_list = conf_list[indices]
    class_list = class_list[indices]

    # apply non-max suppression
    selected_indices = cv2.dnn.NMSBoxes(
        bbox_list.tolist(), conf_list.tolist(), confidence_threshold, iou_threshold)

    # get selected bounding boxes, confidences, and classes
    selected_boxes = bbox_list[selected_indices[:, 0]].tolist()
    # selected_boxes = bbox_list[selected_indices[:, 0]]
    selected_confidences = conf_list[selected_indices[:, 0]].tolist()
    selected_classes = class_list[selected_indices[:, 0]].tolist()

    return selected_boxes, selected_confidences, selected_classes


# אני מנסה שיהיה רק תיבה אחת
def non_max_suppression(boxes, scores, threshold):
    # חשב את שטח התיבות
    area = (boxes[:, 2] - boxes[:, 0] + 1) * (boxes[:, 3] - boxes[:, 1] + 1)

    # מיין את התיבות לפי ציון הביטחון
    idxs = np.argsort(scores)

    # תיבות התוחמות המתאימות לכל אובייקט
    final_boxes = []

    # לולאה חיצונית לעבור על כל אובייקט בתמונה
    for i in range(len(idxs)):
        # תיבות התוחמות הקשורות לאותו אובייקט
        obj_boxes = []

        # לולאה פנימית למציאת תיבות התוחמות הקשורות לאותו אובייקט
        for j in range(i, len(idxs)):
            # חשב את איזור ההכסה של התיבות
            xx1 = max(boxes[idxs[i], 0], boxes[idxs[j], 0])
            yy1 = max(boxes[idxs[i], 1], boxes[idxs[j], 1])
            xx2 = min(boxes[idxs[i], 2], boxes[idxs[j], 2])
            yy2 = min(boxes[idxs[i], 3], boxes[idxs[j], 3])
            w = max(0, xx2 - xx1 + 1)
            h = max(0, yy2 - yy1 + 1)

            # חשב את אינדקס התיבה עם הציון הגבוה ביותר
            if w * h > 0 and ((w * h) / area[idxs[j]]) >= threshold:
                obj_boxes.append(idxs[j])

        # הוסף את התיבה עם הציון הגבוה ביותר לרשימת התיבות המתאימות לאותו אובייקט
        if obj_boxes:
            final_boxes.append(max(obj_boxes, key=lambda x: scores[x]))

    return final_boxes


# opencv DNN
net = cv2.dnn.readNet("resource/model/dnn_model/yolov4-tiny.weights",
                      "resource/model/dnn_model/yolov4-tiny.cfg")

# מודל זהוי אוביקט
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)

# load classes list
classes = []
with open("resource/model/dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

# print("objects list")
# print(classes)

# Initialize camera
# cap=cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# Create a Tkinter window
# Tk().withdraw()

# filename = askopenfilename()

# Open the image using Pillow+9-

# img = Image.open(filename)
# np_img = np.array(img)
# (class_ids, scores, bbox) = model.detect(np_img)
# (x, y, w, h) = bbox
# cv2.putText(np_img, class_ids, (x, y-5),
# בחר קובץ תמונה
#                 cv2.FONT_HERSHEY_PLAIN, 1, (200, 0, 50), 2)
# cv2.rectangle(np_img, (x, y), (x+w, y+h), (200, 0, 50), 2)
# cv2.imshow("Frame", np_img)
# cv2.waitKey(0)

x = 17

# while True:
# get frame
# frame = cv2.imread("python/2022-02-04-test_image.jpg")
frame = Image.open("IMG_0077.jpg")
img = frame.convert("RGB")
frame = np.array(img)

# np.resize(frame,( 320,320))
# object Detection
l_of_frame = []
i = 0
(class_ids, scores, bboxes) = model.detect(frame)

# final_boxes = non_max_suppression(bboxes, scores, 0.5)
# print(final_boxes)

# final_boxes =One_bounding_box.one_box(bboxes, scores,frame.shape[0],frame.shape[1])



# cv2.imwrite("try.png", frame)


# # טעינת התמונה
# image = plt.imread('image.jpg')

# # נקה את הצירים מריבועים קודמים
# plt.clf()

# # הצגת התמונה
# plt.imshow(image)

# # עבור כל אינדקס בפרמטר final_boxes צייר מלבן סביב האובייקט המתאים
# for idx in final_boxes:
#     # קבלת המיקום והמידות של התיבה המתאימה
#     x1, y1, x2, y2 = bboxes[idx]
    
#     # חישוב רוחב התיבה
#     width = x2 - x1
    
#     # ציור מלבן סביב התיבה
#     plt.gca().add_patch(
#         plt.Rectangle((x1, y1), width, y2 - y1, fill=False, edgecolor='r', linewidth=2)
#     )

# # הצגת התמונה עם המלבנים
# plt.show()


# עבור כל תיבה סופית ברשימה צייר ריבוע על התמונה
# for i in final_boxes:
#     print(bboxes[i])
#     print(class_ids[i])
#     print(scores[i])
#     print("--------------")
#     x1, y1, x2, y2 = bboxes[i]
#     # cv2.rectangle(frame, (x1, y1), (x1+x2, y1+y2), (0, 255, 0), 2)
#     cv2.putText(frame,str(classes[class_ids[i]])  + str(scores[i]*100), (x1, y1-5),
#                     cv2.FONT_HERSHEY_PLAIN, 1, (120, 50, 190), 2)
#     cv2.rectangle(frame, (x1, y1), (x1+x2, y1+y2), (0, 0, 0), 2)
#     # שמירת האוביקט כתמונה
#     box = (x1, y1, x1 + x2, y1 + y2)
#     img2 = img.crop(box)
#     # שמירת התמונה החתוכה
#     img2.save('resource/img/objects/object{}SO.jpg'.format(i))

for class_id, score, bbox in zip(class_ids, scores, bboxes):
        # כאן אם האוביקט שעכשיו מצא הוא מאותה קטגוריה של מה שמחפשים תשמור לי את זה
        # if(class_id==2):
        (x, y, w, h) = bbox
        class_name = classes[class_id]

        l_of_frame.append(
            {"class_name": classes[class_id], "score": score, "bbox": bbox})

        cv2.putText(frame, class_name, (x, y - 10),
                cv2.FONT_HERSHEY_PLAIN, 2, (120, 50, 190), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

        # # שמירת האוביקט כתמונה
        # box = (x, y, x + w, y + h)
        # img2 = img.crop(box)
        # # שמירת התמונה החתוכה
        # img2.save('resource/img/objects/object{}.jpg'.format(i))
        # i += 1

print("class ids", class_ids)
print("scores", scores)
print("bboxes", bboxes)

print("list", l_of_frame)

cv2.imshow("Frame", frame)
cv2.waitKey(0)
# key= cv2.waitKey(1)
# if key==27:
#   break

# cap.release()
# cv2.destroyAllWindows()


# apply non-max suppression to the model outputs
# outputs = (bboxes, scores, class_ids)
# selected_boxes, selected_confidences, selected_classes = non_max_suppression(outputs)

# loop over the selected bounding boxes and draw them on the image
# for box, confidence, class_id in zip(selected_boxes, selected_confidences, selected_classes):
#     x, y, w, h = box
#     cv2.rectangle(np_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     label = f"{classes[class_id]}: {confidence:.2f}"
#     cv2.putText(np_img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


# for class_id, score, bbox in zip(class_ids, scores, bboxes):
#     # כאן אם האוביקט שעכשיו מצא הוא מאותה קטגוריה של מה שמחפשים תשמור לי את זה
#     # if(class_id==2):
#     (x, y, w, h) = bbox
#     class_name = classes[class_id]

#     l_of_frame.append(
#         {"class_name": classes[class_id], "score": score, "bbox": bbox})

#     cv2.putText(frame, class_name + str(score*100), (x, y-5),
#                 cv2.FONT_HERSHEY_PLAIN, 1, (200, 0, 50), 1)
#     cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 0, 50), 2)

#     # שמירת האוביקט כתמונה
#     box = (x, y, x + w, y + h)
#     img2 = img.crop(box)
#     # שמירת התמונה החתוכה
#     img2.save('resource/img/objects/object{}.jpg'.format(i))
# i += 1

# ... קוד נוסף
