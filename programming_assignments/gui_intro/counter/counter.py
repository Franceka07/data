#!/usr/bin/env python

import tkinter as tk
import turtle
import logging
import sys


class Counter:
  def __init__(self, window, seconds = 15, debug = False):
    ''' 
       parameters:
        window: this class uses turtle window that was setup externally
        seconds: by default we count down from 15
        debug: indicate if we want to see debug messages
       interface methods:
          countdown: print the counter value 1000 ms
          stop:  stop counter
          reset: reset counter
          clear: delete writing
      
    '''
    if debug == True:
        logging.basicConfig(level=logging.DEBUG)
    else: 
        logging.basicConfig(level=logging.INFO)
    logging.info('starting the counter class')

    # set seconds_default and counter values to seconds param
    self.seconds_default = seconds
    self.seconds_cnt = seconds

    # we will use the window that was created externally, window param
    self.window = window

    # turtle element for the countdown counter
    self.counter = turtle.Turtle()
    self.counter.penup()
    self.counter.hideturtle()

    # position coutner on the window
    self.counter.sety( round((-1 * self.window.window_height())/2) + 50 )
       
    # need to keep track of counter id, so we can cancel it
    self.c_id = None    

    # disabled since we are doing an import 
    # self.reset()
    # turtle.mainloop()
    

  def countdown(self):
    if self.seconds_cnt >= 0 and self.seconds_cnt <= self.seconds_default:
      self.counter.clear()
      self.counter.write(self.seconds_cnt, font=("Courier", 45), align = 'center')
      self.seconds_cnt-=1
      # https://www.pythontutorial.net/tkinter/tkinter-after/
      self.c_id = self.window.getcanvas().after(1000, self.countdown)
    else:
      # we are out of time
      self.counter.clear()
      self.counter.write('out of time', font=("Courier", 45), align = 'center')
      self.stop()

  def stop(self):
    'interface to stop timer'
    if self.c_id:
      self.window.getcanvas().after_cancel(self.c_id)
      self.c_id = None
      logging.debug('> STOP: counter has been stopped')

  def reset(self):
    'interface to reset timer'
    logging.debug('> RESET_COUNTER')
    self.stop()
    self.seconds_cnt= self.seconds_default
    self.countdown()

  def clear(self):
    'interface to clear the writing'
    logging.debug('> CLEAR')
    self.counter.clear()

