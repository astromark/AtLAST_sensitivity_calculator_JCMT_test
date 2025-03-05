AM FOR AtLAST README
--------------------

This directory contains the code that was used to run AM atmospheric modeling to produce a grid of values that the sensitivity calculator uses to calculate atmospheric parameters. This code is not necessary for atlast_sc, and should be deleted/archived at some point.
The resulting grids are stored in ``atlast_sc/static/lookups`` so versions here are redundant.


AM downloaded December 2021.

ACT_annual_50.amc copied from AM cookbook
am code downloaded from: https://zenodo.org/records/13748403 
am manual is here: https://zenodo.org/records/13748391
The .amc files were edited to produce desired output only by changing line 38 of the configuration files to:

output f GHz  tau  Tb K

The output is then in the format:

frequency (GHz)    tau (nepers)   T (K)   

Run via: 

am configs/ACT_annual_5.amc 30 GHz 1000 GHz 10 MHz 0 deg 1.0 > output/ACT_30_1000_GHz_el60_annual_05.txt
am configs/ACT_annual_25.amc 30 GHz 1000 GHz 10 MHz 0 deg 1.0 > output/ACT_30_1000_GHz_el60_annual_25.txt
am configs/ACT_annual_50.amc 30 GHz 1000 GHz 10 MHz 0 deg 1.0 > output/ACT_30_1000_GHz_el60_annual_50.txt
am configs/ACT_annual_75.amc 30 GHz 1000 GHz 10 MHz 0 deg 1.0 > output/ACT_30_1000_GHz_el60_annual_75.txt
am configs/ACT_annual_95.amc 30 GHz 1000 GHz 10 MHz 0 deg 1.0 > output/ACT_30_1000_GHz_el60_annual_95.txt

(NB: el60 in the file names is incorrect as these are created with 0 deg.)
Grid then produced in makegrid.py, outputting two files: am_ACT_T_annual.txt and am_ACT_tau_annual.txt