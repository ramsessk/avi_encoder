#!/usr/bin/env python

import os, sys
import logging


'''

0. find tools (conversion python files and HandbreakCLI)
1. smi to srt
2. srt to individual srt
3. preprocess to encoder [[mp4, srt_1, srt2], [mp4,srt], [mp4,srt_1, srt_2, srt_3],...]
4. avi to mp4 (external tool : HandbreakCLI)

~/Movies/HandBreakCLI/HandBrakeCLI -i $1.avi -o $1.mp4 --srt-codeset UTF-8 --srt-file $var1,$var2 
		--srt-lang kor,eng --srt-default 1 --subtitle-burn 1

'''

###################################################################################################
def searchFiles(FileExtension, directory):
	""" Looking for files which has 'FileExtension' in current directory.

	:param FileExtension: file extension to look for, Ex. avi, or mkv. it should not include '.'.
	:type FileExtension : str
	:param directory: directory to look for
	:type directory : str

	:returns: Returns a list of files found:
		:rtype: list
	"""
	
	foundfiles = []
	dir_list = os.listdir(directory)
	#print FileExtension, dirs
	FileExtension = '.' + FileExtension
	for s in dir_list:
		if len(s) > len(FileExtension) and s[-len(FileExtension):] == FileExtension:
			foundfiles.append(s)
			logging.info("Found: {0}".format(s))
			#print s


	return foundfiles

###################################################################################################
def matchFiles(files1, ext, files2):
	""" match list index which has same file name except extension.
	Ex. for return data : [[mp4, srt_1, srt2], [mp4,srt], [mp4,srt_1, srt_2, srt_3],...]

	:param files1: It should be list of movie files
	:type files : list
	:param ext: movie file extension
	:type ext : str
	:param files2: list of srt files
	:type files2 : list

	:returns: Returns a list of matched files:
		:rtype: list
	"""
	
	matched_list = []
	job = []
	for s1 in files1:
		job.append(s1)
		name = s1[0:-len(ext)-1]
		print name
		for s2 in files2:
			if (name == s2[0:len(name)]):
				job.append(s2)
		matched_list.append(job)
		job = []
	return matched_list


###################################################################################################

logging.basicConfig(level=logging.ERROR)
if( os.path.exists(os.path.expanduser('~/bin/HandBrakeCLI')) == False ):
	print 'External encoder not available. It should be located at /Users/[USER]/bin'
	print 'External encoder : HandBrakeCLI '
	sys.exit()

avis = searchFiles('avi', sys.argv[1])
srts = searchFiles('srt', sys.argv[1])

m = matchFiles(avis, 'avi', srts)
print m
#print avis, srts

for m1 in m:
	#print m1
	cmd = '~/bin/HandBrakeCLI -i '
	cmd = cmd + m1[0]
	#print (m1[0])[0:-4]
	cmd = cmd + ' -o ' + (m1[0])[0:-4] + '.mp4' + ' --srt-codeset UTF-8 '
	srt_num = len(m1) - 1
	#print 'srt_num=', srt_num
	if( srt_num > 0 ):
		cmd = cmd + ' --srt-file '
		i = 1
		while srt_num > 0:
			cmd = cmd + m1[i]
			srt_num = srt_num - 1
			if( srt_num > 0):
				cmd = cmd + ','
			i = i + 1
		
		if((len(m1)-1) > 1):
			cmd = cmd + ' --srt-lang kor, eng '
			cmd = cmd + ' --srt-default 1 --subtitle-burn 1'
			
		cmd = cmd + ' --srt-default 1 --subtitle-burn 1'
	else:	# no subtitle
		pass
	cmd = cmd + ' --preset="AppleTV 2" '
	print cmd
	#os.system(cmd)


#~/Movies/HandBreakCLI/HandBrakeCLI -i $1.avi -o $1.mp4 --srt-codeset UTF-8 --srt-file $var1,$var2 
#		--srt-lang kor,eng --srt-default 1 --subtitle-burn 1




#if len(sys.argv) <= 1:
#	print """
#	usage : python mp2encode.py avi_directory
#	example : avi_dirctory : /Volumes/usb_stick/movies/
#	
#	Location of related files to execution .....
#	HandbreakCLI location : ~/Movies/HandBreakCLI/
#	avi2mp4withsrt.sh or avi2mp4.sh location : ~/bin/
#	english_from_srt.py location : ~/bin/
#	"""
#	exit()
#
#avi_files = []
#srt_files = []
#dirs = os.listdir(sys.argv[1])
#for s in dirs:
#	#print s
#	if s[-4:] == '.avi':
#		avi_files.append(s[0:-4])
#		#print s[0:-4]
#
#for s in dirs:
#	#print s
#	if s[-4:] == '.avi':
#		srt_files.append(s[0:-4])
#		#print s[0:-4]
#
#print len(avi_files), len(srt_files)
#
#print "extract english subtile only from srt file ..."
#print
#curdir = os.getcwd()
##print curdir
#os.system('cd ' + sys.argv[1])
#os.system('python ~/bin/english_from_srt.py')
#os.system('cd ' + curdir)
#print "completed english subtile extraction ..."
#os.getcwd()
#
#n = 0
#for s in avi_files:
#	print "==============================================================="
#	print 'start : ', s
#	print "==============================================================="
#	
#	no_srt = False
#	try :
#		idx = srt_files.index(avi_files[n])
#	except:
#		print avi_files[n], ': No SRT file found'
#		no_srt = True
#		
#	if no_srt:
#		cmd = './avi2mp4.sh ' + sys.argv[1] + avi_files[n]
#	else:
#		cmd = './avi2mp4withsrt.sh ' + sys.argv[1] + avi_files[n]
#	
#	print cmd
#	os.system(cmd)
#	n = n + 1

#print srt_files.index('abc')
