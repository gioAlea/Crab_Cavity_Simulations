"myjob"
-------

This script is originally from [Rama Calaga](https://rcalaga.web.cern.ch/rcalaga/LHCCRABS/MP/SIXTRACK/run_lsf_template/myjob).

This script runs SixTrack, BeamLossPattern and CleanInelastic (don't forget to make them executables!). For more information about this executables please check the [__run_lsf_template/bin__](https://github.com/KFubuki/Crab_Cavity_Simulations/tree/master/run_lsf_template/bin) folder.

It then zips all the __".dat"__ and "__.s__" output files and saves them to your computer. This script is launched with __"joblauncher.sh"__ and will be executed in [LSF](http://information-technology.web.cern.ch/services/batch).

------------------------------------------------------------------------------------

First set the directory where the results will be saved:

```
set DIR=/afs/cern.ch/work/a/ansantam/private/simulations/run_lsf_template
```

For this script to work you will have to set a __"run_lsf_template"__ folder like in this repository, or [here](https://rcalaga.web.cern.ch/rcalaga/LHCCRABS/MP/SIXTRACK/), with the same structure and files inside. This files are needed for SixTrack to work, and will be copied to the remote computer to be used there. 

------------------------------------------------------------------------------------

The last thing to take into account is the size allocated to run your job in MB:

```
"pool>100000"
```

If the pool is too small or too big the job will be killed, or copied partially:

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

To send the job we type:

```
./joblauncher.sh lowb .coll hor b1 1nd 1 1800
```

* ``lowb`` (low beta) = collision (.coll--> output file, we could write __lowb .coll1__)
* ``hor``= horizontal
* ``b1`` = beam1
* ``1nd`` = farm of 1 day. We also have 8 hours ``8nh`` and 8 minutes ``8nm``
* ``1800`` = number of jobs I will send.
