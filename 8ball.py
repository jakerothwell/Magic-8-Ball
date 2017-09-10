import time
from random import randint
from Tkinter import *

responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
"As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not to tell you", "Cannot predict now", "Concentrate and ask again", "Dont count on it", "My reply is no"
, "My sources say no", "Fuck off", "Very doubtful"]

master = Tk()
master.title("Magic 8 Ball")
Label(master, text="Question:").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
var = StringVar()


def start():
	
	var.set("Ask the Magic 8 Ball a question!")
	label = Label(master, textvariable = var)
	label.grid(row=5)


def updatetext(input):
	
	var.set(input)
	master.update_idletasks()


def question_entry():

	qstn = e1.get()
	e1.delete(0, END)
	
	if qstn == '':
		
		master.after(1000, updatetext("Please ask a valid question."))
		start()
	
	else:
	
		master.after(1000,updatetext("You asked: "+ qstn))
		question()

def question():

	chosen = randint(0, 19)
	output_list = ["Thinking", "Thinking.", "Thinking..", "Thinking...", "The Magic 8 Ball has spoken: " + responses[chosen], "Would you like to play again?"]
	
	
	for x in range (0, 7):
		if x == 4:
			master.after(3000, updatetext(output_list[x]))
			print(var.get())

		else:
			master.after(1000, updatetext(output_list[x]))
			print(var.get())

def clear_text():
	e1.delete(0,END)

Button(master, text='Ask', command=question_entry).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Clear', command=clear_text).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Play again', command=start).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=4, column=1, sticky=W, pady=4)

start()
master.mainloop()