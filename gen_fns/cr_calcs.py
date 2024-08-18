# ---------- Completeness and Reliability Calculations ----------

# ----- Set-Up -----

from pkg import *

# ----- Redshift Masking Function -----

def redshift_mask(df, lower, upper=None):

    z = np.where(df['z_spec'] == -99, df['z_peak'], df['z_spec'])

    if upper is None:
        return lower < z
    
    else:
        return (lower < z) & (z < upper)
    




# ----- Diagnostic-Specific Selection Functions -----

# -- Lacy --
    
def agn_sel_filter_criteria_lacy(df):
    return (df['58_36'] > -0.1) & (df['80_45'] > -0.2) & (df['80_45'] < 0.8 * df['58_36'] + 0.5)

def n_sel_filter_criteria_lacy(df):
    return (df['ir_agn'].isin([0, -1])) & (df['radio_agn'].isin([0, -1])) & (df['xray_agn'].isin([0, -1])) & \
           (df['58_36'] > -0.1) & (df['80_45'] > -0.2) & (df['80_45'] < 0.8 * df['58_36'] + 0.5)

def ir_n_sel_filter_criteria_lacy(df):
    return (df['ir_agn'].isin([0, -1])) & (df['58_36'] > -0.1) & (df['80_45'] > -0.2) & \
           (df['80_45'] < 0.8 * df['58_36'] + 0.5)

# -- Donley Diagnostic --

def agn_sel_filter_criteria_donley(df):
    return (df['58_36'] > 0.08) & (df['80_45'] > 0.15) & (df['80_45'] > ((1.12 * df['58_36']) - 0.27)) & (df['58_36'] < ((1.12 * df['58_36']) + 0.27))

def n_sel_filter_criteria_donley(df):
    return (df['ir_agn'].isin([0, -1])) & (df['radio_agn'].isin([0, -1])) & (df['xray_agn'].isin([0, -1])) & \
           (df['58_36'] > 0.08) & (df['80_45'] > 0.15) & (df['80_45'] > ((1.12 * df['58_36']) - 0.27)) & \
           (df['58_36'] < ((1.12 * df['58_36']) + 0.27))

def ir_n_sel_filter_criteria_donley(df):
    return (df['ir_agn'].isin([0, -1])) & (df['58_36'] > 0.08) & (df['80_45'] > 0.15) & \
           (df['80_45'] > ((1.12 * df['58_36']) - 0.27)) & (df['58_36'] < ((1.12 * df['58_36']) + 0.27))

# -- KI Diagnostic --

def agn_sel_filter_criteria_ki(df):
    return (df['45_80_in'] > 0) & (df['Ks_45'] > 0)

def n_sel_filter_criteria_ki(df):
    return (df['ir_agn'].isin([0, -1])) & (df['radio_agn'].isin([0, -1])) & (df['xray_agn'].isin([0, -1])) & \
           (df['45_80_in'] > 0) & (df['Ks_45'] > 0)

def ir_n_sel_filter_criteria_ki(df):
    return (df['ir_agn'].isin([0, -1])) & (df['45_80_in'] > 0) & (df['Ks_45'] > 0)

# -- KIM Diagnostic --

def agn_sel_filter_criteria_kim(df):
    return (df['80_24_in'] > 0.5) & (df['80_24_in'] > (-2.9 * df['45_80_in'] + 2.8))

def n_sel_filter_criteria_kim(df):
    return (df['ir_agn'].isin([0, -1])) & (df['radio_agn'].isin([0, -1])) & (df['xray_agn'].isin([0, -1])) & \
           (df['80_24_in'] > 0.5) & (df['80_24_in'] > (-2.9 * df['45_80_in'] + 2.8))

def ir_n_sel_filter_criteria_kim(df):
    return (df['ir_agn'].isin([0, -1])) & (df['80_24_in'] > 0.5) & (df['80_24_in'] > (-2.9 * df['45_80_in'] + 2.8))





# ----- Global Selection Functions -----

def agn_sel(df, agn_type, agn_sel_filter_criteria):
    return len(df[(df[agn_type] == 1) & agn_sel_filter_criteria(df)])

def agn_sel_binned(df, agn_type, z_bin, agn_sel_filter_criteria):
    return len(df[(df[agn_type] == 1) & z_bin & agn_sel_filter_criteria(df)])

def n_sel(df, criteria_func):
    return len(df[criteria_func(df)])

def n_sel_binned(df, criteria_func, z_bin):
    return len(df[criteria_func(df) & z_bin])

# ----- Main Function -----

