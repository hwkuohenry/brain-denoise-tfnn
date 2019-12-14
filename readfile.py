import numpy as np
import matplotlib.pyplot as plt
import math


### ===== Read Data ====== ###
filepath = 'data/101006/MNINonLinear/T2w.nii.gz/0/'
filename = 'tgt_img.npy'
img = np.load(filepath + filename) 

plt.figure()

