#! /usr/bin/env python
# made by following  this :  https://bitbucket.org/cpbotha/indicator-cpuspeed



import os
import subprocess
from gi.repository import Gtk, GLib
import about_window
try: 
       from gi.repository import AppIndicator3 as AppIndicator  
except:  
       from gi.repository import AppIndicator


#Config variables

MINUTES_FOR_BREAK = 50			#time after which alert should be given
SNOOZE_TIME = 10 				
BREAK_INTERVAL = 5 				#min idle time after which we assume that the user has taken a break

class TakeBreak:
    def __init__(self):

        # param1: identifier of this indicator
        # param2: name of icon. this will be searched for in the standard dirs
        # param3: finally, the category of the indicator.
        self.ind = AppIndicator.Indicator.new(
                            "indicator-takebreak",
                            os.path.dirname(os.path.realpath(__file__)) + "/Invisible.png",
                            AppIndicator.IndicatorCategory.SYSTEM_SERVICES)

        
        self.minutes = 0

        # need to set this for indicator to be shown
        self.ind.set_status (AppIndicator.IndicatorStatus.ACTIVE)
        
        
        self.menu = Gtk.Menu()

        #menu item for reseting the minutes.
        item = Gtk.MenuItem()
        item.set_label("Reset")
        item.connect("activate", self.handler_menu_reset )
        item.show()
        self.menu.append(item)

        #menu item for reseting the minutes.
        item = Gtk.MenuItem()
        item.set_label("About")
        item.connect("activate", self.handler_menu_about )
        item.show()
        self.menu.append(item)

        # menu item for quiting the indicator
        item = Gtk.MenuItem()
        item.set_label("Exit                      ")
        item.connect("activate", self.handler_menu_exit	)
        item.show()
        self.menu.append(item)

        self.menu.show()
        self.ind.set_menu(self.menu)
    

        # initialize time display with 0 min.
        self.update_time()

        # then start updating every 60 seconds
        GLib.timeout_add_seconds(60, self.handler_timeout)

    

    def handler_menu_exit(self, evt):
        Gtk.main_quit()

    def handler_menu_reset(self,evt):
    	self.minutes = 0
    	self.update_time()

    def handler_menu_about(self,evt):
    	AboutWindow = about_window.AboutWindow()
    	AboutWindow.main()

    def handler_timeout(self):
        # This will be called every minute by the GLib.timeout. 	
         
        # Resets the time counter if the user has been idle for too long

		if idle_too_long(): 	
			self.minutes = 0
		else:
			self.minutes += 1
		self.update_time()
		return True


    #Note: Here the second parameter is a label_guide
    #label_guide: An optional string to provide guidance to the panel on how big the AppIndicator label string could get.
    #			   If this is set correctly then the panel should never 'jiggle' as the string adjusts through out the range of options.
    def update_time(self):
        self.ind.set_label(str(self.minutes)+"m","101m")
        if(self.minutes >=	MINUTES_FOR_BREAK and (self.minutes-MINUTES_FOR_BREAK)%SNOOZE_TIME==0): 
        	self.notify()


    def notify(self):
    	msg = '"Time for a Break.."'
        notification = os.system('notify-send -i face-laugh '+msg)
        
        try:
        	os.system("cvlc /usr/share/sounds/freedesktop/stereo/complete.oga  --play-and-exit")
    	except OSError:
    		pass
        
        return

    def main(self):
        Gtk.main()


# Function to determine if user has taken a break
# if idletime is greater that BREAK_INTERVAL (by default 5 minutes) we assume that user has taken a break.
# xprintidle is utility tool that prints out the user's idle time in milliseconds (60000ms is 1 min)
# the error handling part will make sure that problems with xprintidle will not break the app completely.
def idle_too_long():
	
	try:
		idletime = subprocess.Popen(["xprintidle"], stdout=subprocess.PIPE).communicate()[0]
	except OSError:
		return False

	idletime = int(idletime[:len(idletime)-1])
	idletime = idletime/60000
	
	if idletime>= BREAK_INTERVAL: return True
	else: return False



if __name__ == "__main__":
    ind = TakeBreak()
    ind.main()


