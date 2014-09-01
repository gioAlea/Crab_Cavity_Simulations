# --------------------------------------------------------------------------------------------------------------
# BEAM DISTRIBUTION PLOT
# ANDREA SANTAMARIA
# LAST MODFIIED: 26/08/2014
# This script plots the generated distribution
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
from collections import Counter
import pylab as P
import scipy.stats
from scipy.stats import gaussian_kde
from mpl_toolkits.axes_grid1 import ImageGrid
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


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

def beam_histogram(n_part, variable, string):

	fig 		= figure()
	ax 			= fig.add_subplot(1, 1, 1)

	mu 			= np.mean(variable)
	sigma 		= np.std(variable)

	# To put it in units of sigma 
	# --------------------------------------------------------------------------------------------------------------
	var_sigma	= variable/sigma

	# --------------------------------------------------------------------------------------------------------------
	# Compute the best number of bins 
	# --------------------------------------------------------------------------------------------------------------

	# Interquartile range (IQR)
	# --------------------------------------------------------------------------------------------------------------
	IQR 		= np.percentile(var_sigma, 0.75) - np.percentile(var_sigma, 0.25)

	# Bin size following the Freedman Diaconis rule
	# --------------------------------------------------------------------------------------------------------------
	bin_size 	= 2 * IQR * n_part**(-1.0/3)
	print 'Bin size = %s'% bin_size

	# Number of bins
	# --------------------------------------------------------------------------------------------------------------
	nbins 		= int(max(var_sigma) - min(var_sigma) / (bin_size))
	print 'Number of bins= %s'% nbins

	# --------------------------------------------------------------------------------------------------------------
	# Plot Histogram of Samples
	# --------------------------------------------------------------------------------------------------------------
	n, bins, patches = P.hist((var_sigma), bins = nbins - nbins/3, normed = True, histtype = 'stepfilled', label = 'Histogram of the samples')
	P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

	# --------------------------------------------------------------------------------------------------------------
	# Plot the Probability Density Function
	# --------------------------------------------------------------------------------------------------------------
	mu_new			= np.mean(var_sigma)
	sigma_new		= np.std(var_sigma)
	y 				= P.normpdf(bins, mu_new, sigma_new)
	P.plot(bins, y, 'k--', linewidth=1.5, label = 'Probability Density Function')

	density = gaussian_kde(var_sigma)  # your data
	xgrid = np.linspace(min(var_sigma), max(var_sigma), n_part)   
	plt.plot(xgrid, density(xgrid),'k--', color = 'red', linewidth=1.5, label = 'Kernel Density Estimation Method')

	# Horizontal axis
	# --------------------------------------------------------------------------------------------------------------
	plt.xlabel(r'%s [$\sigma$]'%string)
	plt.ticklabel_format(style = 'sci', axis = 'x', scilimits = (0,0))
	plt.xlim(min(var_sigma), max(var_sigma))
	# plt.grid(b = True, which = 'both', axis = 'both', linestyle = '--')

	# Vertical axis
	# --------------------------------------------------------------------------------------------------------------
	plt.ylabel(r'Normalized beam profile')
	# ax.set_yscale('log')
	# plt.ylim(0, max(pdf_fitted))
	# plt.grid(b = True, which = 'minor', axis = 'both', linestyle = '--')
	
	# Title, legends and annotations
	# --------------------------------------------------------------------------------------------------------------
	# title 		= 'Distribution in : particles = %.0f, $\mu$ = %E, $\sigma$ = %E'%(n_part,mu,sigma)
	# plt.title(title)
	plt.legend(loc = 'upper left')
	plt.text((max(var_sigma)/2) + (max(var_sigma)/14), max(y)/2 + max(y)/3.0, r'Particles = %.0f'%n_part)
	plt.text((max(var_sigma)/2) + (max(var_sigma)/14), max(y)/2 + max(y)/3.7 , r'$\mu$ = %E'%mu)
	plt.text((max(var_sigma)/2) + (max(var_sigma)/14), max(y)/2 + max(y)/4.5, r'$\sigma$ = %E'%sigma)   

	

