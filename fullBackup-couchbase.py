import time
import os
import commands
username="Administrator"
password="'supersecret'"

#Setup variables for the name repository
PATH = "/bck_couchbase/repositorios"
DATE = time.strftime('%m%d%Y-%H%M%S')
BACKUPNAME =  '' + DATE
#Let's create the new repository 
DATE = time.strftime('%m%d%Y-%H%M%S')
DUMP_PATH="/tmp/"
BACKUPNAME =  DUMP_PATH + DATE
if not os.path.exists(BACKUPNAME):
    os.makedirs(BACKUPNAME)
    print (BACKUPNAME)
commands="cd /opt/couchbase/bin && ./cbbackup http://localhost:8091 "  + BACKUPNAME + " -u " + username + " -p " + password
run=os.system(commands)
zipit="zip -r " + BACKUPNAME + ".zip " + BACKUPNAME
os.system(zipit)
upload= "aws s3 mv " + BACKUPNAME +".zip s3://couchbasebackups/"
os.system(upload)
