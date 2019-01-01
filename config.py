##IMPORTANT!!!## you must turn off "Use a prediction service to load pages more quickly" in Google Chrome for this to work

#path to hosts file
##for Windows
hostsPath = "C:/Windows/System32/drivers/etc/hosts"
##for MacOS
#hostsPath = "/private/etc/hosts"

#hosts to blackList
#example: google.com not www.google.com
blockSites = ["youtube.com"]

#Time to block(in minutes)(must be an integer)
time = 2

#browsers to restart
##for Windows
webBrowsers = ["firefox.exe", "chrome.exe", "opera.exe", "MicrosoftEdge.exe", "Safari"]
##for MacOS
#webBrowsers = ["Safari", "Google Chrome", "firefox", "Opera"]
