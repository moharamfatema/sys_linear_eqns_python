import json
from operator import eq
from turtle import color
import pandas as pd
import numpy as np
from math import exp
import os
import sys

from sympy.core import symbol
import parse
import tkinter as tk
from tkinter import E, filedialog
from tkinter import messagebox


EQUATIONS = []

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def string_entered(exp_entry):
    try:
        if exp_entry.get()[-1] == "(":
            exp_entry.insert(exp_entry.index(tk.INSERT), ")")
            exp_entry.icursor(exp_entry.index(tk.INSERT) - 1)
    except IndexError:
        pass

def destroyer(root):
    if messagebox.askquestion("Quit", "Are you sure you want to quit?") == "yes":
        root.quit()
        root.destroy()
        sys.exit()

def method_change(all_widgets, method_name, methods_list):
    # receive list of widgets and the method name chosen
    # remove visible widgets from grid
    # if name is bisection or regula falsi: show widgets for lowerbound and upperbound
    # if name is newton raphson or fixed point: show widgets for initial guess
    # if name is secant: show widgets for first guess and second guess
    # Extra: for fixed point and secant, specify that user enters g(x), f(x) otherwise


    for widget in all_widgets:
        widget.grid_remove()
    
    if method_name == methods_list[0] or method_name == methods_list[4]:
        all_widgets[0].grid(column=0, row=6, sticky=tk.W)
        all_widgets[2].grid(column=1, row=6, sticky=tk.W)

        all_widgets[1].grid(column=0, row=7, sticky=tk.W, pady=(0, 5))
        all_widgets[3].grid(column=1, row=7, sticky=tk.W, pady=(0, 5))

def choose_file(exp_entry, out):
    filename = filedialog.askopenfilename(initialdir="", title="Choose a file", filetypes=(("Text files", "*.txt"), ("JSON files", "*.json"), ("All files", "*.*")))
    if filename.endswith('.txt'):
        try:
            dict = parse.dict_from_file(filename)
            calc(input_list=None, out=out, vars=dict, filename=filename)
        except FileNotFoundError as e:
            update_output(out, e, color="red")
    else:
        update_output(out, "Not a valid file!", color="red")   

def update_output(output, text, color="black", append=False):
    output.configure(state='normal', foreground=color)
    if append:
        output.insert(tk.END, text)
    else:
        output.delete("1.0", tk.END)
        output.insert('1.0', text)
    output.configure(state='disabled')

def confirm(numofeqns, reset_btn, enter_btn, exp_entry):
    global NUMBER_OF_EQUATIONS
    NUMBER_OF_EQUATIONS = numofeqns
    if numofeqns > 0:
        reset_btn.configure(state="enable")
        enter_btn.configure(state="enabled")
        exp_entry.configure(state="enabled")
    else:
        reset_btn.configure(state="disabled")
        enter_btn.configure(state="disabled")
        exp_entry.configure(state="disabled")


def enter_eqn(out, equation, numofeqns, enter_btn, exp_entry):
    global NUMBER_OF_EQUATIONS
    global EQUATIONS
    if equation != '' and NUMBER_OF_EQUATIONS > 0:
        try:
            parse.test_expression(equation)
            EQUATIONS.append(equation)
            NUMBER_OF_EQUATIONS -= 1
            update_output(out, "Equation #" + str(numofeqns - NUMBER_OF_EQUATIONS) + ": " + equation + "\n", append=True)
        except Exception as e:
            update_output(out, e, color="red", append=True)

    if NUMBER_OF_EQUATIONS == 0:
        enter_btn.configure(state="disabled")
        exp_entry.configure(state="disabled")


def reset(out, reset_btn, enter_btn, exp_entry):
    global NUMBER_OF_EQUATIONS
    global EQUATIONS
    NUMBER_OF_EQUATIONS = 0
    EQUATIONS = []
    update_output(out, "")
    reset_btn.configure(state="disabled")
    enter_btn.configure(state="disabled")
    exp_entry.delete(0, tk.END)
    exp_entry.configure(state="disabled")



def button_click(exp_entry, symbol):
    current = exp_entry.get()
    exp_entry.insert(exp_entry.index(tk.INSERT), symbol)
    exp_entry.focus()
    if "()" in symbol:
        exp_entry.icursor(exp_entry.index(tk.INSERT) - 1)

def x(exp_entry):
    button_click(exp_entry, "x")

def plus(exp_entry):
    button_click(exp_entry, "+")

def minus(exp_entry):
    button_click(exp_entry, "-")

def mult(exp_entry):
    button_click(exp_entry, "*")

def div(exp_entry):
    button_click(exp_entry, "/")

def pwr(exp_entry):
    button_click(exp_entry, "^")

def sqrt(exp_entry):
    button_click(exp_entry, "sqrt()")

def leftbracket(exp_entry):
    button_click(exp_entry, "()")

def rightbracket(exp_entry):
    button_click(exp_entry, ")")

def cos(exp_entry):
    button_click(exp_entry, "cos()")

def sin(exp_entry):
    button_click(exp_entry, "sin()")

def e(exp_entry):
    button_click(exp_entry, "E")

def clear(exp_entry):
    exp_entry.delete(0, tk.END)
    exp_entry.focus()

def calc ():
    pass 