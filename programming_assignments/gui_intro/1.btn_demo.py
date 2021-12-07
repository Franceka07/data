#!/usr/bin/env python

import tkinter as tk
import turtle
from counter import *

'''
https://docs.python.org/3/library/tkinter.html
https://www.tutorialspoint.com/python/tk_button.htm
'''


class Ui:
  def __init__(self, button_ctl = True):

    # setup new window 
    self.window = turtle.Screen() # screen

    # and create a dog
    self.dog = turtle.Turtle()
 

    # demo button control
    if button_ctl == True:
      self.btn = tk.Button(text='bark', command=self.sayit) # command specifies the function to be called on click 
      self.btn.pack(padx=10, pady=15, side=tk.LEFT)
      self.btn.config(bg='lightblue')

      self.btn2 = tk.Button(text='clear', command=self.clear)
      self.btn2.config(state = 'disabled') 
      self.btn2.pack(padx=10, pady=15, side=tk.LEFT)
      print('state',self.btn2['state'])

    else:
      self.dog.write('button control is disabled', font=('Courier', 25, 'italic'), align='center')

    # After setup is done we
    # enter event-loop (--> react to user input in event-callbacks)
    turtle.mainloop()

  def sayit(self):
    self.btn2.config(state='normal')
    self.dog.write('wolf says I am hungry', font=('Courier', 45), align='center')

  def clear(self):
    self.dog.clear()

  
ui = Ui(button_ctl = True)



