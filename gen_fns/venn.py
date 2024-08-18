# ---------- AGN Venn Diagram ----------

# ----- Set-Up -----

from pkg import *

ir_agn_set, radio_agn_set, xray_agn_set = set(all.index[all['ir_agn'] == 1]), set(all.index[all['radio_agn'] == 1]), set(all.index[all['xray_agn'] == 1])

plt.figure(figsize = (10, 8))

venn = venn3([ir_agn_set, radio_agn_set, xray_agn_set], ('IR AGN', 'Radio AGN', 'X-Ray AGN'))

# ----- Aesthetics -----

# -- Custom Patterns --

for patch, pattern, color in zip(['100', '010', '001'], ['--', '\\\\\\', '||'], ['darkred', 'darkblue', 'darkgreen']):

    venn.get_patch_by_id(patch).set_edgecolor(color); venn.get_patch_by_id(patch).set_hatch(pattern); venn.get_patch_by_id(patch).set_linewidth(0)

def add_custom_hatch(ax, patch, hatch_pattern, color):

    path = patch.get_path(); patch_bbox = patch.get_extents()
    hatch = patches.PathPatch(path, facecolor = 'none', edgecolor = color, hatch = hatch_pattern, linewidth = 0.5, alpha = 0.2, transform = ax.transData, clip_on = True)
    ax.add_patch(hatch)

ax = plt.gca()

for patch, pattern, color in zip(['100', '010', '001'], ['--', '\\\\\\', '||'], ['darkred', 'darkblue', 'darkgreen']):
    add_custom_hatch(ax, venn.get_patch_by_id(patch), pattern, color)

# -- Labels --

for subset in venn.subset_labels:

    if subset:
        subset.set_fontsize(12)

for setlabel in venn.set_labels:

    setlabel.set_fontsize(14)

venn.get_label_by_id("100").set_x(-0.2); venn.get_label_by_id("100").set_y(0.28); venn.get_label_by_id("010").set_x(0.23); venn.get_label_by_id("010").set_y(0.28); venn.get_label_by_id("001").set_x(0.14); venn.get_label_by_id("001").set_y(-0.19)
venn.get_label_by_id("110").set_x(0.12); venn.get_label_by_id("110").set_y(0.29); venn.get_label_by_id("011").set_x(0.24); venn.get_label_by_id("011").set_y(0.15); venn.get_label_by_id("111").set_x(0.12); venn.get_label_by_id("111").set_y(0.19)

# -- Save and Output --

plt.savefig('/Users/jess/Desktop/git_mphil/outputs/misc/venn.png', bbox_inches = 'tight', dpi = 300, facecolor = 'white', transparent = False)

plt.show()