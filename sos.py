#!/usr/bin/env python3
import os, subprocess, datetime

source_folder = "/home/tttt/Projekte/scripts/secure-upload-sync/test-upload/test1/"
def upload(folder):
    print("will upload" + folder) 
    cmdline = "rsync -ruvhe  %s mvierthaler.at:/www/htdocs/w00e2fd1/sus/manual_upload/" % folder
    os.system(cmdline)

def computeChecksum(folder):
    hash = "sha256sum"
    cmdline = "find %s -type f -print0 | xargs -0 %s | awk {'print $1'} | tr '\n' ' ' | %s | awk {'print $1'}" % (folder, hash,hash)
    hashsum_result = subprocess.check_output(cmdline, shell=True)
    print(str(hashsum_result))
#todo compute hashes of directory names
#find test-upload -type d -print | xargs -I blah echo "blah"
    file_hashsum_result = open('./hashsum_result', 'w')
    file_hashsum_result.write(str(hashsum_result))
    file_hashsum_result.close()

def packThingsTogether(targetArchive):
    cmdline = "tar -vzcf %s -C ~ .tmux .zshrc Documents/ZIM_offline_clean/" % targetArchive
    os.system(cmdline)


#upload()
#computeChecksum("/home/tttt/Projekte/scripts/secure-upload-sync/test-upload")
archive_filename = "/tmp/convima_" + str(datetime.datetime.now().date()) + ".tar.gz"
print(archive_filename)
packThingsTogether(archive_filename)
upload(archive_filename)
cmdline = 'rm -r %s' % archive_filename
#os.system(cmdline)
