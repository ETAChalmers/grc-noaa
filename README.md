# grc-noaa
Gnuradio script for splitting incomming spectra to three channels, one per NOAA sattelite

splitterscript_main.py is the main component, it's function is to split a 850K spektra into three channels sedning them via UDP to a IP adress on port 1230,1231,1232 
udp-recive.grc is the script that (for now) will recive the incomming udp stream on the destination IP.
