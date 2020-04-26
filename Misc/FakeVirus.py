# Do not worry! This isn't a real Virus, just a program that makes a picture of a red pepper show up!
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        load = Image.open(indrafolder/"Images/chili.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


root = Tk()
app = Window(root)
root.wm_title("Chili Virus")
root.geometry("1000x800")
root.mainloop()
