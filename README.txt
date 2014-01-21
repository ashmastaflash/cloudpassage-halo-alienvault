This plugin requires that the Halo API event retrieval program (located at https://github.com/cloudpassage/halo-event-connector-python) be installed on your AlienVault Sensor/AllInOne.  Which is unsupported by AlienVault.  Bring your sense of adventure.

You must kick off the halo-event-connector-python script to output to CEF in a log file located at /var/log/halo.log.  Don’t forget to set up log rotate.
Example:
 ./haloEvents.py --cef >> /var/log/halo.log

There are better instructions on setting this up as a cron job in the halo-event-connector-python script documentation.


Here’s a breakdown of the files you see here:
cloudpassage-halo.cfg			AlienVault plugin

sidmap/alienvaultSidBuilder.py		Creates SQL script from Halo SIDs, 
					depends on haloEventMappings.py

sidmap/haloEventMappings.py		This contains the event name to SID mapping, 
					and a list of events to elevate rel/priority for.
					Ensures that certain events will become alarms
					when they involve an asset with a value of 3
					or greater.

sidmap/cloudpassage-halo.sql		This is the SQL file to load into AlienVault for
					the Halo plugin to work properly.
