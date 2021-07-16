import requests
import tkinter as tk

response = requests.get("http://api.covid19api.com/summary")
#when we request this URL, this website will send a json object,which stores data in Javascript

window = tk.Tk()
window.geometry("800x400")
window.title("Covid Stats")

for index in response.json()["Countries"]:
    #response.json() is a dictionary, response.json()["Countries"] is the value of "Countries", which is a long list
    #this list consists of dictionaries, each dictionary contains the covid info of a country
    #index is the item in this list, so index is a dictionary
    if index["Country"] == "Canada":
        print(index) #print out the whole dictionary, in which contains the info of Canada


window.mainloop()

