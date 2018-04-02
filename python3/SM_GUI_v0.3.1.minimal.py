# python3
from sys import version_info
from time import sleep, strftime
from base64 import encodebytes
from io import BytesIO
from random import randint
from requests import head
from PIL import Image
from PIL import ImageTk
from pyspectator.processor import Cpu
import os
import PIL.Image
import RPi.GPIO as IO
if version_info[0] == 2:
    from urllib2 import urlopen
    from Tkinter import *
else:
    from urllib.request import urlopen
    from tkinter import *
#tkutils
def createImg(window, name, url, method, resizeX=None, resizeY=None):
    if method == 'TK':
        window.name = PhotoImage(data=encodebytes(urlopen(url).read()))
    elif method == 'PIL':
        window.name = ImageTk.PhotoImage(PIL.Image.open(BytesIO(urlopen(url).read())).resize((resizeX, resizeY), PIL.Image.ANTIALIAS))
    return window.name
def searchImg(url1, url2, rangeMin, rangeMax, debugInfos=False, fillZero=True):
    statusCode = [300, 1]
    while (
        statusCode[0] != 200 and
        statusCode[0] != 201 and
        statusCode[0] != 202 and
        statusCode[0] != 203 and
        statusCode[0] != 204 and
        statusCode[0] != 205 and
        statusCode[0] != 206 and
        statusCode[0] != 207 and
        statusCode[0] != 208 and
        statusCode[0] != 226):
        url = randint(rangeMin, rangeMax)
        if url > 9:
            if url > 99:
                if url > 999:
                    url = ''+str(url)
                else:
                    url = '0'+str(url)
            else:
                url = '00'+str(url)
        else:
            url = '000'+str(url)
        url = url1+url+url2
        resp = head(url)
        statusCode[0] = resp.status_code
        if debugInfos == True:
            print('[DEBUG] Code: '+str(statusCode[0])+' | URL: '+url+' | Try: '+str(statusCode[1]))
        statusCode[1] += 1
    return url
#gpioControl
def loadGpio(gpioMode=None, setwarnings=False, pins=[[]]):
    if gpioMode == 'BCM':
        IO.setmode(IO.BCM)
    elif gpioMode == 'BOARD':
        IO.setmode(IO.BOARD)
    if gpioMode == 'BCM' or gpioMode == 'BOARD':
        IO.setwarnings(setwarnings)
        for i in range(len(pins)):
            pin = pins[i]
            if pin[1] == 'IN':
                IO.setup(pin[0],IO.IN)
            elif pin[1] == 'OUT':
                IO.setup(pin[0],IO.OUT)
    elif gpioMode == 'CLEAN':
        IO.setwarnings(setwarnings)
        for i in range(len(pins)):
            IO.cleanup(pins[i])
    elif gpioMode == None or gpioMode == '':
        print('[WARNING] Mode unset. use \'BCM\' or \'BOARD\' or \'UNLOAD\'! setting mode \'',gpioMode,'\' because it was the default value.')
    else:
        print('[ERROR] Invalid Mode. use \'BCM\' or \'BOARD\' or \'UNLOAD\'! setting mode \'',gpioMode,'\' because it was the default value.')
def statusLed(status=0, red=17, green=27):
    if IO.getmode() == IO.BCM or IO.getmode()  == IO.BOARD:
        if status == 0 or status == 'off' or status == 'OFF':
            print('status: 0 / off   / OFF')
            IO.output([red, green],IO.LOW)
        elif status == 1 or status== 'green' or status == 'GRN':
            print('status: 1 / green / GRN')
            IO.output(red,IO.LOW)
            IO.output(green, IO.HIGH)
        elif status == 2 or status == 'red' or status == 'RED':
            print('status: 2 / red   / RED')
            IO.output(green,IO.LOW)
            IO.output(red, IO.HIGH)
        elif status == 3 or status == 'test' or status == 'TST':
            print('status: 3 / test  / TST')
            print('[+ statusLED-Test]')
            i = 0
            for i in range(3):
                statusLed(i)
                i += 1
                sleep(1)
            i = 0
            statusLed(0)
            print('[- statusLED-Test]')
