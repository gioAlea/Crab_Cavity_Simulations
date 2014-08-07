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


data 		= 	np.loadtxt(r'BPM1',delimiter=',',dtype=str)
x		=	[]
xp		=	[]
y		=	[]
yp		=	[]
z		=	[]
e		=	[]
de 		=	[]
for	values in data:
	x.append(float(values[0]))
	xp.append(float(values[1]))
	y.append(float(values[2]))
	yp.append(float(values[3]))
	z.append(float(values[4]))
	e.append(float(values[5]))
	de.append(float(values[6]))


ax1.plot(x,xp)
ax1.set_xlabel(r'x (mm)')
ax1.set_ylabel(r'x\'(mm)')
ax1.ticklabel_format(style='sci', axis='both', scilimits=(0,0))

ax2.plot(z,x)
ax2.set_xlabel(r'y (mm)')
ax2.set_ylabel(r'y \' (mm)')
ax2.ticklabel_format(style='sci', axis='both', scilimits=(0,0))

ax3.plot(z,e)
ax3.set_xlabel(r'z (mm)')
ax3.set_ylabel(r'E (MeV)')
ax3.ticklabel_format(style='sci', axis='both', scilimits=(0,0))

ax4.plot(z,de)
ax4.set_xlabel(r'z (mm)')
ax4.set_ylabel(r'dE (MeV)')
ax4.ticklabel_format(style='sci', axis='both', scilimits=(0,0))

show()



