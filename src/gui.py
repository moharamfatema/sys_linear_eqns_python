from cmath import exp
from tkinter import Label, ttk 
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image
import guicontroller as gc


FROM_X = -50
TO_X = 50
SPIN_WIDTH = 10
PADY_BOXES = (0, 5)
BUTTON_PAD = 3
BUTTON_WIDTH = 5


def run():
    # Configuring window
    root = ThemedTk(theme="breeze")
    root.title("System of Linear Equations")
    root.geometry('1000x630+250+100')
    root.resizable(False, False) 

    # Creating the widgets
    input_frame = ttk.LabelFrame(root, text="Input", padding=20)
    output_frame = ttk.LabelFrame(root, text="Output", padding=20)

    button_frame = ttk.Frame(input_frame, padding=20)

    # Input widgets

    numofeqn_label = ttk.Label(input_frame, text="Number of Equations")
    numofeqn_var = tk.IntVar()
    numofeqn_var.set(3)
    numofeqn_spin = ttk.Spinbox(input_frame, textvariable=numofeqn_var, width=SPIN_WIDTH, from_=0, to=TO_X)


    enter_label= ttk.Label(input_frame, text="Enter equation", width=20)
    entry_string = tk.StringVar()
    exp_entry = ttk.Entry(input_frame, textvariable=entry_string, width=40, state="disabled")
    entry_string.trace_add("write", lambda *args: gc.string_entered(exp_entry))
    file_btn = ttk.Button(input_frame, text="Choose from a file", command=lambda:gc.choose_file(output_txt))

    calc_btn = ttk.Button(input_frame, text="Calculate", command=lambda: gc.calc(output_txt, method.get(), precision_var.get(), maxiter_var.get()))
    gc.CreateToolTip(exp_entry, text = 'Make sure to confirm number of equations first!')

    init_label= ttk.Label(input_frame, text="Initial values")
    init_var = tk.DoubleVar()
    init_entry = ttk.Entry(input_frame, textvariable=init_var, state="disabled")
    enter_init_btn = ttk.Button(input_frame, text="Enter", state="disabled", width=BUTTON_WIDTH, command=lambda *args: gc.enter_init_vals(output_txt, init_entry, enter_init_btn))
    gc.CreateToolTip(init_entry, text = 'Make sure to enter all equations first!')

    confirm_btn = ttk.Button(input_frame, text="Confirm", width=BUTTON_WIDTH + 2, command=lambda *args: gc.confirm(output_txt, numofeqn_var.get(), reset_btn, enter_btn, exp_entry, init_entry, enter_init_btn))
    reset_btn = ttk.Button(input_frame, text="Reset", state="disabled", width=BUTTON_WIDTH, command=lambda *args: gc.reset(output_txt, reset_btn, enter_btn, exp_entry, init_entry, enter_init_btn))
    enter_btn = ttk.Button(input_frame, text="Enter", state="disabled", width=BUTTON_WIDTH, command=lambda *args: gc.enter_eqn(output_txt, exp_entry.get(), enter_btn, exp_entry, init_entry, enter_init_btn))


    methods = [
        "All",
        "Gaussian elimination",
        "LU decomposition",
        "Gaussian Jordan",
        "Gauss siedel"
    ]
    method = tk.StringVar()
    method.set(methods[0])
    method_label = ttk.Label(input_frame, text="Method")
    method_options = ttk.Combobox(input_frame, textvariable=method, values=methods, state="readonly")
    method_options.config(width=20)


    precision_label = ttk.Label(input_frame, text="Precision")
    precision_var = tk.DoubleVar()
    precision_var.set(0.00001)
    precision_spin = ttk.Spinbox(input_frame, textvariable=precision_var, width=SPIN_WIDTH, from_=0, to=1, increment=.00001)

    maxiter_label = ttk.Label(input_frame, text="Max Iterations")
    maxiter_var = tk.IntVar()
    maxiter_var.set(50)
    maxiter_spin = ttk.Spinbox(input_frame, textvariable=maxiter_var, width=SPIN_WIDTH, from_=FROM_X, to=TO_X)

   
    var_widgets = [
        precision_label, precision_spin,
        maxiter_label, maxiter_spin,
        init_label, init_entry,
        enter_init_btn
    ]


    #method_options.bind('<<ComboboxSelected>>', lambda *args: gc.method_change(var_widgets, method.get(), methods, sim_btn))
    method.trace_add("write", lambda *args: gc.method_change(var_widgets, method.get(), methods, output_txt, reset_btn, enter_btn, exp_entry, init_entry, enter_init_btn))
    
    # Output widgets
    output_txt = tk.Text(output_frame, width=40, state="disabled", height=30, wrap=tk.NONE)
    scrollbar_y = ttk.Scrollbar(output_frame, orient='vertical', command=output_txt.yview)
    scrollbar_x = ttk.Scrollbar(output_frame, orient='horizontal', command=output_txt.xview)
    output_txt.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    

    notes = "Notes for expression entry: \n \
        - You can enter expression using keyboard, provided buttons, or by uploading a txt file \n \
        - You can also upload entire input parameters as a json file \n \
        - Exponential must be written as 'E' \n \
        - Multiplication must be done as '2*x' not 2x \n \
        - You can evaluate square root using 'sqrt()' \n \
        - You can evaluate powers using '^' or '*'"
    notes_label = ttk.Label(input_frame, text=notes, foreground="#808080")

    # creating some buttons to help the user
    clear_btn = ttk.Button(button_frame, text="clear", width=BUTTON_WIDTH, command=lambda *args: gc.clear(exp_entry))
    plus_button = ttk.Button(button_frame, text="+", width=BUTTON_WIDTH, command=lambda *args: gc.plus(exp_entry))
    minus_button = ttk.Button(button_frame, text="-", width=BUTTON_WIDTH, command=lambda *args: gc.minus(exp_entry))
    mult_button = ttk.Button(button_frame, text="*", width=BUTTON_WIDTH, command=lambda *args: gc.mult(exp_entry))
    div_button = ttk.Button(button_frame, text="/", width=BUTTON_WIDTH, command=lambda *args: gc.div(exp_entry))
    pwr_button = ttk.Button(button_frame, text="^", width=BUTTON_WIDTH, command=lambda *args: gc.pwr(exp_entry))
    sqrt_button = ttk.Button(button_frame, text="sqrt()", width=BUTTON_WIDTH, command=lambda *args: gc.sqrt(exp_entry))
    leftbracket_button = ttk.Button(button_frame, text="(", width=BUTTON_WIDTH, command=lambda *args: gc.leftbracket(exp_entry))
    rightbracket_button = ttk.Button(button_frame, text=")", width=BUTTON_WIDTH, command=lambda *args: gc.rightbracket(exp_entry))
    cos_button = ttk.Button(button_frame, text="cos()", width=BUTTON_WIDTH, command=lambda *args: gc.cos(exp_entry))
    sin_button = ttk.Button(button_frame, text="sin()", width=BUTTON_WIDTH, command=lambda *args: gc.sin(exp_entry))
    e_button = ttk.Button(button_frame, text="E", width=BUTTON_WIDTH, command=lambda *args: gc.e(exp_entry))
    x_button = ttk.Button(button_frame, text="x", width=BUTTON_WIDTH, command=lambda *args: gc.x(exp_entry))



    # Styling 
    # style = ttk.Style()
    # style.configure("Red.TCheckbutton", foreground="red")

    # Displaying the widgets
    input_frame.grid(column=0, row=0, padx=20, pady=20)
    output_frame.grid(column=1, row=0, padx=20, pady=20. , sticky=tk.N+tk.S+tk.W)

    button_frame.grid(column=3, row=2, rowspan=10)

    method_label.grid(column=0, row=0, sticky=tk.W)
    method_options.grid(column=0, row=1, columnspan = 2, sticky=tk.W, pady=PADY_BOXES)
    file_btn.grid(column=3, row=1)

    numofeqn_label.grid(column=0, row=2, sticky=tk.W)
    numofeqn_spin.grid(column=0, row=3, sticky=tk.W, pady=PADY_BOXES)
    confirm_btn.grid(column=1, row=3,sticky=tk.W, padx=BUTTON_PAD, pady=BUTTON_PAD)
    reset_btn.grid(column=2, row=3, sticky=tk.W, padx=BUTTON_PAD, pady=BUTTON_PAD)

    enter_label.grid(column=0, row=4, sticky=tk.W)
    exp_entry.grid(column=0, row=5, columnspan=2, sticky=tk.W, pady=PADY_BOXES)
    enter_btn.grid(column=2, row=5, sticky=tk.W, padx=BUTTON_PAD, pady=BUTTON_PAD)

    
    init_label.grid(column=0, row=6, sticky=tk.W)
    init_entry.grid(column=0, row=7, sticky=tk.W, pady=PADY_BOXES)
    enter_init_btn.grid(column=1, row=7, sticky=tk.W, padx=BUTTON_PAD, pady=BUTTON_PAD)

    precision_label.grid(column=0, row=8, sticky=tk.W)
    maxiter_label.grid(column=1, row=8, sticky=tk.W)

    precision_spin.grid(column=0, row=9, sticky=tk.W, pady=PADY_BOXES)
    maxiter_spin.grid(column=1, row=9, sticky=tk.W, pady=PADY_BOXES)


    calc_btn.grid(column=3, row=12, padx=10, pady=10)
    notes_label.grid(column=0, row=13, columnspan=4, pady=PADY_BOXES)

    clear_btn.grid(column=0, row=0, columnspan=2, padx=BUTTON_PAD, pady=BUTTON_PAD)
    plus_button.grid(column=0, row=1, padx=BUTTON_PAD, pady=BUTTON_PAD)
    minus_button.grid(column=1, row=1, padx=BUTTON_PAD, pady=BUTTON_PAD)
    mult_button.grid(column=0, row=2, padx=BUTTON_PAD, pady=BUTTON_PAD)
    div_button .grid(column=1, row=2, padx=BUTTON_PAD, pady=BUTTON_PAD)
    pwr_button.grid(column=0, row=3, padx=BUTTON_PAD, pady=BUTTON_PAD)
    sqrt_button.grid(column=1, row=3, padx=BUTTON_PAD, pady=BUTTON_PAD)
    leftbracket_button.grid(column=0, row=4, padx=BUTTON_PAD, pady=BUTTON_PAD)
    rightbracket_button.grid(column=1, row=4, padx=BUTTON_PAD, pady=BUTTON_PAD)
    cos_button.grid(column=0, row=5, padx=BUTTON_PAD, pady=BUTTON_PAD)
    sin_button.grid(column=1, row=5, padx=BUTTON_PAD, pady=BUTTON_PAD)
    e_button.grid(column=0, row=6, padx=BUTTON_PAD, pady=BUTTON_PAD)
    x_button.grid(column=1, row=6, padx=BUTTON_PAD, pady=BUTTON_PAD)


    output_txt.grid(column=0, row=0)
    scrollbar_y.grid(column=1, row=0, sticky=tk.N+tk.S)
    scrollbar_x.grid(column=0, row=1, columnspan=2, sticky=tk.W+tk.E)

    root.protocol("WM_DELETE_WINDOW", lambda:gc.destroyer(root))
    root.mainloop()

run()