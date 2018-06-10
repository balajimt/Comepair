__author__ = 'Balaji'
from tkinter import *
import tkinter.font
from PIL import Image, ImageTk
from new import *
import urllib.request
import webbrowser
import os
import os.path

list_new = ['Product title','Product Price','Product Rating','Product Seller','Seller Rating']
list_new1 = ['Product title','Product Price','Product Rating','Product Seller','Seller Rating','Comments']

class MyApp:
    def __init__(self,parent):

        self.myparent = parent
        self.logo1 = ImageTk.PhotoImage(Image.open("amazon.png"))
        self.logo2 = ImageTk.PhotoImage(Image.open("flipkart.png"))
        self.buynow = ImageTk.PhotoImage(Image.open("buy_now.png"))

        self.customfont = tkinter.font.Font(family="Gadugi", size=11)

        self.textbox = Label(self.myparent, image=self.logo1)
        self.textbox.grid(row = 0, column = 0)

        self.textbox1 = Label(self.myparent, image=self.logo1)
        self.textbox1.grid(row = 1, column = 0)
        self.textbox2 = Label(self.myparent, image=self.logo2)
        self.textbox2.grid(row = 1, column =1)
        self.mycontainer = Frame(self.myparent)
        self.mycontainer.grid(row = 2,column =0)

        for i in list_new:
            self.textbox3 = Label(self.mycontainer, text = i, font = self.customfont)
            self.textbox3.pack(side = TOP)
        self.mycontainer2 = Frame(self.myparent)
        self.mycontainer2.grid(row = 2,column =1)

        for i in list_new1:
            self.textbox4 = Label(self.mycontainer2, text = i, font = self.customfont,bg='#77FF85')
            self.textbox4.pack(side = TOP)

        self.textbox5 = Label(self.myparent, image=self.buynow)
        self.textbox5.grid(row = 3, column = 0)
        self.textbox6 = Label(self.myparent, image=self.buynow)
        self.textbox6.grid(row = 3, column = 1)










root = Tk()
# root.geometry('{}x{}'.format(1000,400)) #Setting default window size,not expnadable
myapp = MyApp(root)
root.mainloop()