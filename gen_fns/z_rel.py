# ---------- Spectroscopic vs Photometric Redshift Relationship ----------

# This script provides a comparison of the spectroscopic and photometric redshifts for SF candidates, AGN candidates, and "True" candidates. An excerpt 
# from Cowley et al. (2015) says the following of redshift measurements: "AGN emission is known to complicate the computation of photometric redshifts, 
# which can ultimately impact the derivation of RF colours and stellar population properties. In order to test the accuracy of [their] AGN sample, [they] 
# compare the sample's photometric redshifts from ZFOURGE to a secure sample of publicly available spectroscopic redshifts sources from the compilation
# of the 3DHST and ZFIRE surveys. [They] use the Normalized Median Absolute Deviation (NMAD) to calculate scatter (equation 2)"

# ----- Set-Up -----

from pkg import *

fig, ax = plt.subplots(figsize = (10, 10))

# ----- Adjustables -----

# -- Data --

filt_all = all[all['true_agn'] == 1]
df = all[(all['z_spec'] != -99) & (all['z_peak'] != -99) & (all['agn'] == 1)]

# -- Plot Parameters --

xd, yd = 'z_spec', 'z_peak'
xlim, ylim = [0, 4], [0, 4]
xtick, ytick = np.arange(0, 4, 0.5), np.arange(0, 4, 0.5)

# ----- Loops -----

for agn_type, w_param in zip(agn_types, w_params):
    ax.scatter(
        x=df.loc[df[agn_type] == 1, xd],
        y=df.loc[df[agn_type] == 1, yd],
        **w_param
    )

for agn_type, rgb_param in zip(agn_types, rgb_params):
    ax.scatter(
        x=df.loc[df[agn_type] == 1, xd],
        y=df.loc[df[agn_type] == 1, yd],
        label=agn_labels.get(agn_type, agn_type),
        **rgb_param
    )

# ----- Relation -----
    
ax.plot([0, 4], [0, 4], color='k', linestyle='-', linewidth=0.5, zorder=1)

# ----- Calculate Sample NMAD and SD -----

x_vals = df[xd].values
y_vals = df[yd].values

nmad = 1.48 * np.median(np.abs((y_vals - x_vals) - np.median(y_vals - x_vals)) / (1 + x_vals))
nmad = str(round(nmad, 4))

sd = np.std(x_vals - y_vals)
sd = str(round(sd, 4))

n = len(df)

# ----- Aesthetics -----

ax.set_xlim(xlim); ax.set_ylim(ylim)
ax.set_xticks(xtick); ax.set_yticks(ytick)

xticks = ax.xaxis.get_major_ticks(); yticks = ax.yaxis.get_major_ticks()
xticks[0].label1.set_visible(False); yticks[0].label1.set_visible(False)

ax.tick_params(axis = "x", direction = "in")
ax.tick_params(axis = "y", direction = "in")

ax.set_facecolor('#e0e8ff')

ax.axhline(2, color = 'w', linewidth = 1, linestyle = '--', zorder = 0)
ax.axvline(2, color = 'w', linewidth = 1, linestyle = '--', zorder = 0)

# ----- Labels -----

ax.set_xlabel('Spectroscopic Redshift', size = '17'); ax.set_ylabel('Photometric Redshift', size = '17')
ax.xaxis.labelpad = 15; ax.yaxis.labelpad = 15

ax.legend(loc = 'upper left', fontsize = '15', frameon = True)

ax.text(0.1, 3.25, f'$\sigma_{{NMAD}}$ = {nmad}', fontsize = 13, color = 'k')
ax.text(0.1, 3.05, f'$\sigma$ = {sd}', fontsize = 13, color = 'k')
ax.text(0.1, 2.85, f'$N$ = {n}', fontsize = 13, color = 'k')

# ----- Inset Histogram -----

ax_inset = inset_axes(ax, width = "65%", height = "65%", loc = "lower right", bbox_to_anchor = (0.55, 0.1, 0.4, 0.4), bbox_transform = ax.transAxes)

norm_diff = (y_vals - x_vals) / (1 + x_vals)

ax_inset.hist(norm_diff, bins = 45, color = '#e0e8ff', edgecolor = 'k', histtype = 'stepfilled', linewidth = 1)
ax_inset.set_xlabel('Normalized Difference')
ax_inset.set_xlim(-0.25, 0.25)

ax_inset.tick_params(axis = 'both', direction = 'in', which = 'both')

for spine in ax_inset.spines.values():
    spine.set_edgecolor('k')
    spine.set_linewidth(1.5)

# ----- Save and Output -----
    
fig.savefig('/Users/jess/Desktop/git_mphil/outputs/misc/z_relation.png', bbox_inches = 'tight', dpi = 300, transparent = False)

plt.show()