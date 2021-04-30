from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkfont

name = ""
x=16
boldset=0
itaset=0


master = Tk()
master.title(name + "untitled - Editor")
master.geometry("1000x640")

top = Frame(master)
bottom = Frame(master)
top.pack(side=TOP)
bottom.pack(side=TOP)

def colour(just):
    color = var.get()
    siz = var1.get()
    bo = var2.get()
    type1 = var3.get()
    master.clipboard_clear()
    text['fg'] = color
    if boldset==1:
    	if itaset==1:
    		text.config(font=(type1, siz, "bold italic"))
    	else:
    		text.config(font=(type1, siz, "bold"))
    else:
    	if itaset==1:
    		text.config(font=(type1, siz, "italic"))
    	else:
    		text.config(font=(type1, siz))


var = StringVar(master)
var.set('black')
choices = ['red', 'green', 'blue', 'yellow', 'white', 'magenta', 'orange', 'black', 'cyan', 'pink', 'brown']
option = OptionMenu(master, var, *choices, command=colour)
option.pack(in_=top, side=LEFT)


def font_type(just):
    color = var.get()
    siz = var1.get()
    bo = var2.get()
    type1 = var3.get() 
    text['fg'] = color
    if boldset==1:
    	if itaset==1:
    		text.config(font=(type1, siz, "bold italic"))
    	else:
    		text.config(font=(type1, siz, "bold"))
    else:
    	if itaset==1:
    		text.config(font=(type1, siz, "italic"))
    	else:
    		text.config(font=(type1, siz))


var3 = StringVar(master)
var3.set('Arial')
choices = ['Times', 'Arial', 'Comic Sans MS', 'Helvetica', 'Arial Black', 'Verdana', 'Algerian', 'Gill Sans Ultra Bold', 'Goudy Stout', 'Jokerman', 'Lucida Handwriting', 'Magneto', 'Monotype corsiva', 'Txt']
option = OptionMenu(master, var3, *choices, command=font_type)
option.pack(in_=top, side=LEFT)


def size(just):
    color = var.get()
    siz = var1.get()
    bo = var2.get()
    type1 = var3.get()
    text['fg'] = color
    if boldset==1:
    	if itaset==1:
    		text.config(font=(type1, siz, "bold italic"))
    	else:
    		text.config(font=(type1, siz, "bold"))
    else:
    	if itaset==1:
    		text.config(font=(type1, siz, "italic"))
    	else:
    		text.config(font=(type1, siz))




var1 = StringVar(master)
var1.set('16')
choices = ['6', '8', '10', '12', '14', '16', '18','20', '22', '24', '26', '28', '30']
option = OptionMenu(master, var1, *choices, command=size)
option.pack(in_=top, side=LEFT)


def bold():
	color = var.get()
	siz = var1.get()
	type1 = var3.get()
	text['fg'] = color
	global boldset
	global itaset
	if boldset!=1:
		boldset = 1
		text['fg'] = color
		if itaset==1:
			text.config(font=(type1, siz, "bold italic"))
			button.config(bg = "grey")
		else:
			text.config(font=(type1, siz, "bold"))
			button.config(bg = "grey")
	elif boldset==1:
		boldset = 0
		text['fg'] = color
		if itaset==1:
			text.config(font=(type1, siz, "italic"))
			button.config(bg = "lightgrey")
		else:
			text.config(font=(type1, siz))
			button.config(bg = "lightgrey")


def bolde(event):
	color = var.get()
	siz = var1.get()
	type1 = var3.get()
	text['fg'] = color
	global boldset
	global itaset
	if boldset!=1:
		boldset = 1
		text['fg'] = color
		if itaset==1:
			text.config(font=(type1, siz, "bold italic"))
			button.config(bg = "grey")
		else:
			text.config(font=(type1, siz, "bold"))
			button.config(bg = "grey")
	elif boldset==1:
		boldset = 0
		text['fg'] = color
		if itaset==1:
			text.config(font=(type1, siz, "italic"))
			button.config(bg = "lightgrey")
		else:
			text.config(font=(type1, siz))
			button.config(bg = "lightgrey")



var2 = StringVar(master)
var2.set('0')
button = Button(master, text="B", command=bold, padx=10)
button.pack(in_=top, side=LEFT)



def italic():
	color = var.get()
	siz = var1.get()
	type1 = var3.get()
	text['fg'] = color
	global boldset
	global itaset
	if itaset!=1:
		itaset = 1
		text['fg'] = color
		if boldset==1:
			text.config(font=(type1, siz, "bold italic"))
			button1.config(bg = "grey")
		else:
			text.config(font=(type1, siz, "italic"))
			button1.config(bg = "grey")
	elif itaset==1:
		itaset = 0
		text['fg'] = color
		if boldset==1:
			text.config(font=(type1, siz, "bold"))
			button1.config(bg = "lightgrey")
		else:
			text.config(font=(type1, siz))
			button1.config(bg = "lightgrey")
		

