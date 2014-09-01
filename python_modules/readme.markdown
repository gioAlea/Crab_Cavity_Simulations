Python Modules README
=====================

Below I describe the functions defined in each module.

Data Treatment Module
------------------------------

### Concatenate files

```
concatenate1(regex)
```

This function concatenates the files in a folderfollowing a regular expression, i.e, concantenates the files starting with the same name:

```
concatenate1('lowb.coll.run1/dist0*.dat')
```

### Convert text files to csv

```
convert_to_csv(inp, outp)
```
This function converts SixTrack text output to csv format, where `inp` is the name of the input file and `outp` is the name of the output file.


Distribution Generator Module
------------------------------

```
dist_generator(outfile, particles, emittance, beta, alpha, bunch, spread)
```
This function generates a particle distribution following the input parameters: Name of the output file, number of particles, normalised emittance [m . rad], beta [m], alpha [m], bunch length [m] and energy spread [%]. The output file can be read by the collimation block in SixTrack.


Plot Absorptions Module
------------------------------

```
plot_absorptions(all, aperture)
```

This function plots the loss maps of the number of particles lost in each turn and particles lost in which longitudinal position. `all` is a csv file with the losses in the collimators, and `aperture` is a csv file with the losses in the aperture.

Plot Distributions Module
------------------------------

```
beam_histogram(n_part, variable, string)
```

```
beam_profile(n_part, variable, string)
```

```
beam_scatter(variable_1, variable_2, string_1, string_2)
```

```
beam_scatter_three(variable_1, variable_2, variable_3, string_1, string_2, string_3)
```

```
beam_scatter_comparison(variable_1, variable_2, variable_3, variable_4, string_1, string_2)
```

```
beam_scatter_comparison_three(variable_1, variable_2, variable_3, variable_4, variable_5, variable_6 )
```