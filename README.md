# obup

This is what I am using to determine whether my OpenBazaar Server instance is up and responding.  If it is not then it will stop/kill any proceses, update the server, then start the server.  The process is:

1. Log in to get session token.
2. Use session token to get Profile.
3. Comprare GUID returned from Profile to GUID in settings file.
4. Restart openbazaard.py if unable to connect or get profile.


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

## Run
```
./check.sh test
```
check.sh is the main script.  By providing test at the command line it won't try to restart the server automatically if it fails to see the server up.  This will allow you to test your settings.  The format is:
```
[Time to Login] [Time to get profile] [Total Check Time] : [Status Text]
```
It is made this way to be easily parsable.  Ideally the times will always be 0.0000s.  If they are not then your server and or instance may be lagging.


## Cron
I have the script run every 5 minutes.  Here is an example entry for cron.
```
*/5 *   *   *   *   /home/ob/obup/check.sh 2>&1 | ts [\%Y.\%m.\%d.\%k.\%M.\%S] >> /home/ob/obup/check.log
```

**__Be sure your script is working correctly before leaving cron running or else you might just have your server restarting every 5 minutes__**

## Warranty/Support
These scripts come **AS-IS**.  I don't mind answering questions or taking suggestions but I'm just sharing the scripts I use and not releasing a product.

## Thanks or Suggestions
Did you find any of this useful?  Do you have a better way?  Tell me so.  I'm @serp and @obmod in the OpenBazaar network.
