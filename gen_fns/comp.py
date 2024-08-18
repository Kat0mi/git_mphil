# ---------- Redshift vs Stellar Mass ----------

from pkg import *

combined_data = pd.concat([cdfs, cos, uds])
filtered_dataset = combined_data[combined_data['true_agn'] == 1]

fig, ax = plt.subplots(figsize = (10, 10))



# ----- Plot Loops & Variable Stand-Ins -----

df = combined_data

df['z'] = np.where(df['z_spec'] == -99, df['z_peak'], df['z_spec'])

xd, yd = 'z', 'lmass'

xlim, ylim = [0, 3.5], [7, 12]
xtick, ytick = np.arange(0, 3.5, 1), np.arange(7, 12, 1)



# ----- Plot Loops Continued -----

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

ax.scatter(x = df.loc[df['agn'] == 0, xd], y = df.loc[df['agn'] == 0, yd],
    s = 50, color = 'white', marker = 'o', linewidth = 0.5, zorder = 1)

ax.scatter(x = df.loc[df['agn'] == 0, xd], y = df.loc[df['agn'] == 0, yd], label = 'All Sources',
    s = 30, color = 'white', edgecolor = 'black', marker = 'o', linewidth = 0.6, zorder = 1)

# ----- Mass Cut and Completeness -----

ax.plot([0, 3.5], [9.75, 9.75], linestyle = '--', dashes = (10, 5), color = 'k', zorder = 4, linewidth = 2)
ax.fill_between([0, 3.5], 9.75, 12, color = 'none', edgecolor = 'xkcd:salmon', hatch = 'x', zorder = 1)

x = np.linspace(0, 3.5, 100)
y = 6.78 + 4.01 * x - 2.27 * x ** 2 + 0.57 * x ** 3 - 0.05 * x ** 4

plt.plot(x, y, color = 'white', linestyle = '-', linewidth = 4, zorder = 6)
plt.plot(x, y, color = 'red', linestyle = '--', linewidth = 1.5, zorder = 6)


# ----- Aesthetics -----
    
ax.set_xlim(xlim); ax.set_ylim(ylim)
ax.set_xticks(xtick); ax.set_yticks(ytick)

xticks = ax.xaxis.get_major_ticks(); yticks = ax.yaxis.get_major_ticks()
xticks[0].label1.set_visible(False); yticks[0].label1.set_visible(False)

ax.tick_params(axis = "x", direction = "in"); ax.tick_params(axis = "y", direction = "in")

ax.set_facecolor('#e0e8ff')

# ----- Labels -----

ax.set_xlabel('Redshift', size = '17'); ax.set_ylabel(f'$log(M_{{*}} / M_{{\odot}})$', size = '17')
ax.xaxis.labelpad = 15; ax.yaxis.labelpad = 15

ax.legend(loc = 'lower right', fontsize = '15', frameon = True)


fig.savefig('/Users/jess/Desktop/git_mphil/outputs/misc/z_lmass_comp.png', bbox_inches = 'tight', dpi = 300, transparent = False)

plt.show()