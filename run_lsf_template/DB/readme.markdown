DB folder
=========

"CC_dataf"
----------

The information concerning the crab cavities is gathered in a crab cavity database, following the same approach as the collimation block.

Here is an example of a CC database:

```
		# Database for cleaning insertion CC
		6
		#
(1) 	CRAB1		# Name of the cavity in uppercase
(2) 	crab1		# Name of the cavity in lowercase
(3) 	1			# CC kick plane (1 - horizontal, 2 - vertical)
(4) 	0			# Number of free turns (cc voltage = 0)
(5) 	0			# Number of turns of linear ramp of the voltage up to the plateau voltage
(6) 	20			# Number of turns at plateau voltage (defined in _fort.2_)
(7) 	0			# Number of turns from plateau voltage to failure voltage (also linear)
(8) 	0.0 		# Failure voltage [MV]
(9) 	0			# Number of free turns (cc phase = 0)
(10) 	0			# Number of turns of linear ramp of the phase up to the plateau phase
(11) 	20			# Number of turns at plateau phase
(12) 	0			# Number of turns from plateau phase to failure phase (also linear)
(13) 	0.0 		# Failure phase [rad]
```

"CollDB.alltclp-tcld.b1.new"
----------------------------

These files contain mechanical and optical data related to the collimators planned for LHC. (Note that at present only Phase I collimators have a length different from zero). A sample block of either one of these input files follows:

```
TCP.D6L7.B1                   	# collimator name in capital letters
tcp.d6l7.b1                     # collimator name in minimal letters
5.7                             # collimator nominal opening (in sigma units)
C                               # collimator material (C = graphite, CU = copper, W=tungsten)
    0.2000000000000000          # collimator length [m]
    1.5710000000000000          # collimator angle [rad]
    0.0000000000000000          # collimator offset [m] 
  90.4467000000000070           # design Beta x [m] 
156.4360000000000070          	# design Beta y [m]  
#                               # line jump to next block  
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