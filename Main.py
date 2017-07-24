import tkMessageBox
from Tkinter import *
from ttk import Style

from Solution import Solution


class window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.initUI()

    def initUI(self):
        self.radiusEntryText = StringVar()
        self.lengthEntryText = StringVar()
        self.master.resizable(width="false", height="false")
        self.master.title("CHEERS")

        self.master.minsize(width=480, height=600)
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        descButton = Button(self, text="Description")
        descButton.bind("<Button-1>", self.showdescription)
        descButton.place(x=40, y=40)
        radiusLabel = Label(self, text="Enter Radius:")
        radiusLabel.place(x=0, y=200)
        radiusEntry = Entry(self, textvariable=self.radiusEntryText)
        radiusEntry.config(width=60)
        radiusEntry.place(x=110, y=200)
        lengthLabel = Label(self, text="Calculated Length")
        lengthLabel.place(x=0, y=300)
        self.lengthEntry = Entry(self, width=60)
        self.lengthEntry.place(x=110, y=300)
        self.lengthEntry.config(state='readonly')
        calculateButton = Button(self, text="Calculate")
        calculateButton.bind("<Button-1>", self.performCalculations)
        calculateButton.place(x=100, y=400)

    def performCalculations(self, event):
        try:
            if (self.radiusEntryText.get() == ""):
                tkMessageBox.showwarning("Invalid Output", "The radius field can't be empty")
            else:
                length = Solution.getLenght(float(self.radiusEntryText.get()))
                self.lengthEntry.config(state='normal')
                self.lengthEntry.delete(0, END)
                self.lengthEntry.insert(0, length)
                self.lengthEntry.config(state='readonly')
        except BaseException as e:
            tkMessageBox.showwarning("Error", e.message)

    def showdescription(self, event):
        tkMessageBox.showinfo("Description",
                              "Suppose there are two circular beverage coasters of equal area.The purpose is to find how far the two coasters need to be moved on top of each other,such that the area of the overlapping region is half the area of any of the coasters.The input should be the radius of the circles and the output would be the distance at which coasters must be placed in order to meet the condition.\n\nImage ref. -\nhttp://users.encs.concordia.ca/~kamthan/courses/soen-6441/project_description.pdf")


def main():
    root = Tk()
    root.geometry("600x480+300+300")
    app = window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
