# ----- Import Packages -----

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# ----- Function Body -----

def bpt(datasets, xd, yd, masks = None, save_path = None, dataset_names = None, colour_bar = None):
    num_datasets = len(datasets)

    fig, axs = plt.subplots(nrows = 1, ncols = num_datasets, sharey = True, figsize = (30, 10))
    plt.subplots_adjust(wspace = 0.0)

    if num_datasets == 1:
        axs = [axs]

    # -- BPT Demarcations --
      
    x1 = np.linspace(-2, 0, 100)
    x2 = np.linspace(-2, 0.3, 100)
    y1 = 0.61 / (x1 - 0.05) + 1.3
    y2 = 0.61 / (x2 - 0.47) + 1.19

    # -- Plot Parameters --

    kde_params = {'cmap': 'Greys', 'fill': False, 'alpha': 0.7, 'zorder': 0, 'linewidths': 2}

    scatter_params = {
        'b_param': {'s': 180, 'color': 'xkcd:periwinkle blue', 'marker': 's', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 3},
        'g_param': {'s': 160, 'color': 'xkcd:hospital green', 'marker': 'D', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 3},
        'r_param': {'s': 150, 'color': 'xkcd:salmon', 'marker': 'o', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 3},
    }

    white_params = {
        'bw_param': {'s': 230, 'color': 'xkcd:white', 'marker': 's', 'edgecolor': 'w', 'linewidth': 2, 'zorder': 3},
        'gw_param': {'s': 210, 'color': 'xkcd:white', 'marker': 'D', 'edgecolor': 'w', 'linewidth': 2, 'zorder': 3},
        'rw_param': {'s': 200, 'color': 'xkcd:white', 'marker': 'o', 'edgecolor': 'w', 'linewidth': 2, 'zorder': 3},
    }

    agn_types = ['xray_agn', 'radio_agn', 'ir_agn']
    agn_labels = {'xray_agn': 'X-Ray AGN', 'radio_agn': 'Radio AGN', 'ir_agn': 'Infrared AGN'}

    # -- Masks --

    scatter_plots = []
    global_min = np.inf
    global_max = -np.inf

    for i, df in enumerate(datasets):

        if colour_bar in df.columns:

            min_val = df[colour_bar].min()
            max_val = df[colour_bar].max()

            if min_val < global_min:
                global_min = min_val

            if max_val > global_max:
                global_max = max_val

    for i, (ax, df, dataset_name) in enumerate(zip(axs, datasets, dataset_names)):

        for mask in masks:

            condition, val, condition_type = mask

            if condition_type == 'geq':
                mask_condition = df[condition] >= val

            elif condition_type == 'leq':
                mask_condition = df[condition] <= val

            elif condition_type == 'bool':
                mask_condition = df[condition] == val

            else:
                raise ValueError(f"Unknown condition type: {condition_type}")

            df = df[mask_condition]

        # -- KDE --
            
        agn_columns_available = all(agn in df.columns for agn in agn_types)

        if agn_columns_available and colour_bar is None:
            sns.kdeplot(x = xd[i], y = yd[i], data = df[df['agn'] == 0], warn_singular = False, **kde_params, ax = ax)

        # -- White and RGB Scatter Plots, Respectively --
            
        if colour_bar:

            scatter = ax.scatter(

                x = df[xd[i]], 
                y = df[yd[i]], 
                c = df[colour_bar], 
                cmap = 'winter',
                s = 40,
                vmin = global_min,
                vmax = global_max,
                zorder = 3
            )

            scatter_plots.append(scatter)

        else:

            if agn_columns_available:

                for agn_type, w_param in zip(agn_types, white_params.values()):
                    ax.scatter(

                        x = df.loc[df[agn_type] == 1, xd[i]], 
                        y = df.loc[df[agn_type] == 1, yd[i]], 
                        **w_param
                    )

                for agn_type, rgb_param in zip(agn_types, scatter_params.values()):
                    ax.scatter(

                        x = df.loc[df[agn_type] == 1, xd[i]], 
                        y = df.loc[df[agn_type] == 1, yd[i]], 
                        label = agn_labels.get(agn_type, agn_type), 
                        **rgb_param
                    )

            else:

                ax.scatter(x = df[xd[i]], y = df[yd[i]], c = 'xkcd:white', s = 100, zorder = 3, edgecolor = 'w', linewidth = 2)
                ax.scatter(x = df[xd[i]], y = df[yd[i]], c = 'xkcd:periwinkle blue', s = 90, zorder = 3, edgecolor = 'k', linewidth = 0.5)
                ax.scatter(x = df[xd[i]], y = df[yd[i]], c = 'xkcd:periwinkle blue', s = 65, zorder = 3)

        # -- General Aesthetics --
                
        ax.set_xlim([-2, 1]); ax.set_ylim([-1, 1.5])
        ax.set_xticks(np.arange(-2, 1, 0.5)); ax.set_yticks(np.arange(-1, 1.5, 0.5))
        ax.tick_params(axis = "x", direction = "in"); ax.tick_params(axis = "y", direction = "in")

        xticks = ax.xaxis.get_major_ticks(); yticks = ax.yaxis.get_major_ticks()
        xticks[0].label1.set_visible(False); yticks[0].label1.set_visible(False)

        ax.set_facecolor('#e0e8ff')
        ax.axhline(0.25, color = 'w', linewidth = 1, linestyle = '--', zorder = 1)
        ax.axvline(-0.5, color = 'w', linewidth = 1, linestyle = '--', zorder = 1)
        ax.xaxis.labelpad = 15; ax.yaxis.labelpad = 15

        # -- Axes Labels and Legend --

        ax.set_xlabel('$log ([NII]/H\\alpha)$', size = '20')

        if i == 0:
            ax.set_ylabel('$log ([OIII]/H\\beta)$', size = '20')

        if colour_bar is None and i == 0 and agn_columns_available:
            ax.legend(loc = 'upper right', fontsize = '15', frameon = True)

        ax.text(0.75, -0.75, dataset_name, fontsize = 20, ha = 'right')

        ax.text(-1.1, 0, 'HII', fontsize = 17, ha = 'right')
        ax.text(0.2, 0.75, 'AGN', fontsize = 17, ha = 'right')
        ax.text(-0.015, -0.34, 'Comp', fontsize = 17, ha = 'right')

        # -- BPT Demarcations --

        ax.plot(x1, y1, color = 'w', linewidth = 3.5, zorder = 2)
        ax.plot(x2, y2, color = 'w', linewidth = 3.5, zorder = 2)

        ax.plot(x1, y1, color = 'k', linewidth = 1.5, zorder = 2)
        ax.plot(x2, y2, color = 'k', linewidth = 1.5, zorder = 2)

    if colour_bar and scatter_plots:
       
        if hasattr(axs, 'ravel'):
            cbar = plt.colorbar(scatter_plots[0], ax = axs.ravel().tolist(), label = colour_bar)

        else:
            cbar = plt.colorbar(scatter_plots[0], ax = axs, label = colour_bar)
        cbar.ax.tick_params(labelsize = 15)

    if save_path:
        fig.savefig(save_path, bbox_inches = 'tight', dpi = 300, transparent = False)

    plt.show()