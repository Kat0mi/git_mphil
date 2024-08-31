# ---------- Multivariate PCA ----------

from pkg import *

agn_colors = {'cdfs': 'xkcd:periwinkle blue', 'cosmos': 'xkcd:hospital green', 'uds': 'xkcd:salmon'}
sfg_colors = {'cdfs': 'xkcd:light blue', 'cosmos': 'xkcd:light green', 'uds': 'xkcd:light salmon'}

pca_dfs = []

# ----- Generate and Normalise PCA DataFrames -----

for df, field_name in zip([cdfs, cos, uds], ['cdfs', 'cosmos', 'uds']):
    
    # -- Generate Variable-Limited DataFrame --

    df_pca = df[['HR', 'Av', 'lmass', 'lsfr', 'lssfr', 're', 'si']].copy()

    # -- Z-Score Normalisation --

    df_pca = (df_pca - df_pca.mean()) / df_pca.std()

    # -- Restore Original AGN and Redshift Columns --

    df_pca['agn'] = df['agn']
    df_pca['z'] = df['z']

    # -- Add Field ID Column for Concatenation --

    df_pca['field'] = field_name

    # -- Append --

    pca_dfs.append(df_pca)

# -- Concatenate --
    
combined_pca_df = pd.concat(pca_dfs)

# -- Separate Target Columns --

X = combined_pca_df[['HR', 'Av', 'lmass', 'lsfr', 'lssfr', 're', 'si']]

# -- Perform and Store PCA --

pca = PCA(n_components = 2)
pca_result = pca.fit_transform(X)

combined_pca_df['PCA1'] = pca_result[:, 0]
combined_pca_df['PCA2'] = pca_result[:, 1]

# ----- Scatter Plot -----

plt.figure(figsize = (10, 7))

# -- SFG Scatter --

for field_name in ['cdfs', 'cosmos', 'uds']:

    agn_color = agn_colors[field_name]
    sfg_color = sfg_colors[field_name]

    plt.scatter(combined_pca_df[(combined_pca_df['field'] == field_name) & (combined_pca_df['agn'] == 0)]['PCA1'],
                combined_pca_df[(combined_pca_df['field'] == field_name) & (combined_pca_df['agn'] == 0)]['PCA2'],
                marker = 'o', color = sfg_color, label = f'{field_name} AGN = 0')

# -- AGN Scatter --
    
for field_name in ['cdfs', 'cosmos', 'uds']:

    agn_color = agn_colors[field_name]
    sfg_color = sfg_colors[field_name]

    plt.scatter(combined_pca_df[(combined_pca_df['field'] == field_name) & (combined_pca_df['agn'] == 1)]['PCA1'],
                combined_pca_df[(combined_pca_df['field'] == field_name) & (combined_pca_df['agn'] == 1)]['PCA2'],
                marker='o', color = agn_color, edgecolors = 'k', linewidths = 0.5, s = 20, label = f'{field_name} AGN = 1')


plt.xlim(-4, 10); plt.ylim(-2, 8)
plt.xlabel('PCA1'); plt.ylabel('PCA2')
plt.legend(loc = 'upper left')

plt.savefig('/Users/jess/Desktop/git_mphil/outputs/misc/pca/pca_z_all.png', bbox_inches = 'tight', dpi = 300, facecolor = 'white', transparent = False)

plt.show()