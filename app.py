import tkinter as tk
from tkinter import filedialog, Text
import os




root = tk.Tk()

apps = []

def AddApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def RunApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

open_file = tk.Button(root, text="Open File", padx=10, pady=10, fg="white", bg="#263D42", command=AddApp)
open_file.pack()

runApps = tk.Button(root, text="Runn App", padx=10, pady=10, fg="white", bg="#263D42", command=RunApps)
runApps.pack()



root.mainloop()