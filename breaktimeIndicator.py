

from gi.repository import Gtk, GLib

try: 
       from gi.repository import AppIndicator3 as AppIndicator  
except:  
       from gi.repository import AppIndicator

import re

class TakeBreak:
    def __init__(self):
        # param1: identifier of this indicator
        # param2: name of icon. this will be searched for in the standard dirs
        # finally, the category. We're monitoring CPUs, so HARDWARE.
        #"/usr/share/unity/icons/launcher_icon_glow_62.png",
        self.ind = AppIndicator.Indicator.new(
                            "indicator-cpuspeed",
                            "/home/nishanth/Desktop/Invisible.png",
                            AppIndicator.IndicatorCategory.HARDWARE)

        # some more information about the AppIndicator:
        # http://developer.ubuntu.com/api/ubuntu-12.04/python/AppIndicator3-0.1.html
        # http://developer.ubuntu.com/resources/technologies/application-indicators/
        self.minutes = 0
        # need to set this for indicator to be shown
        self.ind.set_status (AppIndicator.IndicatorStatus.ACTIVE)
        
        # have to give indicator a menu
        self.menu = Gtk.Menu()

        # this is for exiting the app
        item = Gtk.MenuItem()
        item.set_label("Exit                      ")
        item.connect("activate", self.handler_menu_exit	)
        item.show()
        self.menu.append(item)

        self.menu.show()
        self.ind.set_menu(self.menu)
        	
        # initialize cpu speed display
        self.update_time()
        # then start updating every 2 seconds
        # http://developer.gnome.org/pygobject/stable/glib-functions.html#function-glib--timeout-add-seconds
        GLib.timeout_add_seconds(60, self.handler_timeout)

    

    def handler_menu_exit(self, evt):
        Gtk.main_quit()


    def handler_timeout(self):
        """This will be called every few seconds by the GLib.timeout.
        """
        self.minutes += 1
        self.update_time()
        return True

    
    def update_time(self):
        self.ind.set_label(str(self.minutes)+"m","101m")

    def main(self):
        Gtk.main()

if __name__ == "__main__":
    ind = TakeBreak()
    ind.main()


