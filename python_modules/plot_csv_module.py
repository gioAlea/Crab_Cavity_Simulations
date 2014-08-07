import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
from matplotlib import cm
import numpy

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
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(223)
ax3=fig.add_subplot(222)
ax4=fig.add_subplot(224)


# def plot_csv(normal, failure):
# 
def plot_csv(one, three, no_crabs):

	#1 SIGMA BUNCHLENGTH
	data1 		= 	np.loadtxt(one, delimiter=',',dtype=str)
	x		=	[]
	xp		=	[]
	y		=	[]
	yp		=	[]
	z		=	[]
	e		=	[]
	de 		=	[]
	for	values in data1:
		x.append(float(values[0]))
		xp.append(float(values[1]))
		y.append(float(values[2]))
		yp.append(float(values[3]))
		z.append(float(values[4]))
		e.append(float(values[5]))
		de.append(float(values[6]))


	ax1.scatter(x,xp, color = 'red', label = 'Bunchlength 1 ${\sigma}_z$')
	ax1.set_xlabel(r'x (mm)')
	ax1.set_ylabel(r'xp (mm)')
	ax1.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax1.grid(b=True, which='major',linestyle='--')
	# ax1.set_xlim([-150,150])
	# ax1.set_ylim([-150,150])
	ax1.legend(loc='upper right')

	ax2.scatter(z,x, color = 'red')
	ax2.set_xlabel(r'z (mm)')
	ax2.set_ylabel(r'x (mm)')
	ax2.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax2.grid(b=True, which='major',linestyle='--')
	# ax2.set_xlim([-150,150])
	# ax2.set_ylim([-150,150])

	ax3.scatter(z,e, color = 'red')
	ax3.set_xlabel(r'z (mm)')
	ax3.set_ylabel(r'E (MeV)')
	ax3.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax3.grid(b=True, which='major',linestyle='--')
	# ax3.set_xlim([-150,150])
	# ax3.set_ylim([-150,150])

	ax4.scatter(z,de, color = 'red')
	ax4.set_xlabel(r'z (mm)')
	ax4.set_ylabel(r'dE (MeV)')
	ax4.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax4.grid(b=True, which='major',linestyle='--')
	# ax4.set_xlim([-150,150])
	# ax4.set_ylim([-150,150])


	#FAILURE
	data2 		= 	np.loadtxt(three, delimiter=',',dtype=str)
	x		=	[]
	xp		=	[]
	y		=	[]
	yp		=	[]
	z		=	[]
	e		=	[]
	de 		=	[]
	for	values in data2:
		x.append(float(values[0]))
		xp.append(float(values[1]))
		y.append(float(values[2]))
		yp.append(float(values[3]))
		z.append(float(values[4]))
		e.append(float(values[5]))
		de.append(float(values[6]))


	ax1.scatter(x,xp, color = 'green', label = 'Bunchlength 3 ${\sigma}_z$')
	ax1.set_xlabel(r'x (mm)')
	ax1.set_ylabel(r'xp (mm)')
	ax1.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax1.grid(b=True, which='major',linestyle='--')
	# ax1.set_xlim([-150,150])
	# ax1.set_ylim([-150,150])
	ax1.legend(loc='upper right')

	ax2.scatter(z,x, color = 'green')
	ax2.set_xlabel(r'z (mm)')
	ax2.set_ylabel(r'x (mm)')
	ax2.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax2.grid(b=True, which='major',linestyle='--')
	# ax2.set_xlim([-150,150])
	# ax2.set_ylim([-150,150])

	ax3.scatter(z,e, color = 'green')
	ax3.set_xlabel(r'z (mm)')
	ax3.set_ylabel(r'E (MeV)')
	ax3.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax3.grid(b=True, which='major',linestyle='--')
	# ax3.set_xlim([-150,150])
	# ax3.set_ylim([-150,150])

	ax4.scatter(z,de, color = 'green')
	ax4.set_xlabel(r'z (mm)')
	ax4.set_ylabel(r'dE (MeV)')
	ax4.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax4.grid(b=True, which='major',linestyle='--')
	# ax4.set_xlim([-150,150])
	# ax4.set_ylim([-150,150])
	
	# NO CRABS
	data3 		= 	np.loadtxt(no_crabs, delimiter=',',dtype=str)
	x		=	[]
	xp		=	[]
	y		=	[]
	yp		=	[]
	z		=	[]
	e		=	[]
	de 		=	[]
	for	values in data3:
		x.append(float(values[0]))
		xp.append(float(values[1]))
		y.append(float(values[2]))
		yp.append(float(values[3]))
		z.append(float(values[4]))
		e.append(float(values[5]))
		de.append(float(values[6]))


	ax1.scatter(x,xp, color = 'blue', label = 'No Crabs')
	ax1.set_xlabel(r'x (mm)')
	ax1.set_ylabel(r'xp (mm)')
	ax1.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax1.grid(b=True, which='major',linestyle='--')
	# ax1.set_xlim([-150,150])
	# ax1.set_ylim([-150,150])
	ax1.legend(loc='upper right')

	ax2.scatter(z,x, color = 'blue')
	ax2.set_xlabel(r'z (mm)')
	ax2.set_ylabel(r'x (mm)')
	ax2.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax2.grid(b=True, which='major',linestyle='--')
	# ax2.set_xlim([-150,150])
	# ax2.set_ylim([-150,150])

	ax3.scatter(z,e, color = 'blue')
	ax3.set_xlabel(r'z (mm)')
	ax3.set_ylabel(r'E (MeV)')
	ax3.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax3.grid(b=True, which='major',linestyle='--')
	# ax3.set_xlim([-150,150])
	# ax3.set_ylim([-150,150])

	ax4.scatter(z,de, color = 'blue')
	ax4.set_xlabel(r'z (mm)')
	ax4.set_ylabel(r'dE (MeV)')
	ax4.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
	ax4.grid(b=True, which='major',linestyle='--')
	# ax4.set_xlim([-150,150])
	# ax4.set_ylim([-150,150])

	suptitle('Comparison of the effect of the CCs for different bunchlengths')
	# suptitle('Tracking of one particle during 600 turns, without collimation. Failure in 10 turns starting at the turn number 580. 3 sigma bunchlength')

	show()



