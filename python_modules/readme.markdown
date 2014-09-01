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


```python
import sys
import os
import matplotlib
from matplotlib import pyplot as plt

sys.path.append("path_to_folder/python_modules/")

from data_treatment_module import *
from plot_distributions_module import *
from distribution_generator_module import *

dist_generator('./initial_dist.txt', 600000, 3.75e-6, 0.15, 0.0, 0.075, 1.129e-4)

convert_to_csv('initial_dist.txt', 'initial_dist.csv')

data 	= 	np.loadtxt(r'initial_dist.csv', delimiter=',',dtype=str)
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


beam_scatter_three(x, y, z, 'x', 'y', 'z')

beam_histogram(n_part, x, 'x')
beam_profile(n_part, x, 'x')

beam_histogram(n_part, xp, 'xp')
beam_profile(n_part, xp, 'xp')

beam_scatter(x, xp, 'x', 'xp')

plt.show()
```