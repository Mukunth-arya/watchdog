import watchdog.events
import watchdog.observers
import shutil
import os

class myfile(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.txt'], ignore_patterns= None, ignore_directories= False, case_sensitive= True )
    def keyvalue(self):
        main = "myfile"
        dir =  "/mnt/c/Users/mukunth/PycharmProjects/pythonProject/mypackage2"
        main2 = os.path.join(dir, main)
        mode = 0o666
        os.mkdir(main2, mode)
    def on_created(self, event):
        print(f"here comes the event {event.src_path}")
    def on_deleted(self, event):
        print(f"here comes the event deleted {event.src_path}")


datadriven = myfile()


server1 = watchdog.observers.Observer()
datadriven.keyvalue()
server1.schedule(datadriven,"/mnt/c/Users/mukunth/PycharmProjects/pythonProject/mypackage2", recursive= False)
server1.start()
server1.join()