# Import the required libraries
from tkinter import *
from tkinter import ttk, filedialog
import numpy
import pandas as pd

# Create an instance of tkinter frame
win = Tk()
win.title("SunFamily")
win.configure(bg='blue')
# Set the size of the tkinter window
win.geometry("700x550")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')

# Create a Frame
frame = Frame(win)
frame.pack(pady=20)
# Define a function for opening the file
def hello():
    win.destroy()
    import step3

def open_file():
   filename = filedialog.askopenfilename(title="Open a File", filetype=(("xlsx files", ".*xlsx"),
("All Files", "*.csv")))

   if filename:
      try:
         filename = r"{}".format(filename)
         df = pd.read_csv(filename)
      except ValueError:
         label.config(text="File could not be opened")
      except FileNotFoundError:
         label.config(text="File Not Found")

   # Clear all the previous data in tree
   clear_treeview()

   # Add new data in Treeview widget
   tree["column"] = list(df.columns)
   tree["show"] = "headings"

   # For Headings iterate over the columns
   for col in tree["column"]:
      tree.heading(col, text=col)

   # Put Data in Rows
   df_rows = df.to_numpy().tolist()
   for row in df_rows:
         tree.insert("", "end", values=row)

   tree.pack()

# Clear the Treeview Widget
def clear_treeview():
   tree.delete(*tree.get_children())

# Create a Treeview widget
tree = ttk.Treeview(frame)

# Add a Menu
m = Menu(win)
win.config(menu=m)

# Add Menu Dropdown
file_menu = Menu(m, tearoff=False)
m.add_cascade(label="Browse", menu=file_menu)
file_menu.add_command(label="choose your csv file", command=open_file)

# Add a Label widget to display the file content
label = Label(win, text='')
label.pack(pady=20)
lab = Label(win, text='NOTE:- please note independent and dependent values just browse to note it otherwise you know that just continue',fg='red')
lab.pack(pady=20,)

b = Button(win,text = "continue",command=hello)  
  
b.pack()  


win.mainloop()
