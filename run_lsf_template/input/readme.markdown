input folder
============

"fort.2"
--------

This file indicates the __lattice of the machine without magnetic field errors__. It has to be modified to introduce the crab cavities and to indicate the tracking point.

There are some important flags:

* ``GO`` indicates the initial point of the tracking.
* ``CAV`` has to appear before the first cavity element. It is very important for tracking in 6D. If this flag doesn't appear the tracking will be done in 4D.

Now we will describe the crab elements that appear:

``CRAB1            23   3.571590715e+00   4.007896026e+02    0.000000000e+00    0.000000000e+00    0.``

* __First column__: name of the cavity as described in __"CC_dataf"__ , like ``CRAB1``.
* __Second column__: indicates a cavity element. It is indicated by the number ``23``.
* __Third column__: cavity voltage.
* __Fourth column__: cavity frequency.
* __Fifth column__: phase angle (0).


"fort.3"
--------
This file indicates the __tracking parameters__ (number of particles and turns), type of beam and type of halo. The parameters of the simulation have to be inserted by hand before being executed by SixTrack.

Some comments about the general input of SixTrack from the official documentation:

> The idea of RACETRACK input is to use a sequence of input blocks, each block with a specific
> keyword in the first line, the keyword ``NEXT`` in the last line and the input data in the lines in
> between. The keyword ``ENDE`` ends this sequence, and all blocks after this keyword are ignored.
> This system makes it easy to read input and allows easy change and addition of input blocks.


###Geometry Block

```
(1) 	GEOM
(2) 	PRINTOUT
(3) 	NEXT
```
1. ``GEOM`` indicates if the geometry part is in __"fort.2"__.

2. The use of the Print Selection input block causes the printing of the input data to the output file __"fort.6"__. It is advisable to always use this input block to have a complete protocol of the tracking run.


###Tracking Block

All tracking parameters are defined with this input block, the initial coordinates are generally set here, too. A fine tuning of the initial condition is done with Initial Coordinates block.

```
 		TRACKING
(1) 	20 0 32 0 17 0 1
(2) 	1 1 0 0 0
(3) 	0 0 1 1 1 20000 2
		NEXT
```

1.

* ``20``: integer, number of turns in the forward direction.
* ``0``: integer, number of turns in the backward direction.
* ``32``:integer, number of amplitude variations.
* ``0`` and ``17``: (floats) start and end amplitude (any sign) in the horizontal phase space plane for the amplitude variations. The vertical amplitude is calculated using the ratio between the horizontal and vertical emittance set in the Initial Coordinates block, where the initial phase in phase space are also set. Additional information can be found in the Remarks.
* ``0``: integer, switch for the type of amplitude variation. In case napx = 1 the amplitude nstart is used.
	* ``0``: amplitudes are varied between the amplitudes amp(1) and amp0 with equal increments.
	* ``1``: amplitude variation to find an estimate for the short term dynamic aperture. The amplitude is increased or decremented corresponding to stable motion or particle loss respectively.
* ``1``: integer, number of variations of the relative momentum deviation relative momentum deviation ∆p/po. The maximum value of the relative momentum deviation is taken from that of the first particle in the Initial Coordinates block.

2.

* ``1`` and  ``1``: a tracking where one of the transversal motion planes shall be ignored is only possible when all coupling terms are switched off. The part of the coupling that is due to closed orbit and other effects can be turned off with these switches.
	* ``1`` and  ``1``: coupling on.
	* ``0`` and  ``0``: coupling to the horizontal and vertical motion plane respectively switched off.
* ``0``: usually the closed orbit is added to the initial coordinates. This can be turned off using this,
for instance when a run is to be prolonged.
	* ``0``: closed orbit added.
	* ``1``: initial coordinates unchanged.
	* ``2``: prolongation of a run, taken the initial coordinates from unit # 13.
* ``0``: to reduce the amount of tracking data after each amplitude and relative momentum deviation iteration ∆p/po the binary output units 90 and lowerare rewound. This is always done when the post–processing is activated. For certain applications it may be useful to store all data. This switch allows that.
	* ``0``: unit 90 (and lower) rewound.
	* ``1``: all data on unit 90 (and lower).
