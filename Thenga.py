from tkinter import*

def raise_frame(frame):
    frame.tkraise()
# creating a tkinter window.
root = Tk()
root.title = 'THENGA'
root.geometry('180x400')

# Creating different frames for the window.
Home = Frame(root)
Page1 = Frame(root)
Page2 = Frame(root)
Page3 = Frame(root)
Page4 = Frame(root)

for frame in (Home,Page1,Page2,Page3,Page4):
    frame.grid(row=0,column=0,sticky='news')
   
# creating labels and buttons for Home page.
Label(Home,text='').pack()
Label(Home,text='Enter UserID :').pack()
Entry(Home,text='').pack()
Label(Home,text='').pack()
Label(Home,text = 'Enter Password', pady = 2).pack()
Entry(Home,text='').pack()
Label(Home,text='').pack()
Button(Home, text = 'Enter', command = lambda:raise_frame(Page1)).pack()

# creating labels and buttons for  Page1.
Label(Page1,text='').pack()
Label(Page1,text='Are you a').pack()
Label(Page1,text='').pack()
Button(Page1, text = 'Buyer', command = lambda:raise_frame(Page2)).pack()
Label(Page1,text='').pack()
Label(Page1,text='Or').pack()
Label(Page1,text='').pack()
Button(Page1, text = 'Seller', command = lambda:raise_frame(Page2)).pack()
Label(Page1,text='').pack()
Button(Page1, text = 'Back', command = lambda:raise_frame(Home)).pack()

# creating labels and buttons for Page2.
Label(Page2,text='').pack()
Label(Page2,text='Enter Region:').pack()
Entry(Page2,text='').pack()
Label(Page2,text='').pack()
Button(Page2, text = 'Search', command = lambda:raise_frame(Page3)).pack()
Label(Page2,text='').pack()
Button(Page2, text = 'Back', command = lambda:raise_frame(Page1)).pack()


# creating labels and buttons for Home Page3. 
Label(Page3,text='').pack()
Label(Page3,text='What would you like to see?').pack()
Label(Page3,text='').pack()
Button(Page3, text = 'Fruit and Veg', command = lambda:raise_frame(Page4)).pack()
Label(Page3,text='').pack()
Button(Page3, text = 'Cooked Food', command = lambda:raise_frame(Page4)).pack()
Label(Page3,text='').pack()
Button(Page3, text = 'Snacks', command = lambda:raise_frame(Page4)).pack()
Label(Page3,text='').pack()
Button(Page3, text = 'Show all Foods', command = lambda:raise_frame(Page4)).pack()
Label(Page3,text='').pack()
Button(Page3, text = 'Back', command = lambda:raise_frame(Page2)).pack()

Label(Page4,text='').pack()
Button(Page4,text='Adams Apples').pack()
Label(Page4,text='''Fresh fruit and veggies 
at affordable prices''').pack()
Label(Page4,text='').pack()
Button(Page4,text=' Corner shop').pack()
Label(Page4,text='Get all your pantry essentials').pack()
Label(Page4,text='').pack()
Button(Page4,text='Mariahs Veggie Truck').pack()
Label(Page4,text='''All your fresh produce 
delivered to your door''').pack()
Label(Page4,text='').pack()
Button(Page4, text = 'Back', command = lambda:raise_frame(Page3)).pack()


raise_frame(Home)
root.mainloop()

    

    