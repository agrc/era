# agrc/ERA
<!--
![Build Status](https://github.com/agrc/python/workflows/Build%20and%20Test/badge.svg)
[![codecov](https://codecov.io/gh/agrc/python/branch/main/graph/badge.svg)](https://codecov.io/gh/agrc/python) -->

A script for updating the Emergency Rental Assistance Program's data and map using [palletjack](https://github.com/agrc/palletjack) for the heavy lifting.

## Installation

1. Create new environment for the project with Arcpy, ArcGIS installed
   - `conda create --name era`
   - `activate era` (or `conda activate era` for older versions of conda)
   - `conda install arcpy arcgis -c esri`
1. Clone the repo
   - `cd path\to\parent\folder`
   - `git clone https://github.com/agrc/era`
1. Install via pip
   - `cd era`
   - `pip install -e .`
1. Set configuration variables in `secrets.py`
   - Copy `secrets_template.py` to `secrets.py`
   - Set all variables to appropriate values

## Running

1. `era` does not depend on any command line arguments; all needed info is set in `secrets.py`. Simply call `era` from your conda environment.

It first downloads the latest data from SFTP and loads it into a dataframe. There should just be a single file that is overwritten by DWS every Monday morning.

Next, it uses this dataframe to update the specified feature service row-by-row, skipping rows that don't appear in the dataframe.

Finally, it loads the specified web map, gets the information from the specified layer, and reclassifies the layer's symbology ranges based on a simple linear ramp from the min value to the mean plus one standard deviation (which appears to be AGOL's default unclassed classification scheme).

## Notifications

The log level, logging directory, and log rotation count are defined in `secrets.py`. By default, it is set to `logging.INFO`, but `logging.DEBUG` is available and will log detailed info about the process, mostly from `palletjack`. The log is sent to both stdout and the a rotating log file in the logging directory.

When it's finished, `era` builds a summary message and fires it off using Supervisor and the email settings in `secrets.py`. You will need a SendGrid API key. The email will include a copy of the latest log file.