* ``0``: this switch allows to calculate the 6D closed orbit using the differential algebra package. It is ignored in the regular tracking versions. It is active in all versions that link to the Differential Algebra package. This 6D closed orbit can be calculated from any longitudinal position contrary to earlier versions.
	* ``0``: switched off
	* ``1``:calculated
	* ``2``:  calculated and added to the initial coordinates
	* ``5`` or ``6``: like for 1 and 2 but in addition a guess closed orbit is read (in free format) from file unit # 33.

3.

* ``0``: number of turns at flat bottom, useful for energy ramping.
* ``0``: number of turns for the energy ramping. For constant energy with this column and the one before set to ``0``, the particles are considered to be on the flat top.
* ``1``: Every nwr(1)’th turn the coordinates will be written on unit 90 (and lower) in the flat bottom part of the tracking.
* ``1``: Every nwr(2)’th turn the coordinates in the ramping region will be written on unit 90 (and lower).
* ``1``: every nwr(3)’th turn at the flat top a write out of the coordinates on unit 90 (and lower) will occur. For constant energy this number controls the amount of data on unit 90 (and lower), as the particles are considered on the flat top.
* ``20000``: in cases of very long runs it is sometimes useful to save all coordinates for a prolongation of a run after a possible crash of the computer. Every nwr(4)’th turn the coordinates are written to unit 6.
* ``2``: For the analysis of the Lyapunov exponent it is usually sufficient to store the calculated distance of phase space together with the coordinate of the first particle (ntwin set to one). You may want to improve the 6D calculation of the distance in phase space with sigcor, dpscor when the 6D closed orbit is not calculated with iclo6 = 2. If storage space is no problem, one can store the coordinates of both particles (ntwin set to two). The distance in phase space is then calculated in the post–processing procedure. This also allows a subsequent refined Lyapunov analysis using differential–algebra and Lie–algebra techniques.


###Initial Coordinates Block

The Initial Coordinates input block is meant to manipulate how the initial coordinates are organise, which are generally set in the tracking parameter block. Number of particles, initial phase, ratio of the horizontal and vertical emittances and increments of 2 × 6 coordinates of the two particles, the reference energy and the starting energy for the two particles.

```
		INITIAL COORDINATES
(1) 	2 0 0 1
(2) 	0.0
(3) 	0.0
(4) 	0.0
(5) 	0.0
(6) 	0.0
(7) 	0.0
(8) 	0.0
(9) 	0.0
(10) 	0.0
(11) 	0.0
(12) 	0.000001
(13) 	0.0
(14) 	7000000.0
(15) 	7000000.0
(16) 	7000000.0
		NEXT
```

1.

* ``2``: number of particles.
	* ``0``: amplitude values of tracking parameter block ( 3.6.1) are ignored and coordinates
	of data line 2–16 are taken. itra is set internally to 2 for tracking with two particles. This
	is necessary in case a run is to be prolonged.
	* ``1``: tracking of one particle, twin particle ignored.
	* ``2``: tracking the two twin particles.
* ``0``: starting phase of the initial coordinate in the horizontal and vertical phase space projections.
* ``0``: phase difference between first and second particles.
* ``1``: denotes the emittance ratio (eII /eI ) of horizontal and vertical motion. 


