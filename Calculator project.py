'''
env python3
Created on Tue Oct 27 2020
@author: Ganesh Thorat
-*-coding: utf-8 -*-
'''

import tkinter as tk
from tkinter import messagebox

expression=''

def click(num):
	
	global expression
	expression+=str(num)
	equation.set(expression)
	
def sol():
	global expression
	try:
		
		total=eval(expression)
		
		equation.set('Ans:            '+str(total))
		expression=''
	except:
		
		equation.set('ERROR')
		expression=''
		
def ac():
	global expression
	expression=''
	equation.set('')
	
	
	
def cr():
	global expression
	expression=expression[:-1]
	equation.set(expression)
	
	
def close():
	msgb=messagebox.askyesno('Exit','Do you really want to close')
	if msgb==True:
		window.destroy()
	


if __name__=='__main__':
	window=tk.Tk()
	window.title('Calculator')
	window.geometry('320x474')
	window.configure(bg='black')
	
	
	
	
	equation=tk.StringVar()
	e=tk.Entry(window,textvariable=equation,state='disabled',selectborderwidth=10,justify='right',relief='sunken',bg='white',fg='black',font=('aerial bold',20))
	

	e.place(x=0,y=0,height=100,width=320)
	equation.set(0)
	
	fram=tk.Frame(window)
	fram.place(x=0,y=100)
	
	butac=tk.Button(fram,text='AC', fg='black',bg='white',width=4,height=1,relief='sunken',bd=5,activeforeground='red',font=('aerial bold',20),command=lambda: ac())
	butac.grid(row=5,column=0)
	
	
	
	butc=tk.Button(fram,text='x', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:cr())
	butc.grid(row=5,column=1,columnspan=1)
	

	
	butdiv=tk.Button(fram,text='/', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click('/'))
	butdiv.grid(row=5,column=2)
	
	
	butmul=tk.Button(fram,text='*', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click('*'))
	butmul.grid(row=5,column=3)
	
	leftbrack=tk.Button(fram,text='(', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click('('))
	leftbrack.grid(row=6,column=0)

	rightbrack=tk.Button(fram,text=')', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click(')'))
	rightbrack.grid(row=6,column=1)
	
	sqrt_=tk.Button(fram,text='x'+str(u'\u00B9')+str(u'\u002F')+str(u'\u2082'), fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click('**(1/2)'))
	sqrt_.grid(row=6,column=2)

	sqr_=tk.Button(fram,text='X'+str(u'\u00B2'), fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click('**2'))
	sqr_.grid(row=6,column=3)



	but7=tk.Button(fram,text='7', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda: click(7))
	but7.grid(row=7,column=0)
	
	
	
	but8=tk.Button(fram,text='8', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click(8))
	but8.grid(row=7,column=1)
	
	
	
	
	but9=tk.Button(fram,text='9', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click(9))
	but9.grid(row=7,column=2)
	
	
	butminus=tk.Button(fram,text='-', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click('-'))
	butminus.grid(row=7,column=3)
	
	
	but4=tk.Button(fram,text='4', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click(4))
	but4.grid(row=8,column=0)
	
	
	
	
	but5=tk.Button(fram,text='5', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click(5))
	but5.grid(row=8,column=1)
	
	
	
	but6=tk.Button(fram,text='6', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click(6))
	but6.grid(row=8,column=2)
	
	
	
	butplus=tk.Button(fram,text='+', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click('+'))
	butplus.grid(row=8,column=3)
	
	
	
	but1=tk.Button(fram,text='1', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click(1))
	but1.grid(row=9,column=0)
	
	
	
	
	but2=tk.Button(fram,text='2', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click(2))
	but2.grid(row=9,column=1)
	
	
	
	but3=tk.Button(fram,text='3', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click(3))
	but3.grid(row=9,column=2)
	
	
	butequal=tk.Button(fram,text='=', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:sol())
	butequal.grid(row=9,column=3)
	
	
	
	butperc=tk.Button(fram,text='%', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click('*0.01'))
	butperc.grid(row=10,column=0)
	
	
	
	
	but0=tk.Button(fram,text='0', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click(0))
	but0.grid(row=10,column=1)
	
	
	butpoint=tk.Button(fram,text='.', fg='black',bg='white',width=4,height=1,activeforeground='red',relief='sunken',bd=5,font=('aerial bold',20),command=lambda:click('.'))
	butpoint.grid(row=10,column=2)
	
	
	
	butclose=tk.Button(fram,text='CLOSE', fg='black',bg='white',width=4,height=1,relief='sunken',bd=5,activeforeground='red',font=('aerial bold',8),command=lambda:close())
	butclose.flash()
	butclose.grid(row=10,column=3,ipadx=19,ipady=15)
	
window.mainloop()