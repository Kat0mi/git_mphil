# ----- Set-Up ----- 

from pkg import *

dfs = [cdfs, cos, uds]

field_names = ['cdfs', 'cos', 'uds']
diagnostics = ['Lacy', 'Donley', 'KI', 'KIM', 'radio_agn', 'xray_agn']

# ----- Stats Calculations -----

# -- Dictionary --

results = {col: {'Independent NMAD': [], 'Dependent NMAD': [], 
                 
                 'Mean': [], 'Median': [], 'SD': []} 

           for col in diagnostics}

for col in diagnostics:

    for df in dfs:

        vals = df['agn_luminosity'][df[col] == 1].dropna().values
        
        # -- Independent NMADs --

        nmad_ind = 1.48 * np.median(np.abs(vals - np.median(vals)))
        results[col]['Independent NMAD'].append(nmad_ind)

        # -- Dependent NMADs --

        nmad_dep = 1.48 * np.median(np.abs(vals - np.median(df['agn_luminosity'].dropna().values)))
        results[col]['Dependent NMAD'].append(nmad_dep)

        # -- Mean, Median, SD --

        mean_val = np.mean(vals)
        median_val = np.median(vals)
        sd_val = np.std(vals)

        # -- Append Dictionary --

        results[col]['Mean'].append(mean_val)
        results[col]['Median'].append(median_val)
        results[col]['SD'].append(sd_val)

# ----- Output to Text File -----

with open('stats.txt', 'w') as f:

    for col in diagnostics:

        f.write(f"{col}:\n")
        df_output = pd.DataFrame(results[col], index = field_names)
        f.write(df_output.to_string(float_format="{:.4E}".format))
        f.write("\n\n")
