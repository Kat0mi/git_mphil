# ---------- Pairplot ----------

from pkg import *

# -- Target Variables --

vars = ['HR', 'Av', 'lmass', 'lsfr', 'lssfr', 're', 'si', 'z']

# -- Remove -99 and -999 --

all = all.replace([-99, -999], np.nan)

all = all[~all.index.duplicated(keep = 'first')]

# -- Sub Sources --

all = all[all['class'] != 'NIL']
all = all[all['class'] != 'L']
#all = all[all['class'] != 'D']
#all = all[all['class'] != 'KI']
#all = all[all['class'] != 'KIM']

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
                 vars = vars,
                 hue = "class",
                 kind = 'kde',
                 markers = 'o',
                 plot_kws = {'color': 'xkcd:grey'},
                 diag_kws = diag_kws)

# -- Axes Customisation --

for ax in g.axes.flatten():
    ax.xaxis.label.set_size(18)
    ax.yaxis.label.set_size(18)
    ax.xaxis.set_label_coords(0.5, -0.2)
    ax.yaxis.set_label_coords(-0.25, 0.5)

# -- Title --

plt.suptitle('all: AGN == 0', size = 20, y = 1.02)

# -- Save --

plt.savefig('/Users/jess/Desktop/testpp.png', bbox_inches = 'tight', dpi = 300, facecolor = 'white', transparent = False)
