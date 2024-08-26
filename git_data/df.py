# ---------- Import Packages ----------

import pandas as pd; import os; import numpy as np; from astropy.io import fits; import warnings;

warnings.filterwarnings("ignore", message = "invalid value encountered in log10")
warnings.filterwarnings("ignore", message = "divide by zero encountered in log10")

os.chdir("/Users/jess/Desktop/og_data/fits")



# ---------- Import and Export FITS Files ----------

cdfs_fit, cos_fit, uds_fit = fits.open('cdfs_results.fits'), fits.open('cosmos_results.fits'), fits.open('uds_results.fits')
cdfs_fits, cos_fits, uds_fits = cdfs_fit[1].data, cos_fit[1].data, uds_fit[1].data
cdfs_fits, cos_fits, uds_fits = pd.DataFrame(cdfs_fits), pd.DataFrame(cos_fits), pd.DataFrame(uds_fits)

cdfs_fits.to_csv('/Users/jess/Desktop/og_data/fits/cdfs_fits.csv', index = False)
cos_fits.to_csv('/Users/jess/Desktop/og_data/fits/cosmos_fits.csv', index = False)
uds_fits.to_csv('/Users/jess/Desktop/og_data/fits/uds_fits.csv', index = False)



# ---------- Define File Paths ----------

# ----- MULTIWAVELENGTH DATA -----

# -- Primary ZFOURGE Catalogue Paths (Optical, NIR and MIR Data, Quality Flags, etc) --

cdfs_main_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.11.cat')
cos_main_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.8.cat')
uds_main_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.10.cat')

# -- Rest-Frame Catalogue Paths (Rest Frame UV, Optical and NIR Flux) --

cdfs_rest_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.9.rest.v0.9.cat')
cos_rest_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.6.rest.v0.9.cat')
uds_rest_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.8.rest.v0.9.cat')

# -- SFR Catalogue Paths (MIPS 24um M/FIR Data and UV + IR SFRs) --

cos_sfr_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.6.sfr.v0.4.cat')
uds_sfr_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.8.sfr.v0.4.cat')

# -- Herschel Catalogue Paths (Same as SFR Catalogue but with PACS FIR Data) --

cdfs_herschel_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.9.herschel.v0.4.cat')

# -- 3DHST Catalogue (NIR spectroscopic survey) -- 

cdfs_3dhst_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.9.3dhst.v0.4.cat')
cos_3dhst_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.6.3dhst.v0.4.cat')
uds_3dhst_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.8.3dhst.v0.4.cat')

#  -- Radio Catalogue Paths -- 

cdfs_radio_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.9.radio.v0.3.cat')
cos_radio_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.6.radio.v0.3.cat')
uds_radio_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.8.radio.v0.3.cat')

#  -- X-Ray Catalogue Paths -- 

cdfs_xray_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.9.xray.v0.4.cat')
cos_xray_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.6.xray.v0.4.cat')
uds_xray_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.8.xray.v0.4.cat')

# ----- ASTROPHYSICAL PARAMETERS AND AGN FLAGS -----

#  -- Primary ZFOURGE Redshift Catalogue Paths (Redshifts, sigma intervals, etc) -- 

cdfs_zout_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.9.zout')
cos_zout_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.6.zout')
uds_zout_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.8.zout')

#  -- FAST Stellar Population Catalogue Paths (Stellar Masses, SFRs, metallicity, dust reddening, etc) -- 

cdfs_fout_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.9.fout')
cos_fout_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.6.fout')
uds_fout_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.8.fout')

#  -- Spectroscopic Redshift Catalogue Paths -- 

cdfs_zspec_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.9.zspec.v0.4.cat')
cos_zspec_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.6.zspec.v0.4.cat')
uds_zspec_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.8.zspec.v0.4.cat')

#  -- Van der Wel et al. (2012) GALFIT Catalogue Paths (ZFOURGE matches, separation, structural parameters, etc) -- 

