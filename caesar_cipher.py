import string

def let2int (c):
	return ord(c) - ord('a')

def int2let (n):
	return chr(ord('a') + n)

def shift (n, c):
	return int2let((let2int(c) + n) % 26)

def encode (n, msg):
	return string.join([shift(n, c) for c in msg], '')
