import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
from matplotlib import cm
import numpy

import sys
sys.path.append("../../../private/simulations/python_plotting/")

import distributionx
import distributiony
import distributionxy
import distributionzy
import distributionzx
import distributionze
import distr_3D


def plot_distributions(dist0, distn):
	#INITIAL DISTRIBUTION
	
	data0 	= np.loadtxt(dist0,delimiter=',',dtype=str)
	x		=	[]
	xp		=	[]
	y		=	[]
	yp		=	[]
	z		=	[]
	e		=	[]
	for	values in data0:
		x.append(float(values[0]))
		xp.append(float(values[1]))
		y.append(float(values[2]))
		yp.append(float(values[3]))
		z.append(float(values[4]))
		e.append(float(values[5]))


	#FINAL DISTRIBUTION
	datan 	= np.loadtxt(distn,delimiter=',',dtype=str)
	xn		=	[]
	xpn		=	[]
	yn		=	[]
	ypn		=	[]
	zn		=	[]
	en		=	[]
	for	values in datan:
		xn.append(float(values[0]))
		xpn.append(float(values[1]))
		yn.append(float(values[2]))
		ypn.append(float(values[3]))
		zn.append(float(values[4]))
		en.append(float(values[5]))


	# distributionx.scatter(x,xp,xn,xpn)
	# distributiony.scatter(y,yp,yn,ypn)
	# distributionxy.scatter(x,y,xn,yn)
	# distributionzy.scatter(z,y,zn,yn)
	# distributionzx.scatter(z,x,zn,xn)
	# distributionze.scatter(z,e,zn,en)
	distr_3D.scatter(z,x,xp,zn,xn,xpn)


	show()