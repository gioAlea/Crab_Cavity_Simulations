from data_treatment_module import *
from absorptions_module import *

#TREAT THE APERTURE FILES
concatenate('../result/lowb.coll/LPI*.s')
convert_to_csv('out.dat', 'aperture.csv')

#TREAT THE ABSORPTIONS FILES
concatenate('../result/lowb.coll/all_absorptions.lowb*.dat')
convert_to_csv('out.dat', 'all.csv')

#PLOT THEM TOGETHER
plot_absorptions('all.csv', 'aperture.csv')

