import tkinter as tk
from tkinter import *
import speedtest
import threading

def speedcheck():
    try:
        sp = speedtest.Speedtest()
        sp.get_servers()
        down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
        up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
        lab_Dowm.config(text=down)
        lab_up.config(text=up)
    except Exception as e:
        lab_Dowm.config(text="error")
        lab_up.config(text="error")
        print("Error:", e)

def start_speedcheck():
    thread = threading.Thread(target=speedcheck)
    thread.start()

sp = Tk()
sp.title("Internet Speed Tester")
sp.geometry("500x600")
sp.config(bg="green")

lab = Label(sp, text="Internet Speed Tester", font=("Times New Roman", 30, "bold"), bg="green", fg="black")
lab.place(x=50, y=40, height=50, width=400)

lab = Label(sp, text="Downloading speed", font=("Times New Roman", 20, "bold"), bg="green", fg="black")
lab.place(x=50, y=150, height=50, width=400)

lab_Dowm = Label(sp, text="00", font=("Times New Roman", 20, "bold"), bg="green", fg="black")
lab_Dowm.place(x=50, y=220, height=50, width=400)

lab = Label(sp, text="Uploading speed", font=("Times New Roman", 20, "bold"), bg="green", fg="black")
lab.place(x=50, y=300, height=50, width=400)

lab_up = Label(sp, text="00", font=("Times New Roman", 20, "bold"), bg="green", fg="black")
lab_up.place(x=50, y=380, height=50, width=400)

button = Button(sp, text="Check speed", font=("Times New Roman", 20, "bold"), bg="red", fg="black", relief=RAISED, command=start_speedcheck)
button.place(x=50, y=480, height=50, width=400)

sp.mainloop()