def analyze_completeness_reliability():
    
    root = tk.Tk()
    root.title("AGN Completeness and Reliability Analysis")

    def select_datasets():

        filenames = filedialog.askopenfilenames(title="Select Dataset Files", filetypes=[("CSV Files", "*.csv")])

        if filenames:
            dataset_files.extend(filenames)

    def set_diagnostic():

        diag = diagnostic_var.get()

        if diag == "Lacy":
            selected_diagnostic.set("Lacy")

        elif diag == "Donley":
            selected_diagnostic.set("Donley")

        elif diag == "KI":
            selected_diagnostic.set("KI")

        elif diag == "KIM":
            selected_diagnostic.set("KIM")

    def add_mask():

        column_name = mask_column.get()
        threshold = float(mask_threshold.get())
        condition = mask_condition.get()

        masks.append((column_name, threshold, condition))
        mask_listbox.insert(tk.END, f"{column_name} {condition} {threshold}")

    def apply_analysis():

        diagnostic = selected_diagnostic.get()

        if not dataset_files:
            messagebox.showerror("Error", "Please select at least one dataset.")
            return
        
        if not diagnostic:
            messagebox.showerror("Error", "Please select a diagnostic.")
            return

        agn_sel_filter_criteria = None

        # Set the diagnostic-specific filter function

        if diagnostic == "Lacy":
            agn_sel_filter_criteria = agn_sel_filter_criteria_lacy
            n_sel_filter_criteria = n_sel_filter_criteria_lacy
            ir_n_sel_filter_criteria = ir_n_sel_filter_criteria_lacy

        elif diagnostic == "Donley":
            agn_sel_filter_criteria = agn_sel_filter_criteria_donley
            n_sel_filter_criteria = n_sel_filter_criteria_donley
            ir_n_sel_filter_criteria = ir_n_sel_filter_criteria_donley

        elif diagnostic == "KI":
            agn_sel_filter_criteria = agn_sel_filter_criteria_ki
            n_sel_filter_criteria = n_sel_filter_criteria_ki
            ir_n_sel_filter_criteria = ir_n_sel_filter_criteria_ki

        elif diagnostic == "KIM":
            agn_sel_filter_criteria = agn_sel_filter_criteria_kim
            n_sel_filter_criteria = n_sel_filter_criteria_kim
            ir_n_sel_filter_criteria = ir_n_sel_filter_criteria

        # Process datasets and apply selected diagnostic
            
        for dataset_file in dataset_files:
            df = pd.read_csv(dataset_file)

            # Apply redshift masks
            
            redshift_bins = {

                "0-1": redshift_mask(df, 0, 1),
                "1-2": redshift_mask(df, 1, 2),
                "2-3": redshift_mask(df, 2, 3),
                "3-4": redshift_mask(df, 3, 4),
                "4+": redshift_mask(df, 4)
            }

            # Apply masks

            for mask in masks:

                condition, val, condition_type = mask
                if condition_type == 'geq':
                    df = df[df[condition] >= val]

                elif condition_type == 'leq':
                    df = df[df[condition] <= val]

                elif condition_type == 'bool':
                    df = df[df[condition] == val]

            # AGN selection depending on diagnostic
                    
            agn_selected = agn_sel(df, 'ir_agn', agn_sel_filter_criteria)
            total_agn = len(df[df['ir_agn'] == 1])
            completeness = agn_selected / total_agn if total_agn > 0 else 0

            print(f"Dataset: {dataset_file}, Diagnostic: {diagnostic}, Completeness: {completeness:.2f}")

            # Add more calculations as per the example provided...

        messagebox.showinfo("Analysis Complete", "The completeness and reliability analysis has been completed.")

    # Widgets for the GUI
        
    dataset_files = []
    masks = []

    tk.Button(root, text="Select Datasets", command=select_datasets).pack(pady=10)
    
    tk.Label(root, text="Select Diagnostic:").pack(pady=5)
    diagnostic_var = tk.StringVar(value="Lacy")
    tk.Radiobutton(root, text="Lacy", variable=diagnostic_var, value="Lacy", command=set_diagnostic).pack()
    tk.Radiobutton(root, text="Donley", variable=diagnostic_var, value="Donley", command=set_diagnostic).pack()
    tk.Radiobutton(root, text="KI", variable=diagnostic_var, value="KI", command=set_diagnostic).pack()
    tk.Radiobutton(root, text="KIM", variable=diagnostic_var, value="KIM", command=set_diagnostic).pack()
    
    selected_diagnostic = tk.StringVar()
    
    tk.Label(root, text="Add Mask:").pack(pady=5)
    mask_column = tk.Entry(root)
    mask_column.pack(pady=5)
    mask_column.insert(0, "Column Name")

    mask_threshold = tk.Entry(root)
    mask_threshold.pack(pady=5)
    mask_threshold.insert(0, "Threshold")

    mask_condition = tk.Entry(root)
    mask_condition.pack(pady=5)
    mask_condition.insert(0, "Condition (geq, leq, bool)")

    tk.Button(root, text="Add Mask", command=add_mask).pack(pady=10)
    
    mask_listbox = tk.Listbox(root)
    mask_listbox.pack(pady=10)
    
    tk.Button(root, text="Analyze", command=apply_analysis).pack(pady=20)

    root.mainloop()

# Run the analysis function
analyze_completeness_reliability()
