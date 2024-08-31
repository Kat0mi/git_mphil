# ---------- UVJ ----------

from pkg import *

combined_data = pd.concat([cdfs, cos, uds])
filtered_dataset = combined_data[combined_data['true_agn'] == 1]

fig, ax = plt.subplots(figsize = (12, 10))



# ----- Plot Loops & Variable Stand-Ins -----

df = all[(all['z'] >= 4) & (all['z'] <= 10) & (all['si'] != -999)]

xd, yd = 'V_J', 'U_V'

xlim, ylim = [0, 2.5], [0, 2.5]
xtick, ytick = np.arange(0, 2.5, 0.5), np.arange(0, 2.5, 0.5)

# -- SFG --

sns.kdeplot(x = xd, y = yd, data = df[df['agn'] == 0], warn_singular = False, **kde_params, ax = ax)

#- -- AGN --

for agn_type, w_param in zip(agn_types, w_params):

        ax.scatter(
            x = df.loc[df[agn_type] == 1, xd],
            y = df.loc[df[agn_type] == 1, yd],
            **w_param)
    
for agn_type, rgb_param in zip(agn_types, rgb_params):
       
        ax.scatter(
            x = df.loc[df[agn_type] == 1, xd],
            y = df.loc[df[agn_type] == 1, yd],
            label = agn_labels.get(agn_type, agn_type), 
            **rgb_param)



# ----- Boundaries & Region Labels -----
        
# -- SF/Dusty SF Boundary --

ax.plot([1.2, 1.2], [0, 1.6], 'w-', linewidth = 3)
ax.plot([1.2, 1.2], [0, 1.6], 'k--', linewidth = 1.5, dashes = (10, 5))

# -- Quiescent/SF Boundary --

ax.plot([-0.5, 0.85], [1.3, 1.3], 'w-', linewidth = 3)
ax.plot([0.85, 1.6], [1.3, 1.95], 'w-', linewidth = 3)
ax.plot([1.6, 1.6], [1.95, 2.5], 'w-', linewidth = 3)

ax.plot([-0.5, 0.85], [1.3, 1.3], 'k-', linewidth = 1.5)
ax.plot([0.85, 1.6], [1.3, 1.95], 'k-', linewidth = 1.5)
ax.plot([1.6, 1.6], [1.95, 2.5], 'k-', linewidth = 1.5)

# -- Colour Regions --

ax.fill_between([-0.5, 0.85, 1.6], [1.3, 1.3, 1.95], [2.5, 2.5, 2.5], color = 'xkcd:salmon', alpha = 0.05)
ax.fill_between([-0.5, 0.85, 1.2], [1.3, 1.3, 1.6], [0, 0, 0], color = 'xkcd:periwinkle blue', alpha = 0.05)
ax.fill_between([1.2, 1.6, 1.6, 2.6], [1.6, 1.95, 2.5, 2.5], [0, 0, 0, 0], color = 'xkcd:hospital green', alpha = 0.05)

# -- Region labels --

ax.text(0.1, 1.4, 'Quiescent', fontsize = 24, ha = 'left', color = 'xkcd:salmon')
ax.text(0.1, 0.1, 'Star Forming', fontsize = 24, ha = 'left', color = 'xkcd:periwinkle blue')
ax.text(2.4, 0.1, 'Dusty', fontsize = 24, ha = 'right', color = 'xkcd:hospital green')



# ----- Aesthetics -----
    
ax.set_xlim(xlim); ax.set_ylim(ylim)
ax.set_xticks(xtick); ax.set_yticks(ytick)

xticks = ax.xaxis.get_major_ticks(); yticks = ax.yaxis.get_major_ticks()
xticks[0].label1.set_visible(False); yticks[0].label1.set_visible(False)

ax.tick_params(axis = "x", direction = "in"); ax.tick_params(axis = "y", direction = "in")

# ----- Axes, Legend & Redshift Labels -----

ax.set_xlabel('V - J [AB]', size = '17'); ax.set_ylabel('U - V [AB]', size = '17')
ax.xaxis.labelpad = 15; ax.yaxis.labelpad = 15

ax.legend(loc = 'upper left', fontsize = '15', frameon = True)

ax.text(2.45, 2.4, 'z > 4', fontsize = 16, ha = 'right', color = 'k')


fig.savefig('/Users/jess/Desktop/git_mphil/outputs/misc/uvj/uvj_z_40.png', bbox_inches = 'tight', dpi = 300, transparent = False)