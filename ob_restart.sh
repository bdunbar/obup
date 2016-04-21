#!/bin/sh

echo "############################################################"
cd $OBHOME 
echo "STOPPING OPENBAZAAR"
python openbazaard.py stop
echo "WAITING 5 SECONDS"
sleep 5 
echo "KILL ZOMBIES"
killall -9 python
echo "UPDATING SERVER"
git pull
echo "REMOVING PIDFILE"
rm -f /tmp/openbazaard.pid
#echo "PICKLE DANCE"
#rm -f ~/.openbazaar/cache.pickle
echo "STARTING SERVER"
if [ -z $OBALLOWEDIP ]; then python openbazaard.py start -d; else python openbazaard.py start -da $OBALLOWEDIP; fi
echo "############################################################"
