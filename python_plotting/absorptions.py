import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
from collections import Counter
from matplotlib import pyplot

params = {'backend': 'pdf',
	  	'font.size':20,	
          'axes.labelsize': 20,
          'legend.fontsize': 16,
          'xtick.labelsize': 20,
          'ytick.labelsize': 20,
	  'text.usetex':True,
         } 

# 1=name 2=turn 3=s
tup		=	[]
for	line in	open("all_absorptions.csv"):
		val =	line.strip("\n")
		tup.append(val)

x=[i.split(',',2)[1] for i in tup]
y=[i.split(',',1)[0] for i in tup]

xx=[]
for m in x:
	xx.append(float(m))

yy=[]
for n in y:
	yy.append(int(n))

#---------------------------------
#APERTURE
#---------------------------------

tupa		=	[]
for	line in	open("aperture_absorptions.csv"):
		val =	line.strip("\n")
		tupa.append(val)

xa=[i.split(',',2)[1] for i in tupa]
ya=[i.split(',',1)[0] for i in tupa]

xxa=[]
for m in xa:
	xxa.append(float(m))

yya=[]
for n in ya:
	yya.append(int(n))

# bn=zip(xx,yy)
# sort=sorted(bn, key=lambda bin: bin[1])
# sort1=map(list,zip(*sort))

# lturn=yy.count(1)

#FIRST PLOT
fig=figure()
ax1=fig.add_subplot(211)
ax2=fig.add_subplot(212)

turn=sorted(yy)
t=Counter(turn)
t_absorbed=t.values()
t_turns=t.keys()

turna=sorted(yya)
d=Counter(turna)
d_absorbed=d.values()
d_turns=d.keys()

ax1.bar(t_turns,t_absorbed,log=True,width=0.08, align='center')
ax1.bar(d_turns,d_absorbed,log=True,width=0.08, align='center')
ax1.set_xlabel('Turn number')
ax1.set_ylabel('Number of particles absorbed')


#SECOND PLOT
ss=sorted(xx)
s=Counter(ss)
s_absorbed=s.values()
s_length=s.keys()

ssa=sorted(xxa)
b=Counter(ssa)
b_absorbed=b.values()
b_length=b.keys()

ax2.bar(s_length,s_absorbed,color='r',label='Collimators',log=True,width=20, align='center',edgecolor='r')
ax2.bar(b_length,b_absorbed,color='g',label='Aperture',log=True,width=20, align='center',edgecolor='g')
ax2.set_xlabel('s(m)')
ax2.set_ylabel('Number of particles absorbed')
ax2.legend(loc='upper right')

#COMMON TITLE
pyplot.suptitle('Particle absorption per turn and position', fontsize=25)

show()


	