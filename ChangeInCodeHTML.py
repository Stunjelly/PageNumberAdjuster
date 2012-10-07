import shutil
import os
import re

## Script will change pagenumbers inside the HTML to the filename found.

folder = "C:\wamp\www\parker\working\Text\edit\do"
os.chdir(folder)
startingpage = 0

def changenumbers(folder):
	for afile in os.listdir(folder):
		if afile.endswith('.xhtml'):
			page = re.search('page([0-9]*)\.xhtml', afile)
			if int(page.group(1)) > startingpage:
				shutil.move( afile, afile + ".bak" )
				destination = open( afile, "w" )
				source = open( afile + ".bak", "r" )
				if page:
					print "Processing Page" + page.group(1)
					for line in source:
						m = re.match(r'<div class="pagenumber">([0-9]*)</div>', line)
						if m is not None:
							#print "Found in page " + page.group(1) + ", text showing " + m.group(1)
							#newpage = m.sub('',line)
							line = re.sub(r'<div class="pagenumber">([0-9]*)</div>', '<div class="pagenumber">'+page.group(1)+'</div>', line)
							destination.write(line)
						else:
							destination.write(line)

				source.close()
				destination.close()

def restorebaks(folder):
	for afile in os.listdir(folder):
		if afile.endswith('.xhtml'):
			os.remove(afile)
		elif afile.endswith('.bak'):
			shutil.move( afile, afile[:-4] )


changenumbers(folder)
#restorebaks(folder)