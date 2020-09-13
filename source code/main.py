from tkinter import *
from tkinter.filedialog import askopenfilename
import os

window = Tk()

#main window for the program
window.title('Py2Exec') #title of the window.
window.geometry("300x140") #window size.
window.resizable(0, 0) #stops the user from changing the window size.
window.config(bg="black") #background color of the window.
window.iconbitmap("icon.ico") #icon to be displayed next to the title of the window.

folderlbl=Label(window, text="Please select your desired file",bg="black", fg="cyan")
folderlbl.place(x=20,y=30)
#button to select the file the user want's to convert to a .exe file.
folderbtn = Button(window, text="Select", command=folder, bg="gray", fg="cyan")
folderbtn.place(x=200, y=28)

#this is the main process used to convert the .py file to .exe file using pyinstaller.
def mainproc():
    direc = askopenfilename() #fetches the file path the user selected.
    os.system('cmd /c "pyinstaller --onefile {}"'.format(direc)) #opens a CMD window to run the pyinstaller command.
    window.update()

#the button that runs the mainproc function
startProc = Button(window, text="Start Process", command=mainproc, bg="gray", fg="cyan")
startProc.place(x=110, y=70)

window.mainloop()
