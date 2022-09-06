from tkinter import *
from tkinter.filedialog import *

filename = None
WIDTH = 400
HEIGHT = 400

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END) # Where you start

    with open(filename, 'w') as f:
        f.write(t)
        f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')

    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Error", message="Unable to save file")

def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
root = Tk()
root.title("Peem")
root.minsize(width=WIDTH, height=HEIGHT)
root.maxsize(width=WIDTH, height=HEIGHT)

text = Text(root, width=WIDTH, height=HEIGHT)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar) # Nest this and turn it into a submenu

filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=openFile)
filemenu.add_command(label="Save as...", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

# TODO add >>functional<< quit functionality
# menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
