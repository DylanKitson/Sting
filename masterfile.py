print("Software Started...")
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

import plotly.offline as offline
offline.init_notebook_mode()
import decimal
import datetime
from itertools import product
import math
from math import log10, floor
import scipy
from scipy import stats
import keyboard
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter.simpledialog
print("Open image (.jpg or .png)")
root = Tk()
rawlist1 = np.array([]).reshape(-1,2)
rawlist2 = np.array([]).reshape(-1,2)
w = Canvas(root, width=1400, height=900)
def analyze(self):
     userbase = int(input("Input graph resolution. Smaller values create a more 'detailed' graph, but it's harder to visualize data. -> I suggest 5, 10, 20 or 50: "))
     def calculateDistance(x1,y1,x2,y2):  
          return math.hypot(x2-x1,y2-y1)  
     def myround(x):
          return int(userbase * round(int(x)/userbase))
     ds1 = np.array(rawlist1)
     ds1 = np.reshape(ds1, (-1,2))
     ds2 = np.array(rawlist2)
     ds2 = np.reshape(ds2, (-1,2))
     c = list(product(ds1, ds2))
     x = np.array(c).reshape(-1,4)
     print(x)
     outarray = []
     outrounded = []
     abundance = []
     for i in x:
          a = calculateDistance(i[0],i[1],i[2],i[3])
          outarray.append(a)

     print("outarray ",np.array(outarray).reshape(-1,1))
     mean = np.mean(outarray)
     median = np.median(outarray)
     std = np.std(outarray)
     minimum = np.amin(outarray)
     maximum = np.amax(outarray)
     q10 = np.percentile(outarray, 10)
     q20 = np.percentile(outarray, 20)
     q30 = np.percentile(outarray, 30)
     q40 = np.percentile(outarray, 40)
     q50 = np.percentile(outarray, 50)
     q60 = np.percentile(outarray, 60)
     q70 = np.percentile(outarray, 70)
     q80 = np.percentile(outarray, 80)
     q90 = np.percentile(outarray, 90)
     q100 = np.percentile(outarray, 100)
     print("Please wait while data is analyzed. This can take between 0.1 seconds and a few minutes...")
     for k in outarray:
          c = myround(k)
          outrounded.append(c)

     np.array(outrounded).reshape(-1,1)
     np.sort(outrounded, axis=None)

     abundance = np.bincount(np.array(outrounded))
     outrange = np.array(list(range(len(abundance))))

     mode = np.amax(abundance)

     py.sign_in('DylanKitson', 'cUoNo5UgNyQ1p74VlMfS') # Replace the username, and API key with your credentials.

     trace1 = go.Bar(x=outrange, y=abundance, marker=dict(
        color='rgb(49,130,189)',
    ))
     data = [trace1]
     layout = go.Layout(
          margin=go.Margin(
             l=100,
             r=250,
             b=100,
             t=100,
             pad=4
         ),
         xaxis=dict(
             title='Distance (1 d.p.)',
             titlefont=dict(
                 family='Arial, sans-serif',
                 size=18,
                 color='grey'
             ),
             showticklabels=True,
             tickfont=dict(
                 family='Old Standard TT, serif',
                 size=14,
                 color='black'
             ),
             exponentformat='e',
             showexponent='all'
         ),
         yaxis=dict(
             title='Abundance (arb. units)',
             titlefont=dict(
                 family='Arial, sans-serif',
                 size=18,
                 color='grey'
             ),
             showticklabels=True,
             tickfont=dict(
                 family='Old Standard TT, serif',
                 size=14,
                 color='black'
             ),
             exponentformat='e',
             showexponent='all'
         )
     )


     fig = go.Figure(data=data, layout=layout)
     name1 = str(input("Enter a file name (without image type) to generate graph: "))
     name1.replace(" ", "")
     name1 = name1 + ".png"
     py.image.save_as(fig, filename=name1)
     
     from PIL import Image, ImageDraw, ImageFont
          
     image = Image.open(name1)
            
     draw = ImageDraw.Draw(image)
     with Image.open(name1) as img:
         width, height = img.size
     font = ImageFont.truetype("arial.ttf", 13)
      
     (x, y) = (50, 50)
     title = str(input("Enter graph title: "))
     titledraw = "Title: " + title 
     color = 'rgb(0, 0, 0)' # black color

     draw.text((x, y), titledraw, fill=color, font=font)
     meandraw = 'Mean Distance: ' + str(mean)
     color = 'rgb(0, 0, 0)'
     draw.text((width-230, height-460), meandraw, fill=color, font=font)
     modedraw = 'Modal Abundance Class: ' + str(mode)
     draw.text((width-230, height-440), modedraw, fill=color, font=font)
     mediandraw = 'Median Distance: ' + str(median)
     draw.text((width-230, height-420), mediandraw, fill=color, font=font)
     stddraw = 'Standard Deviation: ' + str(std)
     draw.text((width-230, height-400), stddraw, fill=color, font=font)
     minimumdraw = 'Min Distance: ' + str(minimum) 
     draw.text((width-230, height-380), minimumdraw, fill=color, font=font)
     maximumdraw = 'Max Distance: ' + str(maximum)
     draw.text((width-230, height-360), maximumdraw, fill=color, font=font)
     q10draw = 'Q10: ' + str(q10)
     draw.text((width-230, height-340), q10draw, fill=color, font=font)
     q20draw = 'Q20: ' + str(q20)
     draw.text((width-230, height-320), q20draw, fill=color, font=font)
     q30draw = 'Q30: ' + str(q30)
     draw.text((width-230, height-300), q30draw, fill=color, font=font)
     q40draw = 'Q40: ' + str(q40)
     draw.text((width-230, height-280), q40draw, fill=color, font=font)
     q50draw = 'Q50: ' + str(q50)
     draw.text((width-230, height-260), q50draw, fill=color, font=font)
     q60draw = 'Q60: ' + str(q60)
     draw.text((width-230, height-240), q60draw, fill=color, font=font)
     q70draw = 'Q70: ' + str(q70)
     draw.text((width-230, height-220), q70draw, fill=color, font=font)
     q80draw = 'Q80: ' + str(q80)
     draw.text((width-230, height-200), q80draw, fill=color, font=font)
     q90draw = 'Q90: ' + str(q90)
     draw.text((width-230, height-180), q90draw, fill=color, font=font)
     q100draw = 'Q100: ' + str(q100)
     draw.text((width-230, height-160), q100draw, fill=color, font=font)
     
     graphres = 'Graph Resolution: ' + str(userbase)
     color = 'rgb(0, 0, 50)' 
     draw.text((width-230, height-140), graphres, fill=color, font=font)
     createdraw = 'Image Created: ' + str(datetime.datetime.now())
     color = 'rgb(250, 20, 0)'
     draw.text((width-230, height-120), createdraw, fill=color, font=font)
      
     image.save(name1)
     print("Image has been saved as ",name1,"in the same folder as this program.")
     print("Run successful. Please exit to run again")

