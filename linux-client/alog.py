#! /usr/bin/env python
########################################################################
########################################################################


from Tkinter import BOTH, RIGHT, LEFT, StringVar, Text, TOP, Tk, X, Y
from ttk import Button, Combobox, Frame, Style


class ActivityLogger(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

        # Pop-up interval, in secods
        self.interval = 15 * 60

        # List of all tasks, sorted alphabetically
        self.tasks = []

        # Last-reported task
        self.last_task = ""
        return


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

        self.combo['values'] = ["Not much", "Bugger all", "SFA"]
        self.combo.pack(side=TOP, padx=5, pady=5, fill=X, expand=0)

        #self.entry = Text(self, bg="white", height="5")
        #self.entry.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=1)
        
        self.pack(fill=BOTH, expand=1)
        self.centre()

        self.cancel = Button(self, text="Cancel", command=self.do_cancel)
        self.cancel.pack(side=RIGHT, padx=5, pady=5)

        self.ok = Button(self, text="Ok", command=self.do_ok)
        self.ok.pack(side=RIGHT, padx=5, pady=5)

        self.journal = Button(self, text="Journal", command=self.do_journal)
        self.journal.pack(side=RIGHT, padx=5, pady=5)

    
    def combo_complete(self, partial):
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

        # Hide the window.
        self.parent.withdraw()

        # Schedule a reappearance.
        self.parent.after(2000, self.do_show)

        # Record the activity
        print "Did:", activity
        return


    def do_cancel(self):
        self.quit()
        return


    def do_show(self):
        self.parent.deiconify()
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
    
