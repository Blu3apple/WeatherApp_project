import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature: %s °C' % (name, desc, temp)

    except:
        final_str = "There was a problem retrieving that info"

    return final_str

def get_weather(city):
    weather_key = "11f53ea654b20b95cf106e3dd80b85a5"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "Metric"}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

root = tk.Tk()
root.title("Weather App")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='C:\\Users\\Blu3apple\\Documents\\CODING\\Python\\Projets personnels\\Weather_App\\red_umbrella_wp.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=('Cambria', 14), fg="#83add6")
entry.place(relwidth=0.65, relheight=1)
entry.insert(0, 'Enter a Zip Code or City Name')
entry.bind("<FocusIn>", lambda args: entry.delete('0', 'end'))

button = tk.Button(frame, text="Get Weather", font=('Cambria', 14), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=('Cambria', 18), anchor="nw", justify="left", bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()