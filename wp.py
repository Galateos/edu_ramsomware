import ctypes
import os 

# СЃРјРѕС‚СЂРё РІРѕС‚ СЌС‚Сѓ СЃС‚СЂРѕС‡РєСѓ РєРѕРґР°
#dir = os.path.abspath(os.curdir)
#print(dir)

#directory = "c:\CuratedWallpaper"
#imagePath = dir + "/1.jpg"

def changeBG(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imagePath, 3)
    return

#changeBG(imagePath)