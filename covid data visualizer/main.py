from tkinter import * 
from PIL import Image,ImageTk
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from covid import Covid



def showdata():

    covid=Covid()

    cases=[]
    deaths=[]
    confirmed=[]
    active=[]
    recovered=[]

    try:
        root.update()
        countries=data.get()
        country_name=countries.strip()
        country_name=country_name.replace(" ",",")
        country_name=country_name.split(",")

        for x in country_name:
            cases.append(covid.get_status_by_country_name(x))
            root.update()
        for y in cases:
            confirmed.append(y["confirmed"])
            active.append(y["active"])
            recovered.append(y["recovered"])
            deaths.append(y["deaths"])    

        confirmed_patch=mpatches.Patch(color='green',label='confirmed')
        active_patch=mpatches.Patch(color='red',label='active')
        recovered_patch=mpatches.Patch(color='blue',label='recovered')
        deaths_patch=mpatches.Patch(color='black',label='deaths')

        plt.legend(handles=[confirmed_patch,recovered_patch,active_patch,deaths_patch])   

        for x in range(len(country_name)):
            plt.bar(country_name[x],confirmed[x],color='green')
            plt.bar(country_name[x],recovered[x],color='red')
            plt.bar(country_name[x],active[x],color='blue')
            plt.bar(country_name[x],deaths[x],color='black')

        plt.title('Current Covid Case')
        plt.xlabel('Country Names')
        plt.ylabel('Case(in millions)')

    except Exception as e:
        data.set("Enter correct details again")            



root=Tk()

root.geometry("650x720")

root.title("Covid-19 Data")

img=ImageTk.PhotoImage(Image.open(r"D:\covid data visualizer\covid191.jpg"))
panel=Label(root,image=img)
panel.pack(fill="both",expand="no")

Label(root,text="Enter Countries Name",font="Raleway 18").pack()

data=StringVar()
entry=Entry(root,textvariable=data,width=70).pack()
Button(root,text="Get Data",command=showdata).pack()



root.mainloop()