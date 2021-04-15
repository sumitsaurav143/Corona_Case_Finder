from tkinter import *
from plyer import notification
import requests
#from bs4 import BeautifulSoup
import re
from tkinter import ttk

def getData(url):
    r = requests.get(url)
    return r.text

State=[]
StateData= getData("https://api.covid19india.org/csv/latest/state_wise.csv")
sd=re.split(r'\r',StateData)
for i in range(2,len(sd)):
    State.append(sd[i].split(",")[0][1:])
State.sort()
#print(State)

Dist={}

DistData= getData("https://api.covid19india.org/csv/latest/district_wise.csv")
dd=re.split(r'\r',DistData)
for i in State:
    data={}
    for j in dd:
        if j.split(",")[2]==i:
            data[j.split(",")[4]]=[j.split(",")[5],j.split(",")[6],j.split(",")[7],j.split(",")[8]]
    else:
        Dist[i]=data


        

def status():
        c=0
        find=statechoose.get()
        if statechoose.get() in Dist.keys():
            Dis=[]
            for j in Dist[statechoose.get()].keys():
                Dis.append([j+" : "+"Total Cases="+str(Dist[statechoose.get()][j][0])])#District Data
        
         
  
        listbox = Listbox(root,width=66,height=24,font="arial 13 bold")  
        for i in range(len(Dis)):
            listbox.insert(i,Dis[i])    
   
        listbox.place(x=640,y=200)  
        
            
        for i in sd:
            if ((i.split(",")[0][1:]).lower())==find.lower():
                    tc=Label(root,
                             font="arial 15 bold",
                             text="Total Confirm Cases: "+i.split(",")[1]+
                             "\nRecovered Cases: "+i.split(",")[2]+
                             "\nTotal Deaths: "+(i.split(",")[3])+
                             "\nActive Cases: "+(i.split(",")[4])+"\n"+
                             "\nDate_Time: "+(i.split(",")[5]))
                    tc.place(x=85,y=540)
                    l4=Label(root,text="----------Status Updated On----------",font="arial 10 bold",bg="red")
                    l4.place(x=132,y=640)
                    '''notifyme(i.split(",")[0][1:]+" (Corona Status)",
                             "Total Confirm Cases: "+i.split(",")[1]+
                             "\nRecovered Cases: "+(i.split(",")[2]))
                             '''
                    c=1
        if c==0:
            l4=Label(root,text=" Wrong State!! ",font="arial 10 bold",bg="yellow")
            l4.place(x=165,y=148)
            
def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon = "corona.ico",
        timeout=10
        )

root=Tk()
#root.attributes('-fullscreen', True)
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
#root.geometry("1000x600+450+150")
root.config(bg="Black")
root.resizable(True,True)
logo = PhotoImage(file="bg.gif")
w1 = Label(root, image=logo).pack()
root.title("Covide Status Finder")
l=Label(root,text="INDIA COVID STATUS FINDER",bg="Black",fg="red",font="arial 17 bold")
l.pack()
l1=Label(root,text="Select State: ",bg="white",font="arial 15 bold")
l1.place(x=55,y=130)


# Combobox creation
n = StringVar()
statechoose = ttk.Combobox(root, width = 27, textvariable = n)
statechoose['values'] = State
statechoose.place(x=180,y=135)
statechoose.current()


b1=Button(root,text="SHOW STATUS",bg="red",font="arial 12 bold",command=status)
b1.place(x=172,y=190)
l3=Label(root,text="Created By Sumit Saurav",bg="Black",fg="white",font="arial 8 bold")
l3.place(x=260,y=710)


root.mainloop()