#main
loadGpio('BCM', False, [[2, 'IN'], [3, 'IN'], [4, 'IN'], [17, 'OUT'], [27, 'OUT']])
statusLed(2)
SmartMirrorGUI = Tk()
SmartMirrorGUI.configs = [False, True, 0.75, 0.75, 0.3, "$$", "$$", "foto99e83cda40fd2d3cd0a4d11485dffca2"]                #[ maximised{bool} , fullscreen{bool} , windowWidth(%){float} , windowHeight(%){float} , versionNr{float} ]
SmartMirrorGUI.settings = ['']
SmartMirrorGUI.width = [SmartMirrorGUI.winfo_screenwidth(), SmartMirrorGUI.winfo_screenwidth()*SmartMirrorGUI.configs[2]]
SmartMirrorGUI.height = [SmartMirrorGUI.winfo_screenheight(), SmartMirrorGUI.winfo_screenheight()*SmartMirrorGUI.configs[3]]
SmartMirrorGUI.canvasSize = int(not SmartMirrorGUI.configs[1])
def toggleFullscreen(event):
    SmartMirrorGUI.configs[1] = not SmartMirrorGUI.configs[1]
    SmartMirrorGUI.attributes('-fullscreen', SmartMirrorGUI.configs[1])
    SmartMirrorGUI.canvas.configure(width=SmartMirrorGUI.width[int(not SmartMirrorGUI.configs[1])], height=SmartMirrorGUI.height[int(not SmartMirrorGUI.configs[1])])
    return 'break'
def exitGUI(event):
    SmartMirrorGUI.configs[1] = False
    SmartMirrorGUI.attributes('-fullscreen', False)
    SmartMirrorGUI.canvas.configure(width=SmartMirrorGUI.width[1], height=SmartMirrorGUI.height[1])
    print('[DEBUG] Exiting . . .')
    statusLed(2)
    sleep(0.1)
    statusLed(1)
    sleep(0.1)
    statusLed(2)
    sleep(0.25)
    statusLed(1)
    sleep(1)
    loadGpio('CLEAN', True, [2, 3, 4, 17, 27], True)
SmartMirrorGUI.bind('<F11>', toggleFullscreen)
SmartMirrorGUI.bind('<Escape>', exitGUI)
SmartMirrorGUI.title('SmartMirror v'+str(SmartMirrorGUI.configs[4])+' >> GUI')
SmartMirrorGUI.geometry(
    '%dx%d+%d+%d' % (
        SmartMirrorGUI.width[1],
        SmartMirrorGUI.height[1],
        (SmartMirrorGUI.winfo_screenwidth()/2-(SmartMirrorGUI.winfo_screenwidth()*SmartMirrorGUI.configs[2])/2),
        (SmartMirrorGUI.winfo_screenheight()/2-(SmartMirrorGUI.winfo_screenheight()*SmartMirrorGUI.configs[3])/2)
    )
)
SmartMirrorGUI.attributes(
    '-zoomed', SmartMirrorGUI.configs[0],
    '-fullscreen', SmartMirrorGUI.configs[1]
)
SmartMirrorGUI.canvas = Canvas(
    SmartMirrorGUI,
    bg='black',
    cursor='none',
    width=SmartMirrorGUI.width[SmartMirrorGUI.canvasSize],
    height=SmartMirrorGUI.height[SmartMirrorGUI.canvasSize],
    borderwidth=0,
    highlightthickness=0
)
SmartMirrorGUI.canvas.pack()
SmartMirrorGUI.canvasImgWeather = createImg(SmartMirrorGUI, 'canvasImgWeather', ('https://www.theweather.com/wimages/'+SmartMirrorGUI.configs[7]+'.png'), 'TK')
SmartMirrorGUI.canvas.create_image(
    SmartMirrorGUI.winfo_screenwidth()/2,
    100,
    image=SmartMirrorGUI.canvasImgWeather,
    anchor=CENTER
)
SmartMirrorGUI.canvasImgRutheUrl = searchImg('http://ruthe.de/cartoons/strip_', '.jpg',0 , 9999, True, True)
SmartMirrorGUI.canvasImgRuthe = createImg(SmartMirrorGUI, 'canvasImgWeather', SmartMirrorGUI.canvasImgRutheUrl, 'PIL', round(425*0.9), round(596*0.9))
SmartMirrorGUI.canvas.create_image(
    SmartMirrorGUI.winfo_screenwidth()/2,
    625,
    image=SmartMirrorGUI.canvasImgRuthe,
    anchor=CENTER
)
SmartMirrorGUI.canvasImgRutheId = SmartMirrorGUI.canvas.create_text(
    round(SmartMirrorGUI.winfo_screenwidth()/2),
    625+round(596/2*0.9)+20,
    fill='white',
    font=('Helvetica', 20),
    anchor=CENTER,
    text=SmartMirrorGUI.canvasImgRutheUrl.split('_')[1].split('.jpg')[0],
    activefill='white'
)
SmartMirrorGUI.canvasTextTempOutside = SmartMirrorGUI.canvas.create_text(
    round(SmartMirrorGUI.winfo_screenwidth()/4),
    625+round(596/2*0.9)+75,
    fill='white',
    font=('Helvetica', 20),
    anchor=CENTER,
    text=(SmartMirrorGUI.configs[5],'°C'),
    activefill='white'
)
SmartMirrorGUI.canvasTextTempInside = SmartMirrorGUI.canvas.create_text(
    round(SmartMirrorGUI.winfo_screenwidth()/4*2),
    625+round(596/2*0.9)+75,
    fill='white',
    font=('Helvetica', 20),
    anchor=CENTER,
    text=(SmartMirrorGUI.configs[6],'°C'),
    activefill='white'
)
SmartMirrorGUI.canvasTextTempCpu = SmartMirrorGUI.canvas.create_text(
    round(SmartMirrorGUI.winfo_screenwidth()/4*3),
    625+round(596/2*0.9)+75,
    fill='white',
    font=('Helvetica', 20),
    anchor=CENTER,
    text=(Cpu(monitoring_latency=1).temperature,'°C'),
    activefill='white'
)
SmartMirrorGUI.clock = Label(
    SmartMirrorGUI,
    font=('Helvetica', 50),
    text='HH:MM:SS',
    fg='white',
    bg='black',
    cursor='none'
)
SmartMirrorGUI.clock.place(
    relx=0.5,
    y=275,
    anchor='center'
)
print(round(SmartMirrorGUI.winfo_screenwidth()/2-SmartMirrorGUI.clock.winfo_width()*100/2))
print(SmartMirrorGUI.winfo_screenwidth()/2-SmartMirrorGUI.clock.winfo_width()/2*100)
print(SmartMirrorGUI.winfo_screenwidth()/2)
print(SmartMirrorGUI.clock.winfo_width())
def relayToTkinter(channel):
    if channel == 2:
        SmartMirrorGUI.event_generate('<<B1>>', when='tail')
    elif channel == 3:
        SmartMirrorGUI.event_generate('<<B2>>', when='tail')
    elif channel == 4:
        SmartMirrorGUI.event_generate('<<B3>>', when='tail')
