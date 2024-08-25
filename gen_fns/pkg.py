# ---------- This script is used to import all the necessary packages and data files ----------

# Call using: from pkg import *

# ----- Imports -----

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as PathEffects
import tkinter as tk
import importlib.util
import inspect
import sys
import decimal



# ----- From -----

from numpy import cov
from astropy.io import fits
# from matplotlib_venn import venn3
from matplotlib.lines import Line2D
from sklearn.decomposition import PCA
from matplotlib.patches import PathPatch
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.gridspec import GridSpec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from tkinter import filedialog, simpledialog, messagebox
from sklearn.preprocessing import StandardScaler
from decimal import Decimal, getcontext
from astropy.stats import median_absolute_deviation



# ----- Data -----

cdfs = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_mphil', 'git_data', 'cdfs.csv'))
cos = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_mphil', 'git_data', 'cos.csv'))
uds = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_mphil', 'git_data', 'uds.csv'))

all = pd.concat([cdfs, cos, uds])



# ---------- Masks and Parameters ----------

# ----- Plot Parameters -----

kde_params = {'cmap': 'Greys', 'fill': False, 'alpha': 0.7, 'zorder': 0, 'linewidths': 2}

b_param, bw_param = {'s': 180, 'color': 'xkcd:periwinkle blue', 'marker': 's', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 3}, {'s': 230, 'color': 'xkcd:white', 'marker': 's', 'edgecolor': 'w', 'linewidth': 2, 'zorder': 3}
g_param, gw_param = {'s': 160, 'color': 'xkcd:hospital green', 'marker': 'D', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 3}, {'s': 210, 'color': 'xkcd:white', 'marker': 'D', 'edgecolor': 'w', 'linewidth': 2, 'zorder': 3}
r_param, rw_param = {'s': 150, 'color': 'xkcd:salmon', 'marker': 'o', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 3}, {'s': 200, 'color': 'xkcd:white', 'marker': 'o', 'edgecolor': 'w', 'linewidth': 2, 'zorder': 3}


# ----- Consistent Loop Parameters -----

rgb_params, w_params = [b_param, g_param, r_param], [bw_param, gw_param, rw_param]
datasets, fields = [cdfs, cos, uds], ['cdfs', 'cos', 'uds']
agn_types, agn_labels = ['xray_agn', 'radio_agn', 'ir_agn'], {'xray_agn': 'X-Ray AGN', 'radio_agn': 'Radio AGN', 'ir_agn': 'IR AGN'}