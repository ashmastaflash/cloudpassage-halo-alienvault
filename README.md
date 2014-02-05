#Halo Plugin for AlienVault/OSSIM
This plugin requires that the Halo API event retrieval program (located at https://github.com/cloudpassage/halo-event-connector-python) be installed on your AlienVault Sensor/AllInOne. 

##Before We Begin
We'll leave it to you to set up the halo-event-connector-python program.  This document assumes that you already have it set up and running on your AlienVault All-In-One appliance.  If you are using a distributed setup, you should set up the halo-event-connector-python script on the AlienVault Sensor, along with the plugin enclosed in this project, and load the SQL (cloudpassage-halo.sql) into the USM/SIEM Server device (The device running the ossim-server process).  More details on that later.
Installing this into a test environment beforehand is recommended (OSSIM is free, after all)... it doesn't take very long to get this going and it is well worth your time to play around in a test environment to get a handle on data flow before making a production change.

###Step by Step
First, set up the halo-event-connector-python component.  Use the documentation in that project, but substitute the cron script we have included in this project.  Place the cloudpassage-halo.cfg file in the /etc/ossim/agent/plugins directory on the All-In-One (or Sensor).  Edit the /etc/ossim/agent/config.cfg.orig file and add an entry in the [plugins] section.  It will look something like this:

    [plugins]
    ...
    cloudpassage-halo=/etc/ossim/agent/plugins/cloudpassage-halo.cfg
Then run the alienvault-setup program to enable the plugin, or enable it under AlienVault Center in the web UI.

Update the AlienVault SID table in the All-In-One (or USM Server in distributed environments)
    cat cloudpassage-halo.sql|ossim-db
    /etc/init.d/ossim-server restart

Now, clear the file that contains your last retrieval timestamp and the next time the halo-event-connector-python script kicks off it will retrieve all events, and the ossim-agent service should pick them up.

Don't forget to put the logrotate config file and the cron config file in place (mentioned below) to ensure that events keep flowing in and don't consume the entire disk.

Here’s a breakdown of the files you see here:
cloudpassage-halo.cfg   			AlienVault plugin

sidmap/alienvaultSidBuilder.py		Creates SQL script from Halo SIDs, depends on haloEventMappings.py

sidmap/haloEventMappings.py		    This contains the event name to SID mapping, and a list of events to elevate rel/priority for Ensures that certain events will become alarms when they involve an asset with a value of 3 or greater.  This is derived from information in the halo-event-connector-python project.

sidmap/cloudpassage-halo.sql        This is the SQL file to load into AlienVault for the Halo plugin to work properly.

cloudpassage-halo-cron              This is the cron script, it goes in /etc/cron.d

cloudpassage-halo-logrotate         This is the logrotate config, place it in /etc/logrotate.d/

