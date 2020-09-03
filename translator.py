from tkinter import *
from translate import Translator

class Trans:
    def __init__(self, mainframe, *args, **kwargs):
        self.mainframe = mainframe

        self.lang1 = StringVar(root)
        self.lang2 = StringVar(root)

        self.CHOICES = {'English', 'Hindi', 'Spanish', 'German', 'Russian', 'Korean', 'Gujarati'}
        self.lang1.set('English')
        self.lang2.set('Select to translate into ')

        self.Choices1 = {'English'}
        self.lang1menu = OptionMenu(mainframe, self.lang1, *self.Choices1)
        Label(mainframe, text='Select a Language').grid(row=0, column=1)
        self.lang1menu.grid(row=1, column=1)

        self.lang2menu = OptionMenu(mainframe, self.lang2, *self.CHOICES)
        Label(mainframe, text='Select a Language').grid(row=0, column=0)
        self.lang2menu.grid(row=1, column=2)

        Label(mainframe, text='Enter text').grid(row=2, column=0)
        self.var = StringVar()
        self.textbox = Entry(mainframe, textvariable=self.var).grid(row=2, column=1)

        Label(mainframe, text='Output').grid(row=2, column=2)
        self.var1 = StringVar()
        # textbox2 = Entry(mainframe, textvariable=self.var1).grid(row=2, column=3)

        self.b = Button(mainframe, text='Translate', command=self.translate).grid(row=3, column=1, columnspan=3)
        # self.c = Button(mainframe, text='Clear', command=self.clear).grid(row=3, column=0, columnspan=3)

    def translate(self):
        self.translator = Translator(from_lang=self.lang1.get(), to_lang=self.lang2.get())
        self.translation = self.translator.translate(self.var.get())
        self.var.set(self.translation)

    # def clear(self):
    #     self.textbox.delete(0, 'END')

root = Tk()
root.title("TRANSLATOR")
yo=Trans(root)
print(yo)
mainframe = Frame(root)
# mainframe.geometry('400x200')
# image1= Tk.PhotoImage(file="C:\\Users\\ayush\\Desktop\\a.png")
# label_for_image= Label(mainframe, image=image1)
# label_for_image.pack()
mainframe.grid(column=0,row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=2)
mainframe.rowconfigure(0,weight=1)
# mainframe.pack(pady=100,padx=100)

root.mainloop()



