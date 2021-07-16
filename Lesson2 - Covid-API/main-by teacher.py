import requests
import tkinter as tk

response = requests.get("http://api.covid19api.com/summary")

window = tk.Tk()
window.geometry("800x400")
window.title("Covid stats")

def show_data(country_name):
    for index in response.json()["Countries"]:
        if index['Country'] == country_name:
            country_label = tk.Label(window, font="Ariel 20", text=country_name)
            country_label.pack()
            total_confirmed = index["TotalConfirmed"]
            confirmed_label = tk.Label(window, font="Ariel 10", text='Total confirmed covid cases: ' + str(total_confirmed))
            confirmed_label.pack()

show_data("Canada")


window.mainloop()