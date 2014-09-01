SHELL = /bin/sh

FC = lf95
FCF = --o1 --tp -Wa,--32
FCL = -static -m32 -L/usr/lib/ -lc -L/usr/lib/gcc/x86_64-redhat-linux/3.4.6/32 -lgcc_eh
FCLMAP = -Wl,--print-map -static -m32 -L/usr/lib/ -lc -L/usr/lib/gcc/x86_64-redhat-linux/3.4.6/32 -lgcc_eh
CRLIBM = 
CERNLIB = 
gfortran_lib = 
BOINC = 
NAGLIBC = 
BEAMGAS = 

%.o: %.f
	$(FC) -c $(FCF) $<

%.o: %.f90
	$(FC) -c $(FCF) $<

all: %%SIXTRACK%%

dafor: dafor.o
	$(FC) $(FCL) -o dafor dafor.o

astuce: astuce.o
	$(FC) $(FCL) -o astuce astuce.o $(NAGLIBC)

boinc_api_fortran.o: boinc_api_fortran.C
	gcc -c boinc_api_fortran.C

%%SIXTRACK%%: $(MYHDF5LIB) track.o sixve.o sixvefox.o dabnews.o lielib.o $(BEAMGAS) $(BOINC) $(CRLIBM)
	$(FC) $(FCLMAP) -o %%SIXTRACK%% track.o sixve.o sixvefox.o dabnews.o lielib.o $(BEAMGAS) \
	$(BOINC) $(CERNLIB) $(CRLIBM) $(gfortran_lib) > sixtrack.map 2>&1

%%SIXTRACK_DA%%: sixda.o sixsc.o sixscfox.o dabnew.o lielib.o $(CRLIBM)
	$(FC) $(FCLMAP) -o %%SIXTRACK_DA%% sixda.o sixsc.o sixscfox.o dabnew.o lielib.o \
	$(NAGLIB) $(CRLIBM) $(gfortran_lib) > sixtrack_da.map 2>&1

clean: 
	rm -f *.ast *.s *.c *.o %%SIXTRACK%% %%SIXTRACK_DA%%