def beam_profile(n_part, variable, string):

	fig 		= figure()
	ax 			= fig.add_subplot(1, 1, 1)

	mu 			= np.mean(variable)
	sigma 		= np.std(variable)

	# To put it in units of sigma 
	# --------------------------------------------------------------------------------------------------------------
	var_sigma	= variable/sigma

	mu_new 		= np.mean(var_sigma)
	sigma_new 	= np.std(var_sigma)

	# --------------------------------------------------------------------------------------------------------------
	# Compute the best number of bins 
	# --------------------------------------------------------------------------------------------------------------

	# Interquartile range (IQR)
	# --------------------------------------------------------------------------------------------------------------
	IQR 		= np.percentile(var_sigma, 0.75) - np.percentile(var_sigma, 0.25)

	# Bin size following the Freedman Diaconis rule
	# --------------------------------------------------------------------------------------------------------------
	bin_size 	= 2 * IQR * n_part**(-1.0/3)
	print 'Bin size = %s'% bin_size

	# Number of bins
	# --------------------------------------------------------------------------------------------------------------
	nbins 		= int(max(var_sigma) - min(var_sigma) / (bin_size))
	print 'Number of bins= %s'% nbins

	# --------------------------------------------------------------------------------------------------------------
	# Plot Histogram of Samples
	# --------------------------------------------------------------------------------------------------------------
	n, bins, patches = P.hist((var_sigma), bins = nbins - nbins/3, normed = False, histtype = 'step', label = 'Beam Profile')
	P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)


	# Horizontal axis
	# --------------------------------------------------------------------------------------------------------------
	plt.xlabel(r'%s [$\sigma$]'%string)
	plt.ticklabel_format(style = 'sci', axis = 'x', scilimits = (0,0))
	plt.xlim(min(var_sigma), max(var_sigma))
	# plt.grid(b = True, which = 'both', axis = 'both', linestyle = '--')

	# Vertical axis
	# --------------------------------------------------------------------------------------------------------------
	plt.ylabel(r'Number of Particles')
	# ax.set_yscale('log')
	# plt.ylim(0, max(pdf_fitted))
	# plt.grid(b = True, which = 'minor', axis = 'both', linestyle = '--')
	
	# Title, legends and annotations
	# --------------------------------------------------------------------------------------------------------------
	# title 		= 'Distribution in : particles = %.0f, $\mu$ = %E, $\sigma$ = %E'%(n_part,mu,sigma)
	# plt.title(title)
	plt.legend(loc = 'upper left')
	plt.text((max(var_sigma)/2) + (max(var_sigma)/14), (n_part/20)/(sqrt(2*pi)*sigma_new), r'Particles = %.0f'%n_part)
	plt.text((max(var_sigma)/2) + (max(var_sigma)/14), (n_part/22)/(sqrt(2*pi)*sigma_new), r'$\sigma$ = %E'%sigma)


	# # Plot exactly what's in the file (no normalisation)
	# # --------------------------------------------------------------------------------------------------------------
	# c 			= Counter(var_sigma)
	# x_values 	= c.keys()
	# y_values	= c.values()
	# ax.bar(x_values, y_values, log = False, width = bin_size, align = 'center')
	# plt.xlabel(r'%s [$\sigma$]'%string)
	# plt.ylabel(r'Number of Particles')
	# plt.text((max(var_sigma)/2) + (max(var_sigma)/14), max(y)/2 + max(y)/3.1, r'Particles = %.0f'%n_part)
	
	
	
