# coding: utf-8
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib import rc
import matplotlib
import scipy
import scipy.stats
from scipy.stats import gaussian_kde

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


fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

def scatter(z,x,y,zn,xn,yn):

	ax1.scatter(z, x, y)
	ax1.set_xlabel(r'z (m)')
	ax1.set_ylabel(r'x (m)')
	ax1.set_zlabel(r'y (m)')
	ax1.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	# ax1.set_xlim([-0.00007,0.00007])
	# ax1.set_ylim([-0.0005,0.0005])
	# ax1.set_zlim([-0.0005,0.0005])

	ax2.scatter(zn, xn, yn)
	ax2.set_xlabel(r'z (m)')
	ax2.set_ylabel(r'x (m)')
	ax2.set_zlabel(r'y (m)')
	ax2.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	# ax2.set_xlim([-0.00007,0.00007])
	# ax2.set_ylim([-0.0005,0.0005])
	# ax2.set_zlim([-30,10])
	# fig = plt.gcf()
	# fig.set_size_inches(18.5,10.5)
	# plt.savefig('test2.png',dpi=150)
	
	#COMMON TITLE
	# pyplot.suptitle(r'Initial and final distributions \\ \\ $n_1$ = turns with $V_{cc} = 0$, $n_2$ = voltage ramping turns, $n_3$ = turns in plateau, $n_4$ = turns from plateau to failure voltage ($n_1=100$, $n_2=5$, $n_3=2$, $n_4=1$)\\ \\ 10 tracking turns of 100 packs of 64 particles. Flat distribution in the x plane at $4\sigma$, gaussian in the y plane at $3 \sigma$ ', fontsize=20)




