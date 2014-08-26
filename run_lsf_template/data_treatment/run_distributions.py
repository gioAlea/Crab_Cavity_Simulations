# --------------------------------------------------------------------------------------------------------------
# BEAM DISTRIBUTION PLOT
# ANDREA SANTAMARIA
# LAST MODFIIED: 26/08/2014
# 
# This script allows you to:
# 	- Generate a full bunch
# 	- Plot it in 3D, plot it's histograms, fits, scatter plots and beam profiles
# 	- Treat several output files from SixTrack and compare them
# --------------------------------------------------------------------------------------------------------------

import sys
import os
import matplotlib
from matplotlib import pyplot as plt

sys.path.append("/afs/cern.ch/work/a/ansantam/private/simulations/python_modules/")

from data_treatment_module import *
from plot_initial_distribution import *
from distribution_generator import *

# --------------------------------------------------------------------------------------------------------------
# ------------------------------ONLY TO GENERATE A DISTRIBUTION-------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# Generate the particle distribution as input for SixTrack following the parameters (for protons and round beams): 
# Name of the file, number of particles, normalised emittance [m . rad], beta [m], alpha [m], bunch length [m], 
# energy spread [%]. The following parameters are for IP1.
# --------------------------------------------------------------------------------------------------------------
# dist_generator('./initial_dist.txt', 6400, 3.75e-6, 0.15, 0.0, 0.075, 1.129e-4)

# --------------------------------------------------------------------------------------------------------------
# Convert the SixTrack input to csv
# --------------------------------------------------------------------------------------------------------------
convert_to_csv('dist0.dat', 'dist0.csv')
convert_to_csv('distn.dat', 'distn.csv')



# --------------------------------------------------------------------------------------------------------------
# ------------------------------ONLY TO TREAT SEVERAL FILES-----------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# #TREAT THE INITIAL DISTRIBUTION
# concatenate1('../result/lowb.coll/dist0*.dat')
# convert_to_csv('out1.dat', 'dist0.csv')

# #TREAT THE FINAL DISTRIBUTION
# concatenate2('../result/lowb.coll/distn*.dat')
# convert_to_csv('out2.dat', 'distn.csv')

# #ERASE TEMP FILES
# os.remove(r'out1.dat')
# os.remove(r'out2.dat')

# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------
# Load each parameter from the initial distribution to use it in the plots
# --------------------------------------------------------------------------------------------------------------
data 	= 	np.loadtxt(r'dist0.csv', delimiter=',',dtype=str)
x		=	[]
xp		=	[]
y		=	[]
yp		=	[]
z		=	[]
e		=	[]
for	values in data:
	x.append	(float(values[0]))
	xp.append	(float(values[1]))
	y.append	(float(values[2]))
	yp.append	(float(values[3]))
	z.append	(float(values[4]))
	e.append	(float(values[5]))


# --------------------------------------------------------------------------------------------------------------
# Load each parameter from the final distribution to use it in the plots
# --------------------------------------------------------------------------------------------------------------
datan 	= 	np.loadtxt(r'distn.csv', delimiter=',',dtype=str)
xn		=	[]
xpn		=	[]
yn		=	[]
ypn		=	[]
zn		=	[]
en		=	[]
for	values in datan:
	xn.append	(float(values[0]))
	xpn.append	(float(values[1]))
	yn.append	(float(values[2]))
	ypn.append	(float(values[3]))
	zn.append	(float(values[4]))
	en.append	(float(values[5]))


# --------------------------------------------------------------------------------------------------------------
# Check that the number of lines = number of particles simulated
# --------------------------------------------------------------------------------------------------------------
n_part 		 = sum(1 for _ in data)
print 'Number of initial distribution = %s'% n_part

n_part_final = sum(1 for _ in datan)
print 'Number of particles final distribution = %s'% n_part_final

lost = n_part - n_part_final 
print 'Number of particles lost = %s'% lost


# --------------------------------------------------------------------------------------------------------------
# Plot the initial distribution generated
# --------------------------------------------------------------------------------------------------------------

# 3D overview of the bunch
# --------------------------------------------------------------------------------------------------------------
# beam_scatter_three(x, y, z, 'x', 'y', 'z')

# X coordinate
# --------------------------------------------------------------------------------------------------------------
# beam_histogram(n_part, x, 'x')
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
# beam_scatter(z, y, 'z', 'e')


# --------------------------------------------------------------------------------------------------------------
# Plot the initial and final distributions for comparison
# --------------------------------------------------------------------------------------------------------------

# 3D overview of the bunches
# --------------------------------------------------------------------------------------------------------------
# beam_scatter_comparison_three(x, y, z, xn, yn, zn)

# X coordinate
# --------------------------------------------------------------------------------------------------------------
# beam_scatter_comparison(x, xp, xn, xpn, 'x', 'xp')

# Y coordinate
# --------------------------------------------------------------------------------------------------------------

# beam_scatter_comparison(y, yp, yn, ypn, 'y', 'yp')

# Z coordinate
# --------------------------------------------------------------------------------------------------------------
# beam_scatter_comparison(z, e, zn, en, 'z', 'e')
# beam_scatter_comparison(z, x, zn, xn, 'z', 'x')
# beam_scatter_comparison(z, y, zn, yn, 'z', 'y')

plt.show()