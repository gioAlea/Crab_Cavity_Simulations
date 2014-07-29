from data_treatment_module import *
from absorptions_module import *

#TREAT THE APERTURE FILES
concatenate('LPI*.s')
convert_to_csv('out.dat', 'aperture.csv')

#TREAT THE ABSORPTIONS FILES
concatenate('all_absorptions.lowb*.dat')
convert_to_csv('out.dat', 'all.csv')

#PLOT THEM TOGETHER
plot_absorptions('all.csv', 'aperture.csv')

