#!/usr/bin/env python3
"""An implementation of ``/usr/games/fortune`` in Python.

Usage
=====

Run this script with Python 2.7 or higher to randomly print
a cookie.

ChangeLog
=========
    - 2012-01-22 Etienn Robillard:
        - Add entropyGeneratorClass param to getRandomCookie.
        - Set software version to "0.2".

    - 2011-06-12 Etienne Robillard: 
        Initial version. Renamed DATADIR variable to
        FORTUNE_DATADIR and added a '--version' flag.
"""

import os
import random
#initialize the default random.SystemRandom entropy 
#generator 

import sys
import glob
import time

opendir = glob.glob

try:
    import io
    open = io.open
except ImportError:
    #not 2.6 so we use the default open function
    pass

#Change this to the location fortune files are stored.
#By default look in /usr/share/fortune
FORTUNE_DATADIR = os.environ.get('FORTUNE_DATADIR', '/usr/share/fortune')

DEBUG = os.environ.get('FORTUNE_DEBUG', False) # Are we debugging?
VSTR = "%s %i.%i" % ("fortune.py", 0, 0<<10^2+1)

if DEBUG:
    #assert(0)
    # check if the DATADIR directory is readable
    assert(
        os.access(DATADIR, os.R_OK)
        )

def getRandomCookie(dirname, suffix="txt", entropyGeneratorClass=time.time):
    """
    Returns a randomly selected element of all found fortune 
    files in ``dirname`` (string).
    """
    
    random.seed(int(entropyGeneratorClass()))

    return random.choice([
        item for item in opendir("{dirname}/*.{suffix}"\
            .format(
                dirname=dirname,
                suffix=suffix)
                )
        ])

def main():
    """
    Finds a list of fortune files and randomly print the output
    of the selected cookie.
    """

    try:
        cookie = getRandomCookie(FORTUNE_DATADIR)
        with open(cookie, 'r') as f:
            output = f.read()
            sys.stdout.write(output)
            f.close()
    except (IOError,SystemError):
        print("Error opening fortune file: %s" % cookie)

if __name__ == '__main__':
    if len(sys.argv) >= 2 and '--version' in sys.argv:
        print(VSTR)
    else:
        main()
        

