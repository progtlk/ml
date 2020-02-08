import logging
import os

import pickle
from flask import Flask

#import joblib

#from sklearn.externals import joblib  #deprecated so import joblib directly below

#import joblib         #importing joblib directly not from sklearn

# create logger for app
logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)

app = Flask(__name__)
app.config.from_object("app.config")


path= os.getcwd()

# unpickle my models
MODELS = {
    "iris": {
        #"estimator" : joblib.load(path+'models/iris/model.pkl'),       #For Linux execution and Azure Deployment
        
        "estimator" : pickle.load(path+'models/iris/model.pkl'),       #For Linux execution and Azure Deployment avoiding Joblib library using pickle instead
        
        #"estimator" : joblib.load(path+'\\app\\models\\iris\\model.pkl'),     #For Windows 10 desktop execution 
        "target_names": ['setosa', 'versicolor', 'virginica']
    }
}

from .views import *   # flake8: noqa


# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found"""
    return render_template('404.html'), 404
