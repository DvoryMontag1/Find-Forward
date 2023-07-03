import tkinter as tk
from PIL import ImageTk, Image
import Previous_searches
import webbrowser


class SearchResultScreen:
    def __init__(self):
        # self.root = root
        # self.search_results = search_results
        # self.create_screen()

        self.root =  tk.Tk()
        self.root.state('zoomed') 
        self.objects = Previous_searches.get_all_searches()
        # self.create_screen()


    
    # search_result_screen = SearchResultScreen(root, objects)

    def create_screen(self):
        # יצירת מרכיבי הממשק במסך התוצאות
        title_label = tk.Label(self.root, text="Search Results", font=("Arial", 24))
        title_label.pack(pady=20)

        # יצירת פריים
        frame_width = int(self.root.winfo_screenwidth() * 0.5)  # רוחב הפריים יהיה 50% מרוחב המסך
        frame_height = self.root.winfo_screenheight()  # גובה הפריים יהיה כמו גובה המסך
        frame = tk.Frame(self.root, width=frame_width, height=frame_height, bg="blue")
        # frame.pack(side=tk.RIGHT)

        for result in self.objects:
            # יצירת מלבן עבור כל תוצאה

            result_frame = tk.Frame(self.root, borderwidth=2, relief="solid", bg="lightgray" )
            result_frame.pack(pady=7, padx=10, ipadx=100, ipady=8)
            
            date_label = tk.Label(result_frame, text=result.date, font=("Arial", 16), bg="lightgray", fg="black")
            date_label.pack(pady=10, padx=10, ipadx=20, ipady=10,side="right")
            
            view_button = tk.Button(result_frame, text="View", command=lambda r=result: self.show_details(r), font=("Arial", 14), bg="#800020",bd=3, fg="white")
            view_button.pack(pady=(30, 20))
            


    def play_video(self, result):
        video_path = result.pathVideo
        webbrowser.open(video_path)
            

    def show_details(self, result):
        # יצירת מסך פרטי התוצאה
        details_screen = tk.Toplevel()

        details_screen.geometry("700x500+100+100")

        title_label = tk.Label(details_screen, text="Search details", font=("Arial", 20))
        title_label.pack(pady=20)

        # תיאור
        description_label = tk.Label(details_screen,font=("Arial", 13) , text=f"The search inside {result.camera} number {result.numCamera}")
        description_label.pack()

        # תיאור
        description_label = tk.Label(details_screen,font=("Arial", 13) , text=f"The time range in which they searched: from {result.TimeRangeStart} until {result.TimeRangeEnd}" )
        description_label.pack()

        # תיאור
        description_label = tk.Label(details_screen, text="the object they were looking for")
        description_label.pack()

        # תמונה
        print(result.pathImage)

        image = Image.open(result.pathImage)
        image = image.resize((200, 200))  # גודל התמונה
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(details_screen, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)

        # תיאור
        description_label = tk.Label(details_screen,font=("Arial", 13), text=f"The object is in motion on {result.Bargain_time}")
        description_label.pack()
     
        # כפתור צפייה בסרטון
        play_button = tk.Button(details_screen, text="to watch the video",font=("Arial", 14,"bold"),width=20, height=2,bd=3,fg="#800020", command=lambda r=result:  self.play_video(r))
        play_button.pack(pady=10)