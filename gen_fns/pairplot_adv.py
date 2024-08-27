# ---------- Pairplot ----------

from pkg import *

# -- Target Variables --

vars = ['HR', 'Av', 'lmass', 'lsfr', 'lssfr', 're', 'si', 'z']

# -- Remove -99 and -999 --

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

# ----- Plot -----

g = sns.pairplot(cdfs[(cdfs['agn'] == 0)],
                 vars = vars,
                 diag_kind = 'kde',
                 plot_kws = plot_kws,
                 diag_kws = diag_kws,
                 markers = 'o')

# -- Stat Annotations --

for i, var in enumerate(vars):

    data = cdfs[var].dropna()

    # -- Calculations --

    mean = np.mean(data)
    median = np.median(data)
    sd = np.std(data)
    nmad = 1.4826 * median_absolute_deviation(data, ignore_nan = True)

    # -- Print Vals --

    stats = (f"$\sigma_{{NMAD}}$ = {nmad:.2f}\n"
             f"$\sigma$ = {sd:.2f}\n"
             f"$\overline{{x}}$ = {mean:.2f}\n"
             f"$\widetilde{{x}}$ = {median:.2f}")
    
    # -- Position Text --

    ax = g.diag_axes[i]

    if var in ['HR', 'lmass', 'lsfr', 'lssfr']:

        # -- Upper Left --

        ax.text(0.075, 0.975, f"$\sigma_{{NMAD}}$ = {nmad:.2f}", transform = ax.transAxes, fontsize = 10,
                verticalalignment = 'top', horizontalalignment = 'left', bbox = dict(facecolor = 'none', edgecolor = 'none', pad = 2))
        ax.text(0.075, 0.875, f"$\sigma$ = {sd:.2f}", transform = ax.transAxes, fontsize = 10,
                verticalalignment = 'top', horizontalalignment = 'left', bbox = dict(facecolor = 'none', edgecolor = 'none', pad = 2))
        ax.text(0.075, 0.775, f"$\overline{{x}}$  =  {mean:.2f}", transform = ax.transAxes, fontsize = 10,
                verticalalignment = 'top', horizontalalignment = 'left', bbox = dict(facecolor = 'none', edgecolor = 'none', pad = 2))
        ax.text(0.075, 0.675, f"$\widetilde{{x}}$  =  {median:.2f}", transform = ax.transAxes, fontsize = 10,
                verticalalignment = 'top', horizontalalignment = 'left', bbox = dict(facecolor = 'none', edgecolor = 'none', pad = 2))
    else:

        # -- Upper Right --

        ax.text(0.975, 0.975, f"$\sigma_{{NMAD}}$ = {nmad:.2f}", transform = ax.transAxes, fontsize = 10,
                verticalalignment = 'top', horizontalalignment = 'right', bbox = dict(facecolor = 'none', edgecolor = 'none', pad = 2))
        ax.text(0.975, 0.875, f"$\sigma$  =  {sd:.2f}", transform = ax.transAxes, fontsize = 10,
                verticalalignment = 'top', horizontalalignment = 'right', bbox = dict(facecolor = 'none', edgecolor = 'none', pad = 2))
        ax.text(0.975, 0.775, f"$\overline{{x}}$  =  {mean:.2f}", transform = ax.transAxes, fontsize = 10,
                verticalalignment = 'top', horizontalalignment = 'right', bbox = dict(facecolor = 'none', edgecolor = 'none', pad = 2))
        ax.text(0.975, 0.675, f"$\widetilde{{x}}$  =  {median:.2f}", transform = ax.transAxes, fontsize = 10,
                verticalalignment = 'top', horizontalalignment = 'right', bbox = dict(facecolor = 'none', edgecolor = 'none', pad = 2))

# -- Axes Customisation --
        
for ax in g.axes.flatten():
    ax.xaxis.label.set_size(18)
    ax.yaxis.label.set_size(18)
    ax.xaxis.set_label_coords(0.5, -0.2)
    ax.yaxis.set_label_coords(-0.25, 0.5)

# -- Title --
    
plt.suptitle('CDFS: AGN == 0', size = 20, y = 1.02)

# -- Save --

plt.savefig('/Users/jess/Desktop/git_mphil/outputs/misc/pairplot_sfg_cdfs.png', bbox_inches = 'tight', dpi = 300, facecolor = 'white', transparent = False)
