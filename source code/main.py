from tkinter import *
from tkinter.filedialog import askopenfilename
import os

window = Tk()

#main window for the program
window.title('Py2Exec')
window.geometry("300x140")
window.resizable(0, 0)
#config for main window
window.config(bg="black")
window.iconbitmap("icon.ico")


def folder():
    global path
    path = askopenfilename()

folderlbl=Label(window, text="Please select your desired file",bg="black", fg="cyan")
folderlbl.place(x=20,y=30)
folderbtn = Button(window, text="Select", command=folder, bg="gray", fg="cyan")
folderbtn.place(x=200, y=28)

def mainproc():
    direc = path
    os.system('cmd /c "pyinstaller --onefile {}"'.format(direc))
    window.update()

startProc = Button(window, text="Start Process", command=mainproc, bg="gray", fg="cyan")
startProc.place(x=110, y=70)

window.mainloop()