import watchdog.events
import watchdog.observers
import shutil
import os

class datafile(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self,patterns = ["*txt","*jpg","*png"], ignore_patterns= None,ignore_directories=False,case_sensitive=True)

    #def value(self,key,value):
        #data1 = key
        #data2 = value
        #data3 = os.path.join(data2, data1)
        #mode = 0o666
        #os.mkdir(data3,mode)
    def on_created(self, event):
        print(f"hey there someting is creatwd here{event.src_path}")
        if event.src_path.endswith(".txt"):
            shutil.move(event.src_path,r"C:\Users\mukunth\Desktop\myfile" )
        elif event.src_path.endswith(".jpg"):
            shutil.move(event.src_path, r"C:\Users\mukunth\Desktop\myfile")
        else:
            print("he there file is created")
    def on_deleted(self, event):
        print(f"hey something is swapped out {event.src_path}")

datafile = datafile()
server1 = watchdog.observers.Observer()
#datafile.value("myfile",r"C:\Users\mukunth\Desktop\New folder")

server1.schedule(datafile,r"C:\Users\mukunth\Desktop\New folder\\myfille", recursive=True )
server1.start()
server1.join()