#!/usr/bin/env python
import logging
from app import app as application


###---> Installing missing modules that are not pre-installed on Azure eg joblib https://stackoverflow.com/questions/40563512/install-python-modules-in-azure

import os,pip,sys,time

##try:
##    #import pyodbc    #Original code
##    import joblib
##except:
##    #package = 'pyodbc-3.0.10-cp27-none-win32.whl'       #Original code
##    package = 'joblib-0.14.1-py2.py3-none-any.whl'
##    pip.main(['install', '--user', package])
##    raise ImportError('Restarting')



###---<  FINISHED INSTALLING JOBLIB


#logger = logging.getLogger("app")  # Original code


#def main(port=9000, debug=True):   # Original code

def main():
    #logger.info("Staring App at Port: {} with Debug Option: {}".format(port, debug))   #Original code
    #application.run(port=port, debug=debug)  # Original code
    application.run()


#if __name__ == '__main__':   #Original code
#    main()                   #Original code
