#import os, sys
#from stat import *
#
#def walktree(top, callback):
#	'''recursively descend the directory tree rooted at top,
#	   calling the callback function for each regular file'''
#	
#	for f in os.listdir(top):
#		pathname = os.path.join(top, f)
#		try:
#			mode = os.stat(pathname).st_mode
#		except:
#			print "Error"
#			continue
#		
#		if S_ISDIR(mode):
#			# It's a directory, recurse into it
#			walktree(pathname, callback)
#		elif S_ISREG(mode):
#			# It's a file, call the callback function
#			callback(pathname)
#		else:
#			# Unknown file type, print a message
#			print 'Skipping %s' % pathname
#
#def visitfile(filename):
#	print 'visiting', filename
#
#
#
#if __name__ == '__main__':
#	walktree(sys.argv[1], visitfile)



import unittest
import datetime

class DatePattern:
	def __init__(self, year, month, day):
		self.date = datetime.date(year, month, day)
	def matches(self, date):
		return self.date == date

class FooTests(unittest.TestCase):
	def testMatches(self):
		p = DatePattern(2004,9,28)
		d = datetime.date(2004,9,28)
		self.failUnless(p.matches(d))
		
	def testMatchesFalse(self):
		p = DatePattern(2004,9,28)
		d = datetime.date(2004,9,29)
		self.failIf(p.matches(d))
		

def main():
	unittest.main()

if __name__ == '__main__':
    main()
