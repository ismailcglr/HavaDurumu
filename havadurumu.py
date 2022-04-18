from tkinter import *
from PIL import ImageTk,Image
import  requests

url = "http://api.openweathermap.org/data/2.5/weather"
apikey = "ded389ce358ee4de97b57da2b66a2ecb"
iconurl = "http://openweathermap.org/img/wn/{}@2x.png"

def getweather(city) : 
    params = {'q' : city, 'appid' : apikey, 'lang' : 'tr'}
    data = requests.get(url, params=params).json()
    if data : 
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return (city ,country ,temp ,icon ,condition)

def main() : 
    city = cityEntry.get()
    weather = getweather(city)
    if weather : 
        locationlabel['text'] = '{}, {}'. format(weather[0], weather[1])
        templabel['text'] = '{}C'.format(weather[2])
        conditionlabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconurl.format(weather[3]),stream=True).raw))
        iconlabel.configure(image=icon)
        iconlabel.image = icon


app = Tk()
app.geometry('300x450')
app.title('GÜNCEL HAVA DURUMU ')



cityEntry = Entry(app,justify='center')
cityEntry.pack(fill=BOTH,ipady=18,ipadx=18,pady=5)
cityEntry.focus()

searchbutton = Button(app, text='Arama', font=('Arial', 10), command=main,)
searchbutton.pack(ipady=10,ipadx=10)

iconlabel = Label(app,bg='blue')
iconlabel.pack()

locationlabel = Label(app, font=('Arial', 20) )
locationlabel.pack()

templabel = Label(app, font=('Arial ', 30, 'bold'))
templabel.pack()

conditionlabel = Label(app, font=('Arial', 20, ))
conditionlabel.pack()

app.mainloop()

