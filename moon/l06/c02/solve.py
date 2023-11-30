#
# Hide text in the image /tmp/image.gif
# Append the word alieneye to end of the file.
#
with open("/tmp/image.gif", "a+") as f:
  f.write("alieneye\n")
