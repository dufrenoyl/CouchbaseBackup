#!usr/bin/python

import time
import os
import commands
import sys, getopt

#Setup variables for the name repository
#path = "/bck_couchbase/repositorios"
path = "/Users/ludovic/Documents/Documents/Development/CouchbaseBackupsFiles/"
pathcouchbase = "/opt/couchbase/bin/"
date = time.strftime('%m%d%Y-%H%M%S')
username="Administrator"
password="'supersecret'"
usage="fullBackup-couchbase.py --room (-r) <roomname> --cluster (-c) <clusterIP> --bucket (-b) <bucketname>"

#Get script arguments
try:
    opts, args = getopt.getopt(sys.argv[1:],"hr:b:",["room=","bucket=","cluster="])
except getopt.GetoptError:
    print usage
    sys.exit(2)
#If we are missing arguments
if len(sys.argv[1:]) != 6:
    print "ERROR: Wrong Number of Arguments => " + usage
    sys.exit(2)
#Parsing arguments
for opt, arg in opts:
    if opt == '-h':
        print usage
        sys.exit()
    elif opt in ("-r", "--room"):
        roomname = arg
    elif opt in ("-b", "--bucket"):
        bucketname = arg
    elif opt in ("-c", "--cluster"):
        clusterIP = arg

backupname =  roomname + "_" + bucketname + "_" + date
print "!NEW WEEKLY BACKUP!"
print "Room= " + roomname
print "Cluster= " + clusterIP
print "Backupfile= " + backupname

#Let's create & configure the new repository
os.system("cd " + path)
if not os.path.exists(path):
    print "ERROR: Path is not correct"
    sys.exit(2)
else:
    #os.system(pathcouchbase + "cbbackupmgr config --archive " + path + " --repo " + backupname + " --include-buckets " + bucketname)
    print (pathcouchbase + "cbbackupmgr config --archive " + path + " --repo " + backupname + " --include-buckets " + bucketname)

#List repositories
#os.system(pathcouchbase + "cbbackupmgr list --archive " + path)
print (pathcouchbase + "cbbackupmgr list --archive " + path)

#Backup couchbase
#cbbackupmgr backup --archive /data/backup --repo sala1Semana32 --cluster lnxcmr1cb1.intrallianz.es --username Administrator --password password
print (pathcouchbase + "cbbackupmgr backup --archive " + path + " --repo " + backupname + " --cluster " + clusterIP + "--username " + username + " --password " + password)
