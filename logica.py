from mhyt import yt_download
import pyautogui as pg


url = input('Link do Youtube: ')
print(type(url))
file_mp4 = input('Nome do arquivo mp4: ')
file_mp3 = input('Nome do arquivo mp3: ')
yt_download(url, file_mp4)
#########################
yt_download(url, file_mp3, ismusic=True)
pg.alert('Download concluido com sucesso!!')