def beam_scatter(variable_1, variable_2, string_1, string_2):

	fig 		= figure()
	ax 			= fig.add_subplot(1, 1, 1)


	a = np.vstack([variable_1,variable_2])
	t = gaussian_kde(a)(a)						# This uses multiple normal distributions (gaussian functions) to estimate 
												# the probability density function. 
												# kde = kernel density estimation: is a non-parametric way to estimate the 
												# probability density function of a random variable.

	ax.scatter(variable_1, variable_2, c = t)
	ax.set_xlabel(r'%s'%string_1)
	ax.set_ylabel(r'%s'%string_2)
	ax.set_xlim([min(variable_1) + (min(variable_1)), max(variable_1) + (max(variable_1))])
	ax.set_ylim([min(variable_2) + (min(variable_2)), max(variable_2) + (max(variable_2))])
	ax.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax.grid(b=True, which='major',linestyle='--')

	

def beam_scatter_three(variable_1, variable_2, variable_3, string_1, string_2, string_3):

	fig 		= figure()
	ax 			= fig.add_subplot(111, projection='3d')

	ax.scatter(variable_1, variable_2, variable_3)
	ax.set_xlabel('%s'%string_1)
	ax.set_ylabel('%s'%string_2)
	ax.set_zlabel('%s'%string_3)
	ax.ticklabel_format(style='sci', axis='both', scilimits=(0,0))

	

def beam_scatter_comparison(variable_1, variable_2, variable_3, variable_4, string_1, string_2):

	fig 	= figure()
	ax1 	= fig.add_subplot(121)
	ax2 	= fig.add_subplot(122)

	#FIRST PLOT (INITIAL CONDITIONS)
	# --------------------------------------------------------------------------------------------------------------

	a 		= np.vstack([variable_1,variable_2])
	t		= gaussian_kde(a)(a)

	ax1.scatter(variable_1, variable_2, c = t)
	ax1.set_xlabel(r'%s'%string_1)
	ax1.set_ylabel(r'%s'%string_2)
	ax1.set_xlim([min(variable_1) + (min(variable_1)), max(variable_1) + (max(variable_1))])
	ax1.set_ylim([min(variable_2) + (min(variable_2)), max(variable_2) + (max(variable_2))])
	ax1.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax1.grid(b=True, which='major',linestyle='--')
	
	#SECOND PLOT (FINAL CONDITIONS)
	# --------------------------------------------------------------------------------------------------------------

	b = np.vstack([variable_3, variable_4])
	m = gaussian_kde(b)(b)

	ax2.scatter(variable_3, variable_4, c = m)
	ax2.set_xlabel(r'%s'%string_1)
	ax2.set_ylabel(r'%s'%string_2)
	ax2.set_xlim([min(variable_3) + (min(variable_3)), max(variable_3) + (max(variable_3))])
	ax2.set_ylim([min(variable_4) + (min(variable_4)), max(variable_4) + (max(variable_4))])
	ax2.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax2.grid(b=True, which='major',linestyle='--')

	#COMMON TITLE
	# --------------------------------------------------------------------------------------------------------------
	pyplot.suptitle('Initial and final particle distributions', fontsize=30)


def beam_scatter_comparison_three(variable_1, variable_2, variable_3, variable_4, variable_5, variable_6 ):

	fig = plt.figure()
	ax1 = fig.add_subplot(121, projection='3d')
	ax2 = fig.add_subplot(122, projection='3d')

	ax1.scatter(variable_3, variable_1, variable_2)
	ax1.set_xlabel(r'z (m)')
	ax1.set_ylabel(r'x (m)')
	ax1.set_zlabel(r'y (m)')
	ax1.ticklabel_format(style='sci', axis='both', scilimits=(0,0))


	ax2.scatter(variable_6, variable_4, variable_5)
	ax2.set_xlabel(r'z (m)')
	ax2.set_ylabel(r'x (m)')
	ax2.set_zlabel(r'y (m)')
	ax2.ticklabel_format(style='sci', axis='both', scilimits=(0,0))

	#COMMON TITLE
	# --------------------------------------------------------------------------------------------------------------
	pyplot.suptitle('Initial and final particle distributions', fontsize=30)






