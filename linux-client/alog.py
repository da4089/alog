#! /usr/bin/env python
########################################################################
########################################################################

import time
from Tkinter import BOTH, RIGHT, LEFT, StringVar, Text, TOP, Tk, X, Y
from ttk import Button, Combobox, Frame, Style


class ActivityLogger(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

        # Pop-up interval, in minutes.
        self.interval = 2

        # List of all tasks, sorted alphabetically.
        self.tasks = []

        # Last-reported task.
        self.last_task = ""

        # Change flag.
        self.changed = False
        return


    def get_next_time(self):
        
        now = time.time()
        bits = time.localtime(now)

        m = (bits.tm_hour * 60) + bits.tm_min
        used = m % self.interval
        start = (m / self.interval) * self.interval
        next = start + self.interval

        t = time.mktime((bits.tm_year, bits.tm_mon, bits.tm_mday,
                         next / 60, next % 60, 0,
                         0, 0, 0))
        s = t - now

        print "Time now is %u:%02u:%02u" % (bits.tm_hour, bits.tm_min, bits.tm_sec)
        print "Interval started at %u:%02u:00" % (start / 60, start % 60)
        print "Next interval starts at %u:%02u:00" % (next / 60, next % 60)
        print "Sleeping for %f seconds" % s

        return s


    def init_ui(self):
        self.parent.title("Activity Logger")
        self.parent.focusmodel("active")
        
        self.style = Style()
        self.style.theme_use("aqua")

        self.combo_text = StringVar()
        cb = self.register(self.combo_complete)
        self.combo = Combobox(self,
                              textvariable=self.combo_text,
                              validate="all",
                              validatecommand=(cb, '%P'))

        self.combo['values'] = ["Food", "Email", "Web"]
        self.combo.pack(side=TOP, padx=5, pady=5, fill=X, expand=0)

        #self.entry = Text(self, bg="white", height="5")
        #self.entry.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=1)
        
        self.pack(fill=BOTH, expand=1)
        self.centre()

        self.ok = Button(self, text="Ok", command=self.do_ok)
        self.ok.pack(side=RIGHT, padx=5, pady=5)

        self.journal = Button(self, text="Journal", command=self.do_journal)
        self.journal.pack(side=RIGHT, padx=5, pady=5)

        self.exit = Button(self, text="Exit", command=self.do_exit)
        self.exit.pack(side=RIGHT, padx=5, pady=5)


    
    def combo_complete(self, partial):
        # Flag field touched.
        self.changed = True

        # Do completion on combobox text
        #print self.combo_text.get()
        if partial:
            print partial
        return True


    def do_journal(self):
        print "journal not yet implemented, sorry"
        return


    def do_ok(self):

        # Get entered activity name.
        activity = self.combo_text.get()

        # Get current list of known activity names.
        activities = list(self.combo['values'])
        
        # Prepend the latest activity if it wasn't already known.
        if activity not in activities:
            activities.insert(0, activity)
            self.combo['values'] = activities

        # Save this activity.
        self.last_task = activity

        # Hide the window.
        self.parent.withdraw()

        # Get remaining time in interval.
        s = self.get_next_time()

        # Schedule a reappearance.
        self.parent.after(int(s * 1000), self.do_show)

        # Record the activity
        print "Did:", activity
        return


    def do_exit(self):
        self.quit()
        return


    def do_show(self):

        # Reset change flag.
        self.changed = False

        # Restore last activity.
        self.combo_text.set(self.last_task)

        # Show window.
        self.parent.deiconify()

        # Pop-down after a minute if not touched.
        self.parent.after(1000 * 60, self.do_timeout)
        return


    def do_timeout(self):
        if self.changed:
            return
        
        # Hide the window.
        self.parent.withdraw()

        # Get remaining time in interval.
        s = self.get_next_time()

        # Schedule a reappearance.
        self.parent.after(int(s * 1000), self.do_show)
        return

        
    def centre(self):
        w = 400
        h = 75

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry("%ux%u+%u+%u" % (w, h, x, y))


def main():
    root = Tk()
    app = ActivityLogger(root)
    root.mainloop()



if __name__ == "__main__":
    main()
    
