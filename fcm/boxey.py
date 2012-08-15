#!/usr/bin/env python2

import os

def toporbottom (sep = '=', width = 30):
	return "+%s+" % (sep * (width - 2))

def fmt_list (item, value):
	return "| %s %s |" % (item.ljust(20, " "), str(value).ljust(5, " "))

def box_list (items):
	print toporbottom()
	for item in items:
		print fmt_list(item, items[item])
	print toporbottom("-")
	print fmt_list("Total", sum(items.values()))
	print toporbottom()

if __name__ == '__main__':
	print "List (q to quit):\n"
	items = {}
	item = ' '
	price = 0
	while 1:
		item = raw_input("Enter the item: ")
		if item == 'q':
			break
		price = input("Enter the price: ")
		items[item] = price
	os.system('clear')
	box_list(items)