cdfs_vdw_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.9.vdw.v0.4.cat')
cos_vdw_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.6.vdw.v0.4.cat')
uds_vdw_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.8.vdw.v0.4.cat')

#  -- AGN Catalogue Paths (Binary AGN Candidate Flags for X-Ray, IR and Radio Diagnostics) -- 

cdfs_agn_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cdfs', 'cdfs.v1.6.9.agn.v0.5.cat')
cos_agn_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'cosmos', 'cosmos.v1.3.6.agn.v0.5.cat')
uds_agn_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'raw', 'uds', 'uds.v1.5.8.agn.v0.5.cat')

#  -- FITS Files -- 

cdfs_fits_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'fits', 'cdfs_fits.csv')
cos_fits_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'fits', 'cosmos_fits.csv')
uds_fits_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'og_data', 'fits', 'uds_fits.csv')

#  -- ZFIRE Data w/ ZFOURGE IDs -- 

cos_zfire_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'git_mphil', 'git_data', 'cos_zfire.csv')



# ---------- Read Files Into Pandas Dataframes ----------

cdfs_3dhst, cos_3dhst, uds_3dhst = [pd.read_csv(path, sep = '\s+') for path in [cdfs_3dhst_path, cos_3dhst_path, uds_3dhst_path]]

cdfs_radio, cos_radio, uds_radio = [pd.read_csv(path, sep = '\s+') for path in [cdfs_radio_path, cos_radio_path, uds_radio_path]]

cdfs_zspec, cos_zspec, uds_zspec = [pd.read_csv(path, sep = '\s+') for path in [cdfs_zspec_path, cos_zspec_path, uds_zspec_path]]

cdfs_rest, cos_rest, uds_rest = [pd.read_csv(path, sep = '\s+') for path in [cdfs_rest_path, cos_rest_path, uds_rest_path]]

cdfs_xray, cos_xray, uds_xray = [pd.read_csv(path, sep = '\s+') for path in [cdfs_xray_path, cos_xray_path, uds_xray_path]]

cdfs_zout, cos_zout, uds_zout = [pd.read_csv(path, sep = '\s+') for path in [cdfs_zout_path, cos_zout_path, uds_zout_path]]

cdfs_fout, cos_fout, uds_fout = [pd.read_csv(path, sep = '\s+') for path in [cdfs_fout_path, cos_fout_path, uds_fout_path]]

cdfs_cat, cos_cat, uds_cat = [pd.read_csv(path, sep = '\s+') for path in [cdfs_main_path, cos_main_path, uds_main_path]]

cdfs_vdw, cos_vdw, uds_vdw = [pd.read_csv(path, sep = '\s+') for path in [cdfs_vdw_path, cos_vdw_path, uds_vdw_path]]

cdfs_agn, cos_agn, uds_agn = [pd.read_csv(path, sep = '\s+') for path in [cdfs_agn_path, cos_agn_path, uds_agn_path]]

cdfs_sfr, cos_sfr, uds_sfr = [pd.read_csv(path, sep = '\s+') for path in [cdfs_herschel_path, cos_sfr_path, uds_sfr_path]]

cdfs_fits, cos_fits, uds_fits = [pd.read_csv(path, sep = ',') for path in [cdfs_fits_path, cos_fits_path, uds_fits_path]]

cdfs_main, cos_main, uds_main = [pd.read_csv(path, sep = '\s+') for path in [cdfs_main_path, cos_main_path, uds_main_path]]

cos_zfire = pd.read_csv(cos_zfire_path, sep = ',')



# ---------- Generate Custom Dataframe ----------

