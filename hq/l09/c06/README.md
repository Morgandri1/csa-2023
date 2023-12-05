# Mission extension
For this challenge, SSH into the server, and run this command:
``for f in `ls Contents/`; do file Contents/${f}; done``
then, find the file with the JPEG file header and execute the following command:
``cat Contents/<filename> > out.jpg``
Exit the SSH instance and open up an SFTP provider (or open the image file in this writeup) then locate the out.jpg file in the home directory. you'll read the SN from there.
