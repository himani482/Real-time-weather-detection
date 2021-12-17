import tkinter as tk
import requests
import time
import json


def getweather(root):
	city = textfield.get()
	api=" http://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=c6f8e2b47f3da52d76ceb2234d559a64"
	data= requests.get(api).json()
	condition = data["weather"][0]["main"]
	temp = int(data["main"]['temp'] -273.15)
	min_temp = int(data["main"]['temp_min'] -273.15)
	max_temp = int(data["main"]['temp_max'] -273.15)
	pressure= data['main']['pressure']
	humidity=data['main']['humidity']
	wind= data['wind']['speed']
	sunrise=time.strftime("%I:%M:%S",time.gmtime(data['sys']['sunrise'] -21600))
	sunset=time.strftime("%I:%M:%S",time.gmtime(data['sys']['sunset'] -21600))

	final_info = condition +"\n" +str(temp)+"°C"
	final_data = "\n" +"Max Temp :" + str(max_temp) + "\n"+ "Min Temp:" + str(min_temp) + "\n" + "pressure:" + str(pressure) +"\n"+" humidity: " + str(humidity)+ "\n" + "wind speed" + str(wind)+ "\n" + "sunrise :" + sunrise +"\n" +"sunrise:" + sunrise
	label1.config(text = final_info)
	label2.config(text = final_data)




root = tk.Tk()
root.geometry("600x500")
root.title("weather report")

f = ("poppins", 15,"bold")
t= ("poppins",25,"bold")

textfield= tk.Entry(root, font=t)
textfield.pack(pady =20)
textfield.focus()
textfield.bind('<Return>',getweather)

label1= tk.Label(root,font=t)
label1.pack()
label2= tk.Label(root,font=f)
label2.pack()

root.mainloop()