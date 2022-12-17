#tkinter final
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk


variables= dict()
records_saved=0

def on_submit():
    #confirmation it worked
    name=name_entry.get()
    #the print of confirmation
    print('Order for: ' + name)
    #making sure that the confirmation
    if name=='':
        nameWindow()
    else:
        submitWindow()
        #if
        root.destroy()
    #closing old window
    

def submitWindow():
    #setting up submit window
    subWindow = tk.Tk()
    subWindow.title('Submit Form')
    subWindow.geometry('215x100+25+0')
    subWindow.configure(background='dark blue')
    subWindow.resizable(False, False)
    
    #buttons
    exit_button= tk.Button(subWindow, text= 'Exit', command=subWindow.destroy)
    labelOne=tk.Label(subWindow, text='Thank you for ordering with us. ', bg='light blue')
    labelTwo=tk.Label(subWindow, text=' Your delicious desert will be ready soon', bg='light blue')
    output_line = tk.Label(root, text = '', anchor = 'w', justify = 'left')
    #layout
    labelOne.grid(row=1, columnspan=2)
    labelTwo.grid(row=2, columnspan=2)
    output_line.grid(row=3,column=2)
    exit_button.grid(row=4, columnspan=2)
   
def nameWindow():
    #setting up submit window
    nameWindow = tk.Tk()
    nameWindow.title('Submit Form')
    nameWindow.geometry('182x100+25+0')
    nameWindow.configure(background='dark blue')
    nameWindow.resizable(False, False)
    
    #buttons, labels and more
    exit_button= tk.Button(nameWindow, text= 'Continue', command=nameWindow.destroy)
    labelOne=tk.Label(nameWindow, text='Please enter a name for you Order', bg='light blue')
    spaceBreak = tk.Label(root, text = '', anchor = 'w', justify = 'left')
    #layout for nameWindow
    labelOne.grid(row=1, columnspan=2)
    spaceBreak.grid(row=2,column=2)
    exit_button.grid(row=3, columnspan=2)


#building the window
root = tk.Tk()
root.title("Ike's Ice Parlor")

#setting up the window
root.geometry('300x300')
root.configure(background='dark blue')
root.resizable(False, False)

#building widgets
#title widget
title = tk.Label(root, text='Select your Ice Cream', font= 'Arial 16 bold', bg = 'light blue', fg = '#FFFFFF')

#building name label and entry
name_label = tk.Label(root, text = 'Name on the order', bg='light blue', fg = '#FFFFFF')
name_entry = tk.Entry(root)

#building sundae
Sundae_txt = tk.Label(root, text = 'Sundaes', bg='light blue', fg = '#FFFFFF')
num_label = tk.Label(root, text = 'How many scoops, 1-3', bg='light blue', fg = '#FFFFFF')
options = ['1', '2', '3']
num_input = tk.Spinbox(root, from_= 0, to = 3, increment = 1)
sundae_label = tk.Label(root, text = 'Toppings for your Sundae', bg='light blue', fg = '#FFFFFF')
sundae_input = tk.Listbox(root, height = 3)
sundae_choices = ('Whip cream', 'Nuts', 'Cherry on top')
for choice in sundae_choices:
    sundae_input.insert(tk.END, choice)
    
#building shakes
shakes_txt = tk.Label(root, text = 'Shakes', bg='light blue', fg = '#FFFFFF')
shakes_label = tk.Label(root, text = 'Toppings for your shake', bg='light blue', fg = '#FFFFFF')
shakes_input = tk.Listbox(root, height = 3)
shakes_choices = ('Whip cream', 'Nuts', 'Cherry on top')
for choice in shakes_choices:
    shakes_input.insert(tk.END, choice)
#flavour drop down
shakesF_label = tk.Label(root, text = 'What flavour for your shake', bg='light blue', fg = '#FFFFFF')
flavour_values= ['Strawberry', 'Chocolate', 'Vanilla']
variables['Flavor'] = tk.StringVar()
flavour_var = tk.StringVar()
shakesF_input= ttk.Combobox(root, textvariable = flavour_var, values=flavour_values, state= 'readonly')
#size drop down
shakesS_label = tk.Label(root, text = 'What flavour for your shake', bg='light blue', fg = '#FFFFFF')
sizes_values= ['Small', 'Medium', 'Large']
variables['size'] = tk.StringVar()
sizes_var = tk.StringVar()
shakesS_input= ttk.Combobox(root, textvariable = flavour_var, values=flavour_values, state= 'readonly')

#buttons
submit_button = tk.Button(root, text = 'Submit order', command = on_submit)
exit_button = tk.Button(root, text = 'Cancel Order', command = root.destroy)

#output information
output_title = tk.Label(root, text = '', justify = 'center', bg='dark blue')
#output_line = tk.Label(root, text = '', anchor = 'w', justify = 'left', bg='dark blue')

#layout application
#general layout
title.grid(row = 0, columnspan = 4)
name_label.grid(row = 1, column = 1)
name_entry.grid(row = 1, column = 2)
#Sundae layout
Sundae_txt.grid(row = 2, columnspan = 2)
num_label.grid(row = 3, column = 1)
num_input.grid(row = 4, column = 1)
sundae_label.grid(row = 5, column = 1)
sundae_input.grid(row = 6, column = 1)
#Shake layout, drop downs 
shakes_txt.grid(row = 2, column = 2)
shakes_label.grid(row = 7, column = 2)
shakes_input.grid(row = 8, column = 2)
shakesF_label.grid(row = 3, column = 2) 
#Flavour
shakesF_input.grid(row = 4, column = 2)
shakesS_input.grid(row = 6, column = 2) 
#Size
shakesS_label.grid(row = 5, column = 2)
#buttons, submit and exit
submit_button.grid(row = 10, column = 1)
exit_button.grid(row = 10, column = 2)


root.mainloop()