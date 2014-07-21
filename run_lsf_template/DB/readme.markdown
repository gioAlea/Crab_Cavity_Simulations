DB folder
=========

"CC_dataf"
----------

When you want to work with several cavities per beam (in Bruce's work there are 3 per beam), changing the SixTrack code is not practical. Instead he does like in collimation, and reads from a database. The __"CC_dataf"__ is a crab cavity database.

Let's see how this works:

```
		# Database for cleaning insertion CC
		6
		#
(1) 	CRAB1
(2) 	crab1
(3) 	1
(4) 	0
(5) 	0
(6) 	20
(7) 	0
(8) 	0.0
(9) 	0
(10) 	0
(11) 	20
(12) 	0
(13) 	0.0
```
The first number ``6``, indicates the __number of independent CCs__. Bruce works with 3 cavities per IP side per beam, so a total of 12 cavities. But using each one of them independently is not useful, so he decides to use only 6 independently.

1. and 2. ``CRAB1`` and ``crab1`` indicates the way that the __"fort.2"__ file can read the crab name. In this case it doesn't matter if we write the name with uppercase or lowercase letters, __"fort.2"__ will read it.

3. Indicates in __which plane the CC is going to generate the kick__ (horizontal plane = ``1``, vertical plane = ``2``).

4. Indicates the __number of free turns__, i.e., the number of turns with the cavity voltage to 0, so it acts like a drift space.

5. Indicates the __number of voltage ramping turns__. At the moment the code is done such as the voltage increases linearly.

6. Indicates the __ number of turns at plateau voltage__, i.e. at design voltage.

7. Indicates the __number of turns in which the voltage changes from the plateau voltage to the failure voltage__.

8. Indicates the __failure voltage__, i.e. the final voltage we want.

9. ,10., 11. are the same as before, but for the __phase__. For instance, these three lines indicate the number of free turns, the ramping turns and nominal phase, but because the phase is 0 in this 3 cases these lines are not very relevant.

12. Indicates the __number of turns in which the nominal phase increases until the failure phase__.

13. Indicates the __failure phase__.

The voltage values have to be written in volts, and the phase in radians.

"CollDB.alltclp-tcld.b1.new"
----------------------------

These files contain mechanical and optical data related to the collimators planned for LHC. (Note that at present only Phase I collimators have a length different from zero). A sample block of either one of these input files follows:

```
TCP.D6L7.B1                   	<-- collimator name in capital letters
tcp.d6l7.b1                     <-- collimator name in minimal letters
5.7                             <-- collimator nominal opening (in sigma units)
C                               <-- collimator material (C = graphite, CU = copper, W=tungsten)
    0.2000000000000000          <-- collimator length [m]
    1.5710000000000000          <-- collimator angle [rad]
    0.0000000000000000          <-- collimator offset [m] 
  90.4467000000000070           <-- design Beta x [m] 
156.4360000000000070          	<-- design Beta y [m]  
#                               <-- line jump to next block  
```

The introduction of the optic parameter β allows studies of error scenarios (orbit distortion, beta-beating) and/or to see the effect of misaligned collimators.

This structure is then repeated within the file for each of the collimators to be included in the study.

"CollPositions.alltclp-tcld.b1.dat"
-----------------------------------

Indicates the longitudinal position of each collimator on the ring.


"SurveyWithCrossing_no-offset_lowb_B1.dat"
-----------------------------------------
The "survey" files are generated as a spline interpolation of MADX survey files (see examples: MADX survey, MADX twiss and required shell script). The calculations are carried out with a Matlab script that converts the survey trajectory into an offset of the aperture for the D1, D2, D3 and D4 magnets around the ring. The procedure is delicate.


"allapert_ats_20121023.b1 "
---------------------------
Contains the aperture data. The LHC aperture model has mostly been set by using that MADX interfaces with the LHC layout database. 

For the moment, the aperture model for the LHC optics version V6.5 (sequence) contains:

* Beam screen location for all cold elements (form database).
* Aperture definition for the cold elements within beam screen markers (MADX script).
* Aperture definitions for warm elements (warm).
* Aperture of the various BPM types (BPM).
* Experimental regions (IR1, IR2, IR5, IR8).
* Standard aperture definition of the vacuum chambers - no flange position (drifts).
* Fixing by hand some special elements (fix holes).
* Known missing elements: Recombination chambers, position of vacuum chamber flanges of IR6 kickers.

__Remark__: It is noted that the aperture of collimators and protection devices are not included in the aperture model of the ring. The reason for this choice is that the treatment of these elements is carried out within the tracking code, which provides directly the number of impacting particles on the collimators and the locations of inelastic impacts within the volume of the collimator jaws. Therefore, the aperture of the above 'injection' and 'lowb' lattices are identical (movable elements with different settings at injection or top energy are the only aperture differences that can arise). Different names for the two cases are kept for compatibility with the BeamLossPattern input.