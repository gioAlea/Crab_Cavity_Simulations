# --------------------------------------------------------------------------------------------------------------
# BEAM DISTRIBUTION COMPARISON AFTER SIMULATION
# ANDREA SANTAMARIA
# LAST MODFIIED: 02/09/2014
# 
# This script allows you to:
# 	- Treat several output files from SixTrack and compare them
# --------------------------------------------------------------------------------------------------------------

import 	sys
import 	os
import 	matplotlib
from 	matplotlib import pyplot as plt

sys.path.append("/afs/cern.ch/work/a/ansantam/private/simulations/python_modules/")

from 	data_treatment_module import *
from 	plot_distributions_module import *

# --------------------------------------------------------------------------------------------------------------
# Treat the initial distribution files
#--------------------------------------------------------------------------------------------------------------
# concatenate1('/afs/cern.ch/work/a/ansantam/public/ramping_100_turns/result/lowb.coll.run1/dist0*.dat')
# convert_to_csv('out1.dat', 'dist0.csv')

# --------------------------------------------------------------------------------------------------------------
# Treat the final distribution files
# --------------------------------------------------------------------------------------------------------------
# concatenate2('/afs/cern.ch/work/a/ansantam/public/ramping_100_turns/result/lowb.coll.run1/distn*.dat')
# convert_to_csv('out2.dat', 'distn.csv')

# --------------------------------------------------------------------------------------------------------------
# Erase temp files
# --------------------------------------------------------------------------------------------------------------
# os.remove(r'out1.dat')
# os.remove(r'out2.dat')

# --------------------------------------------------------------------------------------------------------------
# Load each parameter from the initial distribution to use it in the plots
# --------------------------------------------------------------------------------------------------------------
(x, xp, y, yp, z, e) 		= np.loadtxt(r'dist0.csv', delimiter = ',', unpack=True)
(xn, xpn, yn, ypn, zn, en) 	= np.loadtxt(r'distn.csv', delimiter = ',', unpack=True)

# --------------------------------------------------------------------------------------------------------------
# Check that the number of lines = number of particles simulated and lost
# --------------------------------------------------------------------------------------------------------------
n_part 		 	= len(x)
print 'Number of particles initial distribution 	= %s'% n_part

n_part_final 	= len(xn)
print 'Number of particles final distribution 		= %s'% n_part_final

lost 			= n_part - n_part_final 
print 'Number of particles lost 					= %s'% lost

percentage_lost = (lost * 100) / n_part
print 'Percentage of particles lost 				= %s'% percentage_lost


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

# Histograms
# --------------------------------------------------------------------------------------------------------------
beam_histogram(n_part, x, 'x')
# beam_profile(n_part, x, 'x')

plt.show()