# --------------------------------------------------------------------------------------------------------------
# BEAM DISTRIBUTION GENERATOR
# ANDREA SANTAMARIA
# LAST MODFIIED: 25/08/2014
# This script generates a full particle distribution at the IP, as an input for the collimation block in SixTrack
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# Import libraries and introduce abbreviations
# --------------------------------------------------------------------------------------------------------------
import numpy as np
import scipy as sp
import scipy.stats as stats
import matplotlib
from matplotlib.pyplot import *
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import ticker
from math import *


fig 		= figure()
ax 			= fig.add_subplot(1, 1, 1)

# --------------------------------------------------------------------------------------------------------------
# Text characteristics of the plot
# --------------------------------------------------------------------------------------------------------------
params 		= {	'backend': 'pdf',
	  		'font.size':20,	
          	'axes.labelsize': 20,
          	'legend.fontsize': 16,
          	'xtick.labelsize': 20,
          	'ytick.labelsize': 20,
	  		'text.usetex':True,
        	 } 
# --------------------------------------------------------------------------------------------------------------
# Activate LaTeX 
# --------------------------------------------------------------------------------------------------------------        
rc('text.latex', preamble=r'\usepackage{cmbright}')
matplotlib.rcParams.update(params)

def dist_generator(outfile, particles, emittance, beta, alpha, bunch, spread):

	# --------------------------------------------------------------------------------------------------------------        
	# Open file where we will write the distribution data (x, x', y, y', z, E)
	# --------------------------------------------------------------------------------------------------------------        

	f 			= open(outfile,'w')

	# --------------------------------------------------------------------------------------------------------------
	# Beam Parameters
	# --------------------------------------------------------------------------------------------------------------

	# Proton mass [eV/c^2], energy [eV], number of particles, relativistic gamma, relativistic beta
	# --------------------------------------------------------------------------------------------------------------
	mp 			= 0.938272046e9
	Ep			= 7e12
	n_part		= particles
	gamma		= Ep/mp
	beta_r 		= sqrt(gamma**2 -1)/gamma

	print 'Relativistic Gamma 		= %E'% gamma
	print 'Relativistic Beta 		= %E'% beta_r

	# Transverse Normalised Emittances [m . rad]
	# --------------------------------------------------------------------------------------------------------------
	em_x 		= emittance					# normalised
	em_y 		= em_x
	emn_x		= em_x/(beta_r*gamma)		# geometric
	emn_y		= em_y/(beta_r*gamma)	

	print 'emn_x 					= %E [m . rad]'% emn_x
	print 'emn_y 					= %E [m . rad]'% emn_y

	# The normalised emittance does not change as a function of energy and so can track beam degradation if the 
	# particles are accelerated.

	# Twiss Parameters [m] (round beams)
	# --------------------------------------------------------------------------------------------------------------
	beta_x		= beta						# Ratio of beam dimension and beam divergence in a symmetry point, 
	beta_y		= beta_x					# associated to the transverse size of the beam. Beta star.

	print 'beta_x 					= %E [m] '% beta_x
	print 'beta_y 					= %E [m] '% beta_y

	alpha_x		= alpha 					# Describes how strong x and x' are correlated. 
	alpha_y		= alpha_x 					# alpha=0 --> beam has minimum or maximum

	print 'alpha_x 				= %E [m] '% alpha_x
	print 'alpha_y 				= %E [m] '% alpha_y

	gamma_x		= (1 + (alpha_x)**2)/beta_x
	gamma_y		= (1 + (alpha_y)**2)/beta_y

	print 'gamma_x 				= %E [m] '% gamma_x
	print 'gamma_y 				= %E [m] '% gamma_y

	# RMS Bunch length [m], RMS energy spread [%] (RMS = root mean square)
	# --------------------------------------------------------------------------------------------------------------
	sigma_z		= bunch
	sigma_E		= spread
	em_z		= sigma_z*sigma_E

	print 'em_z 					= %E [m . rad]'% em_z

	# Standard Deviations
	# --------------------------------------------------------------------------------------------------------------
	sigma_x		= sqrt(beta_x*emn_x)
	sigma_y		= sqrt(beta_y*emn_y) 		# beam half width

	print 'sigma_x 				= %E [m] '% sigma_x
	print 'sigma_y 				= %E [m] '% sigma_y


	sigma_px	= sqrt(gamma_x*emn_x) 		# beam divergence
	sigma_py	= sqrt(gamma_y*emn_y)

	print 'sigma_px 				= %E [m] '% sigma_px
	print 'sigma_py 				= %E [m] '% sigma_py


	# --------------------------------------------------------------------------------------------------------------
	# Writing the distribution file
	# --------------------------------------------------------------------------------------------------------------
	factor = 1

	x 		= np.zeros((n_part))
	xp 		= np.zeros((n_part))
	y 		= np.zeros((n_part))
	yp 		= np.zeros((n_part))
	t 		= np.zeros((n_part))
	pt 		= np.zeros((n_part))

	for i in range(0, n_part):
	  number  = np.random.normal(0, 1)
	  number2 = np.random.normal(0, 1)
	  number3 = np.random.normal(0, 1)
	  number4 = np.random.normal(0, 1)
	  number5 = np.random.normal(0, 1)
	  number6 = np.random.normal(0, 1) 
	  
	  x[i]  = factor*sigma_x*number
	  xp[i] = factor*number2*sqrt(emn_x/beta_x)-(alpha_x*(x[i]/beta_x))
	  
	  y[i]  = factor*sigma_y*number3
	  yp[i] = factor*number4*sqrt(emn_y/beta_y)-(alpha_y*(y[i]/beta_y))
	  
	  t[i]  = factor*number5*sigma_z
	  pt[i] = factor*number6*sigma_E
	  
	  f.write('%12.10f %12.10f %12.10f %12.10f %12.10f %12.10f\n' % (x[i],xp[i],y[i],yp[i],1000*t[i],(Ep+pt[i]*Ep)/1e6))

	f.close()
	  