def italice(event):
	color = var.get()
	siz = var1.get()
	type1 = var3.get()
	text['fg'] = color
	global boldset
	global itaset
	if itaset!=1:
		itaset = 1
		text['fg'] = color
		if boldset==1:
			text.config(font=(type1, siz, "bold italic"))
			button1.config(bg = "grey")
		else:
			text.config(font=(type1, siz, "italic"))
			button1.config(bg = "grey")
	elif itaset==1:
		itaset = 0
		text['fg'] = color
		if boldset==1:
			text.config(font=(type1, siz, "bold"))
			button1.config(bg = "lightgrey")
		else:
			text.config(font=(type1, siz))
			button1.config(bg = "lightgrey")
	

var4 = StringVar(master)
var4.set('0')
button1 = Button(master, text="I", command=italic, padx=10)
button1.pack(in_=top, side=LEFT)



text = Text(master, width=400, height=300, font=("Arial", 16), highlightthickness=0, bd=2, bg="lightgrey", fg="black")
text.pack()


def new():
	global name
	name = "untitled"
	ans = messagebox.askquestion(title="Save File", message="Want to save current file?")
	if ans is True:
		save()
	delete_all()

def newe(event):
	global name
	name = "untitled"
	ans = messagebox.askquestion(title="Save File", message="Want to save current file?")
	if ans is True:
		save()
	delete_all()


def open_file():
	ans = messagebox.askquestion(title="Save File", message="Want to save current file?")
	if ans is True:
		save()
	delete_all()
	file = filedialog.askopenfilename()
	global name
	name = file
	master.title(name + " - Editor")
	f = open(file)
	if file!=None:
		contents = f.read()
		text.insert(INSERT, contents)
		f.close()

def open_filee(event):
	ans = messagebox.askquestion(title="Save File", message="Want to save current file?")
	if ans is True:
		save()
	delete_all()
	file = filedialog.askopenfilename()
	global name
	name = file
	master.title(name + " - Editor")
	f = open(file)
	if file!=None:
		contents = f.read()
		text.insert(INSERT, contents)
		f.close()

def save():
	global name
	if name=="":
		f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
		for i in range(25,60):
			if str(f)[i]!='\'':
				name=name+str(f)[i]
			else:
				break
		master.title(name + " -Editor")
		if f is None:
			return
	else:
		f = open(name, "w")
		master.title(name + " - Editor")
	text2save = str(text.get(1.0, END))
	f.write(text2save)
	f.close() 

def savee(event):
	global name
	if name=="":
		f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
		for i in range(25,60):
			if str(f)[i]!='\'':
				name=name+str(f)[i]
			else:
				break
		master.title(name + " -Editor")
		if f is None:
			return
	else:
		f = open(name, "w")
		master.title(name + " - Editor")
	text2save = str(text.get(1.0, END))
	f.write(text2save)
	f.close() 

def close():
	save()
	master.quit()

def closee(event):
	save()
	master.quit()

def cut():
	master.clipboard_clear()
	text.clipboard_append(string=text.selection_get())
	text.delete(index1=SEL_FIRST, index2=SEL_LAST)

def copy():
	master.clipboard_clear()
	text.clipboard_append(string=text.selection_get())

def paste():
	text.insert(INSERT, master.clipboard_get())

def delete():
	text.delete(index1=SEL_FIRST, index2=SEL_LAST)

def select_all():
	text.tag_add(SEL, "1.0", END)

def select_alle(event):
	text.tag_add(SEL, "1.0", END)

def delete_all():
	text.delete(1.0, END)



menu = Menu(master)
master.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new, accelerator="ctrl+n")
file_menu.add_command(label="Open", command=open_file, accelerator="ctrl+o")
file_menu.add_separator()
file_menu.add_command(label="Save", command=save, accelerator="ctrl+s")
file_menu.add_command(label="Close", command=close, accelerator="ctrl+q")

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text.edit_undo, accelerator="ctrl+z")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut, accelerator="ctrl+x")
edit_menu.add_command(label="Copy", command=copy, accelerator="ctrl+c")
edit_menu.add_command(label="Paste", command=paste, accelerator="ctrl+z")
edit_menu.add_command(label="Delete", command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all, accelerator="ctrl+a")



master.bind_all('<Control-Key-o>', open_filee)
master.bind_all('<Control-Key-n>', newe)
master.bind_all('<Control-Key-s>', savee)
master.bind_all('<Control-Key-q>', closee)
master.bind_all('<Control-Key-a>', select_alle)
master.bind_all('<Control-Key-b>', bolde)
master.bind_all('<Control-Key-i>', italice)


master.mainloop()