def gpioAction(switch):
    if switch == 1:
        SmartMirrorGUI.canvasImgRutheUrl = searchImg('http://ruthe.de/cartoons/strip_', '.jpg',0 , 9999, True, True)
        SmartMirrorGUI.canvasImgRuthe = createImg(SmartMirrorGUI, 'canvasImgWeather', SmartMirrorGUI.canvasImgRutheUrl, 'PIL', round(425*0.9), round(596*0.9))
        SmartMirrorGUI.canvas.create_image(
            SmartMirrorGUI.winfo_screenwidth()/2,
            625,
            image=SmartMirrorGUI.canvasImgRuthe,
            anchor=CENTER
        )
        SmartMirrorGUI.canvas.itemconfigure(SmartMirrorGUI.canvasImgRutheId, text=SmartMirrorGUI.canvasImgRutheUrl.split('_')[1].split('.jpg')[0])
    elif switch == 2:
        print('[DEBUG] Shutting down . . .')
        statusLed(2)
        sleep(0.1)
        statusLed(1)
        sleep(0.1)
        statusLed(2)
        sleep(0.25)
        statusLed(1)
        sleep(1)
        statusLed(2)
        loadGpio('CLEAN', False, [2, 3, 4, 17, 27])
        os.system('shutdown 0')
    elif switch == 3:
        SmartMirrorGUI.canvasImgWeather = createImg(SmartMirrorGUI, 'canvasImgWeather', 'https://www.theweather.com/wimages/fotof62af6d4a7b74d49c1c46034432e36a4.png', 'TK')
        SmartMirrorGUI.canvas.create_image(
            SmartMirrorGUI.winfo_screenwidth()/2,
            100,
            image=SmartMirrorGUI.canvasImgWeather,
            anchor=CENTER
        )
    else:
        print('[WARNING] Error with GPIO Pins')
IO.add_event_detect(2, IO.RISING, callback=relayToTkinter, bouncetime=300)
IO.add_event_detect(3, IO.RISING, callback=relayToTkinter, bouncetime=300)
IO.add_event_detect(4, IO.RISING, callback=relayToTkinter, bouncetime=300)
SmartMirrorGUI.bind("<<B1>>", lambda event:gpioAction(1))
SmartMirrorGUI.bind("<<B2>>", lambda event:gpioAction(2))
SmartMirrorGUI.bind("<<B3>>", lambda event:gpioAction(3))
statusLed(1)
def tick():
    time2 = strftime('%H:%M:%S')
    if time2 != SmartMirrorGUI.settings[0]:
        time1 = time2
        SmartMirrorGUI.clock.config(text=time2)
    # calls itself every 200 milliseconds to update the time display as needed
    # could use >200 ms, but display gets jerky
    SmartMirrorGUI.clock.after(200, tick)
tick()
SmartMirrorGUI.mainloop()
