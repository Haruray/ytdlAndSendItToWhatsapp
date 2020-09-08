from selenium import webdriver
from time import sleep
import youtube_dl
import os
import pathlib

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

url=input('Enter youtube link to download: ')
song_there = os.path.isfile("song.mp3")
if song_there:
    os.remove("song.mp3")
    
ydl_opts = {
        'format': 'bestaudio/best',
        'quiet':True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
for file in os.listdir("./"):
    if file.endswith(".mp3"):
        os.rename(file, 'song.mp3')

name = input('Enter the name of user or group : ')
filepath = str(pathlib.Path(__file__).parent.absolute())+"\song.mp3"

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

image_box = driver.find_element_by_xpath(
    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

send_button = driver.find_element_by_xpath('//span[@data-testid="send"]')
send_button.click()
