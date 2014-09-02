Python Modules README
=====================

Below I describe the functions defined in each module.

Data Treatment Module
------------------------------

### Concatenate files

```python
concatenate1(regex)
```

This function concatenates the files in a folder following a regular expression, i.e, concantenates the files starting with the same name:

```python
concatenate1('lowb.coll.run1/dist0*.dat')
```

### Convert text files to csv

```python
convert_to_csv(inp, outp)
```
This function converts SixTrack text output to csv format, where `inp` is the name of the input file and `outp` is the name of the output file.


Distribution Generator Module
------------------------------

```python
dist_generator(outfile, particles, emittance, beta, alpha, bunch, spread)
```
This function generates a particle distribution following the input parameters: Name of the output file, number of particles, normalised emittance [m . rad], beta [m], alpha [m], bunch length [m] and energy spread [%]. The output file can be read by the collimation block in SixTrack.


Plot Absorptions Module
------------------------------

```python
plot_absorptions(all, aperture)
```

This function plots the loss maps of the number of particles lost in each turn and particles lost in which longitudinal position. `all` is a csv file with the losses in the collimators, and `aperture` is a csv file with the losses in the aperture.

Plot Distributions Module
------------------------------

```python
beam_histogram(n_part, variable, string)
```

```python
beam_profile(n_part, variable, string)
```

```python
beam_scatter(variable_1, variable_2, string_1, string_2)
```

```python
beam_scatter_three(variable_1, variable_2, variable_3, string_1, string_2, string_3)
```

```python
beam_scatter_comparison(variable_1, variable_2, variable_3, variable_4, string_1, string_2)
```

```python
beam_scatter_comparison_three(variable_1, variable_2, variable_3, variable_4, variable_5, variable_6 )
```
Examples of use
----------------
 ### Generation and plotting of initial distribution

```python
# --------------------------------------------------------------------------------------------------------------
# BEAM DISTRIBUTION GENERATION AND PLOTTING
# ANDREA SANTAMARIA
# LAST MODFIIED: 02/09/2014
# 
# This script allows you to:
# 	- Generate a full bunch as SixTrack input
# 	- Plot it in 3D, plot it's histograms, fits, scatter plots and beam profiles
# --------------------------------------------------------------------------------------------------------------

import sys
import os
import matplotlib
from matplotlib import pyplot as plt

sys.path.append("python_modules/")

from data_treatment_module import *
from plot_distributions_module import *
from distribution_generator_module import *

# --------------------------------------------------------------------------------------------------------------
# Generate the particle distribution as input for SixTrack following the parameters (for protons and round beams): 
# Name of the file, number of particles, normalised emittance [m . rad], beta [m], alpha [m], bunch length [m], 
# energy spread [%]. The following parameters are for IP1.
# --------------------------------------------------------------------------------------------------------------
dist_generator('./initial_dist.txt', 6400, 3.75e-6, 0.15, 0.0, 0.075, 1.129e-4)

# --------------------------------------------------------------------------------------------------------------
# Convert the SixTrack input to csv
# --------------------------------------------------------------------------------------------------------------
convert_to_csv('initial_dist.txt', 'initial_dist.csv')

data    =   np.loadtxt(r'initial_dist.csv', delimiter = ',', dtype = str)
x       =   []
xp      =   []
y       =   []
yp      =   []
z       =   []
e       =   []

for values in data:
    x.append    (float(values[0]))
    xp.append   (float(values[1]))
    y.append    (float(values[2]))
    yp.append   (float(values[3]))
    z.append    (float(values[4]))
    e.append    (float(values[5]))

# --------------------------------------------------------------------------------------------------------------
# Check that the number of particles is correct
# --------------------------------------------------------------------------------------------------------------
n_part = sum(1 for _ in data)
print 'Number of particles initial distribution 	= %s'% n_part

# --------------------------------------------------------------------------------------------------------------
# Plot the initial distribution generated
# --------------------------------------------------------------------------------------------------------------

# 3D overview of the bunch
# --------------------------------------------------------------------------------------------------------------
# beam_scatter_three(x, y, z, 'x', 'y', 'z')

# X coordinate
# --------------------------------------------------------------------------------------------------------------
beam_histogram(n_part, x, 'x', 0.1)
# beam_profile(n_part, x, 'x', 0.2)

# beam_histogram(n_part, xp, 'xp', 0.2)
# beam_profile(n_part, xp, 'xp', 0.2)

# beam_scatter(x, xp, 'x', 'xp')

# Y coordinate
# --------------------------------------------------------------------------------------------------------------
# beam_histogram(n_part, y, 'y', 0.2)
# beam_profile(n_part, y, 'y', 0.2)

# beam_histogram(n_part, yp, 'yp', 0.2)
# beam_profile(n_part, yp, 'yp', 0.2)

# beam_scatter(y, yp, 'y', 'yp')

# Z coordinate
# --------------------------------------------------------------------------------------------------------------
# beam_histogram(n_part, z, 'z', 0.2)
# beam_profile(n_part, z, 'z', 0.2)

# beam_histogram(n_part, e, 'e', 0.2)
# beam_profile(n_part, e, 'e', 0.2)

# beam_scatter(zn, en, 'z', 'e')
# beam_scatter(z, x, 'z', 'e')
# beam_scatter(z, y, 'z', 'y')

plt.show()
```

