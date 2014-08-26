import sys
import os

sys.path.append("../../../private/simulations/python_modules/")

from data_treatment_module import *

convert_to_csv('initDist.txt', 'initDist.csv')