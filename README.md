# obup

This is the currently what I am using to determine whether my OpenBazaar Server instance is up and responding.  If it is not then it will stop/kill any proceses, update the server, then start the server.

## Settings
The first step to using the script is to set up the configuration file with the information needed to connect.  You can use the settings.conf.default file as a reference.  Filling it out should be pretty self explanatory.
```
cp settings.conf.default settings.conf
```

## Install moreutils (Optional)
I like to use ts to add timestamps to my log files.  You need to install the moreutils package to get it on Debian/Ubuntu based systems.
```
sudo apt-get install moreutils
```

## Cron
I have the script run every 5 minutes.  Here is an example entry for cron.
```
*/5 *   *   *   *   /home/ob/obup/check.sh 2>&1 | ts [\%Y.\%m.\%d.\%k.\%M.\%S] >> /home/ob/obup/check.log
```

**__Be sure your script is working correctly before leaving cron running or else you might just have your server restarting every 5 minutes__**

## Thanks
Did you find any of this useful?  Tell me so.  I'm @serp and @obmod in the OpenBazaar network.
