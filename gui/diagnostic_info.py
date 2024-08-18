# ----- Import Packages -----

import tkinter as tk
from PIL import Image, ImageTk
import webbrowser


# ----- Read .txt Function -----

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# ----- Diagnostic Input Pop-Up Function -----
    
def get_diagnostic_choice():

    # -- Submit Button Functionality --

    def submit():
        diagnostic_choice.set(option_var.get().strip().lower())
        custom_dialog.destroy()

    # -- Create and Customise Window --
        
    root = tk.Tk()
    root.withdraw() 

    custom_dialog = tk.Toplevel(root)
    custom_dialog.title(" ")
    custom_dialog.configure(bg='#e8eeff')

    tk.Label(custom_dialog, text = "AGN Diagnostic Console", font = ("Helvetica Neue", 12), bg = '#e8eeff').pack(padx = 10, pady = 10)

    # -- Drop Down Menu --

    option_var = tk.StringVar(custom_dialog)
    options = ["Select diagnostic", "Lacy Wedge", "Stern Wedge", "KI/M", "IRAC vs Redshift", "Blue Diagram", "BPT Diagram", "CEx Diagram", "MEx Diagram", "DEW Diagram", "TBT Diagram", "WHAN Diagram", "X-Ray", "Radio", "UVJ Diagram"]
    option_var.set(options[0])
    option_menu = tk.OptionMenu(custom_dialog, option_var, *options)
    option_menu.config(font = ("Helvetica Neue", 12), bg = '#e8eeff', activebackground = '#e8eeff', highlightthickness = 0, bd = 0, relief = 'flat')
    option_menu["menu"].config(bg = '#e8eeff', font = ("Helvetica Neue", 12))
    option_menu.pack(padx = 10, pady = 10)

    diagnostic_choice = tk.StringVar()
    submit_button = tk.Button(custom_dialog, text = "Submit", font = ("Helvetica Neue", 12), command = submit, bg = '#e8eeff', activebackground = '#e8eeff', bd = 0, highlightthickness = 0, relief='flat', pady = 5)
    submit_button.pack(padx = 10, pady = (5, 10))

    custom_dialog.grab_set()
    root.wait_window(custom_dialog)
    root.destroy()

    return diagnostic_choice.get()


# ----- Diagnostic Info Pop-Up Function -----

def show_diagnostic_info(info, header, image_path, links):

    # -- Open Link Functionality --

    def open_link(event, link):
        webbrowser.open_new(link)

    # -- Create and Customise Main Window --
        
    root = tk.Tk()                                          # Create a new window
    root.title("Diagnostic Information")                    # Set window title
    root.configure(bg='#e8eeff')                            # Set window background colour

    # -- Header Label --

    header_label = tk.Label(root, text=header, font = ("Helvetica Neue", 20, "bold"), bg = '#e8eeff')
    header_label.grid(row = 0, column = 0, columnspan = 2, pady = 10, sticky = 'ew')

    # -- Widget Frame --

    image_frame = tk.Frame(root, bg = '#e8eeff')
    image_frame.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = 'ns')

    # -- Embedded Image --

    image = Image.open(image_path).convert("RGBA")          # Converts image to RGBA format
    max_size = (550, 550)                                   # Set maximum image size
    image.thumbnail(max_size, Image.Resampling.LANCZOS)     # Resize while maintaining aspect ratio
    photo = ImageTk.PhotoImage(image)                       # Convert image to tkinter-readable format

    image_label = tk.Label(image_frame, image = photo, bg = '#e8eeff')
    image_label.image = photo
    image_label.pack(padx=10, pady=10)

    # -- Text Frame --

    text_frame = tk.Frame(root, bg = '#e8eeff')
    text_frame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'nsew')

    # -- Dynamic Text --

    root.grid_rowconfigure(1, weight = 1)                   # Configure row 1 to expand with window
    root.grid_columnconfigure(0, weight = 1)                # Configure column 0 to expand with window

    # -- Embedded Text --

    text_widget = tk.Text(text_frame, bg = '#e8eeff', fg = '#8c92ac', font = ("Helvetica Neue", 16), wrap = tk.WORD, padx = 0, pady = 0, bd = 0, highlightthickness = 0)

    lines = info.split('\n')

    for line in lines:
        if line.startswith("**") and line.endswith("**"):
            text_widget.insert(tk.END, line.strip("**") + "\n", 'bold')
        else:
            text_widget.insert(tk.END, line + "\n")

    text_widget.tag_config('bold', font = ("Helvetica Neue", 16, "bold"))
    text_widget.config(state = tk.DISABLED)
    text_widget.pack(expand = True, fill=tk.BOTH)


    # -- Embedded Links --

    for link in links:
        link_label = tk.Label(root, text = "Original Publication", font = ("Helvetica Neue", 14, "underline"), fg = '#8c92ac', bg = '#e8eeff', cursor = "hand2")
        link_label.grid(row = 2, column = 0, columnspan = 2, pady = 10, sticky = 'ew')
        link_label.bind("<Button-1>", lambda event, link = link: open_link(event, link))

    root.mainloop()


