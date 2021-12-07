#!/usr/bin/env python

import tkinter as tk
import turtle
import logging
from counter import *



class Ui:
  def __init__(self, button_ctl = True, seconds = 9, debug = False):

    # change parameter to logging.DEBUG to see debug messages
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else: 
        logging.basicConfig(level=logging.INFO)
    logging.info('starting the counter class')


    # setup new window 
    self.window = turtle.Screen() # screen

    # use the counter class
    self.counter = Counter(self.window, seconds = seconds)

    self.problem = turtle.Turtle()

    # demo button control
    if button_ctl == True:
      self.btn = tk.Button(text='reset counter', command=self.cnt_reset) # command indicates what function to call on click
      self.btn.pack(padx=10, pady=15, side=tk.LEFT)
      self.btn.config(bg='lightblue')

      self.btn2 = tk.Button(text='stop counter', command=self.counter.stop, state = 'disabled') 
      self.btn2.pack(padx=10, pady=15, side=tk.LEFT)
      print('state',self.btn2['state'])

    else:
      self.counter.reset()

    # After setup is done we
    # enter event-loop (--> react to user input in event-callbacks)
    turtle.mainloop()

  def cnt_reset(self):
    self.btn2.config(state='normal')
    self.counter.reset()

   

ui = Ui(button_ctl = True, seconds = 20) # ( button_ctl = True, seconds = 9, debug = False):