def custom_dataframe(cat, zout, agn, xray, fout, main, vdw, sfr, rest, zfire = None):

    cols = {

        # ----- Primary Columns -----

        'id': cat['id'], 'ra': cat['ra'], 'dec': cat['dec'], 'use': cat['use'], 'z_peak': zout['z_peak'], 'z_spec': zout['z_spec'],

        # ----- Combined Redshift Colum -----

        'z': np.where(zout['z_spec'] == -99, zout['z_peak'], zout['z_spec']),

        # ----- Physical Parameters -----

        'HR': xray['HR'], 'Av': fout['Av'], 'lmass': fout['lmass'], 'lsfr': fout['lsfr'], 'lssfr': fout['lssfr'], 'ltau': fout['ltau'], 'lage': fout['lage'], 'snr': main['snr'], 're': vdw['re'], 'e_re': vdw['dre'], 'si': vdw['n'], 'e_si': vdw['dn'],

        # ----- Boolean Flags -----

        'ir_agn': agn['ir_agn'], 'xray_agn': agn['xray_agn'], 'radio_agn': agn['radio_agn'], 'agn': np.where((agn['ir_agn'] == 1) | (agn['xray_agn'] == 1) | (agn['radio_agn'] == 1), 1, 0),

        # ----- Flux, Error, Weight, & SNR -----

        'f_U': cat['f_U'], 'f_xray': xray['f_xray'], 'l_xray': xray['l_xray'], 
        'f_Hs': cat['f_Hs'], 'e_Hs': cat['e_Hs'], 'w_Hs': cat['w_Hs'], 'SNR_Hs': cat['f_Hs'] / cat['e_Hs'], 
        'f_Hl': cat['f_Hl'], 'e_Hl': cat['e_Hl'], 'w_Hl': cat['w_Hl'], 'SNR_Hl': cat['f_Hl'] / cat['e_Hl'], 
        'f_J1': cat['f_J1'], 'e_J1': cat['e_J1'], 'w_J1': cat['w_J1'], 'SNR_J1': cat['f_J1'] / cat['e_J1'], 
        'f_J2': cat['f_J2'], 'e_J2': cat['e_J2'], 'w_J2': cat['w_J2'], 'SNR_J2': cat['f_J2'] / cat['e_J2'], 
        'f_J3': cat['f_J3'], 'e_J3': cat['e_J3'], 'w_J3': cat['w_J3'], 'SNR_J3': cat['f_J3'] / cat['e_J3'], 
        'f_Ks': cat['f_Ksall'], 'e_Ks': cat['e_Ksall'], 'w_Ks': cat['w_Ksall'], 'SNR_Ks': cat['f_Ksall'] / cat['e_Ksall'],

        # ----- ZFOURGE Weighted Broad-Band Averages (NIR; 0.3631 uJy) -----

        'f_H': ((cat['w_Hs'] * cat['f_Hs']) + (cat['f_Hl'] * cat['w_Hl'])) / (cat['w_Hs'] + cat['w_Hl']),
        'f_J': ((cat['w_J1'] * cat['f_J1']) + (cat['f_J2'] * cat['w_J2']) + (cat['f_J3'] * cat['w_J3'])) / (cat['w_J1'] + cat['w_J2'] + cat['w_J3']),

        # ----- IRAC and MIPS Filters (MIR, M/FIR; 0.3631 uJy, mJy) -----
        
        'f_36': cat['f_IRAC_36'], 'e_36': cat['e_IRAC_36'], 'w_36': cat['w_IRAC_36'], 'SNR_36': cat['f_IRAC_36'] / cat['e_IRAC_36'],
        'f_45': cat['f_IRAC_45'], 'e_45': cat['e_IRAC_45'], 'w_45': cat['w_IRAC_45'], 'SNR_45': cat['f_IRAC_45'] / cat['e_IRAC_45'],
        'f_58': cat['f_IRAC_58'], 'e_58': cat['e_IRAC_58'], 'w_58': cat['w_IRAC_58'], 'SNR_58': cat['f_IRAC_58'] / cat['e_IRAC_58'],
        'f_80': cat['f_IRAC_80'], 'e_80': cat['e_IRAC_80'], 'w_80': cat['w_IRAC_80'], 'SNR_80': cat['f_IRAC_80'] / cat['e_IRAC_80'],
        'f_24': sfr['f24'] * 1000, 'e_24': sfr['e24'] * 1000, 'SNR_24': (sfr['f24'] * 1000) / (sfr['e24'] * 1000),

        # ----- UVJ Filters -----

        'f_U': rest['f_U_rf'], 'e_U': rest['e_U_rf'], 'SNR_U': rest['f_U_rf'] / rest['e_U_rf'],
        'f_V': rest['f_V_rf'], 'e_V': rest['e_V_rf'], 'SNR_V': rest['f_V_rf'] / rest['e_V_rf'],
        'f_J': rest['f_J_rf'], 'e_J': rest['e_J_rf'], 'SNR_J': rest['f_J_rf'] / rest['e_J_rf'],
    }

        # ----- ZFIRE Data (COSMOS Only) -----

    if zfire is not None:
        cols.update({
            'f_Ha': zfire['FHa'], 'e_Ha': zfire['e_FHa'],
            'f_Hb': zfire['FHb'], 'e_Hb': zfire['e_FHb'],
            'f_NII': zfire['FNII'], 'e_NII': zfire['e_FNII'],
            'f_OII': zfire['FOII'], 'e_OII': zfire['e_FOII'],
            'f_OIII': zfire['FOIII'], 'e_OIII': zfire['e_FOIII'],
    })

    return pd.DataFrame(cols)

