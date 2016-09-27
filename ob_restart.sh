#!/bin/sh

cd $OBHOME
logger -t openbazaard "STOPPING OPENBAZAAR"
service openbazaard stop
logger -t openbazaard "WAITING 5 SECONDS"
sleep 5
logger -t openbazaard "KILL ZOMBIES"
killall -9 python
#echo "UPDATING SERVER"
#git pull
logger -t openbazaard "REMOVING PIDFILE"
rm -f /tmp/openbazaard.pid
#echo "PICKLE DANCE"
#rm -f ~/.openbazaar/cache.pickle
logger -t openbazaard "STARTING SERVER"
service openbazaard start
