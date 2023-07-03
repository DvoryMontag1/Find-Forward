import numpy as np
import math

# הפרש בין 2 מספרים כערך מוחלט
def Difference(num1,num2):
    return abs(num1-num2)

# חישוב מרחק בין 2 נקודות
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

# רוחב המסגרת באחוזים מתוך כל התמונה
def width(w_rectangle, w_frame):
    return w_rectangle/w_frame*100

# גובה המסגרת באחוזים מתוך כל התמונה
def heigth(h_rectangle, h_frame):
    return h_rectangle/h_frame*100


# מסננת תיבות מיותרות
def one_box(boxes, scores, w_frame, h_frame):
    
     #  מיין את התיבות לפי ציון הביטחון בסדר יורד
    ids = np.flip(np.argsort(scores))
    i = 0
    while i < len(ids)-1:
        w=width(boxes[ids[i],2],w_frame)
        h=width(boxes[ids[i],3],h_frame)
        j=i+1
        while j < len(ids):
            if(Difference(w,width(boxes[ids[j],2],w_frame))<8 and
                 Difference(h,heigth(boxes[ids[j],3],h_frame))<8 and
                    distance(boxes[ids[i],0],boxes[ids[i],1],boxes[ids[j],0],boxes[ids[j],1])<60):
                ids = np.delete(ids, j)
            else:
                j=j+1
        i=i+1
    return ids

