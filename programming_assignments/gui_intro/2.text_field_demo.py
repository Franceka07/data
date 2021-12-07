#!/usr/bin/env python

import tkinter as tk
import turtle

'''
https://docs.python.org/3/library/tkinter.html
https://www.tutorialspoint.com/python/tk_button.htm
https://www.geeksforgeeks.org/how-to-pass-arguments-to-tkinter-button-command/
'''


class Ui:
  def __init__(self, button_ctl = True):

    # setup new window 
    self.window = turtle.Screen() # screen

    # and create a dog
    self.dog = turtle.Turtle()
 
    # placeholder that will hold user input value
    self.user_value = tk.StringVar()

    # Setup text field, connect to the user_value variable
    self.user_input_box = tk.Entry(textvariable=self.user_value)
    self.user_input_box.pack(padx=5,side=tk.LEFT)
    self.user_input_box.focus_set()
    self.user_input_box.bind("<Return>",self.submit_handler)

    self.btn = tk.Button(text='submit', command=lambda: self.submit_handler("<Return>"))
    self.btn.pack(padx=10, pady=15, side=tk.LEFT)

    # After setup is done we
    # enter event-loop (--> react to user input in event-callbacks)
    turtle.mainloop()

  def submit_handler(self,event):
    ''' interface that demonstrates the use of the TextField variable '''
    # get value from variable that is associated with our text box
    value = self.user_input_box.get()
    # print the value to cli and to gui via dog 
    print(value)
    self.dog.clear()
    self.dog.write(value,font=('Courier', 45), align='center')

  
ui = Ui(button_ctl = True)



