# --------------------------------------------------------------------------------------------------------------
# BEAM DISTRIBUTION GENERATION AND PLOTTING
# ANDREA SANTAMARIA
# LAST MODFIIED: 02/09/2014
# 
# This script allows you to:
# 	- Generate a full bunch as SixTrack input
# 	- Plot it in 3D, plot it's histograms, fits, scatter plots and beam profiles
# --------------------------------------------------------------------------------------------------------------

import sys
import os
import matplotlib
from matplotlib import pyplot as plt

sys.path.append("/afs/cern.ch/work/a/ansantam/private/simulations/python_modules/")

from data_treatment_module import *
from plot_distributions_module import *
from distribution_generator_module import *

# --------------------------------------------------------------------------------------------------------------
# Generate the particle distribution as input for SixTrack following the parameters (for protons and round beams): 
# Name of the file, number of particles, normalised emittance [m . rad], beta [m], alpha [m], bunch length [m], 
# energy spread [%]. The following parameters are for IP1.
# --------------------------------------------------------------------------------------------------------------
dist_generator('./initial_dist.txt', 6400, 3.75e-6, 0.15, 0.0, 0.075, 1.129e-4)

# --------------------------------------------------------------------------------------------------------------
# Convert the SixTrack input to csv
# --------------------------------------------------------------------------------------------------------------
convert_to_csv('initial_dist.txt', 'initial_dist.csv')

# --------------------------------------------------------------------------------------------------------------
# Load your data
# --------------------------------------------------------------------------------------------------------------
(x,xp,y,yp,z,e) = np.loadtxt(r'initial_dist.csv', delimiter = ',', unpack=True)

# --------------------------------------------------------------------------------------------------------------
# Check that the number of particles is correct
# --------------------------------------------------------------------------------------------------------------
n_part = len(x)
print 'Number of particles initial distribution 	= %s'% n_part

# --------------------------------------------------------------------------------------------------------------
# Plot the initial distribution generated
# --------------------------------------------------------------------------------------------------------------

# 3D overview of the bunch
# --------------------------------------------------------------------------------------------------------------
# beam_scatter_three(x, y, z, 'x', 'y', 'z')

# X coordinate
# --------------------------------------------------------------------------------------------------------------
beam_histogram(n_part, x, 'x')
# beam_profile(n_part, x, 'x')

# beam_histogram(n_part, xp, 'xp')
# beam_profile(n_part, xp, 'xp')

# beam_scatter(x, xp, 'x', 'xp')

# Y coordinate
# --------------------------------------------------------------------------------------------------------------
# beam_histogram(n_part, y, 'y')
# beam_profile(n_part, y, 'y')

# beam_histogram(n_part, yp, 'yp')
# beam_profile(n_part, yp, 'yp')

# beam_scatter(y, yp, 'y', 'yp')

# Z coordinate
# --------------------------------------------------------------------------------------------------------------
# beam_histogram(n_part, z, 'z')
# beam_profile(n_part, z, 'z')

# beam_histogram(n_part, e, 'e')
# beam_profile(n_part, e, 'e')

# beam_scatter(zn, en, 'z', 'e')
# beam_scatter(z, x, 'z', 'e')
# beam_scatter(z, y, 'z', 'y')

plt.show()