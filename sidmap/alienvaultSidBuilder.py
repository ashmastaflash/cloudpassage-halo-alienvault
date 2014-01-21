#!/usr/bin/python

from haloEventMappings import eventIdMap
from haloEventMappings import eventIdsToElevate
from operator import itemgetter

pluginId = 9876
sqlfile = './cloudpassage-halo.sql'
sqlheader = '-- Cloudpassage Halo \
            \n-- plugin_id: '+str(pluginId)+' \
            \n-- \
            \n-- TODO: Add Full Taxonomy \
            \nDELETE FROM plugin WHERE id = "'+str(pluginId)+'"; \
            \nDELETE FROM plugin_sid where plugin_id = "'+str(pluginId)+'"; \
            \nINSERT IGNORE INTO plugin (id, type, product_type, name, description) VALUES ('+str(pluginId)+', 1, 13, \'Halo\', \'CloudPassage Halo\'); \
            \nINSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name) VALUES \n' 
sqlfooter = '('+str(pluginId)+', 2000000000, NULL, NULL, \'Halo: Generic event\');'
sqlelevate = ''
for e in eventIdsToElevate:
    sqlelevate = sqlelevate+'\nUPDATE plugin_sid set reliability=\'3\', priority=\'3\' where sid='+str(e)+' and plugin_id='+str(pluginId)+';'
sqlresult = sqlheader
for i, j in sorted(eventIdMap.items(), key=itemgetter(1)):
    sqlresult = sqlresult+'('+str(pluginId)+', '+str(j)+', NULL, NULL, \'Halo: '+str(i)+'\'),\n'
sqlresult = sqlresult+sqlfooter+sqlelevate
s = open(sqlfile, 'w')
s.write(sqlresult)
