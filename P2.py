import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk, Gdk
import threading
from P1 import Rfid

class NFCWindow(Gtk.Window):
	def __init__(self):
		super().__init__()
		
		#Box
		self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
		self.add(self.box)
		
		#evBox
		self.evbox = Gtk.EventBox()
		self.evbox.override_background_color(0, Gdk.RGBA(0,0,8,1))
		self.box.pack_start(self.evbox, True, True, 0)
		
		#Label
		self.label = Gtk.Label('<span foreground="white" size="x-large">Please, login with your university card</span>')
		self.label.set_use_markup(True)
		self.label.set_size_request(500,100)
		self.evbox.add(self.label)
		
		#Button
		self.button = Gtk.Button(label="Clear")
		self.button.connect("clicked", self.clicked) 
		self.box.pack_start(self.button, True, True, 0)
		
		self.ini_thread()

	#Press buton => reestart scan thread and change evBox and label
	def clicked(self, widget):
		self.label.set_label('<span foreground="white" size="x-large">Please, login with your university card</span>')
		self.evbox.override_background_color(0, Gdk.RGBA(0,0,8,1))
		self.ini_thread()
		
	#scan the NFC uid and changes the evBox and the label
	def scan_uid(self):
		reader = Rfid()
		uid = reader.read_uid()
		self.label.set_label('<span foreground="white" size="x-large">UID: '+uid+'</span>')
		self.evbox.override_background_color(0, Gdk.RGBA(8,0,0,1))
		
	#new scan thread with daemon = TRUE to end thread when the window is closed
	def ini_thread(self):
		thread = threading.Thread(target=self.scan_uid)
		thread.setDaemon(True)
		thread.start()

if __name__ == "__main__":
    win = NFCWindow()
    win.show_all()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
