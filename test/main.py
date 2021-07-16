import requests
import tkinter as tk

response = requests.get("http://api.covid19api.com/summary")
#when we request this URL, this website will send a json object,which stores data in Javascript

window = tk.Tk()
window.geometry("800x400")
window.title("Covid Stats")

def show_data(country_name):
    for index in response.json()["Countries"]:
    #response.json() is a dictionary, response.json()["Countries"] is the value of "Countries", which is a long list
    #this list consists of dictionaries, each dictionary contains the covid info of a country
    #index is the item in this list, so index is a dictionary
        if index["Country"] == country_name:
        #print(index) #to print out the whole dictionary, in which contains the info of Canada
            country_label = tk.Label(window, font="Ariel 28", text=country_name)
            country_label.pack()
        #confirmed_description = tk.Label(window, text="Total confirmed covid cases")
        #confirmed_description.pack()
            total_confirmed = index["TotalConfirmed"]
            confirmed_label = tk.Label(window, font="Ariel 10", text="Total confirmed covid cases: " + str(total_confirmed))
            confirmed_label.pack()

show_data("Canada")

window.mainloop()

print("I GET HERE!")  #It won't be shown on the screen until the window is closed