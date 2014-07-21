import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
from matplotlib import cm
import numpy

import distributionx
import distributiony
import distributionxy
import distributionzy
import distributionzx
import distributionze
import distr_3D



#INITIAL DISTRIBUTION
x	=	[]
xp	=	[]
y	=	[]
yp	=	[]
z	=	[]
e	=	[]
for	line in	open("dist0.dat"):
		values	=	line.strip("\n").split()
		x.append(float(values[0]))
		xp.append(float(values[1]))
		y.append(float(values[2]))
		yp.append(float(values[3]))
		z.append(float(values[4]))
		e.append(float(values[5]))


#FINAL DISTRIBUTION
xn	=	[]
xpn	=	[]
yn	=	[]
ypn	=	[]
zn	=	[]
en	=	[]
for	line in	open("distn.dat"):
		values	=	line.strip("\n").split()
		xn.append(float(values[0]))
		xpn.append(float(values[1]))
		yn.append(float(values[2]))
		ypn.append(float(values[3]))
		zn.append(float(values[4]))
		en.append(float(values[5]))


distributionx.scatter(x,xp,xn,xpn)
distributiony.scatter(y,yp,yn,ypn)
distributionxy.scatter(x,y,xn,yn)
distributionzy.scatter(z,y,zn,yn)
distributionzx.scatter(z,x,zn,xn)
distributionze.scatter(z,e,zn,en)
distr_3D.scatter(z,x,xp,zn,xn,xpn)


show()