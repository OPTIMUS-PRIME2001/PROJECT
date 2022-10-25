# importing the required modules  
from tkinter import *   # importing all the modules and widgets from tkinter  
import time             # importing the time module  
  
# defining a function to display the time  
def display_time():  
    # using the strftime() method to represent current time in string  
    hour = str(time.strftime("%H"))  
    minute = str(time.strftime("%M"))  
    second = str(time.strftime("%S"))  
  
    # if the hour range between 12 to 24 and minute is greater  
    # than or equal to 0 then set the value of the meridiem_label label to PM  
    if int(hour) >= 12 and int(hour) < 24 and int (minute) >= 0:  
        meridiem_label.config(text = "PM")  
    # else set the value of the meridiem_label to AM  
    else:  
        meridiem_label.config(text = "AM")  
  
    # converting 24-hour time to 12-hour time by  
    # subtracting 12 from hours ranging from 13 to 24  
    if int(hour) > 12:  
        hour = str((int(hour) - 12))  
    # if the hour is equal to 0, setting the hour to 12  
    elif int(hour) == 0:  
        hour = str(12)  
  
    # configuring the text of the hour, minute, and second labels  
    hour_label.config(text = hour)  
    minute_label.config(text = minute)  
    second_label.config(text = second)  
    # using the after() to call the display_time() after 200 milliseconds  
    hour_label.after(200, display_time)  
  
# main function  
if __name__ == "__main__":  
    # creating an object of the Tk() class  
    gui_root = Tk()  
    # setting the title of the window  
    gui_root.title("Digital Clock - JAVATPOINT")  
    # setting the size and position of the window  
    gui_root.geometry("650x250+650+250")  
    # disabling the resizable option for better UI  
    gui_root.resizable(0, 0)  
    # configuring the background color to #2C3C3F  
    gui_root.config(bg = "#2C3C3F")
  
    # creating some frames to provide structure to other widgets  
    header_frame = Frame(gui_root, bg = "#2C3C3F")  
    body_frame = Frame(gui_root, bg = "#2C3C3F")  
  
    # using the pack() method to set the positions of the above  
    # frames on the window screen  
    header_frame.pack(pady = 15)  
    body_frame.pack()  
  
    #------------------- Header Frame -------------------------  
    # defining a label to display the heading  
    header_label = Label(  
        header_frame,  
        text = "Digital Clock",  
        font = ("consolas", "14", "bold"),  
        bg = "#2C3C3F",  
        fg = "#CAF6FF"  
        )  
    # using the pack() method to set the position of the label  
    # on the window screen  
    header_label.pack()  
  
    #------------------- Body Frame ---------------------------  
    # defining some labels to display the time in the "HH:MM:SS AM/PM" format  
    hour_label = Label(  
        body_frame,  
        text = "00",  
        font = ("Technology", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    colon_label_one = Label(  
        body_frame,  
        text = ":",  
        font = ("Technology", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    minute_label = Label(  
        body_frame,  
        text = "00",  
        font = ("Technology", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    colon_label_two = Label(  
        body_frame,  
        text = ":",  
        font = ("Technology", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    second_label = Label(  
        body_frame,  
        text = "00",  
        font = ("Technology", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    meridiem_label = Label(  
        body_frame,  
        text = "AM",  
        font = ("Technology", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
  
    # using the grid() method to set the position of the above  
    # labels in a grid form on the window screen  
    hour_label.grid(row = 0, column = 0, padx = 5, pady = 5)  
    colon_label_one.grid(row = 0, column = 1, padx = 5, pady = 5)  
    minute_label.grid(row = 0, column = 2, padx = 5, pady = 5)  
    colon_label_two.grid(row = 0, column = 3, padx = 5, pady = 5)  
    second_label.grid(row = 0, column = 4, padx = 5, pady = 5)  
    meridiem_label.grid(row = 0, column = 5, padx = 5, pady = 5)  
  
    # calling the display_time() function to display the current time  
    display_time()  
  
    # using the mainloop() method to run the application  
    gui_root.mainloop()  