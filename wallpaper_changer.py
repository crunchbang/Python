#!/usr/bin/python2
# wallpaper_changer.py
# A simple wallpaper changer using python and feh

import os
import sys
import random
import getpass
import errno
import cPickle as pkl



# To avoid repition a list of recently used
# wallpapers is maintained at .wall_list
used_list = []
wall_used = '.wall_list'
if wall_used not in os.listdir('.'):
	os.system('touch %s' % (wall_used))
used = file(wall_used, 'rb')
try:
	used_list = pkl.load(used)
except EOFError:
	pass
except:
	used.close()
# environment variable $USER should be set
user = getpass.getuser()
# location of wallpapers
wall_loc = '/home/' + user + '/.wallpapers/'
walls = os.listdir(wall_loc)
noofwalls = len(walls)
# picks a random wallpaper
choice = random.choice(walls)
used_list.append(choice)
if len(used_list) > noofwalls:
	used_list = []
wall_change = "feh -q --bg-scale %s" % (wall_loc + choice)
# Error number for DATA NOT FOUND
if os.system(wall_change) != 0:
	exit(errno.ENODATA)
used = file(wall_used, 'wb')
pkl.dump(used_list, used)
used.close()


