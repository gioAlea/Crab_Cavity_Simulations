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


SixTrack Program
-----------------

To download the latest version:

```
svn co http://svn.cern.ch/guest/SixTrack
```

This will download something similar to the [__SixTrack__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/SixTrack) folder of this repository. To create the executable you will have to go to __SixTrack/trunk/Sixtrack__ and compile the source code _sixtrack.s_ with the command:

```
./make_six gfortran collimat
```

Check the [official website](http://sixtrack.web.cern.ch/SixTrack/) for more information.


SixTrack with Simulations of Crab Cavities
------------------------------------------

There is a modified version of SixTrack, which includes a block to simulate crab cavities. The changes with respect to the original SixTrack code are:

* A new line describing the new element in the [__fort.2__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template/input#fort2) lattice file.

* A new block in the _fort.3_ input file. Check it out [__here__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template/input#crab-block).

* A new [__database__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template/DB#cc_dataf). 


Find the source code in this repository (_sixtrack.s_CC_block_vlineal_2_), and the executable in [__run_lsf_template/bin__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template/bin).


SixTrack without Collimation
----------------------------

Find a special version of SixTrack without the collimation block in the folder [__run_bpm_template__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_bpm_template). This version comes in handy to study the behaviour of the crab cavities, since without the collimation block the program is much faster. There's a special marker (BPM) to see the trajectory at a certain point.

![alt text](https://raw.githubusercontent.com/KFubuki/Crab_Cavity_Simulations/master/img/comparison_single_CC.png)


Other executables
-----------------

Find other executables complementary to SixTrack for [collimation studies](http://lhc-collimation-project.web.cern.ch/lhc-collimation-project/BeamLossPattern.htm) (namely _BeamLossPattern_ and _CleanInelastic_) and their description in [__run_lsf_template/bin__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template/bin).


How does SixTrack work
----------------------

To run SixTrack you will need several input files: 

* __Databases__ : find them in the folder [__run_lsf_template/DB__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template/DB). 
* __Geometry and parameter files__ :_"fort.2"_ and _"fort.3"_, find them in the folder [__run_lsf_template/input__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template/input). 

### Generate the input with MAD-X

> A converter has been developed which is directly linked to MAD-X. It produces
> the geometry file # 2 (fort.2); an appendix to the parameter file # 3 (fort.3) which defines which of the multipole errors are switched on; the error file # 16 and the file # 8 which holds the transverse misalignments and the tilt of the nonlinear kick elements. It also produce a file (unit 34) with linear lattice functions, phase advances and multipole strengths needed for resonance calculations for the program SODD.

MAD-X can help you generate your accelerator lattice, and store it in the geometry file __"fort.2"__. The parameter file __"fort.3"__ can be written by hand.

To see the MAD-X program that generates SixTrack input please check the folder [__madx__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/madx).


### Execute SixTrack in LSF

Check out how to send SixTrack jobs to [LSF](http://information-technology.web.cern.ch/services/batch) here [__run_lsf_template__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template).


### Execute SixTrack locally

There is an example of the needed files to run SixTrack locally in [__run_local_template__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_local_template). Modify _fort.3_ and _CC_dataf_, and run SixTrack:

```
./SixTrack_coll_fvlineal2
```

It is recommended to only run locally for a few jobs. SixTrack output can sometimes be very heavy and can easily fill your free disk space.


Python Scripts
----------------

You can find some handy python scripts in [__python_modules__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/python_modules).













