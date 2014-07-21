import numpy
import sys, datetime, os, random
from math import sqrt,cos,pi,sin
from string import split


# Open file to fill with tracking commands for PTC

f = open('./initDist.txt','w')


mp = 0.938272013e9
EN = 7e12

if len(sys.argv)>1: factor=float(sys.argv[1])
else: factor=1.0
print "Factor", factor

gammma= EN/mp
emitxn1=3.75e-6 # [m rad]
emityn1=3.75e-6 # [m rad]
emitxgeom= 0.503E-09 #emitxn1/sqrt(gammma**2 -1)
emitygeom= 0.503E-09 #emityn1/sqrt(gammma**2 -1)
#emitxgeom = # [m rad]
#emitygeom = # [m rad]
bbbeta=sqrt(gammma*gammma -1)/gammma
producto=bbbeta*gammma



print "Gamma relat:",gammma
print "Beta relat:",bbbeta
print "Gammarelat * Betarelat:",producto
print "Emit Geom Hor:",emitxgeom
print "Emit Geom Ver:",emitygeom
print "Emit Norm Hor1:",emitxn1
print "Emit Norm Ver1:",emityn1


betx  =  0.150654   # [m]
alfx  =  0.003268 # [-]
emitx =  emitxgeom#10e-9#50e-6         # [m rad]
dx    = 0.003449         # [m]
bety  = 0.150208    # [m]
alfy  = -0.000684 # [-]
emity =  emitygeom#10e-9#49e-6         # [m rad]
dy    =  0.000817           # [m]

sigmax = sqrt(betx*emitx)
sigmay = sqrt(bety*emity)

gammax = (1+alfx**2)/betx
gammay = (1+alfy**2)/bety

sigmaxp = sqrt(gammax*emitx)
print 'Sigma Xp', sigmaxp

sigmapx=sqrt(emitxgeom*gammax)
sigmapy=sqrt(emitygeom*gammay)

print "gammax:",gammax
print "gammay:",gammay
print ""

sigmal = 0.0755        # [m]
sigmap = 0.0001129     # [%]
emitz = sigmal*sigmap

print ""
print 'sigma_x:',sigmax,'[m]'
print 'sigma_Px:',sigmapx,'[m]'
print 'sigma_y:',sigmay,'[m]'
print 'sigma_Py:',sigmapy,'[m]'
print '5*sigma_x:',5*sigmax,'[m]'
print '5*sigma_y:',5*sigmay,'[m]'
print ""


print "emtiz:",emitz
print ""

# Number of particles to be generated

Npart = 6400


# Initialized arrays

x=numpy.zeros((Npart))
xp=numpy.zeros((Npart))
y=numpy.zeros((Npart))
yp=numpy.zeros((Npart))
t=numpy.zeros((Npart))
pt=numpy.zeros((Npart))


for i in range(0,Npart):
    number = random.gauss(0, 1)
    number2 = random.gauss(0, 1)
    number3 = random.gauss(0, 1)
    number4 = random.gauss(0, 1)
    number5 = random.gauss(0, 1)
    number6 = random.gauss(0, 1) # Gaussian distribution nominal sigma=0.6%
    number7 = random.uniform(-0.01,0.01) # Uniform -1% and 1%
    number8 = random.uniform(0,1)

    x[i]  = factor*sigmax*number
    xp[i] = factor*number2*sqrt(emitx/betx)-(alfx*(x[i]/betx))
    
    y[i]  = factor*sigmay*number3
    yp[i] = factor*number4*sqrt(emity/bety)-(alfy*(y[i]/bety))

    t[i]  = number5*sigmal
    pt[i] = number6*sigmap

    f.write('%8.6f %8.6f %8.6f %8.6f %8.6f %8.6f\n' % (x[i],xp[i],y[i],yp[i],1000*t[i],(EN+pt[i]*EN)/1e6))


f.close()

sigmaxcheck=numpy.std(x)
sigmaxpcheck=numpy.std(xp)
sigmaycheck=numpy.std(y)
sigmaypcheck=numpy.std(yp)
sigmatcheck=numpy.std(t)
sigmaptcheck=numpy.std(pt)
print "X Fit", sigmaxcheck
print "PX Fit",sigmaxpcheck
print "Y Fit",sigmaycheck
print "PY Fit",sigmaypcheck
print "T Fit",sigmatcheck
print "PT Fit",sigmaptcheck

sys.exit()