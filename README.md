# Pythonista_SunCalculator_for_iPhone
Pythonista Sun Height and Position Calculator based on time and geolocation. Moon stats also included.

Pythonista Sun Calculator for iPhone installation manual
—————————————————————————

1. Install Stash Shell for Pythonista: https://github.com/ywangd/stash
2. Start `launch_stash.py`
3. Enter `pip install odfpy` to install `odfpy` via pip on Stash Shell.

If installation aborts under Python3 version of Stash, switch to Python2 version by inserting the following first line at the top of the `launch_stash.py` script:

`#! python2`

Then re-open Stash and enter `pip install odfpy`

Copy the odf install files manually from Python2 to Python3 directory in Pythonista App, i.e. Python Modules -> `site-packages-2/odf` to `site-packages-3/odf`.

4. Optional for PDF export: Get a free Cloudmersive API key here: https://account.cloudmersive.com/signup

Use Pythonista to open the `cloudmersive-apikey.txt` file contained in this package and paste in your API key.

Note: Without an API key, reports you generate can only be opened in Pythonista App.

5. Enter in Stash in Python3 mode (e.g. remove `#! python2` tag from `launch_stash.py` script) and enter: `ip install cloudmersive_convert_api_client`

6. Open Stash in Python3 mode and enter:
`pip install timezonefinder`

7. Due to dependencies, URLLib3 could already have been installed via Pip. To be sure, try in Stash in Python3 mode:
`pip install urllib3`

8. Now copy the software to your iPhone:
    * Extract SunCalc.zip to your iCloud-Pythonista3-folder into a separate iCloud directory
    * Open Pythonista, create a local directory SunCalc on your iPad and enter that directory
    * Use `+` and `File Import` and import all files from the iCloud SunCalc directory to your local directory within the Pythonista App (19 files in total including this manual)

9. Now you should be ready to go:
Launch `suncalc.py` in your iPhone and explore!
