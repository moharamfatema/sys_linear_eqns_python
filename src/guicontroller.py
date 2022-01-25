import json
import pandas as pd
import numpy as np
from math import exp
import os
import sys

from sympy.core import symbol
import parse
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


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