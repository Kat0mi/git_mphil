# ---------- Pairplot ----------

from pkg import *

# -- Target Variables --

vars = ['HR', 'Av', 'lmass', 'lsfr', 'lssfr', 're', 'si', 'z']

# -- Remove -99 and -999 --

all = all.replace([-99, -999], np.nan)

# -- Remove sources with z > 8 --

# -- Handle Duplicate Indices --

# Drop duplicate indices, keeping the first occurrence
all = all[~all.index.duplicated(keep='first')]

# Alternatively, reset the index if you need to preserve all rows but avoid duplicate labels
# all = all.reset_index(drop=True)

# -- Plot Parameters --

plot_kws = {
    's': 10,
    'edgecolor': 'k',
    'color': 'xkcd:grey'
}

diag_kws = {
    'color': 'xkcd:grey'
}

# ----- Plot -----

g = sns.pairplot(all,
                 vars=vars,
                 hue="agn",
                 markers='o',
                 plot_kws=plot_kws,
                 diag_kws=diag_kws)

# -- Axes Customisation --

for ax in g.axes.flatten():
    ax.xaxis.label.set_size(18)
    ax.yaxis.label.set_size(18)
    ax.xaxis.set_label_coords(0.5, -0.2)
    ax.yaxis.set_label_coords(-0.25, 0.5)

# -- Title --

plt.suptitle('all: AGN == 0', size=20, y=1.02)

# -- Save --

plt.savefig('/Users/jess/Desktop/testpp.png', bbox_inches='tight', dpi=300, facecolor='white', transparent=False)
