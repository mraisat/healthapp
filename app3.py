from tkinter import *

root = Tk()
root.title('the health map app')
root.geometry("540x800")
root.configure(background="lightgrey")
root.resizable(False, False)

    
#adds the new smaller windows
def mondstadt():
    mondstad = Toplevel()
    mondstad.title("more info")
    tex1 = Label(mondstad, text = "mondstadt hospital", font=('Helvetica bold',15))
    tex1.pack(pady=20)
    tex = Label(mondstad, text = "Maecenas scelerisque velit sed", font=('Helvetica bold',11))
    tex.pack()
    tex = Label(mondstad, text = "aliquet velit. Duis felis erat", font=('Helvetica bold',11))
    tex.pack()
    tex = Label(mondstad, text = "et malesuada fames ac turpis", font=('Helvetica bold',11))
    tex.pack()
    tex = Label(mondstad, text = "Maecenas scelerisque velit sed", font=('Helvetica bold',11))
    tex.pack()
    mondstad.geometry("220x170")

def inazuma():
    inazum = Toplevel()
    inazum.title("more info")
    tex1 = Label(inazum, text = "inazuma hospital", font=('Helvetica bold',15))
    tex1.pack(pady=20)
    tex = Label(inazum, text = "Maecenas scelerisque velit sed", font=('Helvetica bold',11))
    tex.pack()
    tex = Label(inazum, text = "aliquet velit. Duis felis erat", font=('Helvetica bold',11))
    tex.pack()
    tex = Label(inazum, text = "et malesuada fames ac turpis", font=('Helvetica bold',11))
    tex.pack()
    tex = Label(inazum, text = "Maecenas scelerisque velit sed", font=('Helvetica bold',11))
    tex.pack()
    inazum.geometry("220x170")


def liyue():
    liyu = Toplevel()
    liyu.title("more info")
    tex1 = Label(liyu, text = "liyue hospital", font=('Helvetica bold',15))
    tex1.pack(pady=20)
    tex = Label(liyu, text = "Maecenas scelerisque velit sed", font=('Helvetica bold',11))
    tex.pack()
    tex = Label(liyu, text = "aliquet velit. Duis felis erat", font=('Helvetica bold',11))
    tex.pack()
    tex = Label(liyu, text = "et malesuada fames ac turpis", font=('Helvetica bold',11))
    tex.pack()
    tex = Label(liyu, text = "Maecenas scelerisque velit sed", font=('Helvetica bold',11))
    tex.pack()
    liyu.geometry("220x170")

def new_window1():
    nextwin1 = Toplevel()
    nextwin1.title("your results")
    tex3 = Label(nextwin1, text = "★★★☆☆", font=('Helvetica bold',20))
    tex3.pack(pady=23)
    tex1 = Label(nextwin1, text = "inazuma hospital", font=('Helvetica bold',15))
    tex1.pack()
    tex2 = Label(nextwin1, text = "best result for your searches", font=('Helvetica bold',11))
    tex2.pack()
    tex2 = Label(nextwin1, text = "specializing in stuff", font=('Helvetica bold',11))
    tex2.pack()
    tex2 = Label(nextwin1, text = "", font=('Helvetica bold',11))
    tex2.pack()
    nextwin1.geometry("200x220")
    buttonwin = Button(nextwin1, text="more info", command=inazuma)
    buttonwin.pack()

def new_window2():
    nextwin2 = Toplevel()
    tex3 = Label(nextwin2, text = "★★★☆☆", font=('Helvetica bold',20))
    tex3.pack(pady=23)
    tex1 = Label(nextwin2, text = "mondstadt hospital", font=('Helvetica bold',15))
    tex1.pack()
    tex2 = Label(nextwin2, text = "best result for your searches", font=('Helvetica bold',11))
    tex2.pack()
    tex2 = Label(nextwin2, text = "specializing in stuff", font=('Helvetica bold',11))
    tex2.pack()
    tex2 = Label(nextwin2, text = "", font=('Helvetica bold',11))
    tex2.pack()
    nextwin2.title("your results")
    nextwin2.geometry("200x220")
    buttonwin = Button(nextwin2, text="more info", command=mondstadt)
    buttonwin.pack()
    
def new_window3():
    nextwin3 = Toplevel()
    nextwin3.title("your results")
    tex3 = Label(nextwin3, text = "★★★☆☆", font=('Helvetica bold',20))
    tex3.pack(pady=23)
    tex1 = Label(nextwin3, text = "liyue hospital", font=('Helvetica bold',15))
    tex1.pack()
    tex2 = Label(nextwin3, text = "best result for your searches", font=('Helvetica bold',11))
    tex2.pack()
    tex2 = Label(nextwin3, text = "specializing in stuff", font=('Helvetica bold',11))
    tex2.pack()
    tex2 = Label(nextwin3, text = "", font=('Helvetica bold',11))
    tex2.pack()
    nextwin3.geometry("200x220")
    buttonwin = Button(nextwin3, text="more info", command=liyue)
    buttonwin.pack()

#the buttons disappear based on user selection
def make_invisible(x):
    if x == "shortness of breath":
        button1.destroy()
        button2.destroy()
    if x == "swelling or lumps in the body":
        button2.destroy()
        button3.destroy()
    if x == "muscle or body aches":
        button3.destroy()
        button1.destroy()   

label10 = Label(root, text = "the health map", font=('Helvetica bold',40), bg="lightgrey")
label10.pack(pady=20)

#drop down boxes
clicked = StringVar()
clicked.set("select your symptoms")


drop = OptionMenu(root, clicked, "shortness of breath","swelling or lumps in the body","muscle or body aches", command=make_invisible)
drop.pack(pady=10)
drop.configure(background="lightgrey")
   

#add image of the map
bg = PhotoImage(file = "green.jpg")

#canvas
canvas1 = Canvas( root, width = 700,
				height = 400)

canvas1.pack(fill = "both", expand = False)

#displays the image
canvas1.create_image( 0, 0, image = bg,
					anchor = "nw")

#text
canvas1.create_text( 200, 250, text = "")

#buttons
button1 = Button( root, text = "╬",command=new_window1)
button3 = Button( root, text = "╬",command=new_window2)
button2 = Button( root, text = "╬",command=new_window3)

#displays the buttons
button1_canvas = canvas1.create_window( 100, 90,
									anchor = "nw",
									window = button1)

button2_canvas = canvas1.create_window( 300, 280,
									anchor = "nw",
									window = button2)

button3_canvas = canvas1.create_window( 450, 145, anchor = "nw",
									window = button3)



#executes the app 
root.mainloop()

