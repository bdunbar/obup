#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

if [ ! -f settings.conf ]
then
    echo "#######################################################"
    echo "#                                                     #"
    echo "#  ERROR:  settings.conf file is missing.             #"
    echo "#                                                     #"
    echo "#  You can use settings.conf.default as a reference.  #"
    echo "#                                                     #"
    echo "#######################################################"
    exit
fi

source settings.conf
./obup.py 

if [ $? != 0 ]
then
   echo "RESTARTING OB"
   #./ob_restart.sh 
fi

unset OBHOME
unset OBSCRIPTS
unset OBUSERNAME
unset OBPASSWORD
unset OBGUID
unset OB_REST_PORT

