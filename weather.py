from tkinter import*
from tkinter import ttk

import requests






def data_get():
 city= city_name.get()
 data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=").json()

 w_lable1.config(text=data["weather"][0]["main"])
 wb_lable1.config(text=data["weather"][0]["description"])

 t_lable1.config(text=str(data["main"]["temp"]-273.15))
 p_lable1.config(text=data["main"]["pressure"])






win = Tk()
win.title("web ")

win.config(bg = "blue")
win.geometry("500x500")

name_lable = Label(win,text="Wheather app",
             font =("Time New Roman",40,"bold"))


name_lable.place(x=25,y=50,height=50, width = 450)


com = ttk.Combobox(win,text="Weather app",
                   font=("Time New Roman",30,"bold"))

city_name =  StringVar()
list_name= ( "Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru", "Hyderabad",
    "Pune", "Ahmedabad", "Jaipur", "Surat", "Lucknow", "Kanpur",
    "Nagpur", "Indore", "Bhopal", "Patna", "Ranchi", "Guwahati",
    "Chandigarh", "Amritsar", "Shimla", "Dehradun", "Agra", "Varanasi",
    "Coimbatore", "Kochi", "Thiruvananthapuram", "Mysuru", "Visakhapatnam",
    "Goa", "Noida", "Gurgaon", "Vadodara", "Rajkot", "Jodhpur", "Raipur",
    "Vijayawada", "Madurai", "Tiruchirappalli", "Udaipur", "Bhavnagar"
)
com = ttk.Combobox(win,text="Wheater app",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)
                         


w_lable = Label(win,text="Wheather Climate",
             font =("Time New Roman",17,))


w_lable.place(x=25,y=260,height=50, width = 210)

w_lable1 = Label(win,text="",
             font =("Time New Roman",20,))


w_lable1.place(x=280,y=260,height=50, width = 210)







wb_lable = Label(win,text="Wheather discription",
             font =("Time New Roman",17,))



wb_lable.place(x=25,y=330,height=50, width = 210)


wb_lable1 = Label(win,text="",
             font =("Time New Roman",17,))



wb_lable1.place(x=280,y=330,height=50, width = 210)






t_lable = Label(win,text="Temperature",
             font =("Time New Roman",20,))


t_lable.place(x=25,y=430,height=50, width = 210)



t_lable1 = Label(win,text="",
             font =("Time New Roman",20,))


t_lable1.place(x=280,y=430,height=50, width = 210)






p_lable = Label(win,text="pressure",
             font =("Time New Roman",20,))


p_lable.place(x=25,y=500,height=50, width = 210)


p_lable1 = Label(win,text="",
             font =("Time New Roman",20,))


p_lable1.place(x=280,y=500,height=50, width = 210)



done_button = Button(win,text="Done",
                    font=("Time New Roman",20,"bold"),command=data_get)
  


done_button.place(y=190,height=50,width=100,x=200)


                         
win.mainloop()



