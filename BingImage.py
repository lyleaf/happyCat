# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:31:30 2017

@author: liuy
"""
import requests 
from bs4 import BeautifulSoup
import ctypes
import struct
from PIL import Image



bing = "https://www.bing.com/"
r = requests.get(bing)
soup = BeautifulSoup(r.text,'lxml')
image = soup.select('.cursor_zoom img')

SPI_SETDESKWALLPAPER = 20 
sys_parameters_info = ctypes.windll.user32.SystemParametersInfoW if (struct.calcsize('P') * 8 == 64) \
        else ctypes.windll.user32.SystemParametersInfoA
WALLPAPER_PATH = "D:\\Userfiles\\liuy\\Desktop\\BingWallpaper-2017-01-16.jpg"
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH , 0)



img = Image.open(WALLPAPER_PATH)
print img
