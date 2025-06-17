from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as pot

root = Tk()
root.iconbitmap("assets/logo/matplotgui.ico")
root.geometry("500x100")
root.title("MatplotGUI")
root.config(bg = "black")
root.resizable(False,False)
root.eval('tk::PlaceWindow . center')



chartype = StringVar()
title= StringVar()
label_for_x = StringVar()
label_for_y = StringVar()
t_entry = StringVar()
s_entry1 = StringVar()
s_entry2 = StringVar()

def char_creation():
    chartype1 = chartype.get()
    main_title = t_entry.get()
    x_label = s_entry1.get()
    y_label = s_entry2.get()
    try:
        xlist = [str(item.strip()) for item in x_label.split(",")]
        ylist = [int(item.strip()) for item in y_label.split(",")]
    except ValueError:
        messagebox.showerror("Input Error", "Make sure your values are comma-separated without letters in Y-axis!")
        return
    x= np.array(xlist)
    y= np.array(ylist)
    if chartype1 == 'Bar':
        pot.bar(x,y)
        pot.title(main_title)
    elif chartype1 == 'Point':
        pot.plot(x,y)
        pot.title(main_title)
    elif chartype1 == 'Pie':
        pot.pie(y, colors=xlist)
        pot.title(main_title)
    pot.show()



title1 = Label(root, textvariable=title, bg="black", fg="white",font=("Calibri", 20))
l1 = Label(root,textvariable=label_for_x, bg="black", fg="white", font=("Calibri", 20))
l2 = Label(root,textvariable=label_for_y, bg="black", fg="white", font=("Calibri", 20))
title_entry = Entry(root, textvariable=t_entry,selectbackground="Blue", selectforeground="white", font=("Calibri", 20), width= 20)
e1 = Entry(root, textvariable=s_entry1,selectbackground="Blue", selectforeground="white", font=("Calibri", 20), width= 20)
e2 = Entry(root, textvariable=s_entry2,selectbackground="Blue", selectforeground="white", font=("Calibri", 20), width= 20)
b2 = Button(root, text="Submit",activebackground="black",activeforeground="white",borderwidth=0,font=("Calibri", 20), width= 10,command=char_creation)
b2.place(x=200, y= 280, height= 40)

def default():
    root.geometry("500x100")

def settingforxy():
    root.geometry("500x350")
    title.set("Title")
    label_for_x.set("X - Axis")
    label_for_y.set("Y - Axis")
    t_entry.set("")
    s_entry1.set("")
    s_entry2.set("")
    title1.place(x=40,y=100)
    l1.place(x = 30, y=150)
    l2.place(x = 30, y=200)
    title_entry.place(x = 160, y =100)
    e1.place(x = 160, y =150)
    e2.place(x= 160,y=200 )

    
def ok():
    chrttype = chartype.get()
    if chrttype == 'Bar':
        settingforxy()
        
    elif chrttype == 'Select':
        default()
        messagebox.showerror('Error', 'Select a Valid Chart!')

    elif chrttype == 'Pie':
        root.geometry("500x350")
        title.set("Title")
        label_for_x.set("Colors")
        label_for_y.set('Variables')
        t_entry.set("")
        s_entry1.set("")
        s_entry2.set("")
        title1.place(x=40,y=100)
        l1.place(x = 20, y=150)
        l2.place(x = 20, y=200)
        title_entry.place(x = 160, y =100)
        e1.place(x = 160, y =150)
        e2.place(x= 160, y=200)
        b2.place(x=200, y= 280, height= 40)
    elif chrttype == 'Point':
        settingforxy()
    else:
        messagebox.showerror("Error","Select a Valid Chart!")

chartlabel = Label(root, text="Chart Type", bg = "black", fg="white", font=("Calibri", 20))
chartlabel.place(x=10, y = 50)
chartype.set("Select")
chart_select = ttk.Combobox(root,textvariable=chartype ,state="readonly", font=("Calibri", 15))
chart_select['values'] = ['Select',
                            'Bar',
                          'Point',
                          'Pie']
chart_select.place(x=160,y=50)
b1 = Button(root, text="OK", font=("calibri", 10), borderwidth=0, width=7, activebackground="black",activeforeground="white", command=ok)
b1.place(x=400,y=50, height=30)


root.mainloop()
