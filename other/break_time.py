import time
import webbrowser

i = 0
while (i < 3): 
    time.sleep(2*60*60)
    webbrowser.open("http://www.friendlyroad.com")
    i = i + 1
