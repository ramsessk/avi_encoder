#!/usr/bin/env python

import os, sys



'''

0. find tools (conversion python files and HandbreakCLI)
1. smi to srt
2. srt to individual srt
3. preprocess to encoder [[mp4, srt_1, srt2], [mp4,srt], [mp4,srt_1, srt_2, srt_3],...]
4. avi to mp4 (external tool : HandbreakCLI)

'''



#os.system('cd /Volumes/K9/movies/Numbers/S4')
if len(sys.argv) <= 1:
	print """
	usage : python mp2encode.py avi_directory
	example : avi_dirctory : /Volumes/usb_stick/movies/
	
	Location of related files to execution .....
	HandbreakCLI location : ~/Movies/HandBreakCLI/
	avi2mp4withsrt.sh or avi2mp4.sh location : ~/bin/
	english_from_srt.py location : ~/bin/
	"""
	exit()

avi_files = []
srt_files = []
dirs = os.listdir(sys.argv[1])
for s in dirs:
	#print s
	if s[-4:] == '.avi':
		avi_files.append(s[0:-4])
		#print s[0:-4]

for s in dirs:
	#print s
	if s[-4:] == '.avi':
		srt_files.append(s[0:-4])
		#print s[0:-4]

print len(avi_files), len(srt_files)

print "extract english subtile only from srt file ..."
print
curdir = os.getcwd()
#print curdir
os.system('cd ' + sys.argv[1])
os.system('python ~/bin/english_from_srt.py')
os.system('cd ' + curdir)
print "completed english subtile extraction ..."
os.getcwd()

n = 0
for s in avi_files:
	print "==============================================================="
	print 'start : ', s
	print "==============================================================="
	
	no_srt = False
	try :
		idx = srt_files.index(avi_files[n])
	except:
		print avi_files[n], ': No SRT file found'
		no_srt = True
		
	if no_srt:
		cmd = './avi2mp4.sh ' + sys.argv[1] + avi_files[n]
	else:
		cmd = './avi2mp4withsrt.sh ' + sys.argv[1] + avi_files[n]
	
	print cmd
	os.system(cmd)
	n = n + 1

#print srt_files.index('abc')
