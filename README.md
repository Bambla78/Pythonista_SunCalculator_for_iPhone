# Pythonista_SunCalculator_for_iPhone
Pythonista Sun Height and Position Calculator based on time and geolocation. Moon stats also included.

Pythonista Sun Calculator for iPhone installation manual
—————————————————————————

1. Install Stash Shell for Pythonista 
https://github.com/ywangd/stash

2. Install odfpy via pip on Stash Shell and start ‚launch_stash.py‘
3. Enter ‚Pip install odfpy‘ in Stash

If installation aborts under Python3 version of Stash, switch to Python2 version by inserting the following first line at the top of the ‚launch_stash.py‘ script:

#! python2

Then re-open Stash and enter ‚pip install odfpy‘

Copy the odf install files manually from Python2 to Python3 directory in Pythonista App, i.e. Python Modules -> site-packages-2/odf to site-packages-3/odf.

4. Optional for PDF export: Get a free Cloudmersive API key here:  https://account.cloudmersive.com/signup

Copy you API key into the text file ‚cloudmersive-apikey.txt‘ contained in this package (you can use Pythonista app for editing)

Note that without API you will only be able to generate Open Document reports that will be stored in your program folder within Pythonista App.

5. Enter in Stash in Python3 mode (e.g. remove #! python2 tag from launch_stash.py script) and enter: ‚Pip install cloudmersive_convert_api_client‘

6. Open Stash in Python3 mode and enter:
‚Pip install timezonefinder‘

7. Due to dependencies, URLLib3 could already have been installed via Pip. To be sure, try in Stash in Python3 mode:
‚Pip install urllib3‘

8. Now copy the software to your iPad:
a. Extract SunCalc.zip to your iCloud-Pythonista3-folder into a separate iCloud directory
b. Open Pythonista, create a local directory SunCalc on your iPad and enter that directory
c. Use ‚+‘ and ‚File Import‘ and import all files from the iCloud SunCalc directory to your local directory within the Pythonista App (17 files in total including this manual)

9. Now you should be ready to go:
Launch suncalc.py in your iPhone and explore!









