import shutil
import os
import re

folder = "C:\wamp\www\parker\working\Text\edit"
os.chdir(folder)
startingpage = 90

for afile in os.listdir(folder):
	page = re.search('page([0-9]*)\.xhtml', afile)
	if int(page.group(1)) > startingpage:
		shutil.move( afile, afile + ".bak" )
		destination = open( afile, "w" )
		source = open( afile + ".bak", "r" )
		if page:
			for line in source:
				m = re.search('<div class="pagenumber([-l]?)">([0-9]*)</div>', line)
				if m is not None:
					print "n" + page.group(1) + "c" + m.group(2)
				else:
					destination.write(line)

		source.close()
		destination.close()