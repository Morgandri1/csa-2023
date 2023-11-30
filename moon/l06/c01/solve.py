#
# Find the file in the alien directories in /tmp/aliendir to get the flag
#
from os import listdir

for dir in listdir("/tmp/aliendir"):
  cont = listdir("/tmp/aliendir/" + dir)
  print(cont) if cont != [] else print()
