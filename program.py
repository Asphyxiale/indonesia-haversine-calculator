import tkinter as tk
from tkinter import font
import math
from PIL import Image, ImageTk
mapwidth = 1000
mapheight = 400
xpad = 10
ypad = 10
lu = 6.5
ls = -11.5
minbt = 95
maxbt = 141
places = [
  {'cities': 'Ambon', 'lat': -3.654703, 'lon': 128.190643},
  {'cities': 'Banda Aceh', 'lat': 6.247773746532666, 'lon': 96.32526808139016},
  {'cities': 'Bandar Lampung', 'lat': -5.394736490121766, 'lon': 105.26541078883982},
  {'cities': 'Bandung', 'lat': -6.917075501356178, 'lon': 107.61294038860736},
  {'cities': 'Banjarmasin', 'lat': -3.3148213553226147, 'lon': 114.5921514686371},
  {'cities': 'Batam', 'lat': 1.0456, 'lon': 104.0305},
  {'cities': 'Balikpapan', 'lat': -1.2379, 'lon': 116.8529},
  {'cities': 'Bengkulu', 'lat': -3.8004, 'lon': 102.2655},
  {'cities': 'Bukittinggi', 'lat': -0.3039, 'lon': 100.3743},
  {'cities': 'Cirebon', 'lat': -6.7320, 'lon': 108.5523},
  {'cities': 'Denpasar', 'lat': -8.6705, 'lon': 115.2126},
  {'cities': 'Fak-Fak', 'lat': -2.9264, 'lon': 132.2963},
  {'cities': 'Gorontalo', 'lat': 0.5435, 'lon': 123.0568},
  {'cities': 'Jakarta', 'lat': -6.2088, 'lon': 106.8456},
  {'cities': 'Jambi', 'lat': -1.6101, 'lon': 103.6131},
  {'cities': 'Jayapura', 'lat': -2.5337, 'lon': 139.7181},
  {'cities': 'Kendari', 'lat': -3.9973, 'lon': 122.5120},
  {'cities': 'Kupang', 'lat': -10.1772, 'lon': 123.6070},
  {'cities': 'Labuan Bajo', 'lat': -8.4872, 'lon': 119.8807},
  {'cities': 'Makassar', 'lat': -5.1477, 'lon': 119.4327},
  {'cities': 'Malang', 'lat': -7.9666, 'lon': 112.6326},
  {'cities': 'Mamuju', 'lat': -2.6778, 'lon': 118.8877},
  {'cities': 'Manado', 'lat': 1.4748, 'lon': 124.8428},
  {'cities': 'Manokwari', 'lat': -0.8614, 'lon': 134.0620},
  {'cities': 'Mataram', 'lat': -8.5833, 'lon': 116.1167},
  {'cities': 'Medan', 'lat': 3.5952, 'lon': 98.6722},
  {'cities': 'Merauke', 'lat': -8.4991, 'lon': 140.0049},
  {'cities': 'Ngawi', 'lat': -7.4028, 'lon': 111.4452},
  {'cities': 'Padang', 'lat': -0.9471, 'lon': 100.4172},
  {'cities': 'Palangkaraya', 'lat': -2.2106, 'lon': 113.9213},
  {'cities': 'Palu', 'lat': -0.9010, 'lon': 119.8707},
  {'cities': 'Pamekasan', 'lat': -7.1579, 'lon': 113.4697},
  {'cities': 'Palembang', 'lat': -2.9761, 'lon': 104.7754},
  {'cities': 'Pangkalpinang', 'lat': -2.1325, 'lon': 106.1114},
  {'cities': 'Parepare', 'lat': -4.0150, 'lon': 119.6253},
  {'cities': 'Pekanbaru', 'lat': 0.5333, 'lon': 101.4500},
  {'cities': 'Pontianak', 'lat': -0.0263, 'lon': 109.3425},
  {'cities': 'Samarinda', 'lat': -0.5017, 'lon': 117.1536},
  {'cities': 'Semarang', 'lat': -6.9667, 'lon': 110.4167},
  {'cities': 'Serang', 'lat': -6.1200, 'lon': 106.1503},
  {'cities': 'Siantar', 'lat': 2.9645, 'lon': 99.0621},
  {'cities': 'Surabaya', 'lat': -7.2575, 'lon': 112.7521},
  {'cities': 'Tanjung Selor', 'lat': 2.8425, 'lon': 117.3732},
  {'cities': 'Ternate', 'lat': 0.7762, 'lon': 127.3633},
  {'cities': 'Yogyakarta', 'lat': -7.7955, 'lon': 110.3695}
]
def project(lat,lon):
    drawwidth = mapwidth-4*xpad
    drawheight = mapheight-4*ypad
    lonrange = maxbt-minbt
    latrange = lu-ls
    x = ((lon-minbt)/lonrange)*drawwidth
    xf = x+xpad
    y = ((lat-ls)/latrange)*drawheight
    yf = (mapheight-ypad)-y
    return xf,yf

