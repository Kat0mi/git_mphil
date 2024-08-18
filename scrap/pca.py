# ---------- Principal Component Analysis (PCA) ----------

# ----- Step 1: Standardisation -----

# PCA is sensitive to variable variance, and so those those with larger ranges (e.g., between 0 and 100) will dominate over those with smaller ranges 
# (e.g., between 0 and 1). As such, standardisation is needed:

#                                                       z = (value - mean) / standard deviation



# ----- Step 2: Covariance Matrix Computation -----

# A covariance matrix is a p x p (where p = no. of dimensions) symmetric matrix that contains the covariances associated with all possible input 
# variable pairs, where the main diagonal contains the variances of each input variable. Correlated variables have a positive covariance, while
# inversely correlated variables have a negative covariance. A covariance matrix is thus nothing more than a table that summarises correlations 
# between all possible pairs.



# ----- Step 3: Compute Eigenvectors and Eigenvalues -----

# Eigenvectors (aka, the principal component; PC) indicate the direction in which the most variance occurs, while eigenvalues are coefficients that 
# quantify the amount of variance carried by each PC. Eigenvectors can be ranked in order of their eigenvalues, with the greatest eigenvalue
# corresponding to the first PC (i.e., PC1). The percentage of variance associated with a given component can be calculated by dividing its eigenvalue
# by the sum of eigenvalues.



# ----- Step 4: Create a Feature Vector -----

# A feature vector is a matrix containing the eigenvectors of features of interest. Components that carry a low percentage of overall variance may be
# excluded at this step, which will reduce dimensionality/information equivalent to that percentage. 



# ----- Step 5: Recast the Data Along the PC Axis -----

# In this step, we re-orient our data from the original axes to those represented by the PCs. This is done by multiplying the transpose of the 
# standardised dataset (SDS) acquired in step 1 by the transpose of the feature vector (FV) acquired in step 4:

# dataset = FV ^ T * SDS ^ T



# Source: https://builtin.com/data-science/step-step-explanation-principal-component-analysis

# ------------------------------------------------------------------------------------------------------------------------------------------------------

from pkg import *

# ----- Standardising Function -----

def standardise(data):

    for col in data.columns:

        if col not in exclude_cols:
            data[col] = (data[col] - data[col].mean()) / data[col].std()

    return data

# ----- Exclude Boolean Columns -----

exclude_cols = ['id', 'use', 'ir_agn', 'xray_agn', 'radio_agn', 'agn', 'true_agn']

# ----- Standardise Data -----

cdfs, cos, uds = cdfs.copy(), cos.copy(), uds.copy()

cdfs_std, cos_std, uds_std = standardise(cdfs.drop(columns=exclude_cols)), standardise(cos.drop(columns=exclude_cols)), standardise(uds.drop(columns=exclude_cols))

# ----- Numpy Array Conversion -----

cdfs_arr, cos_arr, uds_arr = np.nan_to_num(np.array(cdfs_std)), np.nan_to_num(np.array(cos_std)), np.nan_to_num(np.array(uds_std))

# ----- PCA -----

pca_cdfs, pca_cos, pca_uds = PCA(), PCA(), PCA()

cdfs_pca, cos_pca, uds_pca = pca_cdfs.fit_transform(cdfs_arr), pca_cos.fit_transform(cos_arr), pca_uds.fit_transform(uds_arr)

# ----- Recast Data -----

cdfs_pca_df = pd.DataFrame(cdfs_pca, columns=[f'PC{i+1}' for i in range(cdfs_pca.shape[1])])
cdfs_pca_df = pd.concat([cdfs[exclude_cols].reset_index(drop = True), cdfs_pca_df], axis = 1)

cos_pca_df = pd.DataFrame(cos_pca, columns=[f'PC{i+1}' for i in range(cos_pca.shape[1])])
cos_pca_df = pd.concat([cos[exclude_cols].reset_index(drop = True), cos_pca_df], axis = 1)

uds_pca_df = pd.DataFrame(uds_pca, columns=[f'PC{i+1}' for i in range(uds_pca.shape[1])])
uds_pca_df = pd.concat([uds[exclude_cols].reset_index(drop = True), uds_pca_df], axis = 1)

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# ----- Scatter Plot -----

plt.figure(figsize = (10, 10))