def rightdown(event):
    global rawlist2
    xmpx = xe-x0
    xm = xmt/xmpx
    ympx = ye-y0
    ym = -ymp/ympx

    newx = (event.x-x0)
    newy = (event.y-y0)

    w.create_polygon((event.x,event.y), fill='', outline='red', width=3)
    rawlist2 = np.append(rawlist2,newx)
    rawlist2 = np.append(rawlist2,newy)


w.bind("<Button 3>", rightdown)
w.focus_set()
w.bind("<KeyPress-a>", analyze)
w.focus_set()
w.pack()

File = askopenfilename(parent=root, initialdir="./",title='Select an image')
original = Image.open(File)
##original = original.resize((1000,1000), Image.ANTIALIAS)


baseheight = 800
hpercent = (baseheight / float(original.size[1]))
wsize = int((float(original.size[0]) * float(hpercent)))
original = original.resize((wsize, baseheight), Image.ANTIALIAS)


img = ImageTk.PhotoImage(original)
w.create_image(0, 0, image=img, anchor="nw")
width = img.width()
height = img.height()

xmt = width
ymp = height

xc = 0
yc = 0
print("Grid must be calibrated before each run")
print("Click in the top left, top right then bottom left of the window to set the grid dimensions")
tkinter.messagebox.showinfo("Instructions", "Click: \n" 
                                            "1) Top Left Grid Extreme \n"
                                            "2) Top Right Grid Extreme \n"
                                            "3) Bottom Left Grid Extreme")


def getorigin(eventorigin):
    global x0,y0
    x0 = eventorigin.x
    y0 = eventorigin.y
    print(x0,y0)
    w.bind("<Button 1>",getextentx)
w.bind("<Button 1>",getorigin)
def getextentx(eventextentx):
    global xe
    xe = eventextentx.x
    print(xe)
    w.bind("<Button 1>",getextenty)


def getextenty(eventextenty):
    global ye
    ye = eventextenty.y
    print(ye)
    print("Grid is set. You can start picking coordinates. Left click for species 1, a green dot will appear. Right click for species 2, a red dot will appear. To analyze data, press the a key once then wait.")
    w.bind("<Button 1>",printcoords)


def printcoords(event):
    global rawlist1
    xmpx = xe-x0
    xm = xmt/xmpx
    ympx = ye-y0
    ym = -ymp/ympx


    newx = (event.x-x0)
    newy = (event.y-y0)


    w.create_polygon((event.x,event.y), fill='', outline='green', width=3)
    rawlist1 = np.append(rawlist1,newx)
    rawlist1 = np.append(rawlist1,newy)
    print(rawlist1)

root.mainloop()

   


