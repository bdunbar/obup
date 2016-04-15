#!/usr/bin/python
"""
Python script to test whether an OpenBazaar Server instance is up.
"""

import os
import sys
import json
import requests
from datetime import datetime
from pprint import pprint
import time

#############################################################################
#############################################################################

OBUSERNAME = os.environ.get("OBUSERNAME")
OBPASSWORD = os.environ.get("OBPASSWORD") 
OBGUID = os.environ.get("OBGUID")

OB_REST_PORT = os.getenv("OB_REST_PORT",18469)

URL_LOGIN = 'http://localhost:' + str(OB_REST_PORT) + '/api/v1/login'
URL_PROFILE = 'http://localhost:' + str(OB_REST_PORT) + '/api/v1/profile'
REQUEST_TIMEOUT = 10 #in seconds

#############################################################################
#############################################################################


def obLogin(OBUSERNAME, OBPASSWORD, URL_LOGIN, REQUEST_TIMEOUT):
    try:
        logindata = { 'username': OBUSERNAME, 'password': OBPASSWORD }
        response = requests.post(url=URL_LOGIN, data=logindata, timeout=REQUEST_TIMEOUT)
        logged_in = response.json()["success"]
    except:
        return False

    if not logged_in:
        return None 

    return response.cookies

def getProfile(cookies, URL_PROFILE, REQUEST_TIMEOUT):
    try:
        response = requests.get(url=URL_PROFILE, cookies=cookies, timeout=REQUEST_TIMEOUT)
        return response.json()['profile']['guid']
    except:
        return False


obrestart = False 
obstatus = "UP"
oblogintime = 0
obprofiletime = 0
obguidmatch = False
totaltime = datetime.now()

# Log in to OB Server and get session cookie
beforetime = datetime.now()
cookies = obLogin(OBUSERNAME, OBPASSWORD, URL_LOGIN, REQUEST_TIMEOUT)
oblogintime = (datetime.now() - beforetime).seconds

if cookies == False:
    obrestart = True 
    obstatus = "Unable to Connect"

elif cookies == None:
    obrestart = False
    obstatus = "Invalid Login Credentials"

else:
    # Now the session cookie to pull profile and check the GUID
    beforetime = datetime.now()
    guid = getProfile(cookies, URL_PROFILE, REQUEST_TIMEOUT)
    obprofiletime = (datetime.now() - beforetime).seconds
    
    if guid == False:
        obstatus = "Unable to get Profile"
        obrestart = True 
    elif guid != OBGUID: 
        obstatus = "Profile GUID does not match"
        obrestart = False 

totaltime = (datetime.now() - totaltime).seconds

print "%.5fs %.5fs %.5fs : %s" % (oblogintime, obprofiletime, totaltime, obstatus)
if obrestart:
    sys.exit(1)
else:
    sys.exit(0)

