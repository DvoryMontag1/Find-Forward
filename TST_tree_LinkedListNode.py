
class LinkedListNode:
    def __init__(self, date, time, numFrame,box):
        self.date = date
        self.time = time
        self.numFrame = numFrame
        self.location=box
        self.next = None  # מצביע לצומת הבא ברשימה
        
# 13122, 14122,15122 -suitcase
#- 11122- 18122
# - stage1 - index- 13'14'15
#stage 2 -if not found \ tree minus 13'14'15 === 11'12'16'17'18
#if found - start from the first date. 

# מעקב תזוזה - טווח שזז מנקודה שהתחיל לזוז עד שנעלם מהפריים

# הוספת איבר לרשימה מקושרת תוך שמירה על רשימה מממוינת

def add_sorted(headOfList, new_object):
    if headOfList.next is None:
        # return new_video
        headOfList.next=new_object
        return

    # מיון לפי תאריך ושעה
    if headOfList.next.date > new_object.date or (headOfList.next.date == new_object.date and headOfList.next.time > new_object.time):
        new_object.next = headOfList.next
        headOfList.next=new_object
        return new_object

    curr = headOfList.next
    while curr.next is not None and (curr.next.date < new_object.date or (curr.next.date == new_object.date and curr.next.time <= new_object.time)):
        curr = curr.next

    new_object.next = curr.next
    curr.next = new_object
    return headOfList


# חיפוש ברשימה המקושרת
def search_linked_list(head, date, time , numFrame):
    curr = head.next  # התחל בראש הרשימה
    while curr is not None:
        if curr.date == date and curr.time == time and abs(numFrame - curr.numFrame) <= 30:
            return curr
        curr = curr.next
    return None


# חיפוש מבין האוביקטים שנמצאו בטווח הרצוי
# def find_items_in_range(headList, start_date, start_time, end_date, end_time):
#     current = headList.next
#     while current is not None:
#         if start_date <= current.date <= end_date and start_time <= current.time <= end_time:
#             # הצגת האוביקט למשתמש

#             print(f"Date: {current.date}, Time: {current.time}, NumFrame: {current.numFrame}")
#         current = current.next




# הדפסת הרשימה המקושרת
def print_LinkedListNode(videos):
    curr = videos.next
    while curr is not None:
        print(f"Date: {curr.date}, Time: {curr.time}, Value: {curr.minute}")
        curr = curr.next



