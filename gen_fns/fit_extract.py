# ---------- Extract & Plot .fit Spectra (FAST) ----------

# ----- Imports -----

import os
import pandas as pd
import matplotlib.pyplot as plt

# [Adjust File Paths as Necessary]

cdfs = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_mphil', 'git_data', 'cdfs.csv'))
cos = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_mphil', 'git_data', 'cos.csv'))
uds = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_mphil', 'git_data', 'uds.csv'))


# ----- Extract Data -----

def read_fit_file(file_path):

    data = []
    headers = []

    try:

        with open(file_path, 'r') as file:

            # -- Extract Headers --

            first_line = file.readline().strip()

            if first_line.startswith('#'):

                # -- Manually Set Headers --

                first_line = first_line[1:].strip()                                  # Remove leading '#' and any surrounding whitespace
                headers = ['wl', 'fl (x 10^-19 ergs s^-1 cm^-2 Angstrom^-1)']
            
            # -- Read Data --
                
            for line in file:

                values = line.strip().split()

                if values:

                    # -- Convert To Float --

                    data.append([float(value) for value in values])

        print(f"File {file_path} read successfully.")
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    return headers, data

# ----- Plot Spectra -----

def plot_fit_files(field, ids):

    plt.figure(figsize = (10, 6))

    # -- Define Field-Dependent File Path/Name Structures --
    
    for source_id in ids:

        # [Adjust File Paths as Necessary]

        if field == 'cdfs':
            file_path = f'/Users/jess/Desktop/git_spectra/{field}_fast/{field}.v1.6.9_{source_id}.fit'

        elif field == 'cosmos':
            file_path = f'/Users/jess/Desktop/git_spectra/{field}_fast/{field}.v1.3.6_{source_id}.fit'

        elif field == 'uds':
            file_path = f'/Users/jess/Desktop/git_spectra/{field}_fast/{field}.v1.5.8_{source_id}.fit'

        else:

            print(f"Unknown field: {field}")

            continue

        # -- Plot Data --
        
        headers, data = read_fit_file(file_path)
        
        if data:

            wavelengths = [row[0] for row in data]
            fluxes = [row[1] for row in data]

            plt.plot(wavelengths, fluxes, label = f'ID: {source_id}')
    
    # -- Plot Aesthetics --
            
    # plt.title(f'Select Spectra from {field.upper()}')
                    
    plt.xlabel('Wavelength (Angstrom)')
    plt.ylabel('Flux (x 10^-19 ergs s^-1 cm^-2 Angstrom^-1)')

    plt.text(0.95, 0.05, f'{field.upper()}', fontsize = 13, color = 'k', ha = 'right', va = 'bottom', transform = plt.gca().transAxes)

    plt.xlim(0, 60000)
    plt.ylim(bottom = 0)

    handles, labels = plt.gca().get_legend_handles_labels()

    plt.legend(handles[:10], labels[:10])       # [Adjust no. of labels as necessary, default cap is 10 to prevent overcrowding]

    # [Adjust Save Path as Necessary]

    plt.savefig('/Users/jess/Desktop/git_mphil/outputs/fast/agn_uds.png', bbox_inches = 'tight', dpi = 300, facecolor = 'white', transparent = False)

    plt.show()



# ----- Dynamic Parameters -----
    
# -- Output Masked Array (Optional) --
    
for df in [cdfs, cos, uds]:

    mask = ((df['agn'] == 1))                # [Define desired mask condition(s)]

    id_array = df.loc[mask, 'id'].values        # Extracts IDs of sources that meet mask conditions for plot

# -- Field Name & Source IDs --

field_name = 'uds'                             # [Input desired field: Can be 'cdfs', 'cosmos', or 'uds']
source_ids = id_array                           # [Input desired ID array]

plot_fit_files(field_name, source_ids)          # Calls plot function