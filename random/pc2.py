import re
import urllib2

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = str(82682)
contents = urllib2.urlopen(url+num).read()
match_obj = re.findall(r".* (\d+)", contents)
while match_obj:
    match_obj = re.findall(r".* (\d+)", contents)
    num = match_obj[0]
    print num
    contents = urllib2.urlopen(url+num).read()
print contents
