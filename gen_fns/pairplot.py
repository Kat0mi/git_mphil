# ---------- Pairplot ----------

from pkg import *

vars = ['HR', 'Av', 'lmass', 'lsfr', 'lssfr', 're', 'si', 'z']

cdfs = cdfs.replace([-99, -999], np.nan)
cos = cos.replace([-99, -999], np.nan)
uds = uds.replace([-99, -999], np.nan)

# -- Plot Parameters --

plot_kws = {
    's': 20,
    'edgecolor': 'k',
    'color': 'xkcd:grey'
}

diag_kws = {
    'color': 'xkcd:grey'
}

# -- Plot --

g = sns.pairplot(cdfs[(cdfs['agn'] == 0)],
                 vars = vars,
                 diag_kind = 'kde',
                 plot_kws = plot_kws,
                 diag_kws = diag_kws,   
                 markers = 'o')

# -- Axes Customisation --

for ax in g.axes.flatten():
    ax.xaxis.label.set_size(18)
    ax.yaxis.label.set_size(18)
    ax.xaxis.set_label_coords(0.5, -0.2)
    ax.yaxis.set_label_coords(-0.25, 0.5)

plt.suptitle('CDFS: AGN == 0', size = 20, y = 1.02)

plt.savefig('/Users/jess/Desktop/git_mphil/outputs/misc/pairplot_sfg_cdfs.png', bbox_inches = 'tight', dpi = 300, facecolor = 'white', transparent = False)
