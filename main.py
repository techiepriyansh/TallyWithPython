import tkinter as tk
from tkinter.constants import *
import datetime


withdraw_categories = ["DailyExpenses"]
expenditures = []
deposits = []
net_balance = 0

#Initialize Everything with Known Data---------------

with open("net_balance.txt","r") as fd:
	net_balance = int(fd.read())


#Expense Class------------------------------
class Expense(object):
	def __init__(self,amt,note,category):
		self.amt = amt
		self.datetime = datetime.datetime.now()
		self.note = note
		self.category = category

	def toString(self,net_bal):
		amt_txt = "Amount: " + str(self.amt)
		note_txt = "Note: " + self.note
		category_txt = "Category: " + self.category
		date_txt = "Date Time: " + str(self.datetime)
		net_bal_txt = "Net Balance Now: " + str(net_bal)

		to_return_txt = amt_txt + "\n" + note_txt + "\n" + category_txt + "\n" + net_bal_txt + "\n"+ date_txt + "\n" + "\n"
		return to_return_txt

#Base functions -----------------------------

def deposit(amt,note="---",category="Deposit"):
	global net_balance
	expense = Expense(amt,note,category)
	net_balance += amt
	with open("net_balance.txt","w") as fd:
		fd.write(str(net_balance))
	with open("deposits.txt","a+") as fd:
		fd.write(expense.toString(net_balance))

def expend(amt, note="---", category="DailyExpenses"):
	global net_balance
	expense = Expense(amt, note, category)
	net_balance -= amt
	with open("net_balance.txt","w") as fd:
		fd.write(str(net_balance))
	with open("expenditures.txt","a+") as fd:
		fd.write(expense.toString(net_balance))




#Tkinter Stuff -------------------------------------------


win,amt_field,note_field,category_field,win_state = None,None,None,None,None


def main_window():
	root = tk.Tk()

	tk.Label(root,text="Daily Expenses",font=("Courier",44),width=100).pack()

	btnExpend = tk.Button(root,text="Expend",font=("Courier",20),width=25,command=on_expend_clicked)
	btnExpend.pack(side = LEFT)

	btnDeposit = tk.Button(root,text="Deposit",font=("Courier",20),width=25,command=on_deposit_clicked)
	btnDeposit.pack(side = RIGHT)

	return root


def expend_window():
	root = tk.Tk()

	tk.Label(root,text="Expend",font=("Courier",25),width=10).grid(row =0,column=0)

	tk.Label(root,text="Amount",font=("Courier",20),width=10).grid(row=1,column=0)
	amt_field = tk.Entry(root,font=("Courier",20),width=25)
	amt_field.grid(row=1,column=1)

	tk.Label(root,text="Note",font=("Courier",20),width=10).grid(row=2,column=0)
	note_field = tk.Entry(root,font=("Courier",20),width=25)
	note_field.grid(row=2,column=1)


	tk.Label(root,text="Category",font=("Courier",20),width=10).grid(row=3,column=0)
	category_field = tk.Entry(root,font=("Courier",20),width=25)
	category_field.grid(row=3,column=1)

	tk.Button(root,text="Done",font=("Courier",20), command = on_expend_done).grid(row=4,column=0)

	return (root,amt_field,note_field,category_field,0)

def deposit_window():
	root = tk.Tk()

	tk.Label(root,text="Deposit",font=("Courier",25),width=10).grid(row =0,column=0)

	tk.Label(root,text="Amount",font=("Courier",20),width=10).grid(row=1,column=0)
	amt_field = tk.Entry(root,font=("Courier",20),width=25)
	amt_field.grid(row=1,column=1)

	tk.Label(root,text="Note",font=("Courier",20),width=10).grid(row=2,column=0)
	note_field = tk.Entry(root,font=("Courier",20),width=25)
	note_field.grid(row=2,column=1)


	tk.Label(root,text="Category",font=("Courier",20),width=10).grid(row=3,column=0)
	category_field = tk.Entry(root,font=("Courier",20),width=25)
	category_field.grid(row=3,column=1)

	tk.Button(root,text="Done",font=("Courier",20), command = on_deposit_done).grid(row=4,column=0)

	return (root,amt_field,note_field,category_field,1)




#Gui Helper commands ------------------------------------

#WinState: 0 for expend
#		 : 1 for deposit
def on_expend_clicked():
	mainwindow.destroy()

	global win,amt_field,note_field,category_field,win_state 
	win, amt_field, note_field, category_field, win_state = expend_window()


def on_deposit_clicked():
	mainwindow.destroy()

	global win,amt_field,note_field,category_field,win_state 
	win, amt_field, note_field, category_field, win_state = deposit_window()

def on_expend_done():
	amt = int(amt_field.get())
	note = note_field.get()
	category = category_field.get()

	expend(amt,note,category)

	win.destroy()

	global mainwindow
	mainwindow = main_window()


def on_deposit_done():
	amt = int(amt_field.get())
	note = note_field.get()
	category = category_field.get()

	deposit(amt,note,category)

	win.destroy()

	global mainwindow
	mainwindow = main_window()


#Event Sequentializer------------------------------------
mainwindow = main_window()


#Mainloop -----------------------------------
tk.mainloop()