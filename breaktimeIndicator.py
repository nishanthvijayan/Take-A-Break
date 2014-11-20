# made by following https://bitbucket.org/cpbotha/indicator-cpuspeed

# To-Add:
#	1. Bubble notifications	
#	2. monitor idleness
#	3. reset after logout,lock,suspend ?
#	4. option to change break time (currently 1Hr) 

import os
from gi.repository import Gtk, GLib

try: 
       from gi.repository import AppIndicator3 as AppIndicator  
except:  
       from gi.repository import AppIndicator


MINUTES_FOR_BREAK = 60

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
        # http://developer.gnome.org/pygobject/stable/glib-functions.html#function-glib--timeout-add-seconds
        GLib.timeout_add_seconds(60, self.handler_timeout)

    

    def handler_menu_exit(self, evt):
        Gtk.main_quit()

    def handler_menu_reset(self,evt):
    	self.minutes = 0
    	self.update_time()


    def handler_timeout(self):
        """	This will be called every minute by the GLib.timeout. 	"""
        self.minutes += 1
        self.update_time()
        return True


    #Note: Here the second parameter is a label_guide
    #label_guide: An optional string to provide guidance to the panel on how big the AppIndicator label string could get.
    #			   If this is set correctly then the panel should never 'jiggle' as the string adjusts through out the range of options.
    def update_time(self):
        self.ind.set_label(str(self.minutes)+"m","101m")

    def main(self):
        Gtk.main()



if __name__ == "__main__":
    ind = TakeBreak()
    ind.main()