cdfs = custom_dataframe(cdfs_cat, cdfs_zout, cdfs_agn, cdfs_xray, cdfs_fout, cdfs_main, cdfs_vdw, cdfs_sfr, cdfs_rest)
cos = custom_dataframe(cos_cat, cos_zout, cos_agn, cos_xray, cos_fout, cos_main, cos_vdw, cos_sfr, cos_rest, cos_zfire)
uds = custom_dataframe(uds_cat, uds_zout, uds_agn, uds_xray, uds_fout, uds_main, uds_vdw, uds_sfr, uds_rest)



# ---------- Magnitude Conversion Columns (AB) ----------

conversions = [
    {'filter': 'Hs', 'catalog': [cdfs, cos, uds], 'data': 'f_Hs'},
    {'filter': 'Ks', 'catalog': [cdfs, cos, uds], 'data': 'f_Ks'},
    {'filter': '36', 'catalog': [cdfs, cos, uds], 'data': 'f_36'},
    {'filter': '45', 'catalog': [cdfs, cos, uds], 'data': 'f_45'},
    {'filter': '58', 'catalog': [cdfs, cos, uds], 'data': 'f_58'},
    {'filter': '80', 'catalog': [cdfs, cos, uds], 'data': 'f_80'},
    {'filter': '24', 'catalog': [cdfs, cos, uds], 'data': 'f_24'}
]

for conv in conversions:

    for cat in conv['catalog']:

        if conv['filter'] == '24':
            cat[f'AB_{conv["filter"]}'] = - (5 / 2) * np.log10(cat[conv['data']]) + 16.4

        else:
            cat[f'AB_{conv["filter"]}'] = - (5 / 2) * np.log10(cat[conv['data']]) + 16.4 #23.9

uvj_conversions = [
    {'filter': 'U', 'catalog': [cdfs, cos, uds], 'data': 'f_U'},
    {'filter': 'V', 'catalog': [cdfs, cos, uds], 'data': 'f_V'},
    {'filter': 'J', 'catalog': [cdfs, cos, uds], 'data': 'f_J'}
]

for conv_uvj in uvj_conversions:

    for cat in conv_uvj['catalog']:
        cat[f'AB_{conv_uvj["filter"]}'] = - (5 / 2) * np.log10(cat[conv_uvj['data']]) + 23.9



# ---------- Flux Ratio Comparisons ----------

