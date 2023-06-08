from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather Forecast App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)


def getweather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    tz.config(text=result)
    long_lat.config(
        text=f"{round(location.latitude,2)}°N,{round(location.longitude,2)}°E"
    )
    curr = pytz.timezone(result)
    local_time = datetime.now(curr)
    curr_time = local_time.strftime("%I:%M %p")
    clock.config(text=curr_time)
    api = (
        "https://api.openweathermap.org/data/2.5/forecast?lat="
        + str(location.latitude)
        + "&lon="
        + str(location.longitude)
        + "&units=metric&appid={APIKEY}"
    )
    json_data = requests.get(api).json()

    temp = round(float(json_data["list"][0]["main"]["temp"]), 2)
    humidity = round(float(json_data["list"][0]["main"]["humidity"]), 2)
    pressure = round(float(json_data["list"][0]["main"]["pressure"]), 2)
    wind = round(float(json_data["list"][0]["wind"]["speed"]), 2)
    description = (
        json_data["list"][1]["weather"][0]["main"]
        + "("
        + json_data["list"][1]["weather"][0]["description"]
        + ")"
    )
    tp.config(text=(temp, "°C"))
    hd.config(text=(humidity, "%"))
    pr.config(text=(pressure, "hPa"))
    wd.config(text=(wind, "m/s"))
    ds.config(text=(description))

    firstdayimage = json_data["list"][0]["weather"][0]["icon"]
    photo1 = Image.open(
        f"C:\\Users\\mbaza\\Desktop\\weather\\icons\\{firstdayimage}@2x.png"
    )
    photo1 = photo1.resize((80, 80))
    photo1 = ImageTk.PhotoImage(photo1)
    firstimage.config(image=photo1)
    firstimage.image = photo1
    td1 = round(float(json_data["list"][0]["main"]["temp"]), 2)
    description1 = json_data["list"][0]["weather"][0]["main"]
    d1t.config(text=f"{td1}\n{description1}")

    seconddayimage = json_data["list"][8]["weather"][0]["icon"]
    photo2 = Image.open(
        f"C:\\Users\\mbaza\\Desktop\\weather\\icons\\{seconddayimage}@2x.png"
    )
    photo2 = photo2.resize((40, 40))
    photo2 = ImageTk.PhotoImage(photo2)
    secondimage.config(image=photo2)
    secondimage.image = photo2
    td2 = round(float(json_data["list"][8]["main"]["temp"]), 2)
    description2 = json_data["list"][8]["weather"][0]["main"]
    d2t.config(text=f"{td2}\n{description2}")

    thirddayimage = json_data["list"][16]["weather"][0]["icon"]
    photo3 = Image.open(
        f"C:\\Users\\mbaza\\Desktop\\weather\\icons\\{thirddayimage}@2x.png"
    )
    photo3 = photo3.resize((40, 40))
    photo3 = ImageTk.PhotoImage(photo3)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3
    td3 = round(float(json_data["list"][16]["main"]["temp"]), 2)
    description3 = json_data["list"][16]["weather"][0]["main"]
    d3t.config(text=f"{td3}\n{description3}")

    fourthdayimage = json_data["list"][24]["weather"][0]["icon"]
    photo4 = Image.open(
        f"C:\\Users\\mbaza\\Desktop\\weather\\icons\\{fourthdayimage}@2x.png"
    )
    photo4 = photo4.resize((40, 40))
    photo4 = ImageTk.PhotoImage(photo4)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4
    td4 = round(float(json_data["list"][24]["main"]["temp"]), 2)
    description4 = json_data["list"][24]["weather"][0]["main"]
    d4t.config(text=f"{td4}\n{description4}")

    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))


# icon
image_icon = PhotoImage(file="C:\\Users\\mbaza\\Desktop\\weather\\images\\logo.png")
root.iconphoto(False, image_icon)
R1 = Image.open("C:\\Users\\mbaza\\Desktop\\weather\\images\\rr1.png")
R1 = R1.resize((200, 120))
R1 = ImageTk.PhotoImage(R1)
Label(root, image=R1, bg="#57adff").place(x=30, y=110)


# label
l1 = Label(root, text="Temperature", font=("poppins", 11), fg="white", bg="#203243")
l1.place(x=50, y=120)

l2 = Label(root, text="Humidity", font=("poppins", 11), fg="white", bg="#203243")
l2.place(x=50, y=140)

