MADX folder
===========

In this repository the file that generates the input is called __"job_sample_thin_CC.madx"__ (also called a _mask file_).

In this file we use the macros for [ATS optics](http://journals.aps.org/prstab/abstract/10.1103/PhysRevSTAB.16.111002) and round optics.

``call,file="slhc/toolkit/macro.madx";``

To see how it works just check that file in ``/afs/cern.ch/eng/lhc/optics/HLLHCV1.0/toolkit/macro.madx`` and the examples in ``/afs/cern.ch/eng/lhc/optics/HLLHCV1.0/examples``.

Intallation of new collimators for post-LS1 operation, calling the files: 

* __"tcdq_ir6_2012.thin.madx"__
* __"tcl.ats.madx"__
* __"tctv.madx"__
* __"tct_cell_5.madx"__

These files will have to be updated as they change.

Each cavity can achieve a voltage of 3.5 MV. As 10 MV is needed, three cavities are used. We can see this in the voltage definition:

```
VOLTA1=10.253318497292/3 ;
VOLTA2=11.7084365079951/3;
!VOLTA1=11.4578700490228/3;
!VOLTA2=12.4650249375015/3;
VOLTA3 = 11.6126756161663/3; !IP1 LEFT
VOLTA4 =  9.85841121716882/3; !IP1 RIGHT
crabrf=35640/26658.883200*clight;
frq=crabrf/1e6;
```

Outputs of running this program:

* __"fc.2"__
* __"f.3.aux"__
* __"fc.34"__
* __"fc.8"__
* __"twiss.bruce.b1.dat"__
* __"twiss.hllhcv1.b1.tfs"__ 

__Note 1__: MAD-X must be run with LHC lattice and optics files V6.500 (or more recent layouts), 'thin lens' approximation, and the addition of collimators. 

__Note 2__: for "perfect" machines, the files produced are __"fc.2"__ and __"fc.34"__ (optional) which must be renamed (for SixTrack) __"fort.2"__ and __"fort.34"__.

The next step will be to erase __"fc.2"__ and __"f.3.aux"__, and to copy and rename Bruce's files __"fc.2_nosep_allcc"__ to __"fort.2"__ and __"fort3_blockf"__ to __"fort.3"__. We can also rename the rest of the __"fc"__ files.