def compute_flux_ratios(cdfs, cos, uds):

    datasets = [cdfs, cos, uds]
    nir_bands = ['J1', 'J2', 'J3', 'Hs', 'Hl', 'Ks']
    mir_bands = ['36', '45', '58', '80', '24']

    # ----- X-Ray / UV -----

    for data in datasets:
        
        data['x_u'] = data['f_xray'] / data['f_U']

    # ----- X-Ray / NIR -----

    for data in datasets:

        for nir_band in nir_bands:
            data[f'x_{nir_band}'] = data['f_xray'] / data[f'f_{nir_band}']

    # ----- X-Ray / NIR Averages -----
            
    for data in datasets:

        data['x_J'] = (data['x_J1'] + data['x_J2'] + data['x_J3']) / 3
        data['x_H'] = (data['x_Hs'] + data['x_Hl']) / 2
        data['x_NIR'] = (data['x_J'] + data['x_H'] + data['x_Ks']) / 3

    # ----- MIR / UV -----

    for data in datasets:

        for mir_band in mir_bands:
            data[f'{mir_band}_u'] = data[f'f_{mir_band}'] / data['f_U']

    # ----- MIR / UV Averages -----
            
    for data in datasets:

        data['MIR_U'] = (data['36_u'] + data['45_u'] + data['58_u'] + data['80_u']) / 4

    # ----- MIR / NIR -----
        
    for data in datasets:

        for mir_band in mir_bands:
            for nir_band in nir_bands:
                data[f'{mir_band}_{nir_band}'] = data[f'f_{mir_band}'] / data[f'f_{nir_band}']

    # ----- MIR / NIR Averages -----
                
    for data in datasets:

        for mir_band in mir_bands:
            data[f'{mir_band}_J'] = (data[f'{mir_band}_J1'] + data[f'{mir_band}_J2'] + data[f'{mir_band}_J3']) / 3
            data[f'{mir_band}_H'] = (data[f'{mir_band}_Hs'] + data[f'{mir_band}_Hl']) / 2
            data[f'{mir_band}_NIR'] = (data[f'{mir_band}_J'] + data[f'{mir_band}_H'] + data[f'{mir_band}_Ks']) / 3

    return cdfs, cos, uds

cdfs, cos, uds = compute_flux_ratios(cdfs, cos, uds)



# ---------- Diagnostic Ratio/Index Columns ----------

# ----- Lacy Wedge -----

for data in [cdfs, cos, uds]:

    data['80_45'] = np.log10(data['f_80'] / data['f_45'])
    data['58_36'] = np.log10(data['f_58'] / data['f_36'])
    data['80_36'] = np.log10(data['f_80'] / data['f_36'])
    data['58_36_80_45'] = data['58_36'] / data['80_45']

    data['36_45_in'] = data['AB_36'] - data['AB_45']
    data['58_80_in'] = data['AB_58'] - data['AB_80']

# ----- Lacy Error Propagation -----
    
for data in [cdfs, cos, uds]:

    data['e_80_45'] = np.sqrt((data['e_80'] / data['f_80'])**2 + (data['e_45'] / data['f_45'])**2)
    data['e_58_36'] = np.sqrt((data['e_58'] / data['f_58'])**2 + (data['e_36'] / data['f_36'])**2)
    data['e_80_36'] = np.sqrt((data['e_80'] / data['f_80'])**2 + (data['e_36'] / data['f_36'])**2)
    data['e_58_36_80_45'] = np.sqrt((data['e_58_36'] / data['58_36'])**2 + (data['e_80_45'] / data['80_45'])**2)

# ----- KI/M Diagnostics -----
    
for data in [cdfs, cos, uds]:

    data['45_80_in'] = data['AB_45'] - data['AB_80']
    data['Ks_45_in'] = data['AB_Ks'] - data['AB_45']

    data['80_24_in'] = data['AB_80'] - data['AB_24']

    data['24_58'] = np.log10(data['f_24'] / data['f_58'])

# ----- BPT -----
    
cos['NII_Ha'] = np.log10(cos['f_NII']) / np.log10(cos['f_Ha'])
cos['OIII_Hb'] = np.log10(cos['f_OIII']) / np.log10(cos['f_Hb'])

# ----- UVJ -----

for data in [cdfs, cos, uds]:

    data['U_V'] = data['AB_U'] - data['AB_V']
    data['V_J'] = data['AB_V'] - data['AB_J']



