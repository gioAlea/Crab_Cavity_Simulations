import sys,pylab
from optparse import OptionParser
import numpy as npy
from scipy import optimize

def parsse():
    parser = OptionParser()
    parser.add_option("-p", "--path",
                      help="Path to Sixtrack FirstImpact files",
                      metavar="PATH", default="./",dest="PATH")
    parser.add_option("-t", "--type",
                      help="Specify distribution type",
                      metavar="TYPE", default="GAUSS",dest="TYPE")
    (opt, args) = parser.parse_args()
    return opt, args

def phaseSpace(G):
    x=npy.sqrt(BETX*EX)*G; y=npy.sqrt(BETY*EY)*G
    px=G*(npy.sqrt(EX/BETX)-(ALFX*(x/BETX)))
    py=G*(npy.sqrt(EY/BETY)-(ALFY*(y/BETY)))
    t=SIGT*G; pt=SIGE*G
    return x, px, y, py, t, pt

fitfunc = lambda p, x: p[2]*npy.exp(-(x-p[1])**2/p[0]**2)
errfunc = lambda p, x, y: fitfunc(p, x) - y

def MC(samples):    
        #y=random.random()
        #if math.fabs(y) <= math.fabs(f(x)):
        #    if f(x) > 0 and y > 0 and y <= f(x):
        #        ctr += 1 # area over x-axis is positive
        #    if f(x) < 0 and y < 0 and y >= f(x):
        #        ctr -= 1 # area under x-axis is negative    
        
    return npy.random.randn(samples)


def G1(NPAR,s=1.0,x0=0.0): #Gaussian distribution
    return npy.random.normal(x0,s,NPAR)


def G2(NPAR,s1=1.0,s2=5): #double Gaussian distribution
    return (npy.random.normal(0.0,s1, NPAR)+\
           npy.random.normal(0.0,s2, NPAR))/npy.sqrt(2.0)

def f1(sig,x,x0=0.0,a=1.0): 
    #-- gaussian(mean, sigma, amplitude)
    return npy.exp(-(x-x0)**2/2/sig**2)

def f2(s1,s2,x,x0=0.0): 
    #-- gaussian(mean, sigma, amplitude)
    return (npy.exp(-(x-x0)**2/2/s1**2)+\
           npy.exp(-(x-x0)**2/2/s2**2))/npy.sqrt(2.0)

if __name__ == "__main__":
    #--- Input parameters
    opt,args=parsse()
    MP     = 0.938272013 # Mass of PROTON
    CHARGE = 1.0         # Charge 
    EN     = 7000        # Energy of particle, GeV
    SIGE   = 1.1E-04     # Energy Spread
    SIGT   = 0.075       # Bunch Length
    NPART  = 1.0E+4      # Number of particles per bunch
    EN     = 3.75E-06     # Normalized transverse emittance
    GAMMA  = EN/MP    
    EX     = EN/npy.sqrt(abs(GAMMA**2-1))
    EY     = EN/npy.sqrt(abs(GAMMA**2-1))
    BETX   = 0.55; BETY   = 0.55
    ALFX   = 0.00; ALFY   = 0.0
    
    print "Selected path:", opt.PATH
    print "Distribution type:", opt.TYPE

    
    
    y0,y1=npy.histogram(G1(10**4,s=1.0),50,new=True)
    
    #y2=G2(10**4,s1=1.0,s2=1.5)
    p0=[0.0, 0.0, 0.] 
    p1,suc=optimize.leastsq(errfunc,p0[:],args=(y1[:-1], y0))
    print p1,suc
    sys.exit()
    
    c1,b1,i1=pylab.hist(y,50,normed=True)
    c2,b2,i2=pylab.hist(y2,50,normed=True)
    pylab.plot(b1,f1(1.0,b1))
    pylab.plot(b2,f2(1.0,1.5,b2))
    pylab.show()
    sys.exit()