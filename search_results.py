
import tkinter as tk
import pygame
import os
import moviepy.editor as mp

import Previous_searches
import Single_object_tracking
# import first


class search_results():
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("FINDFORWARD")

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.state('zoomed') 
        self.frame_width = int(self.screen_width * 0.5)  # 50% of the screen width
        self.frame_height = int(self.screen_height * 0.5)  # 50% of the screen height
        self.video_path=None
        self.date=None
        self.time=None

    def play_video(self):
        resized_video = mp.VideoFileClip(self.video_path).resize(width=self.frame_width , height=self.frame_height)
        resized_video.preview()
        resized_video.close()

    def save_results(self):
        #משנה את שם הסרטון 
        time=self.time.replace(":", "-")
        directory, filename = os.path.split(self.video_path)
        new_filename = os.path.join(directory, self.date+"_"+time+".mp4")
        os.rename(self.video_path, new_filename)
        # עדכון במשתנה המכיל את פרטי החיפוש
        Previous_searches.global_variable.pathVideo=new_filename
        Previous_searches.global_variable.Bargain_time=self.date+" at hour "+self.time
        Previous_searches.add_search_result(Previous_searches.global_variable)
        print("Results saved.")
        Single_object_tracking.global_finish=True
        # סגירת הסרטון
        pygame.quit()
        # סגירת המסכים
        self.root.destroy()
        self.root.quit()  # יוצאים מהלולאה הראשית של `mainloop()`
        return Single_object_tracking.global_finish

    def continue_search(self):
        print("Continuing search.")
        Single_object_tracking.global_finish=False
        self.root.destroy()
        # סגירת הסרטון
        pygame.quit()
        # מחיקת הסרטון הזמני
        os.remove(self.video_path)
        self.root.quit()  # יוצאים מהלולאה הראשית של `mainloop()`
        return Single_object_tracking.global_finish

    def display_screen(self,date, start_time, end_time, video_path):
        
        # יצירת מרכיבי הממשק במסך הראשי
        self.video_path=video_path
        self.date=date
        self.time=start_time
        title_label = tk.Label(self.root, text="Find Forward-search results", font=("Arial", 30))
        title_label.pack(pady=20)

        main_frame = tk.Frame(self.root, width=self.frame_width, height=self.frame_height)
        main_frame.pack(pady=20)

        label_text = f"It is found on {date} from {start_time} to {end_time}"


        label = tk.Label(main_frame, text=label_text, font=("Arial", 14))
        label.pack(pady=10)

        video_frame = tk.Frame(main_frame, width=self.frame_width , height=self.frame_height , bg="#000000")
        video_frame.pack(pady=20)

        button_frame = tk.Frame(main_frame, width=self.frame_width, height=50)
        button_frame.pack()

        button1 = tk.Button(button_frame, text="Save Results",width=20, height=2,bd=3,bg="white", command=self.save_results, font=("Arial", 12),fg="#800020")
        button1.pack(side="left", padx=10)

        button2 = tk.Button(button_frame, text="Insufficient Information, Continue Search",width=34, height=2,bd=3,bg="white", command=self.continue_search, font=("Arial", 12),fg="#800020")
        button2.pack(side="left", padx=10)

     
        play_button = tk.Button(video_frame, text="Play Video", command=self.play_video, font=("Arial", 14),fg="red",bg="#000000")
        play_button.place(relx=0.5, rely=0.5, anchor="center")  # שימוש ב-place עם הפרמטרים המתאימים