def haversine(lat1,lon1,lat2,lon2):
    lat1,lon1,lat2,lon2 = map(math.radians,[lat1,lon1,lat2,lon2])
    dlat = lat2-lat1
    dlon = lon2-lon1
    a = (math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2)
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    distance = 6371*c
    return distance

def namecity(item_id):
    tags = canvas.gettags(item_id)
    if not tags or "city_point" not in tags:
        return None
    for tag in tags:
        if tag !=  "city_point":
            return tag
    return None

lis = []
def click(event):
    clicked = canvas.find_overlapping(event.x - 5, event.y - 5, event.x + 5, event.y + 5)
    if clicked:
        cityname = namecity(clicked[1]) 
        if cityname:
            if len(lis) == 2:
                for item in canvas.find_withtag("city_point"):
                    tags  =  canvas.gettags(item)
                    if lis[0] in tags or lis[1] in tags:
                        canvas.itemconfig(item, fill = 'gray')
                canvas.delete('clicked')
                canvas.delete('laine')
                lis.clear()

            if cityname not in lis:
                lis.append(cityname)
                canvas.itemconfig(clicked[1], fill = 'red')
                canvas.delete('hover_text')
                infolabel.config(text = f"Selected City: {cityname}")
            elif cityname in lis and len(lis) == 1:
                canvas.itemconfig(clicked[1], fill = 'gray')
                lis.clear()
                canvas.delete('clicked')
                infolabel.config(text = "")
                return
            if len(lis) == 2:
                city1 = next(item for item in places if item['cities'] == lis[0])
                city2 = next(item for item in places if item['cities'] == lis[1])
                distance = haversine(city1['lat'], city1['lon'], city2['lat'], city2['lon'])
                infolabel.config(text = f"{lis[0]} ✈ {lis[1]}: {distance:.2f} km")
                x1,y1 = project(city1['lat'], city1['lon'])
                x2,y2 = project(city2['lat'], city2['lon'])
                canvas.create_line(x1, y1, x2, y2, fill = "#e11d48", tags = 'laine', width = 3, dash = (6, 4))
            for i in lis:
                x,y = project(places[[p['cities'] for p in places].index(i)]['lat'], places[[p['cities'] for p in places].index(i)]['lon'])
                canvas.create_text(x, y-20, text = i,tags = 'clicked',fill = "black", font = ("Helvetica", 10, "bold"))

def hover(event):
    canvas.delete("hover_text")
    hovered = canvas.find_overlapping(event.x-5, event.y-5, event.x+5, event.y+5)
    if len(hovered) == 2:
        cityname = namecity(hovered[1])
        if cityname:
            if cityname not in lis:
                x,y = project(places[[p['cities'] for p in places].index(cityname)]['lat'], places[[p['cities'] for p in places].index(cityname)]['lon'])
                canvas.create_text(x, y-20, text = cityname, tags = "hover_text", fill = "black", font = ("Helvetica", 10))

root = tk.Tk()
root.title('Distance Calculator')
root.geometry('1050x650')
header = tk.Frame(root, bg = "#0f172a",pady = 15,padx = 20)
header.pack(fill = "x")
title = tk.Label(header, text = "Indonesia Distance Calculator", font = ("Helvetica", 16, "bold"), bg = "#0f172a", fg = "white")
title.pack(side = "left")
img = Image.open("assets/indonesia.png")
aspect_ratio = img.width / img.height
targetwidth = int(mapwidth*1)
targetheight = int(targetwidth/aspect_ratio)
img = img.resize((targetwidth, targetheight), Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(img)
canvas = tk.Canvas(root,width = mapwidth,height = mapheight)
canvas.create_image(-10,-20,image = image,anchor = tk.NW)
canvas.pack(padx = xpad,pady = ypad)
infoframe = tk.Frame(root, bg = "white",padx = 20,pady = 40,relief = "solid",borderwidth = 1)
infoframe.pack(fill = "x",padx = 20)
infolabel = tk.Label(infoframe,text = "Select a city",font = ("Helvetica",20,'bold'),bg = "white",fg = "#64748b")
infolabel.pack()
for i in places:
    x,y = project(i['lat'],i['lon'])
    pointid = canvas.create_oval(x-5, y-5, x+5, y+5, fill = 'gray', tags = (i['cities'], "city_point"))
canvas.bind("<Button-1>", click)
canvas.bind("<Motion>", hover)
root.mainloop()