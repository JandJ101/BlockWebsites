# BlockWebsites
This python script will block websites listed in its config file for a set amount of time also set in its config file.
The script only works on Windows for now, but it could be ported to other operating systems using its config file and making other tweaks.

You should run this script with Python 3.x.x

You must turn off "Use a prediction service to load pages more quickly" in Google Chrome for it to work in the Chrome browser.



## Instructions for config.py
### Choosing websites to block
To set the sites which you want to block, add them as a string to the array called **blockSites**.
Do not include www. in the domains to block

### Setting amount of time to block
change the variable **time** to a value in minutes. *Note: The value must be an integer.*

Most of the other settings can be left at default.
