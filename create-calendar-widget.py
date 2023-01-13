from tkinter import *
from tkcalendar import Calendar

root = Tk()
root.title("Select Your Date Widget")
root.geometry("500x500")
cal = Calendar(root, selectmode='day',year=2023, month=1, day=13)
cal.pack(pady=20)

def grad_date():
	date.config(text='Selected date Is: ' + cal.get_date())
	

Button(root, text='Get Date',background="purple", foreground="white",command=grad_date).pack(pady=20)

date = Label(root, text=' ')
date.pack(pady=20)
root.mainloop()
