from win10toast import ToastNotifier
import time
from format_milis import calculateMilis
import json

class Pomodoro(object):
    def __init__(self,break_time,little_break_time,study_time,max_iterations):
        self.toaster = ToastNotifier()
        self.title = 'Pomodoro'
        self.iterations = 0
        self.break_time = calculateMilis(break_time) // 1000
        self.little_break_time = calculateMilis(little_break_time) // 1000 
        self.study_time = calculateMilis(study_time) // 1000
        self.max_iterations = int(max_iterations)
    def run(self):
        while True:
            self.study()
            if bool(self.iterations % self.max_iterations):
                self.little_break()
            else:
                self.standard_break()
    def study(self):
        self.toaster.show_toast(self.title, "Comienza a estudiar :)", duration = 10, icon_path = "book.ico")
        time.sleep(self.study_time)
        self.iterations = self.iterations + 1
    def little_break(self):
        self.toaster.show_toast(self.title, "Es hora de relajarse un ratito", duration = 10, icon_path = "book.ico")
        time.sleep(self.little_break_time)
    def standard_break(self):
        self.toaster.show_toast(self.title, "Es hora de relajarse", duration = 10, icon_path = "book.ico")
        time.sleep(self.break_time)
        
with open("./config.json") as f :
    config = json.load(f)
    f.close() 

app = Pomodoro(**config)
app.run()


    
    
