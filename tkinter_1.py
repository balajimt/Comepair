from tkinter import *
import tkinter.font
from PIL import Image, ImageTk
from new import *
import urllib.request
import webbrowser
import os
import os.path

product = 'balaji'


class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Canvas(parent)
        # self.myContainer1 = Frame(parent,height = 32,width = 1000)
        # self.myContainer1.pack_propagate(0) #Dont Shrink
        self.myContainer1.pack()


        self.customfont = tkinter.font.Font(family="Gadugi", size=15)
        self.customfont2 = tkinter.font.Font(family="Gadugi", size=12)
        self.customfont3 = tkinter.font.Font(family="Gadugi", size=20)
        self.customfontprice = tkinter.font.Font(family="Gadugi", size=12,weight ='bold')

        self.textbox = Entry(self.myContainer1)
        self.textbox.configure(text=product, cursor='xterm', bd=1, fg='#404040', bg='white', font=self.customfont)
        self.textbox.pack(side=LEFT, expand=YES)

        self.myContainer2 = Frame(parent)
        # self.myContainer1 = Frame(parent,height = 32,width = 1000)
        # self.myContainer1.pack_propagate(0) #Dont Shrink
        self.myContainer2.pack()

        #self.scroll_bar = Scrollbar(self.myContainer2)
        #self.scroll_bar.pack(side=RIGHT, fill=Y)
        #self.scroll_bar.config(command=self.myContainer2.yview)

        self.button1 = Button(self.myContainer1)
        self.image1 = PhotoImage(file='1.gif')
        self.button1.configure(image=self.image1, bd=0)
        self.button1.pack(side=LEFT, expand=YES)
        self.button1.focus_force()
        self.button1.bind("<Button-1>", self.button1Click)
        self.button1.bind("<Return>", self.button1Click)

        self.button2 = Button(self.myContainer1)
        self.image2 = PhotoImage(file='2.gif')
        self.button2.configure(image=self.image2, bd=0)
        self.button2.pack(side=LEFT, expand=YES)
        self.button2.bind("<Button-1>", self.button2Click)
        self.button2.bind("<Return>", self.button2Click)

        self.myContainer3 = Frame(self.myContainer2)
        self.myContainer4 = Frame(self.myContainer2)

    def button1Click(self, event):
        del url_product[:]
        del new_flip_list[:]
        del new_amazon_list[:]

        if os.path.isfile('100.jpeg')== True:
            os.remove('100.jpeg')

        if os.path.isfile('101.jpeg')==True:
            os.remove('101.jpeg')

        self.myContainer3.pack_forget()
        self.myContainer4.pack_forget()

        self.myContainer3 = Frame(self.myContainer2)
        self.myContainer4 = Frame(self.myContainer2)

        report_event(event)
        print(self.textbox.get())

        flipkart(self.textbox.get())
        amazon(self.textbox.get())

        self.myContainer3 = Frame(self.myContainer2)
        self.myContainer3.pack()

        self.myContainer4 = Frame(self.myContainer2)
        self.myContainer4.pack()

        self.space1 = Label(self.myContainer3)
        self.space1.configure(text='  ', font=self.customfont2)
        self.space1.pack(side=TOP)

        if os.path.isfile('100.jpeg')==True:
            self.logo = ImageTk.PhotoImage(Image.open("100.jpeg"))
        else:
            self.logo = ImageTk.PhotoImage(Image.open("100.jpeg"))

        if self.logo.width() < 300:
            self.logo_height = 250
            self.logo_width = int(self.logo.width()/self.logo.height()*250)
        else:
            self.logo_width = 300
            self.logo_height = int(self.logo.height()/self.logo.width()*300)


        if os.path.isfile('100.jpeg') == True:
            self.logo5 = ImageTk.PhotoImage(Image.open("100.jpeg").resize((self.logo_width,self.logo_height)))
        else:
            self.logo5 = ImageTk.PhotoImage(Image.open("error.png").resize((self.logo_width,self.logo_height)))
        self.textbox3 = Label(self.myContainer3, image=self.logo5)
        self.textbox3.pack(side=LEFT)

        try:
            new_flip_list.remove('\n')
        except:
            pass

        self.logo_new = ImageTk.PhotoImage(Image.open("flipkart.png"))
        self.textbox3 = Label(self.myContainer3, image=self.logo_new)
        self.textbox3.pack(side=TOP)

        self.space2 = Label(self.myContainer3)
        self.space2.configure(text='  ', font=self.customfont2)
        self.space2.pack(side=TOP)

        for i in range(len(new_flip_list)):
            self.textbox2 = Message(self.myContainer3)
            if(i!=1):
                self.textbox2.configure(text=new_flip_list[i], font=self.customfont2,width = 250)
            else:
                self.textbox2.configure(text=new_flip_list[i], font=self.customfontprice,width = 250)
            self.textbox2.pack(side=TOP)


        self.space3 = Label(self.myContainer3)
        self.space3.configure(text='  ', font=self.customfont3)
        self.space3.pack(side=TOP)

        self.buy_now = ImageTk.PhotoImage(Image.open("buy_now.png"))
        self.buy_button = Button(self.myContainer3, image=self.buy_now, bd=1)
        self.buy_button.pack(side=TOP)
        self.buy_button.bind("<Button-1>", self.buy_now_click1)
        #image_pil = Image.open(img_name).resize((300, 300))
        if os.path.isfile('101.jpeg')== True:
            self.logo_new3 = ImageTk.PhotoImage(Image.open("101.jpeg"))
        else:
            self.logo_new3 = ImageTk.PhotoImage(Image.open("error.png"))

        self.logo_new3_width = self.logo_width
        self.logo_new3_height = int(self.logo_new3.height()/self.logo_new3.width()*self.logo_new3_width)

        if os.path.isfile('101.jpeg')==True:
            self.logo_new4 = ImageTk.PhotoImage(Image.open("101.jpeg").resize((self.logo_new3_width,self.logo_new3_height)))
        else:
            self.logo_new4 = ImageTk.PhotoImage(Image.open("error.png").resize((self.logo_new3_width,self.logo_new3_height)))

        self.textbox3 = Label(self.myContainer4, image=self.logo_new4)
        self.textbox3.pack(side=LEFT)

        self.logo_new2 = ImageTk.PhotoImage(Image.open("amazon.png"))
        self.textbox3 = Label(self.myContainer4, image=self.logo_new2)
        self.textbox3.pack(side=TOP)

        self.space2 = Label(self.myContainer3)
        self.space2.configure(text='  ', font=self.customfont2)
        self.space2.pack(side=TOP)

        for i in range(len(new_amazon_list)):
            self.textbox2 = Message(self.myContainer4)
            if(i!=1):
                self.textbox2.configure(text=new_amazon_list[i], font=self.customfont2,width = 250)
            else:
                self.textbox2.configure(text=new_amazon_list[i], font=self.customfontprice,width = 250)
            self.textbox2.pack(side=TOP)

        self.space4 = Label(self.myContainer4)
        self.space4.configure(text='  ', font=self.customfont3)
        self.space4.pack(side=TOP)

        self.buy_button2 = Button(self.myContainer4, image=self.buy_now, bd=1)
        self.buy_button2.pack(side=TOP)
        self.buy_button2.bind("<Button-1>", self.buy_now_click2)

        del new_flip_list[:]
        del new_amazon_list[:]

    def button2Click(self, event):
        self.myContainer3.destroy()
        self.myContainer4.destroy()

    def buy_now_click1(self, event):
        webbrowser.open(url_product[0])

    def buy_now_click2(self, event):
        webbrowser.open(url_product[1])
        pass

def report_event(event):
    """Print a description of an event, based on its attributes."""

    event_name = {"2": "KeyPress", "4": "ButtonPress"}
    print("Time:", str(event.time))  ### (6)
    print("EventType=" + str(event.type), \
          event_name[str(event.type)], \
          "EventWidgetId=" + str(event.widget), \
          "EventKeySymbol=" + str(event.keysym))


root = Tk()
# root.geometry('{}x{}'.format(1000,400)) #Setting default window size,not expnadable
myapp = MyApp(root)
root.mainloop()