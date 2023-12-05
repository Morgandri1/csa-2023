# Exposure
Looking at [the seclists forum](https://seclists.org/fulldisclosure/2013/Mar/110), we're given a specific vuln string. 
``?buttonText=test%3Cimg%20src=%27http://demo.swfupload.org/v220/images/logo.gif%27%3E``

The robots.txt hint was a red herring, and the URL manipulation hint subjectively was as well. 
the SWFupload vuln is a url based XSS attack, and the above vuln string appended to the end of the URL will give the flag.
