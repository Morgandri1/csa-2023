#
# Find the valid png file in the /tmp directory using magic bytes.
# The code is hidden in this file.
#
import imghdr
import os

for file in os.listdir("/tmp"):
		t = imghdr.what('/tmp/'+file)
		if t == "png":
				print(file) 
				print(open("/tmp/"+file, "rb").read())
		else:
				continue
