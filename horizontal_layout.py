__author__ = 'Balaji'

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
        self.frame1 = Frame(parent)
        self.frame1.pack()

        #Font description
        self.customfont = tkinter.font.Font(family="Gadugi", size=15)
        self.customfont2 = tkinter.font.Font(family="Gadugi", size=12)
        self.customfont3 = tkinter.font.Font(family="Gadugi", size=20)
        self.customfontprice = tkinter.font.Font(family="Gadugi", size=12,weight ='bold')
        self.creatorfont = tkinter.font.Font(family="barcode font", size=74)

        self.button3 = Button(self.frame1)
        self.image3 = PhotoImage(file='3.gif')
        self.button3.configure(image=self.image3, bd=0)
        self.button3.pack(side=LEFT, expand=YES)
        self.button3.bind("<Button-1>", self.button3Click)
        self.button3.bind("<Return>", self.button3Click)

        #Textbox
        self.textbox = Entry(self.frame1)
        self.textbox.configure(text=product, cursor='xterm', bd=1, fg='#404040', bg='white', font=self.customfont)
        self.textbox.pack(side= LEFT,expand=YES)
        self.textbox.focus_force()
        self.textbox.bind("<Return>", self.button1Click)

        #Search Icon
        self.button1 = Button(self.frame1)
        self.image1 = PhotoImage(file='1.gif')
        self.button1.configure(image=self.image1, bd=0)
        self.button1.pack(side=LEFT, expand=YES)
        self.button1.bind("<Button-1>", self.button1Click)
        self.button1.bind("<Return>", self.button1Click)

        #ClearIcon
        self.button2 = Button(self.frame1)
        self.image2 = PhotoImage(file='2.gif')
        self.button2.configure(image=self.image2, bd=0)
        self.button2.pack(side=LEFT, expand=YES)
        self.button2.bind("<Button-1>", self.button2Click)
        self.button2.bind("<Return>", self.button2Click)



        #Frame with all comparison details
        self.frame2 = Frame(parent)
        self.frame2.configure(bg = 'white')
        self.frame2.pack()

        self.container1 = Frame(self.frame2)
        self.container1.pack(side = LEFT)

        #Empty frame
        self.container2 = Frame(self.frame2)
        self.container2.pack(side = LEFT)

    def button1Click(self, event):
        self.container1.pack_forget()
        self.container2.pack_forget()

        #Buy Button numbers
        row_number1 =2
        row_number2= 2
        row_number3 =2

        try:
            self.creator.destroy()
        except:
            pass

        del url_product[:]
        del url_flip_product[:]
        del url_amazon_product [:]
        del url_snap_product [:]
        del new_flip_list[:]
        del new_amazon_list[:]
        del new_snap_list[:]

        if os.path.isfile('100.jpeg')== True:
            os.remove('100.jpeg')

        if os.path.isfile('101.jpeg')==True:
            os.remove('101.jpeg')

        if os.path.isfile('102.jpeg')==True:
            os.remove('102.jpeg')

        print(self.textbox.get())
        print(type(self.textbox.get()))
        self.n = self.textbox.get().lstrip(' ')
        print('Input taken: '+self.n)

        flipkart(self.n)
        amazon(self.n)
        snapdeal(self.n)

        self.container1 = Frame(self.frame2)
        self.container1.pack(side = TOP)

        self.container2 = Frame(self.frame2)
        self.container2.pack(side = TOP)

        #Flipkart
        try:
            self.flipkart_pic = ImageTk.PhotoImage(Image.open("100.jpeg"))
            self.flip_pic_height = 200
            self.flip_pic_width = int(self.flipkart_pic.width()/self.flipkart_pic.height()*200)
            if self.flip_pic_width > 300:
                self.flip_pic_width = 300
                self.flip_pic_height = int(self.flipkart_pic.height()/self.flipkart_pic.width()*300)
            print(self.flip_pic_width)
        except:
            pass

        if os.path.isfile('100.jpeg') == True:
            self.flipkart_pic = ImageTk.PhotoImage(Image.open("100.jpeg").resize((self.flip_pic_width,self.flip_pic_height)))
        else:
            self.flipkart_pic = ImageTk.PhotoImage(Image.open("error.png"))

        try:
            if new_flip_list[0] not in ('No product found','Internet connection aborted','Enter a valid product'):
                self.textbox1 = Label(self.container1, image=self.flipkart_pic)
                print('it comes here')
                self.textbox1.grid(row=0,column=0)

            try:
                new_flip_list.remove('\n')
            except:
                pass

            try:
                new_flip_list.remove('')
            except:
                pass


            self.flipkart_logo = ImageTk.PhotoImage(Image.open("flipkart.png"))
            self.textbox2 = Label(self.container1, image=self.flipkart_logo)
            self.textbox2.grid(row=1,column=0)

            row_number1 = 2

            for i in range(len(new_flip_list)):
                self.textbox3 = Message(self.container1)
                if(i!=1):
                    self.textbox3.configure(text=new_flip_list[i], font=self.customfont2,width = 250)
                else:
                    self.textbox3.configure(text=new_flip_list[i], font=self.customfontprice,width = 250)
                self.textbox3.grid(row = row_number1, column = 0)
                row_number1 = row_number1 + 1
        except:
            pass

        #Amazon
        try:
            self.amazon_trial = ImageTk.PhotoImage(Image.open("101.jpeg"))
            self.amazon_pic_height = 200
            self.amazon_pic_width = int(self.amazon_trial.width()/self.amazon_trial.height()*200)
            if self.amazon_pic_width > 300:
                self.amazon_pic_width = 300
                self.amazon_pic_height = int(self.amazon_pic.height()/self.amazon_pic.width()*300)
        except:
            pass


        if os.path.isfile('101.jpeg')==True:
            self.amazon_pic = ImageTk.PhotoImage(Image.open("101.jpeg").resize((self.amazon_pic_width,self.amazon_pic_height)))
        else:
            self.amazon_pic = ImageTk.PhotoImage(Image.open("error.png"))

        try:
            if new_amazon_list[0] not in ('No product found','Internet connection aborted','Enter a valid product'):
                self.textbox4 = Label(self.container1, image=self.amazon_pic)
                self.textbox4.grid(row =0,column =1)

            self.amazon_logo = ImageTk.PhotoImage(Image.open("amazon.png"))
            self.textbox5 = Label(self.container1, image=self.amazon_logo)
            self.textbox5.grid(row=1,column=1)

            row_number2 = 2

            for i in range(len(new_amazon_list)):
                self.textbox6 = Message(self.container1)
                if(i!=1):
                    self.textbox6.configure(text=new_amazon_list[i], font=self.customfont2,width = 250)
                else:
                    self.textbox6.configure(text=new_amazon_list[i], font=self.customfontprice,width = 250)
                self.textbox6.grid(row = row_number2,column = 1)
                row_number2=row_number2+1
        except:
            pass

        #SnapDeal
        try:
            self.snap_trial = ImageTk.PhotoImage(Image.open("102.jpeg"))
            self.snap_pic_height = 200
            self.snap_pic_width = int(self.snap_trial.width()/self.snap_trial.height()*200)
            if self.snap_pic_width > 300:
                self.snap_pic_width = 300
                self.snap_pic_height = int(self.snap_pic.height()/self.snap_pic.width()*300)
        except:
            pass

        if os.path.isfile('102.jpeg') == True:
            self.snap_pic = ImageTk.PhotoImage(Image.open("102.jpeg").resize((self.snap_pic_width,self.snap_pic_height)))
        else:
            self.snap_pic = ImageTk.PhotoImage(Image.open("error.png"))


        try:
            if new_snap_list[0] not in ('No product found','Internet connection aborted','Enter a valid product'):
                self.textbox1 = Label(self.container1, image=self.snap_pic)
                self.textbox1.grid(row=0,column=2)

            try:
                new_snap_list.remove('\n')
            except:
                pass

            try:
                new_snap_list.remove('')
            except:
                pass

            self.snap_logo = ImageTk.PhotoImage(Image.open("snapdeal.png"))
            self.textbox6 = Label(self.container1, image=self.snap_logo)
            self.textbox6.grid(row=1,column=2)

            row_number3 = 2

            for i in range(len(new_snap_list)):
                self.textbox7 = Message(self.container1)
                if(i!=1):
                    self.textbox7.configure(text=new_snap_list[i], font=self.customfont2,width = 250)
                else:
                    self.textbox7.configure(text=new_snap_list[i], font=self.customfontprice,width = 250)
                self.textbox7.grid(row = row_number3, column = 2)
                row_number3 = row_number3 + 1
        except:
            pass

        #Buy Now Buttons

        self.buy_now = ImageTk.PhotoImage(Image.open("buy_now.png"))

        try:
            if new_flip_list[0] not in ('No product found','Internet connection aborted','Enter a valid product'):
                self.buy_button = Button(self.container1, image=self.buy_now, bd=1)
                self.buy_button.grid(row = max(row_number2,row_number1,row_number3),column=0)
                self.buy_button.bind("<Button-1>", self.buy_now_click1)
        except:
            pass

        try:
            if new_amazon_list[0] not in ('No product found','Internet connection aborted','Enter a valid product'):
                self.buy_button2 = Button(self.container1, image=self.buy_now, bd=1)
                self.buy_button2.grid(row = max(row_number2,row_number1,row_number3),column =1)
                self.buy_button2.bind("<Button-1>", self.buy_now_click2)
        except:
            pass

        try:
            if new_snap_list[0] not in ('No product found','Internet connection aborted','Enter a valid product'):
                self.buy_button3 = Button(self.container1, image=self.buy_now, bd=1)
                self.buy_button3.grid(row = max(row_number1,row_number2,row_number3),column=2)
                self.buy_button3.bind("<Button-1>", self.buy_now_click3)
        except:
            pass

        del new_flip_list[:]
        del new_amazon_list[:]
        del new_snap_list[:]


    def button2Click(self, event):
        try:
            self.container2.destroy()
        except:
            pass
        self.container1.destroy()

    def button3Click(self, event):
        self.container1.pack_forget()
        self.container2.pack_forget()
        self.container2 = Frame(self.frame2)
        self.container2.pack(side=TOP)

        self.creator1 = Label(self.container2)
        self.creator1.configure(text='',font=self.customfont3)
        self.creator1.pack(side = TOP)

        self.creator1 = Label(self.container2)
        self.creator1.configure(text='PRODUCT COMPARISON TOOL',font=self.customfontprice)
        self.creator1.pack(side = TOP)

        self.creator1 = Label(self.container2)
        self.creator1.configure(text='',font=self.customfont3)
        self.creator1.pack(side = TOP)

        self.creator2 = Label(self.container2)
        self.creator2.configure(text='Supported Sites',font=self.customfont2)
        self.creator2.pack(side = TOP)

        self.miniframe = Frame(self.container2)
        self.miniframe.pack(side=TOP)

        self.snap_logo = ImageTk.PhotoImage(Image.open("snapdeal.png"))
        self.flipkart_logo = ImageTk.PhotoImage(Image.open("flipkart.png"))
        self.amazon_logo = ImageTk.PhotoImage(Image.open("amazon.png"))


        self.image_list = [self.flipkart_logo,self.amazon_logo,self.snap_logo]
        for i in self.image_list:
            self.image_label = Label(self.miniframe)
            self.image_label.configure(image = i)
            self.image_label.pack(side = LEFT)

        self.creator1 = Label(self.container2)
        self.creator1.configure(text='',font=self.customfont3)
        self.creator1.pack(side = TOP)

        self.creator = Label(self.container2)
        self.creator.configure(text='Built by Balaji Muthazhagan T',font=self.creatorfont,cursor='plus')
        self.creator.pack(side = TOP)

    def buy_now_click1(self, event):
        webbrowser.open(url_flip_product[0])

    def buy_now_click2(self, event):
        webbrowser.open(url_amazon_product[0])

    def buy_now_click3(self, event):
        webbrowser.open(url_snap_product[0])




def report_event(event):
    """Print a description of an event, based on its attributes."""

    event_name = {"2": "KeyPress", "4": "ButtonPress"}
    print("Time:", str(event.time))  ### (6)
    print("EventType=" + str(event.type), \
          event_name[str(event.type)], \
          "EventWidgetId=" + str(event.widget), \
          "EventKeySymbol=" + str(event.keysym))

root = Tk()
root.configure(bg = 'white')
root.wm_title("Product Comparison Tool")
myapp = MyApp(root)
root.mainloop()