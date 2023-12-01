#
# We need you to send a spoofed email.
# Use smtp server at '127.0.0.1', port 1025.
# Author needs to be bob-roswell-1947@ship-shape-security.com
# Recipient needs to be zultron@cyberdarkart.com

import smtplib
host = '127.0.0.1'
port = 1025
sender = "bob-roswell-1947@ship-shape-security.com"
recipent = "zultron@cyberdarkart.com"
s = smtplib.SMTP(host=host,port=port)
s.sendmail(from_addr=sender,to_addrs=recipent, msg="Hello, what's up?")
