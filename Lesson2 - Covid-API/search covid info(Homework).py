import requests
import tkinter as tk

response = requests.get("http://api.covid19api.com/summary")
message = ""
try:
    json = response.json()
    message = json["Message"]
except:
    quit("Turns out that there isn't a message in the correct response json.")
if message == "Caching in Progress":
    quit("API is currently unavailable due to caching in progress.")

window = tk.Tk()
window.geometry("800x400")
window.title("Covid Stats")

def show_data():
    try:
        country_name = country_entry.get().capitalize()
        for index in response.json()["Countries"]:
            if index["Country"] == country_name:
                country_label = tk.Label(window, font = "Ariel 20", text = country_name)
                country_label.pack()

                total_confirmed = index["TotalConfirmed"]
                confirmed_label = tk.Label(window, text = "Total Confirmed Covid Cases: " + str(total_confirmed))
                confirmed_label.pack()

                new_confirmed = index["NewConfirmed"]
                new_confirmed_label = tk.Label(window, text="New Confirmed Covid Cases: " + str(new_confirmed))
                new_confirmed_label.pack()

                new_recovered = index["NewRecovered"]
                new_recovered_label = tk.Label(window, text="New Recovered Covid Cases: " + str(new_recovered))
                new_recovered_label.pack()

                if new_recovered > new_confirmed:
                    new_confirmed_label.config(fg="green")
                    new_recovered_label.config(fg="green")

                if new_recovered < new_confirmed:
                    new_confirmed_label.config(fg="red")
                    new_recovered_label.config(fg="red")
    except(KeyError):
        quit("Could not find Countries in response json.")

country_entry = tk.Entry(window)
country_entry.pack()
search_button = tk.Button(window, text="Search", command=show_data)
search_button.pack()

window.mainloop()