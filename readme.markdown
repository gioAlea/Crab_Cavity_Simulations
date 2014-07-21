Crab Cavity Failure Simulation README
======================================

This repository contains the files to simulate a crab cavity failure for HL-LHC using [SixTrack](http://sixtrack.web.cern.ch/SixTrack/).

>The aim of SixTrack is to track two nearby particles taking into account the 
>full six–dimensional phase space including synchrotron oscillations in a 
>symplectic manner. It allows to predict the long–term dynamic aperture which 
>is defined as the border between regular and chaotic motion. This border can 
>be found by studying the evolution of the distance in phase space of two 
>initially nearby particles. Parameters of interest like nonlinear detuning 
>and smear are determined via a post–processing of the tracking data.

SixTrack Input
---------------

To run SixTrack you will need several input files: 

* Databases (find them in the folder [__run_lsf_template/DB__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template/DB)). 
* Geometry and parameter files __"fort.2"__ and __"fort.3"__, respectively (find them in the folder [__run_lsf_template/input__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template/input)). 

### Generate the input with MAD-X

> A converter has been developed which is directly linked to MAD-X. It produces
> the geometry file # 2 (fort.2); an appendix to the parameter file # 3 (fort.3) which defines which of the multipole errors are switched on; the error file # 16 and the file # 8 which holds the transverse misalignments and the tilt of the nonlinear kick elements. It also produce a file (unit 34) with linear lattice functions, phase advances and multipole strengths needed for resonance calculations for the program SODD.

MAD-X can help you generate your accelerator lattice, and store it in the geometry file __"fort.2"__. The parameter file __"fort.3"__ can be written by hand.

To see the MAD-X program that generates SixTrack input please check the folder [__madx__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/madx).

Plotting Absorptions and Distributions
--------------------------------------

Find the scripts I use in the folder [__python_plotting__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/python_plotting).

Creating Some Initial Distributions
-----------------------------------

Find the script to create some distributions in ther folder [__python_initial_distribution__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/python_initial_distribution) (from Rama Calaga).

SixTrack without Collimation
----------------------------

Find a special version of SixTrack without the collimation block in the folder [__run_no_collimation_template__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_no_collimation_template). This version is to see the behaviour of the crab cavities. There's a special marker (BPM) to see the distribution at a certain point.

SixTrack Source Code
--------------------
Check the SixTrack source code __sixtrack.s_CC_block_vlineal_2__.