# ---------- FITS Columns ----------

datasets = [cdfs, cos, uds]
fits = [cdfs_fits, cos_fits, uds_fits]

for data, fit in zip(datasets, fits):

    data['ir_agn_contribution'] = fit['best.agn.fracAGN']
    data['agn_luminosity'] = fit['best.agn.luminosity']
    data['accretion_power'] = fit['best.agn.accretion_power']

    data['true_agn'] = np.where(data['ir_agn_contribution'] >= 0.5, 1, 0)

    data['log_agn_luminosity'] = np.log10(fit['best.agn.luminosity'])

    data['log_agn_luminosity'] = data['log_agn_luminosity'].replace(-np.inf, np.nan)
    
    data['log_agn_luminosity'] = np.where((data['log_agn_luminosity'] < 33), np.nan, data['log_agn_luminosity'])
    data['log_agn_luminosity'] = np.where((data['log_agn_luminosity'] > 39), np.nan, data['log_agn_luminosity'])



# ---------- Diagnostic AGN/SFG Boolean Flags ----------

for data in [cdfs, cos, uds]:

    # -- AGN -- #

    data['Lacy'] = np.where((data['58_36'] > -0.1) & (data['80_45'] > -0.2) & (data['80_45'] < 0.8 * data['58_36'] + 0.5), 1, 0)
    data['Donley'] = np.where((data['58_36'] > 0.08) & (data['80_45'] > 0.15) & (data['80_45'] > ((1.21 * data['58_36']) - 0.27)) & (data['80_45'] < ((1.21 * data['58_36']) + 0.27)) & (data['f_45'] > data['f_36']) & (data['f_58'] > data['f_45']) & (data['f_80'] > data['f_58']), 1, 0)
    data['KI'] = np.where((data['45_80_in'] > 0) & (data['Ks_45_in'] > 0), 1, 0)
    data['KIM'] = np.where((data['80_24_in'] > 0.5) & (data['80_24_in'] > (-2.9 * data['45_80_in'] + 2.8)), 1, 0)

    # -- Classes -- #

    data['diagnostic_class'] = np.where((data['Lacy'] == 1) & (data['Donley'] == 0), 'L', np.where(data['Donley'] == 1, 'D', np.where(data['KI'] == 1, 'KI', np.where(data['KIM'] == 1, 'KIM', 'NIL'))))
    
    data['cowley_class'] = np.where((data['ir_agn'] == 1, 'IR', np.where(data['xray_agn'] == 1, 'X-Ray', np.where(data['radio_agn'] == 1, 'Radio', np.where(data['KIM'] == 1, 'KIM', np.where((data['ir_agn'] == 1) & (data['xray_agn'] == 1), 'IR/X-Ray',  np.where((data['ir_agn'] == 1) & (data['radio_agn'] == 1), 'IR/Radio',  np.where((data['radio_agn'] == 1) & (data['xray_agn'] == 1), 'X-Ray/Radio',  np.where((data['radio_agn'] == 1) & (data['xray_agn'] == 1) & (data['ir_agn'] == 1), 'IR/X-Ray/Radio', 'NIL')))))))))

    data['cowley_class'] = np.where((data['ir_agn'] == 1) & (data['xray_agn'] == 1) & (data['radio_agn'] == 1), 'IR/X-Ray/Radio',
        np.where((data['ir_agn'] == 1) & (data['xray_agn'] == 1), 'IR/X-Ray',
            np.where((data['ir_agn'] == 1) & (data['radio_agn'] == 1), 'IR/Radio',
                np.where((data['xray_agn'] == 1) & (data['radio_agn'] == 1), 'X-Ray/Radio',
                    np.where(data['ir_agn'] == 1, 'IR',
                        np.where(data['xray_agn'] == 1, 'X-Ray',
                            np.where(data['radio_agn'] == 1, 'Radio',
                                'NIL')))))))

    data = data.copy



# ---------- Refine Dataframes ----------