def main():

    diagnostic_choice = get_diagnostic_choice()
    output_to_window = True

    if diagnostic_choice == "lacy wedge":
        info = read_text_file('/Users/jess/Desktop/git_mphil/txt/lacy.txt')
        header = "Lacy Wedge"
        image_path = "/Users/jess/Desktop/diagnostic_plots/diagnostic_info/lacy_cdfs.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "stern wedge":
        info = read_text_file('/Users/jess/Desktop/git_mphil/txt/stern.txt')
        header = "Stern Wedge"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/lacy_donley_32.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "ki/m":
        info = read_text_file('/Users/jess/Desktop/git_mphil/txt/ki.txt')
        header = "KI/M Diagnostic"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "irac vs redshift":
        info = read_text_file('/Users/jess/Desktop/juneau.txt')
        header = "IRAC vs Redshift Diagnostic"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "blue diagram":
        info = read_text_file('/Users/jess/Desktop/blue.txt')
        header = "Blue Diagram"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "bpt diagram":
        info = read_text_file('/Users/jess/Desktop/bpt.txt')
        header = "BPT Diagram"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "cex diagram":
        info = read_text_file('/Users/jess/Desktop/cex.txt')
        header = "Colour-Excitation (CEx) Diagram"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "mex diagram":
        info = read_text_file('/Users/jess/Desktop/mex.txt')
        header = "Mass-Excitation (MEx) Diagram"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "dew diagram":
        info = read_text_file('/Users/jess/Desktop/dew.txt')
        header = "DEW Diagram"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "tbt diagram":
        info = read_text_file('/Users/jess/Desktop/tbt.txt')
        header = "TBT Diagram"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "whan diagram":
        info = read_text_file('/Users/jess/Desktop/whan.txt')
        header = "WHAN Diagram"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "x-ray":
        info = read_text_file('/Users/jess/Desktop/xray.txt')
        header = "X-ray Diagnostic"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "radio":
        info = read_text_file('/Users/jess/Desktop/radio.txt')
        header = "Radio Diagnostic"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    elif diagnostic_choice == "uvj diagram":
        info = read_text_file('/Users/jess/Desktop/uvj.txt')
        header = "UVJ Diagram"
        image_path = "/Users/jess/Desktop/diagnostic_plots/ir/ki_31.png"
        links = ["https://iopscience.iop.org/article/10.1086/422816/pdf"]

    else:
        info = "Warning: Transmission Error"
        header = "Invalid Choice"
        image_path = "/Users/jess/Desktop/diagnostic_plots/sad.png"
        links = []

    if output_to_window:
        show_diagnostic_info(info, header, image_path, links)


if __name__ == "__main__":
    main()