![alt text](https://raw.githubusercontent.com/KFubuki/CC_failure_simulation/trial/coor.png)

####Remarks

1. These 15 coordinates are taken as the initial coordinates if the first parameter is set to zero (see above). If it
is 1 or 2 these coordinates are added to the initial coordinates generally defined in the tracking parameter block. This procedure seems complicated but it allows freely to define the initial difference between the two twin particles. It also allows in case a tracking run should be
prolonged to continue with precisely the same coordinates. This is important as small difference may lead to largely different results.

2. The reference particle is the particle in the centre of the bucket which performs no synchrotron oscillations.

3. The energy of the first and second particles is given explicitly, again to make possible a continuation that leads precisely to the same results as if the run would not have been interrupted.

4. There is a refined way of prolonging a run, see the Tracking Parameters input block.


###Fluctuation Block

If besides mean values for the multipole errors (Gaussian) random errors should be considered this input data structure is used to set the start value for the random generator.

```
FLUCTUATION
100000 1 7 3
NEXT
```

* ``100000``: start value for the random number generator.
* ``1``: disabled, fixed to 1.
* ``7``: binary switch for various purposes, so all options, as described below, can be combined:
	* ``1``: multipole errors read–in from external file. External multipole errors are read–in from file 16 into the array of random values. To
	activate these values one has to set to a value of 1 the relevant r.m.s.–positions of the corresponding multipole blocks. The systematic components are added as usual and multipoles not found in the fort.16 are treated as for (mout = 0 ). An error is only detected if there are too few sets of multipoles in fort.16.
	* ``2``: the geometry and strength file is written to file # 4 in the same format as the input file # 2; the multipole coefficients are written to file # 9; name, misalignments and tilt is written to file # 27 and finally name, random single multipole strength and both random transverse misalignments are written to file # 31.
	* ``4``: name, horizontal and vertical misalignment and also the element tilt are read–in from file # 8.
	* ``8``: name and 3 Random numbers for single kick strength and both random transverse misalignments and also the value of the tilt are read–in from file # 30
* ``3``: the random distribution can be cut by ``3`` sigma of the distribution. No cuts are applied for ``0`` .



###Iteration Accuracy Block

Each data line holds three values as in table 3.1, except for the fourth line one which the horizontal and vertical aperture limits can be additionally specified. This has been added to avoid artificial crashes for special machines.

```
		ITERATION ACCURACY
(1) 	50 0.10E-13 0.10E-14
(2) 	10 0.10E-09 0.10E-09
(3) 	10 0.10E-04 0.10E-05
(4) 	0.10E-07 0.10E-11 0.10E-09
		NEXT
```
![alt text](https://raw.githubusercontent.com/KFubuki/CC_failure_simulation/trial/iter.png)

###Linear Optics Block

Each linear single element has a name, type, inverse bending radius, focusing and a nonzero length.


```
LINEAR OPTICS
ELEMENT  0 1 1 3.75 3.75
NEXT
```
* ``ELEMENT``: name, may contain up to sixteen characters.
* ``0``: type
* ``1``: inverse bending radius in m−1
* ``1``: focusing strength in m−2
* ``3.75``: magnet length in meters
* ``3.75``:

![alt text](https://raw.githubusercontent.com/KFubuki/CC_failure_simulation/trial/elem.png)

###Beam Block

```
BEAM
0.110E+12 3.75 3.75  0.0755E+00  0.4716E-03 1 1 1
NEXT
```
* ``0.110E+12``: float, number of particles in bunch.
* ``3.75``: float, horizontal normalized emittance [μm · rad].
* ``3.75``: float, vertical normalized emittance [μm · rad].
* ``0.0755E+00``: float, r.m.s. bunch length [m].
* ``0.4716E-03``: float, r.m.s. energy spread.
* ``1``: integer, switch (0 = off; 1 = on) to subtract the closed orbit introduced by the separation of the beams. It is recommended to always subtract it as it is not yet calculated in a selfconsistent manner.
* ``1``: integer, Switch (0 = off; 1 = on) to use the fast beam–beam algorithms developped in collaboration with G.A. Erskine and E. McIntosh. The linear optics are calculated with “exact” beam–beam kicks.
* ``1``: integer, for the LHC with its anti–symmetric IR the separation of the beams in one plane can be calculated
by the β–function of the other plane. For flat beams (not anti-symmetric optics) the separation
can be loaded from the fort.2 file. (0 = off; 1 = anti-symmetric; 2 = load from file).


###Sync Block

The parameters needed for treating the synchrotron oscillation in a symplectic manner are given in the Synchrotron Oscillation input block. We can double check this values [here](https://edms.cern.ch/file/445830/5/Vol_1_Chapter_2.pdf).


```
		SYNC
(1) 	35640 .0003225 16 0 26658.864 938.2796 1
(2) 	1 1
		NEXT
```

1.

* ``35640``: harmonic number.
* ``.0003225``: momentum compaction factor, used here only to calculate the linear synchrotron tune QS.
* ``16``: circumference voltage in [MV].
* ``0``: acceleration phase in degrees.
* ``26658.864``: length of the accelerator in meters.
* ``938.2796``: rest mass of the particle in MeV/c2.
* ``1``: transition energy switch.
	* ``0``: for no synchrotron oscillation (energy ramping still possible).
	* ``1``: for above transition energy.
	* ``-1``: for below transition energy.
	
2.

* ``1``: offset relative momentum deviation: a fixpoint with respect to synchrotron oscillations. It becomes active when the 6D closed orbit is calculated. 
* ``1``: scaling factor for relative momentum deviation ∆p and the path length difference (σ = s − vo × t) respectively. They can be used to improve the calculation of the 6D distance in phase space, but is only used when ntwin = 1 in the tracking parameter input block. Please set to 1 when the 6D closed is calculated.


### Crab Block

Created by __Bruce Yee Rendon__.

```
CRAB
1 880 "CC_dataf"
```
* ``1``: indicates the __turn in which the collimators are installed__. The number ``1`` here is used by Bruce to achieve a steady state. 
* ``880``: indicates the __turn in which you start saving the data__. If the data starts being saved before the first impact in the collimators you can have ghost losses, so in general it is recommended to put a high number here to prevent this.
* ``"CC_dataf"``: calls the crab database described below.

This file uses the collimator database __"CollDB.alltclp-tcld.b1.new"__, which describes the details of collimators' geometry, material, settings (opening). It will need to be updated as the collimator settings change.

More information about a more general use of __crabs in SixTrack__ can be found [here](http://rcalaga.web.cern.ch/rcalaga/LHCCRABS/COLLIMATION/crabcoll.html).


### Collimation Block

Developped by the __Collimation Team__. More information about this block can be found [here](http://lhc-collimation-project.web.cern.ch/lhc-collimation-project/code-tracking-2012.php).

```
		COLLIMATION
(1) 	.TRUE. 
(2) 	100 7000000
(3) 	4 5.0 .1 0. 0. "initDist.txt" 1.129E-4 75.5
(4) 	.FALSE.  12.0  15.6  999.  17.6  6.  7.  999.  10.  12.0  999.  8.  7.5   999.0
(5) 	8.3  30. 8.3  30.  8.3  30.  8.3  30.0 999.0  999.0	
(6) 	0 19789.0 20150.0 1 1
(7) 	-1.3899e-6 -9.345e-5 5.05324e-3 -1.6595e-2 2.15955e-2 -9.96261e-3 1.0
(8) 	-1.3899e-6 -9.345e-5 5.05324e-3 -1.6595e-2 2.15955e-2 -9.96261e-3 1.0
(9) 	0.503E-09 0.503E-09
(10) 	.FALSE. .FALSE. 0 .TRUE. TCP.C6L7.B1 .FALSE. .TRUE. .TRUE. .TRUE. 
(11) 	0 0 0 0
(12) 	0 0 0 0 0 0 0 0 0 0 .FALSE.
(13) 	.FALSE. 6.003 .0015
(14) 	0 0 .FALSE. .FALSE. 
(15) 	0 .0019 0.0 0.275E-3 1
(16) 	"CollDB.alltclp-tcld.b1.new" 1
(17) 	.TRUE. .FALSE. HoriLowbcoll 101 1 1.
		NEXT
```

1.

* ``.TRUE.``: logical, switches on/off the collimation studies.
    
2.

* ``100``: number of packs of 64 particles to be tracked (breaks internal limitation). 
* ``7000000``: energy of the beam to be tracked.
     
3.

* ``4`` defines initial distribution to be tracked.
    * ``1``: flat distribution in the selected plane, the amplitude in the other plane is zero.
    * ``2``: flat distribution in the selected plane and a Gaussian distribution cut at 3s in the other plane.
    * ``3``: flat distribution in the selected plane, a Gaussian distribution cut at 3s in the other plane and an __energy spread__ (nominally 3.06E-04 at 450GeV and 1.129E-04 at 7TeV) and a __longitudinal component__ (nominally 11.24cm at 450GeV and 7.55cm at 7TeV).
    * ``4``: reads an external file that contains the beam distribution to be tracked.
    * ``5``: flat distribution both in the horizontal and vertical planes. 
* ``5.0``: normalized amplitude of particles (in sigma units) in the X direction.
* ``.1``: smear (in sigma units) of the beam halo around the amplitude (in X direction). 
* ``0.``: normalized amplitude of particles (in sigma units) in the Y direction. 
* ``0.``: smear (in sigma units) of the beam halo around the amplitude (in Y direction).
* ``"initDist.txt"`` :  name of the distribution file to be read if the first parameter is set to __4__.
* ``1.129E-4``: __energy spread__ of the tracked beam if the first parameter is set to __3__.
* ``75.5``:  __bunch length__ of the tracked beam in millimeters (only if the first parameter is set to __3__).       
                
4. : openings of the primary and secondary collimators.

5., 6., 7., 8.: openings of the tertiary collimators and surface model of the jaw.

9.

* ``0.503E-09`` : geometric emittance in the horizontal plane.
* ``0.503E-09`` : geometric emittance in the vertical plane.

10.

* ``.FALSE.``: logical, does dedicated study of selected collimator 
* ``.FALSE.``: logical, switches on/off the use of design β values of collimators.
* ``0``: seed studied; if set to 0, seed will be selected randomly for every run.
* ``.TRUE.``: logical, saves or not the initial distribution to be tracked.
* ``TCP.C6L7.B1``: name as in the fort.2 file of the collimator one wants a dedicated study.
* ``.FALSE.``: logical, switches on/off the collimator being one-sided. Only positive jaw. If the negative jaw is to be used, it is necessary to turn collimator by 180 degrees in the collimator database file (CollDB_V6.500_[type]_st.[beam].data).
* ``.TRUE.``:  logical, saves the impact parameters for each collimator.
* ``.TRUE.``:  logical, writes a 2ry halo file based on normalized amplitude.
* ``.TRUE.``:  logical, writes checking files for amplitude, closed orbit...

11.

* ``0``:  offset in X for the computation of collimator in case of beta-beating.
* ``0``:  phase offset in X for the computation of collimator in case of beta-beating.
* ``0``: offset in Y for the computation of collimator in case of beta-beating.
* ``0``: phase offset in X for the computation of collimator in case of beta-beating.

12. 

tilt to apply to collimators. All set to 0.

13.

* ``.FALSE.``: logical, switches on/off the radial distribution. 
* ``6.003``: size of the beam to be tracked in number of radial sigma's.
* ``.0015``: smear of the beam to be tracked in number of radial sigma's.

14.

* ``0``: to apply an emittance drift in x direction.
* ``0``: to apply an emittance drift in y direction.
* ``.FALSE.`` : logical, formerly used to select particles to be tracked (set .FALSE.).
* ``.FALSE.``: logical, to deduce C_SYSTILT to C_RMSTILT instead of adding. 

15.

* ``0``: resets original distribution to pencil beam distribution on selected collimator.
* ``0``:  size in sigma units of the desired impact parameter.
* ``.0019``: PENCIL_RMSX.
* ``0.0``: PENCIL_RMSY.
* ``0.275E-3 ``: PENCIL_DISTR.
* ``1``: ??

16.

* ``"CollDB.alltclp-tcld.b1.new"``: name of the collimator database; must be quoted.
* ``1``: "name" of the beam tracked (1 or 2) => TO BE UPGRADED.

17.

* ``.TRUE.``: logical, writes secondary/tertiary halo files.
* ``.FALSE.``: logical, switches on/off to cut halo files in separate pieces, one per 64 particle.
* ``HoriLowbcoll``:  name of the run; MUST BE EXACTLY 16 characters.
* ``101``: 5 digit number, name of the complement to the name of the run (gives seed).
* ``1``: cut in square sigma's x/y for saving particles (e.g. 64 for a cut at 8 σx/σy).
* ``1.``: cut in square sigma's radial for saving particles (e.g. 90.25 for a cut at 9.5 σr).
        