l3 = Label(root, text="Pressure", font=("poppins", 11), fg="white", bg="#203243")
l3.place(x=50, y=160)

l4 = Label(root, text="Wind Speed", font=("poppins", 11), fg="white", bg="#203243")
l4.place(x=50, y=180)

l5 = Label(root, text="Description", font=("poppins", 11), fg="white", bg="#203243")
l5.place(x=50, y=200)


# search box
s_img = Image.open("C:\\Users\\mbaza\\Desktop\\weather\\images\\simg.png")
s_img = s_img.resize((600, 75))
s_img = ImageTk.PhotoImage(s_img)
s_img = Label(root, image=s_img)
s_img.place(x=270, y=120)


textfield = tk.Entry(
    root,
    justify="center",
    width=15,
    font=("poppins", 25, "bold"),
    bg="#203243",
    border=0,
    fg="white",
)
textfield.place(x=420, y=140)
textfield.focus()


# sun image on search bar
sun = Image.open("C:\\Users\\mbaza\\Desktop\\weather\\images\\sun.png")
sun = sun.resize((50, 75))
sun = ImageTk.PhotoImage(sun)
b = Button(image=sun, borderwidth=0, cursor="hand2", bg="#203243", command=getweather)
b.place(x=820, y=120)

# big bottom box
frame = Frame(root, width=900, height=180)
frame.pack(side=BOTTOM)


firstbox = Image.open("C:\\Users\\mbaza\\Desktop\\weather\\images\\rr1.png")
firstbox = firstbox.resize((300, 150))
firstbox = ImageTk.PhotoImage(firstbox)
Label(root, image=firstbox).place(x=30, y=300)

# small boxes
secondbox1 = Image.open("C:\\Users\\mbaza\\Desktop\\weather\\images\\rr2.png")
secondbox1 = secondbox1.resize((150, 150))
secondbox1 = ImageTk.PhotoImage(secondbox1)
Label(root, image=secondbox1).place(x=350, y=300)

secondbox2 = Image.open("C:\\Users\\mbaza\\Desktop\\weather\\images\\rr2.png")
secondbox2 = secondbox2.resize((150, 150))
secondbox2 = ImageTk.PhotoImage(secondbox2)
Label(root, image=secondbox2).place(x=520, y=300)

secondbox3 = Image.open("C:\\Users\\mbaza\\Desktop\\weather\\images\\rr2.png")
secondbox3 = secondbox3.resize((150, 150))
secondbox3 = ImageTk.PhotoImage(secondbox3)
Label(root, image=secondbox3).place(x=690, y=300)

# clock
clock = Label(root, font=("Helvetica", 30, "bold"), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# timezone
tz = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
tz.place(x=550, y=20)

long_lat = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
long_lat.place(x=550, y=50)


tp = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
tp.place(x=150, y=120)
hd = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
hd.place(x=150, y=140)
pr = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
pr.place(x=150, y=160)
wd = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
wd.place(x=150, y=180)
ds = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
ds.place(x=150, y=200)

firstframe = Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=65, y=310)
day1 = Label(firstframe, font="Helvetica", bg="#282829", fg="#fff")
day1.place(x=80, y=5)
firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=0, y=40)
d1t = Label(firstframe, bg="#282829", fg="#57adff", font="Helvetica")
d1t.place(x=100, y=50)

secondframe = Frame(root, width=115, height=132, bg="#282829")
secondframe.place(x=370, y=310)
day2 = Label(secondframe, font="Helvetica", bg="#282829", fg="#fff")
day2.place(x=20, y=5)
secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=0, y=60)
d2t = Label(secondframe, bg="#282829", fg="#57adff", font="Helvetica")
d2t.place(x=50, y=50)

thirdframe = Frame(root, width=115, height=132, bg="#282829")
thirdframe.place(x=540, y=310)
day3 = Label(thirdframe, font="Helvetica", bg="#282829", fg="#fff")
day3.place(x=20, y=5)
thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=0, y=60)
d3t = Label(thirdframe, bg="#282829", fg="#57adff", font="Helvetica")
d3t.place(x=50, y=50)

fourthframe = Frame(root, width=115, height=132, bg="#282829")
fourthframe.place(x=710, y=310)
day4 = Label(fourthframe, font="Helvetica", bg="#282829", fg="#fff")
day4.place(x=20, y=5)
fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=0, y=60)
d4t = Label(fourthframe, bg="#282829", fg="#57adff", font="Helvetica")
d4t.place(x=50, y=50)

root.mainloop()
