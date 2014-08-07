# coding: utf-8
import matplotlib 
from matplotlib.pyplot import *
from matplotlib import rc
from matplotlib import cm
from matplotlib import gridspec
import numpy as np
import scipy
import scipy.stats
from scipy.stats import gaussian_kde
from mpl_toolkits.axes_grid1 import ImageGrid
from matplotlib import pyplot



params = {'backend': 'pdf',
	  	'font.size':20,	
          'axes.labelsize': 20,
          'legend.fontsize': 16,
          'xtick.labelsize': 20,
          'ytick.labelsize': 20,
	  'text.usetex':True,
         } 
rc('text.latex', preamble=r'\usepackage{cmbright}')
matplotlib.rcParams.update(params)

fig=figure()

ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)

# ax1 = subplot2grid((1, 4), (0, 0), colspan=1)
# ax2 = subplot2grid((1, 4), (0, 2), colspan=1)
# ax3 = subplot2grid((1, 4), (0, 1), colspan=1)
# ax4 = subplot2grid((1, 4), (0, 3), colspan=1)



def scatter(a,b,d,e):

	#FIRST PLOT (INITIAL CONDITIONS)
	xxp = np.vstack([a,b])
	t1 = gaussian_kde(xxp)(xxp)

	ax1.scatter(a,b,c=t1)
	ax1.set_xlabel(r'z(m)')
	ax1.set_ylabel(r"$y$(rad)")
	# ax1.set_xlim([-0.00007,0.00007])
	ax1.set_ylim([-0.0002,0.0002])
	ax1.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax1.grid(b=True, which='major',linestyle='--')
	
	#SECOND PLOT (FINAL CONDITIONS)
	xxpn = np.vstack([d,e])
	t2 = gaussian_kde(xxpn)(xxpn)

	ax2.scatter(d,e,c=t2)
	ax2.set_xlabel(r'z(m)')
	ax2.set_ylabel(r"$y$(rad)")
	# ax2.set_xlim([-0.00007,0.00007])
	ax2.set_ylim([-0.0002,0.0002])
	ax2.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax2.grid(b=True, which='major',linestyle='--')

	#COMMON TITLE
	pyplot.suptitle('Initial and final particle distributions', fontsize=30)
	
	#COLORBARS
	# im1=imshow(xxp, vmin=0, vmax=1)
	# cb1=colorbar(im1, cax=ax3)

	# im2=imshow(xxpn, vmin=0, vmax=1)
	# cb2colorbar(im2, cax=ax4)