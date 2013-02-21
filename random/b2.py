#!/usr/bin/python2

import os
import time

source = [
		'/home/athul/transfer',
		'/home/athul/abs'
	]
target_dir = '/tmp/'
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory ' + today
comment = raw_input("Enter a comment ---> ")
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
if os.system(zip_command) == 0:
	print "Backup successful at " + target
else:
	print "Backup FAILED"
