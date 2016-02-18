#!/usr/bin/env python3
import os,hashlib,subprocess

source_folder="/home/tttt/Projekte/scripts/secure-upload-sync/test-upload/test1/"
def upload():
	cmdline="rsync -ruvhe 'ssh -i /home/tttt/.ssh/rsync-zim' %s mvierthaler.at:/www/htdocs/w00e2fd1/sus/temp" % source_folder
	os.system(cmdline)

def computeChecksum(folder):
	hash="sha256sum"
	cmdline="find %s -type f -print0 | xargs -0 %s | awk {'print $1'} | tr '\n' ' ' | %s | awk {'print $1'}" % (folder, hash,hash)
	hashsum_result = subprocess.check_output(cmdline, shell=True)
	print(str(hashsum_result))
	#todo compute hashes of directory names
	#find test-upload -type d -print | xargs -I blah echo "blah"
	file_hashsum_result = open('./hashsum_result','w')
	file_hashsum_result.write(str(hashsum_result))
	file_hashsum_result.close()

#upload()	
computeChecksum("/home/tttt/Projekte/scripts/secure-upload-sync/test-upload")
