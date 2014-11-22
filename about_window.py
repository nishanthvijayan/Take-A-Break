#! /usr/bin/env python

from gi.repository import Gtk

class AboutWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title = "About Take-A-Break Indicator")
		self.set_default_size(400, 300)
		Label = Gtk.Label()
		Label.set_markup(" Take-A-Break is an gnome indicator app that displays\n  the number of minutes for which you have been working \n "
						" and reminds you to take a break after every 1hr or so.\n  Improve your productivity and keep your eyes healthy. \n "
						" Created By: Nishanth Vijayan\n "
						" Please report bugs, contribute translations, \n  and make suggestions either through github or through e-mail.\n\n "
						" Github: <a href='https://github.com/nishanthvijayan/Take-A-Break'>https://github.com/nishanthvijayan/Take-A-Break</a>\n "
						" Email:  nishanththegr8@gmail.com\n "
						)
		Label.set_selectable(True)
		self.add(Label)


	def main(self):
		self.connect("delete-event", Gtk.main_quit)
		self.show_all()
		Gtk.main()
