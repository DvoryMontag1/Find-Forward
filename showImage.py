import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt



window2=None
found=False

def handle_yes():
    global found
    window2.destroy()
    plt.close()
    found=True
    # print("Yes button clicked")
    

def handle_no():
    global found
    # print("No button clicked")
    window2.destroy()
    plt.close()
    found=False

def show(image):
    global window2


    # יצירת חלון של Tkinter
    window2 = tk.Tk()
    window2.title("Image Display")
        
    
    text_label = tk.Label(window2, text="do you mean it?", font=("Arial", 14))
    text_label.pack(pady=10)
    
    # הוספת הכפתורים
    buttons_frame = tk.Frame(window2)
    buttons_frame.pack(pady=10)
    
    yes_button = tk.Button(buttons_frame, text="Yes", command=handle_yes)
    yes_button.pack(side="left", padx=10)
    
    no_button = tk.Button(buttons_frame, text="No", command=handle_no)
    no_button.pack(side="left", padx=10)
    
    # יצירת חלון נוסף להצגת התמונה בMatplotlib
    fig, ax = plt.subplots()
    ax.imshow(image)
    plt.show()

    return found
    