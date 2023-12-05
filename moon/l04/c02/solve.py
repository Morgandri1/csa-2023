#
# Fix the below script to read from each agent file found in /tmp.
# Example agent profile would be /tmp/agent-1.txt
# The contents of each of the agent files makes up the flag
#


import os.path

count = 1
out = []

for i in range(20):
	fname = "/tmp/agent-" + str(count)+".txt"
	if os.path.isfile(fname):
		with open(fname, 'r') as content_file:
			content = content_file.read()
			out.append(content.rstrip())
	count += 1
  
print("".join(out))
