# ---------- Extract & Plot .fit Spectra (FAST) ----------

# ----- Imports -----

import os
import zipfile
import pandas as pd
import matplotlib.pyplot as plt

cdfs = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_python', 'git_data', 'cdfs.csv'))
cos = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_python', 'git_data', 'cos.csv'))
uds = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_python', 'git_data', 'uds.csv'))

# ----- Extract Data -----

def read_fit_file_from_zip(zip_file_path, file_name):
    data = []
    headers = []

    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            with zip_file.open(file_name) as file:
                # -- Extract Headers --
                first_line = file.readline().decode('utf-8').strip()

                if first_line.startswith('#'):
                    # -- Manually Set Headers --
                    first_line = first_line[1:].strip()  # Remove leading '#' and any surrounding whitespace
                    headers = ['wl', 'fl (x 10^-19 ergs s^-1 cm^-2 Angstrom^-1)']

                # -- Read Data --
                for line in file:
                    values = line.decode('utf-8').strip().split()
                    if values:
                        # -- Convert To Float --
                        data.append([float(value) for value in values])

        print(f"File {file_name} read successfully from {zip_file_path}.")

    except FileNotFoundError:
        print(f"File not found: {file_name} in {zip_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

    return headers, data

# ----- Plot Spectra -----

def plot_fit_files(field, ids):

    plt.figure(figsize=(10, 6))

    # -- Define Field-Dependent File Path/Name Structures --
    for source_id in ids:
        if field == 'cdfs':
            file_name = f'{field}.v1.6.9_{source_id}.fit'
        elif field == 'cosmos':
            file_name = f'{field}.v1.3.6_{source_id}.fit'
        elif field == 'uds':
            file_name = f'{field}.v1.5.8_{source_id}.fit'
        else:
            print(f"Unknown field: {field}")
            continue

        zip_file_path = f'/Users/jess/Desktop/git_python/git_spectra/{field}_fast.zip'

        # -- Plot Data --
        headers, data = read_fit_file_from_zip(zip_file_path, file_name)

        if data:
            wavelengths = [row[0] for row in data]
            fluxes = [row[1] for row in data]

            plt.plot(wavelengths, fluxes, label=f'ID {source_id}')

    # -- Plot Aesthetics --
    plt.xlabel('Wavelength (Angstrom)')
    plt.ylabel('Flux (x 10^-19 ergs s^-1 cm^-2 Angstrom^-1)')
    plt.title(f'Spectra for {field.upper()} Field')

    plt.xlim(0, 60000)
    plt.ylim(0, 650)
    plt.legend()

    # plt.savefig('/Users/jess/Desktop/git_data/outputs/fast/xray_rad.png', bbox_inches='tight', dpi=300, facecolor='white', transparent=False)

    plt.show()

# ----- Produce Masked Array -----

for df in [cdfs, cos, uds]:
    mask = (df['xray_agn'] == 1)
    id_array = df.loc[mask, 'id'].values

# ----- Notable Source IDs (COSMOS) -----

field_name = 'cosmos'  # Can be 'cdfs', 'cosmos', or 'uds'
source_ids = id_array  # Replace with your actual source IDs
plot_fit_files(field_name, source_ids)
