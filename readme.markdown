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

* Databases (find them in the folder [__TEST.MP/DB__](https://github.com/KFubuki/CC_failure_simulation/tree/master/TEST.MP/DB)). 
* Geometry and parameter files __"fort.2"__ and __"fort.3"__, respectively (find them in the folder [__TEST.MP/input__](https://github.com/KFubuki/CC_failure_simulation/tree/master/TEST.MP/input)). 

### Generate the input with MAD-X

> A converter has been developed which is directly linked to MAD-X. It produces
> the geometry file # 2 (fort.2); an appendix to the parameter file # 3 (fort.3) which defines which of the multipole errors are switched on; the error file # 16 and the file # 8 which holds the transverse misalignments and the tilt of the nonlinear kick elements. It also produce a file (unit 34) with linear lattice functions, phase advances and multipole strengths needed for resonance calculations for the program SODD.

MAD-X can help you generate your accelerator lattice, and store it in the geometry file __"fort.2"__. The parameter file __"fort.3"__ can be written by hand.

To see the MAD-X program that generates SixTrack input please check the folder [__madx__](https://github.com/KFubuki/CC_failure_simulation/tree/master/madx).

"myjob"
-------

This script is originally from [Rama Calaga](https://rcalaga.web.cern.ch/rcalaga/LHCCRABS/MP/SIXTRACK/TEST.MP/myjob).

This script runs SixTrack, BeamLossPattern and CleanInelastic (don't forget to make them executables!). For more information about this executables please check the [__TEST.MP/bin__](https://github.com/KFubuki/CC_failure_simulation/tree/master/TEST.MP/bin) folder.

It then zips all the __".dat"__ and "__.s__" output files and saves them to your computer. This script is launched with __"joblauncher.sh"__ and will be executed in [LSF](http://information-technology.web.cern.ch/services/batch).

------------------------------------------------------------------------------------

First set the directory where the results will be saved:

```
set DIR=/afs/cern.ch/user/a/ansantam/public/thesis/6track/bruce/TEST.MP
```

For this script to work you will have to set a __"TEST.MP"__ folder like in this repository, or [here](https://rcalaga.web.cern.ch/rcalaga/LHCCRABS/MP/SIXTRACK/), with the same structure and files inside. This files are needed for SixTrack to work, and will be copied to the remote computer to be used there. 

------------------------------------------------------------------------------------

The last thing to take into account is the size allocated to run your job in B:

```
"pool>100000"
```

If the pool is too small the job will be killed, or copied partially:

```
The size of the output file is 253813073 bytes, exceeding the maximum
size of 10000000 bytes. Only the head and the tail (10000154 bytes)
have been returned.
```

###Possible error

Trying to launch this script might give you the following error:

```
/bin/tcsh^M bad interpreter: No such file or directory
```

The script indicates that it must be executed by a shell located at /bin/tcsh^M. There is no such file: it's called /bin/tcsh.

The ^M is a carriage return character. Linux uses the line feed character to mark the end of a line, whereas Windows uses the two-character sequence CR LF. Your file has Windows line endings, which is confusing Linux.

Remove the spurious CR characters. You can do it with the following command:

```
sed -i -e 's/\r$//' myjob
```

"joblauncher.sh"
-----------------
This script launches the __"myjob"__ script. We will have to send it to a [batch farm](http://information-technology.web.cern.ch/book/cern-batch-service-user-guide/getting-started-batch-system/batch-concepts-and-cern-batch-system).

To send a big amount of jobs in order to have good statistics, we will type:

```
./joblauncher.sh lowb .coll hor b1 1nd 1 1800
```

* ``lowb`` (low beta) = collision (.coll--> output file, we could write __lowb .coll1__)
* ``hor``= horizontal
* ``b1`` = beam1
* ``1nd`` = farm of 1 day. We also have 8 hours ``8nh`` and 8 minutes ``8nm``
* ``1800`` = number of jobs I will send.










