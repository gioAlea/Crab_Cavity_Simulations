#!/afs/cern.ch/user/a/ansantam/public/python2.7
import sys
import os

sys.path.append("/afs/cern.ch/work/a/ansantam/private/simulations/python_modules/")

from distribution_generator_module import *

dist_generator('./initial_dist.txt', 3200, 3.75e-6, 0.15, 0.0, 0.075, 1.129e-4)