# We initially restrict our sample to sources with use = 1 (See section 3.9 of Straatman et al. 2015 for an expanded discussion). Sources with use = 1
# meet the following requirements:

#    - star = 0
#    - nearstar = 0
#    - SNR >= 5
#    - wmin_fs > 0.1 (minimum exposure time of at least 0.1x the median exposure in the FourStar bands)
#    - wmin_optical > 0 (coverage in all optical bands)
#    - not a catastrophic EAZY fit: X^2 (reduced) <= 1000
#    - not a catastrophic FAST fit, i.e., a finite and positive stellar mass estimate above 10^6 Msun
#    - consistent flux ratios between similar bands of different instruments, namely the J -, H - and K - bands of the FS and VISTA, and F814W - and 
#      ground-based I - bands
#    - not 5 sigma detection at wavelengths bluer than the restframe 912 Angstrom Lyman limit
#    - not at z < 0.1

# We also restrict sources to those with SNR >= 5 across 

cdfs = cdfs[(cdfs['use'] == 1) & (cdfs['SNR_36'] >= 5) & (cdfs['SNR_45'] >= 5) & (cdfs['SNR_58'] >= 5) & (cdfs['SNR_80'] >= 5) & (cdfs['SNR_U'] >= 5) & (cdfs['SNR_V'] >= 5) & (cdfs['SNR_J'] >= 5)]
cos = cos[(cos['use'] == 1) & (cos['SNR_36'] >= 5) & (cos['SNR_45'] >= 5) & (cos['SNR_58'] >= 5) & (cos['SNR_80'] >= 5) & (cos['SNR_U'] >= 5) & (cos['SNR_V'] >= 5) & (cos['SNR_J'] >= 5)]
uds = uds[(uds['use'] == 1) & (uds['SNR_36'] >= 5) & (uds['SNR_45'] >= 5) & (uds['SNR_58'] >= 5) & (uds['SNR_80'] >= 5) & (uds['SNR_U'] >= 5) & (uds['SNR_V'] >= 5) & (uds['SNR_J'] >= 5)]

cdfs = cdfs[(cdfs['f_36'] != -99) & (cdfs['f_45'] != -99) & (cdfs['f_58'] != -99) & (cdfs['f_80'] != -99) & (cdfs['f_U'] != -99) & (cdfs['f_V'] != -99) & (cdfs['f_J'] != -99)]
cos = cos[(cos['f_36'] != -99) & (cos['f_45'] != -99) & (cos['f_58'] != -99) & (cos['f_80'] != -99) & (cos['f_U'] != -99) & (cos['f_V'] != -99) & (cos['f_J'] != -99)]
uds = uds[(uds['f_36'] != -99) & (uds['f_45'] != -99) & (uds['f_58'] != -99) & (uds['f_80'] != -99) & (uds['f_U'] != -99) & (uds['f_V'] != -99) & (uds['f_J'] != -99)]

cos = cos.dropna(subset = ['AB_36', 'AB_45', 'AB_58', 'AB_80', '80_45', '58_36', 'f_U'])
uds = uds.dropna(subset = ['AB_36', 'AB_45', 'AB_58', 'AB_80', '80_45', '58_36', 'f_U'])
cdfs = cdfs.dropna(subset = ['AB_36', 'AB_45', 'AB_58', 'AB_80', '80_45', '58_36', 'f_U'])



# ---------- Save Dataframes ----------

cdfs.to_csv('/Users/jess/Desktop/og_data/raw/cdfs/cdfs_in_df.csv', index = False)
cos.to_csv('/Users/jess/Desktop/og_data/raw/cosmos/cos_in_df.csv', index = False)
uds.to_csv('/Users/jess/Desktop/og_data/raw/uds/uds_in_df.csv', index = False)

cdfs.to_csv('/Users/jess/Desktop/git_mphil/git_data/cdfs.csv', index = False)
cos.to_csv('/Users/jess/Desktop/git_mphil/git_data/cos.csv', index = False)
uds.to_csv('/Users/jess/Desktop/git_mphil/git_data/uds.csv', index = False)