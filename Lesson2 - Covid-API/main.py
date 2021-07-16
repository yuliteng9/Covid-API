import requests
import tkinter as tk

response = requests.get("http://api.covid19api.com/summary")

window = tk.Tk()
window.geometry("800x400")
window.title("Covid Stats")

def show_data():
    country_name = country_entry.get()
    for index in response.json()["Countries"]:
        if index["Country"] == country_name:
            country_label = tk.Label(window, font = "Ariel 20", text = country_name)
            country_label.pack()
            total_confirmed = index["TotalConfirmed"]
            confirmed_label = tk.Label(window, text = "Total Confirmed Covid Cases: " + str(total_confirmed))
            confirmed_label.pack()

country_entry = tk.Entry(window)
country_entry.pack()
search_button = tk.Button(window, text="Search", command=show_data)
search_button.pack()

window.mainloop()