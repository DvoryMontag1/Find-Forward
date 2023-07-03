from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from tkcalendar import Calendar
from PIL import ImageTk, Image
from datetime import datetime, timedelta
import Detecting_multiple_objects_in_a_video as detect_category
import Search_in_an_index

import Previous_searches
from allResults import*


window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# window.geometry(f"{screen_width}x{screen_height}")
window.state('zoomed')

def button2_click():
    # פעולות שיקרו כשילחצו על הכפתור השני (צפיה בחיפושים אחרונים)
    print("Button 2 clicked")
    showing=SearchResultScreen()
    showing.create_screen()
    

window.title("Find Forward")

# search=searchResults()

# יצירת מסך חדש
def create_new_search():
    
    # יצירת חלון חדש
    new_screen = tk.Toplevel()
    new_screen.title("search")
    # new_screen.geometry(f"{screen_width}x{screen_height}")
    new_screen.state('zoomed')

    # יצירת מרכיבי הממשק במסך הראשי
    title_label = tk.Label(new_screen, text="Find Forward", font=("Arial", 30))
    title_label.pack(pady=20)

    
    # # יצירת התמונה
    image = tk.PhotoImage(file="Logo.png")
    img_resize = image.subsample(2, 2)
    
    # # יצירת התווית המכילה את התמונה
    image_label = tk.Label(new_screen, image=img_resize)
    image_label.place(x=1200, y=25)


    info_frame = Frame(new_screen)
    info_frame.pack(padx=5, pady=5)

    enter_info = Label(info_frame, text="Select a type of camera: ",font=("Arial", 11))
    enter_info.pack(side=LEFT)
    
    camera_options = ["Camera A", "Camera B", "Camera C"]
    camera_var = StringVar()
    camera_var.set(camera_options[0])
    camera_menu = OptionMenu(info_frame, camera_var, *camera_options)
    camera_menu.pack(side=LEFT, padx=5, pady=5)
    
    num_frame = Frame(new_screen )
    num_frame.pack(padx=5, pady=5)
    
    enter_info = Label(num_frame, text="Select a number of camera: ",font=("Arial", 11) )
    enter_info.pack(side=LEFT)
    
    num_camera = ttk.Combobox(num_frame, values=(3117,3118,3119,3120,3121) )
    num_camera.pack(padx=5, pady=5)
    
    # תאריכים
    dates = Frame(new_screen )
    dates.pack(padx=5, pady=5)
    
    # start_date= Label(dates, text="Start date for search",font=("Arial", 11) ).pack(side=LEFT,padx=5, pady=5)
    
    # שעות
    clocks = Frame(new_screen )
    clocks.pack(padx=5, pady=5)
    
    clock_info = Label(clocks, text="start time to search: ",font=("Arial", 11) )
    clock_info.pack(side=LEFT)
    
    clock1 = ttk.Combobox(clocks,
                              values=("00:00","01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00",
                                      "11:00", "12:00",
                                      "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",
                                      "22:00", "23:00"))
    clock1.pack(side=LEFT,padx=5, pady=5)
    
    # end_date= Label(dates, text="end date for search",font=("Arial", 11) ).pack(side=LEFT,padx=5, pady=5)

    # לוחות שנה
    calenders = Frame(new_screen )
    calenders.pack(padx=5, pady=5)
    
    cal1 = Calendar(calenders)
    cal1.pack(side=LEFT, padx=5, pady=5)
    
    clock_info = Label(clocks, text="end time to search: ",font=("Arial", 11) )
    clock_info.pack(side=LEFT)
    
    clock2 = ttk.Combobox(clocks,
                              values=("00:00","01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00",
                                      "11:00", "12:00",
                                      "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",
                                      "22:00", "23:00"))
    clock2.pack(side=LEFT,padx=5, pady=5)
    
    cal2 = Calendar(calenders)
    cal2.pack(side=LEFT,padx=5, pady=5)

    # def handle_radio_selection():
    #     selected_option = search_var.get()
    #     if selected_option == "image":
    #         # label.config(text="Selected: Upload an image")
    #         # הצגת הווידג'טים הרלוונטיים להעלאת תמונה והסתרת הווידג'טים הרלוונטיים להגדרת אובייקט
    #         object_entries_frame.pack_forget()
    #         load_button.pack(padx=5, pady=5)
    #         image_frame.pack(padx=5, pady=5)     

    #     elif selected_option == "object":
    #         # label.config(text="Selected: Define an object")
    #         # הצגת הווידג'טים הרלוונטיים להגדרת אובייקט והסתרת הווידג'טים הרלוונטיים להעלאת תמונה
    #         start_button.pack_forget()
    #         load_button.pack_forget()
    #         image_frame.pack_forget()
    #         object_entries_frame.pack( padx=5, pady=5)
    #         start_button.pack(padx=5, pady=5)
    
    
    # search_frame = Frame(new_screen )
    # search_frame.pack(padx=5, pady=5)
    
    # search_type = Label(search_frame, text="Select the search type: ",font=("Arial", 11) )
    # search_type.pack(side=LEFT)
    
    # search_var = StringVar()
    # search_var.set("image")
    # search_image = Radiobutton(search_frame, text="Upload an image",font=("Arial", 11) , variable=search_var, value="image",command=handle_radio_selection)
    # search_image.pack(side=LEFT, padx=5, pady=5)
    
    # search_object = Radiobutton(search_frame, text="Define an object",font=("Arial", 11) , variable=search_var, value="object",command=handle_radio_selection)
    # search_object.pack(side=LEFT, padx=5, pady=5)
    
    class_id=None
    def load_image():
        file_path = filedialog.askopenfilename(parent=new_screen)
        if file_path:
            # עדכון במשתנה הגלובלי
            Previous_searches.global_variable.pathImage=file_path
            image = Image.open(file_path)
            image.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(image)
            image_label.configure(image=photo)
            image_label.image = photo
            start_button.pack(padx=5, pady=5)

            # זהוי הקטגוריה לחיפוש
            global class_id
            class_id= detect_category.Identify_the_category_to_search_for(file_path)
           
    
    load_button = Button(new_screen, text="Load Image",font=("Arial", 11) , command=load_image)
    load_button.pack()
    
    image_frame = Frame(new_screen )
    image_frame.pack()
    
    image_label = Label(image_frame , width=200, height=200, relief="flat")
    image_label.pack()

    

    # הגדרת החפץ

    # object_entries_frame = Frame(new_screen)

    # property_labels = ["Name of the object:", "Color of the object:", "General description:"]
    # property_entries = []

    # for label_text in property_labels:
    #     label = Label(object_entries_frame, text=label_text,font=("Arial", 11))
    #     label.pack(side=LEFT, padx=5, pady=5)

    #     entry = Entry(object_entries_frame)
    #     entry.pack(side=LEFT, padx=5, pady=5)

    #     property_entries.append(entry)

    
    
    def start_search():
        if len(camera_var.get()) < 1 or len(num_camera.get()) < 1 or len(cal1.get_date()) < 1 or len(clock1.get()) < 1 or len(cal2.get_date()) < 1 or len(clock2.get()) < 1 :
        # אתה חייב להכניס את כל הפרטים
            tk.messagebox.showerror(
                title="ERROR!!!", message="You MUST enter all details",parent=new_screen
            )

        # elif search_var.get() == "object":
        #     if property_entries[0].get()=="":
        #     # אתה חייב להכניס את כל הפרטים
        #         tk.messagebox.showerror(
        #             title="ERROR!!!", message="You MUST enter object's name",parent=new_screen
        #         )
        else:
            # selected_camera = camera_var.get()
            # selected_num_camera = num_camera.get()
            selected_start_date_str = cal1.get_date()
            selected_start_date = datetime.strptime(selected_start_date_str, "%m/%d/%y").date()
            selected_start_time_str = clock1.get()
            selected_start_time = selected_start_time_str.replace(":", "-")
        
            selected_end_date_str = cal2.get_date()
            selected_end_date = datetime.strptime(selected_end_date_str, "%m/%d/%y").date()
            selected_end_time_str = clock2.get()
            selected_end_time = selected_end_time_str.replace(":", "-")
        
        
            # selected_search_type = search_var.get()
            formatted_start_date = selected_start_date.strftime("%d-%m-%Y")
            formatted_end_date = selected_end_date.strftime("%d-%m-%Y")

            # שמירת הפרטים במשנה הגלובלי
            Previous_searches.global_variable.date = datetime.today().date().strftime("%d-%m-%Y")
            Previous_searches.global_variable.camera=camera_var.get()
            Previous_searches.global_variable.numCamera=num_camera.get()
            Previous_searches.global_variable.TimeRangeStart=formatted_start_date+" at "+ clock1.get()
            Previous_searches.global_variable.TimeRangeEnd=formatted_end_date+" at "+clock2.get()
            global class_id
            # קריאה לפונקציה העוברת על עץ אינדקס
            Search_in_an_index.check_in_index(formatted_start_date,selected_start_time,formatted_end_date,selected_end_time,class_id)
         
    
        # Pass the selected data to the server for processing
        # You can replace the print statements with the code to send the data to the server
    
    
    start_button = Button(new_screen, text="Start the search",font=("Arial", 11) , command=start_search)
    start_button.pack(pady=10)


# יצירת מרכיבי הממשק במסך הראשי
title_label = tk.Label(window, text="Find Forward", font=("Arial", 60))
title_label.pack(pady=50)


# # # יצירת התמונה
image = tk.PhotoImage(file="Logo.png")
img_resize = image.subsample(2, 2)
# # יצירת התווית המכילה את התמונה
image_label = tk.Label(window, image=img_resize)
image_label.place(x=1200, y=25)


button_search = tk.Button(window, text="new search", width=10, height=2, bd=3, relief=tk.RAISED, bg="white", command=create_new_search, font=("Arial", 18))
button_search.pack(pady=10)

button_view = tk.Button(window, text="View previous searches",width=20, height=2, bd=3, relief=tk.RAISED, bg="white", command=button2_click, font=("Arial", 18))
button_view.pack(pady=10)

window.mainloop()
