from tkinter import *
import random
root=Tk()
root.title("Country Capital")
root.geometry("500x500")
Country_Input=Entry(root)
Capital_Input=Entry(root)
countrylistlabel=Label(root)
capitallistlabel=Label(root)
country_random=Label(root)
capital_random=Label(root)
countrylist=[]
capitallist=[]
def add():
    countrylist.append(Country_Input.get())
    capitallist.append(Capital_Input.get())
    countrylistlabel["text"]="Country Name :"+str(countrylist)
    capitallistlabel["text"]="City Name :"+str(capitallist)
    capitallistlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
    countrylistlabel.place(relx=0.5,rely=0.4,anchor=CENTER)
    btndisplayrand=Button(root,text="Display Country And City Name Randomly",bg="#4567e6",fg="white",command=rand)
    btndisplayrand.place(relx=0.5,rely=0.6,anchor=CENTER)
def rand():
    random_1=random.randint(0, len(countrylist)-1)
    random_2=random.randint(0, len(countrylist)-1)
    country_random["text"]="Random Country : "+countrylist[random_1]
    capital_random["text"]="Random City : "+capitallist[random_2]
    country_random.place(relx=0.5,rely=0.7,anchor=CENTER)
    capital_random.place(relx=0.5,rely=0.8,anchor=CENTER)
btn_display=Button(root,text="Display Country And City Name",bg="#4567e6",fg="white",command=add)
btn_display.place(relx=0.5,rely=0.3,anchor=CENTER)
Country_Input.place(relx=0.5,rely=0.1,anchor=CENTER)
Capital_Input.place(relx=0.5,rely=0.2,anchor=CENTER)
root.mainloop()