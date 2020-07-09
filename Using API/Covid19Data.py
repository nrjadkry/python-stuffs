from tkinter import *
from tkinter import filedialog
import requests 
import json


root=Tk()

root.title('Covid19 Live Data')

#https://covid-193.p.rapidapi.com/statistics
live_data=requests.get("https://covid-193.p.rapidapi.com/statistics")
api=json.loads(live_data.content)
print(api)


mainloop()