### Treating and plotting initial and final distributions (after simulation)

```python
# --------------------------------------------------------------------------------------------------------------
# BEAM DISTRIBUTION COMPARISON AFTER SIMULATION
# ANDREA SANTAMARIA
# LAST MODFIIED: 02/09/2014
# 
# This script allows you to:
# 	- Treat several output files from SixTrack and compare them
# --------------------------------------------------------------------------------------------------------------

import sys
import os
import matplotlib
from matplotlib import pyplot as plt

sys.path.append("/afs/cern.ch/work/a/ansantam/private/simulations/python_modules/")

from data_treatment_module import *
from plot_distributions_module import *

# --------------------------------------------------------------------------------------------------------------
# Treat the initial distribution files
#--------------------------------------------------------------------------------------------------------------
concatenate1('../result/lowb.coll/dist0*.dat')
convert_to_csv('out1.dat', 'dist0.csv')

# --------------------------------------------------------------------------------------------------------------
# Treat the final distribution files
# --------------------------------------------------------------------------------------------------------------
concatenate2('../result/lowb.coll/distn*.dat')
convert_to_csv('out2.dat', 'distn.csv')

# --------------------------------------------------------------------------------------------------------------
# Erase temp files
# --------------------------------------------------------------------------------------------------------------
os.remove(r'out1.dat')
os.remove(r'out2.dat')

# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# Load each parameter from the initial distribution to use it in the plots
# --------------------------------------------------------------------------------------------------------------
data 	= 	np.loadtxt(r'dist0.csv', delimiter = ',', dtype = str)
x		=	[]
xp		=	[]
y		=	[]
yp		=	[]
z		=	[]
e		=	[]

for	values in data:
	x.append	(float(values[0]))
	xp.append	(float(values[1]))
	y.append	(float(values[2]))
	yp.append	(float(values[3]))
	z.append	(float(values[4]))
	e.append	(float(values[5]))

# --------------------------------------------------------------------------------------------------------------

datan 	= 	np.loadtxt(r'distn.csv', delimiter = ',', dtype = str)
xn		=	[]
xpn		=	[]
yn		=	[]
ypn		=	[]
zn		=	[]
en		=	[]

for	values in datan:
	xn.append	(float(values[0]))
	xpn.append	(float(values[1]))
	yn.append	(float(values[2]))
	ypn.append	(float(values[3]))
	zn.append	(float(values[4]))
	en.append	(float(values[5]))

# --------------------------------------------------------------------------------------------------------------
# Check that the number of lines = number of particles simulated and lost
# --------------------------------------------------------------------------------------------------------------
n_part 		 	= sum(1 for _ in data)
print 'Number of particles initial distribution 	= %s'% n_part

n_part_final 	= sum(1 for _ in datan)
print 'Number of particles final distribution 		= %s'% n_part_final

lost 			= n_part - n_part_final 
print 'Number of particles lost 					= %s'% lost

percentage_lost = (lost * 100) / n_part
print 'Percentage of particles lost 				= %s'% percentage_lost


# --------------------------------------------------------------------------------------------------------------
# Plot the initial and final distributions for comparison
# --------------------------------------------------------------------------------------------------------------

# 3D overview of the bunches
# --------------------------------------------------------------------------------------------------------------
# beam_scatter_comparison_three(x, y, z, xn, yn, zn)

# X coordinate
# --------------------------------------------------------------------------------------------------------------
# beam_scatter_comparison(x, xp, xn, xpn, 'x', 'xp')

# Y coordinate
# --------------------------------------------------------------------------------------------------------------
# beam_scatter_comparison(y, yp, yn, ypn, 'y', 'yp')

# Z coordinate
# --------------------------------------------------------------------------------------------------------------
# beam_scatter_comparison(z, e, zn, en, 'z', 'e')
# beam_scatter_comparison(z, x, zn, xn, 'z', 'x')
# beam_scatter_comparison(z, y, zn, yn, 'z', 'y')

# Histograms
# --------------------------------------------------------------------------------------------------------------
# beam_histogram(n_part, x, 'x', 0.2)
# beam_profile(n_part, x, 'x', 0.2)

plt.show()
```