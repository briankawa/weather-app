import tkinter as tk
import requests
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    units = units_var.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=2c4fa57719c00cac191d09f7421187a1&units={units}"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == "404":
        messagebox.showerror("Error", "City not found!")
    else:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        if units == "imperial":
            temperature_unit = "Fahrenheit"
            wind_unit = "miles/hour"
        else:
            temperature_unit = "Celsius"
            wind_unit = "meter/sec"
            
        result_label.config(text=f"Temperature: {temperature}°{temperature_unit}\nHumidity: {humidity}%\nWind Speed: {wind_speed} {wind_unit}")

# GUI Setup
root = tk.Tk()
root.title("Weather App")

# Style
root.configure(bg="#87CEEB")
root.geometry("300x200")

# Widgets
city_label = tk.Label(root, text="Enter City:", bg="#87CEEB")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

units_label = tk.Label(root, text="Select Units:", bg="#87CEEB")
units_label.pack()

units_var = tk.StringVar()
units_var.set("metric")  # default to Celsius
units_menu = tk.OptionMenu(root, units_var, "metric", "imperial")
units_menu.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, bg="#ADD8E6")
get_weather_button.pack()

result_label = tk.Label(root, text="", bg="#87CEEB")
result_label.pack()

root.mainloop()
