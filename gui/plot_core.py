# ----- Import Packages -----

import tkinter as tk
from tkinter import filedialog, simpledialog
import importlib.util
import pandas as pd
import inspect
import os
import sys
from tkinter import simpledialog, messagebox

# ----- Load Diagnostic Function -----

def load_function(function_path, function_name):

    spec = importlib.util.spec_from_file_location(function_name, function_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return getattr(module, function_name)

def get_function_names(function_path):

    spec = importlib.util.spec_from_file_location("module", function_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return [name for name, obj in inspect.getmembers(module, inspect.isfunction)]

# ----- Run Diagnostic Function -----

def run_diagnostic():

    # -- Select Diagnostic Function Script --

    function_path = filedialog.askopenfilename(title = "Select diagnostic function script", filetypes = [("Python Files", "*.py")])

    if not function_path:
        return

    # -- Get Available Function Names --

    function_names = get_function_names(function_path)

    if not function_names:

        tk.messagebox.showerror("Error", "No functions found in the selected script.")

        return

    # -- Automatically Select the First Function Name --

    function_name = function_names[0]

    # -- Load the Selected Function --

    diagnostic_function = load_function(function_path, function_name)

    # -- Number of Datasets --

    num_datasets = simpledialog.askinteger("Input", "Input number of datasets to analyse:", minvalue = 1)

    if num_datasets is None:
        return

    # -- Select Datasets and Input Names --

    datasets = []
    dataset_names = []

    for i in range(num_datasets):

        dataset_path = filedialog.askopenfilename(title = f"Select dataset {i + 1}", filetypes = [("CSV Files", "*.csv")])

        if not dataset_path:
            return

        dataset_name = simpledialog.askstring("Input", f"Enter dataset ID to appear on subplot {i + 1}:")

        if not dataset_name:
            return

        datasets.append(pd.read_csv(dataset_path))
        dataset_names.append(dataset_name)

    # -- Input Column Names --

    class ColumnNamesDialog(simpledialog.Dialog):

        def body(self, master):

            tk.Label(master, text = "Enter x-axis column ID(s):").grid(row = 0, column = 0, padx = 5, pady = 5)
            self.x_col_entry = tk.Entry(master)
            self.x_col_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

            tk.Label(master, text = "Enter y-axis column ID(s):").grid(row = 1, column = 0, padx = 5, pady = 5)
            self.y_col_entry = tk.Entry(master)
            self.y_col_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

            return self.x_col_entry

        def apply(self):
            self.result = (self.x_col_entry.get().strip(), self.y_col_entry.get().strip())

    def get_column_names():
        root = tk.Tk()
        root.withdraw()

        dialog = ColumnNamesDialog(root, "Input column names") 

        if dialog.result:

            x_col, y_col = dialog.result

            if x_col and y_col:
                return [x_col], [y_col]
            else:
                tk.messagebox.showerror("Input Error", "Both column names must be provided.")
                return None, None
        else:
            return None, None

    xd, yd = get_column_names()

    if xd is None or yd is None:
        return

    xd = xd * num_datasets
    yd = yd * num_datasets

    # -- Masking --
        
    class MaskInputDialog(simpledialog.Dialog):

        def body(self, master):

            tk.Label(master, text = "Column Name:").grid(row = 0)
            tk.Label(master, text = "Threshold Value:").grid(row = 1)
            tk.Label(master, text = "Condition (geq/leq/bool):").grid(row = 2)

            self.column_name_entry = tk.Entry(master)
            self.threshold_value_entry = tk.Entry(master)
            self.condition_entry = tk.Entry(master)

            self.column_name_entry.grid(row = 0, column = 1)
            self.threshold_value_entry.grid(row = 1, column = 1)
            self.condition_entry.grid(row = 2, column = 1)

            return self.column_name_entry  # initial focus

        def apply(self):

            column_name = self.column_name_entry.get()
            try:
                threshold_value = float(self.threshold_value_entry.get())
            except ValueError:
                threshold_value = None
            condition = self.condition_entry.get().lower()

            self.result = (column_name, threshold_value, condition)

    def ask_masks(num_masks):

        masks = []

        for i in range(num_masks):
            dialog = MaskInputDialog(root, title = f"Mask {i + 1}")
            if dialog.result:
                column_name, threshold_value, condition = dialog.result

                if condition not in ['geq', 'leq', 'bool']:
                    tk.messagebox.showerror("Error", "Invalid condition entered.")
                    return

            masks.append((column_name, threshold_value, condition))

        return masks

    num_masks = simpledialog.askinteger("Input", "Enter no. of masks to apply (0 for none):", minvalue = 0)

    if num_masks is None:
        return

    masks = []

    if num_masks > 0:
        masks = ask_masks(num_masks)

    # -- Colour Bar --
        
    colour_bar = simpledialog.askstring("Input", "Enter column ID for colour bar (leave blank for none)")
        
    if colour_bar == "":
        colour_bar = None

    # -- Select Save Path --
            
    save_path = filedialog.asksaveasfilename(title = "Save plot as", defaultextension = ".svg", filetypes = [("SVG Files", "*.svg")])

    if not save_path:
        return

    # -- Call Diagnostic Function with Provided Inputs --

    diagnostic_function(datasets = datasets, xd = xd, yd = yd, masks = masks, save_path = save_path, dataset_names = dataset_names, colour_bar = colour_bar)

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()
    run_diagnostic()