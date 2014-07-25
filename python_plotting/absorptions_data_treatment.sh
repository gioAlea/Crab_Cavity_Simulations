gunzip *.gz;
python absorptions_append.py | python aperture_append.py;
python absorptions_parser.py | python aperture_absorptions_parser.py;

